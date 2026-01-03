import os
import sys
import argparse
import re
import json
import shutil
import subprocess
import urllib.request
import urllib.error
import concurrent.futures
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# --- Configuration ---
DEFAULT_SRC = "kali-tools"
DEFAULT_OUT = "."
TEMPLATE_DIR = "templates"
GENERATED_BY = "chatkali-skills-builder/0.2"
CACHE_FILE = "llm_cache.json"
MAX_WORKERS = 30
FAILED_LOG = "classification_failures.txt"

# Comprehensive Category List (99% Coverage)
KALI_CATEGORIES = {
    "information-gathering": "Tools for collecting data about a target network or system, including DNS enumeration, OSINT, and port scanning.",
    "vulnerability-analysis": "Tools for identifying security flaws, including fuzzers, scanners, and vulnerability assessment frameworks.",
    "web-application-analysis": "Tools specifically designed to attack and analyze web applications, including proxies, crawlers, and SQL injection tools.",
    "database-assessment": "Tools for testing and exploiting database systems, including SQL injection and data extraction utilities.",
    "password-attacks": "Tools for cracking passwords via brute-force, dictionary attacks, or rainbow tables.",
    "wireless-attacks": "Tools for auditing and attacking wireless protocols, including 802.11 Wi-Fi, Bluetooth, RFID, and SDR.",
    "reverse-engineering": "Tools for analyzing compiled binaries, including debuggers, disassemblers, and decompilers.",
    "exploitation-tools": "Tools for executing exploits against target systems, including social engineering toolkits and payload generators.",
    "sniffing-spoofing": "Tools for intercepting network traffic and impersonating devices or users, including MITM and packet sniffers.",
    "post-exploitation": "Tools used after gaining access to a system, including backdoors, rootkits, and privilege escalation scripts.",
    "forensics": "Tools for digital forensics, including disk imaging, file carving, and anti-forensics analysis.",
    "reporting-tools": "Tools for documenting findings, managing evidence, and generating penetration test reports.",
    "social-engineering-tools": "Tools for performing social engineering attacks, such as phishing campaigns and malicious payload creation.",
    "system-services": "Tools related to system services like SSH, HTTP, and TFTP, often used for maintaining access or serving files.",
    "tunneling-exfiltration": "Tools for establishing covert channels, proxying traffic, and exfiltrating data through firewalls.",
    "hardware-hacking": "Tools for auditing and attacking hardware interfaces, embedded systems, IoT devices, and Android.",
    "cryptography-steganography": "Tools for encryption, decryption, and hiding data within other files (steganography).",
    "malware-analysis": "Tools for analyzing malicious software, including sandboxes and signature matching utilities.",
    "defensive-tools": "Tools for protecting systems, including firewalls, intrusion detection systems (IDS), and honeypots.",
    "utilities": "General-purpose utilities for file manipulation, downloading, version control, and other essential tasks."
}

# --- Helper Functions ---

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            pass
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2)

def load_env():
    """Loads environment variables from .env file."""
    env_path = Path(".env")
    if env_path.exists():
        print("Loading .env file...")
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                if '=' in line:
                    k, v = line.split('=', 1)
                    os.environ[k.strip()] = v.strip()

def call_llm_classify(tool_title, tool_content, categories):
    """Classifies a tool using an LLM."""
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL")
    
    if not api_key or not base_url:
        print("Skipping LLM classification: Missing API key or Base URL.")
        return []

    # Use full content as requested
    prompt = f"""
You are an expert cybersecurity analyst and Kali Linux specialist. 
Your task is to analyze a specific tool based on its full documentation.

Here is the list of valid categories:
{json.dumps(list(categories))}

Analyze the following tool documentation carefully to determine:
1. Its primary functions and use cases (Categories).
2. Whether it is primarily a Command Line Interface (CLI) tool.
3. A one-sentence summary description (max 20 words).

Tool Name: {tool_title}

Tool Documentation:
{tool_content}

Return ONLY a valid JSON object with the following structure:
{{
  "categories": ["category1", "category2"],
  "is_cli": true,  // true if it's a CLI tool, false if GUI only, null if unknown
  "description": "A short one-sentence summary of the tool."
}}

- If the tool is a general utility, classify it as "utilities".
- If the tool is related to Bluetooth, RFID, or SDR, classify it as "wireless-attacks".
- If the tool is a web shell or backdoor, classify it as "post-exploitation" or "web-application-analysis".
- Do NOT return an empty list for categories unless the tool is completely unrelated.
"""
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "gpt-5-nano",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that outputs JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0
    }
    
    try:
        print(f"DEBUG: Sending request for {tool_title}...")
        req = urllib.request.Request(f"{base_url}/chat/completions", data=json.dumps(data).encode('utf-8'), headers=headers)
        with urllib.request.urlopen(req) as response:
            resp_body = response.read().decode('utf-8')
            # print(f"DEBUG: Raw response body: {resp_body[:100]}...")
            
            result = json.loads(resp_body)
            if 'choices' not in result or not result['choices']:
                print(f"DEBUG: Unexpected API response structure: {result}")
                return []
                
            content = result['choices'][0]['message']['content']
            print(f"DEBUG: LLM Content for {tool_title}: {content}")

            # Clean up markdown code blocks if present
            if "```" in content:
                match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', content, re.DOTALL)
                if match:
                    return json.loads(match.group(1))
            
            # Try parsing directly
            try:
                return json.loads(content)
            except json.JSONDecodeError:
                print(f"DEBUG: Failed to parse JSON from LLM. Content was:\n{content}\n---End Content---")
                # Attempt to find a dict pattern even without code blocks
                match = re.search(r'\{.*\}', content, re.DOTALL)
                if match:
                    try:
                        return json.loads(match.group(0))
                    except:
                        pass
                return {}

    except urllib.error.HTTPError as e:
        print(f"LLM HTTP Error for {tool_title}: {e.code} {e.reason}")
        try:
            print(f"Server response: {e.read().decode('utf-8')}")
        except:
            pass
        return {}
    except Exception as e:
        print(f"LLM Error for {tool_title}: {e}")
        import traceback
        traceback.print_exc()
        return {}

def slugify(text):
    """Simple slugify function."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def get_git_info(repo_path):
    """Extracts git info from the source repo."""
    info = {
        "url": "unknown",
        "commit": "unknown",
        "branch": "unknown"
    }
    try:
        # Get remote URL
        result = subprocess.run(['git', '-C', repo_path, 'config', '--get', 'remote.origin.url'], capture_output=True, text=True)
        if result.returncode == 0:
            info['url'] = result.stdout.strip()
        
        # Get current commit hash
        result = subprocess.run(['git', '-C', repo_path, 'rev-parse', 'HEAD'], capture_output=True, text=True)
        if result.returncode == 0:
            info['commit'] = result.stdout.strip()
            
        # Get current branch
        result = subprocess.run(['git', '-C', repo_path, 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True)
        if result.returncode == 0:
            info['branch'] = result.stdout.strip()
            
    except Exception as e:
        print(f"Warning: Failed to get git info: {e}")
        
    return info

def parse_front_matter(content):
    """
    Parses YAML-like front matter without external dependencies.
    Supports:
    key: value
    key: [list, items]
    key:
      - item1
      - item2
    """
    fm = {}
    if not content.startswith('---'):
        return fm, content

    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
            return fm, content
        
        yaml_text = parts[1]
        body = parts[2]
        
        current_list_key = None
        
        for line in yaml_text.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            # List item: - value
            if line.startswith('- '):
                if current_list_key:
                    val = line[2:].strip()
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    fm[current_list_key].append(val)
                continue
            
            # Key: Value or Key: [List]
            if ':' in line:
                key, val = line.split(':', 1)
                key = key.strip()
                val = val.strip()
                
                if val == '':
                    current_list_key = key
                    fm[key] = []
                elif val.startswith('[') and val.endswith(']'):
                    # Inline list
                    items = val[1:-1].split(',')
                    fm[key] = [item.strip().strip('"\'') for item in items if item.strip()]
                    current_list_key = None
                else:
                    # Simple value
                    if val.startswith('"') and val.endswith('"'):
                        val = val[1:-1]
                    elif val.startswith("'") and val.endswith("'"):
                        val = val[1:-1]
                    fm[key] = val
                    current_list_key = None
            else:
                current_list_key = None

        return fm, body
    except Exception as e:
        print(f"Error parsing front matter: {e}")
        return {}, content

def fix_links(content, tool_map):
    """
    Fixes relative links in the content.
    Original: [Label](../tool-name/) or [Label](../tool-name/index.md)
    Target: [Label](../tools/tool-name.md)
    """
    def replace_link(match):
        label = match.group(1)
        link = match.group(2)
        
        # Ignore external links, anchors, or absolute paths
        if link.startswith('http') or link.startswith('#') or link.startswith('/'):
            return match.group(0)
        
        # Try to identify tool ID from link
        # ../tool-name/ -> tool-name
        parts = link.split('/')
        possible_id = None
        for part in parts:
            if part in tool_map:
                possible_id = part
                break
        
        if possible_id:
            return f"[{label}](../tools/{possible_id}.md)"
        
        return match.group(0)

    # Markdown link regex: [Label](Link)
    return re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', replace_link, content)

def load_template(name):
    path = Path(TEMPLATE_DIR) / name
    if not path.exists():
        print(f"Warning: Template {name} not found at {path}")
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# --- Main Logic ---

def main():
    parser = argparse.ArgumentParser(description="ChatKali Skills Builder")
    parser.add_argument("--src", help="Source directory (kali-tools repo)")
    parser.add_argument("--out", default=DEFAULT_OUT, help="Output directory")
    parser.add_argument("--clean", action="store_true", help="Clean output directories")
    parser.add_argument("--dry-run", action="store_true", help="Dry run (no writes)")
    parser.add_argument("--limit", type=int, help="Limit number of tools processed")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    # Load Env
    load_env()

    # 1. Detect Source
    src_dir = args.src
    if not src_dir:
        # Auto-detect
        candidates = ["kali-tools", "kali-tools-master", "."]
        for c in candidates:
            if os.path.exists(os.path.join(c, "_index.md")) or os.path.exists(os.path.join(c, "nmap", "index.md")):
                src_dir = c
                break
    
    if not src_dir or not os.path.exists(src_dir):
        print("Error: Could not detect kali-tools source directory.")
        sys.exit(1)
        
    print(f"Using source directory: {src_dir}")
    git_info = get_git_info(src_dir)
    
    # 2. Prepare Output
    out_dir = Path(args.out)
    ref_dir = out_dir / "references"
    tools_dir = ref_dir / "tools"
    
    if args.clean and not args.dry_run:
        if ref_dir.exists():
            shutil.rmtree(ref_dir)
        if (out_dir / "SKILL.md").exists():
            os.remove(out_dir / "SKILL.md")
            
    if not args.dry_run:
        ref_dir.mkdir(parents=True, exist_ok=True)
        tools_dir.mkdir(parents=True, exist_ok=True)

    # Load Templates
    skill_tmpl = load_template("SKILL.md.template")
    cat_tmpl = load_template("category.md.template")
    tool_tmpl = load_template("tool.md.template")

    if not (skill_tmpl and cat_tmpl and tool_tmpl):
        print("Error: Missing templates.")
        sys.exit(1)

    # 3. Scan Tools
    tools = []
    tool_map = {} # id -> title
    
    # Walk through directories
    count = 0
    for root, dirs, files in os.walk(src_dir):
        if args.limit and count >= args.limit:
            break
            
        # Look for index.md or _index.md
        target_file = None
        if "index.md" in files:
            target_file = "index.md"
        elif "_index.md" in files:
            target_file = "_index.md"
            
        if not target_file:
            continue
            
        # Skip root _index.md of the repo itself if it's just the landing page
        if root == src_dir:
            continue

        file_path = os.path.join(root, target_file)
        tool_id = os.path.basename(root)
        
        if args.verbose:
            print(f"Processing {tool_id}...")
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            fm, body = parse_front_matter(content)
            
            title = fm.get('title', tool_id)
            
            # Category Inference
            categories = []
            source_type = "fallback"
            
            # 1. Explicit
            if 'categories' in fm:
                categories = fm['categories']
                source_type = "explicit"
            elif 'tags' in fm:
                categories = fm['tags']
                source_type = "explicit"
            elif 'Metapackages' in fm:
                # Parse Metapackages: "kali-linux-default kali-tools-wireless ..."
                meta = fm['Metapackages']
                if isinstance(meta, str):
                    parts = meta.split()
                    cats = []
                    for p in parts:
                        if p.startswith('kali-tools-'):
                            # Extract category name: kali-tools-wireless -> wireless
                            cat_name = p[len('kali-tools-'):]
                            cats.append(cat_name)
                    if cats:
                        categories = cats
                        source_type = "metapackages"

            # 2. Inferred (Simple heuristic if explicit missing)
            if not categories:
                # Try to find "Categories:" line in body
                match = re.search(r'\*\*Categories\*\*:\s*(.+)', body, re.IGNORECASE)
                if match:
                    cats = match.group(1).split(',')
                    categories = [c.strip() for c in cats]
                    source_type = "inferred"
            
            # 3. Fallback
            if not categories:
                categories = ["uncategorized"]
                source_type = "fallback"
                
            # Normalize categories
            if isinstance(categories, str):
                categories = [categories]
            
            # Ensure list
            categories = [str(c) for c in categories]
            
            tool_data = {
                "id": tool_id,
                "title": title,
                "categories": categories,
                "category_source": source_type,
                "content": body,
                "front_matter": fm,
                "source_path": file_path
            }
            
            tools.append(tool_data)
            tool_map[tool_id] = title
            count += 1
            
        except Exception as e:
            print(f"Failed to process {file_path}: {e}")

    # 3.5 LLM Classification for ALL Tools
    print("-" * 30)
    print(f"Starting LLM Classification for ALL tools with {MAX_WORKERS} threads...")
    
    llm_cache = load_cache()
    cache_hits = 0
    failed_list = []
    
    # Helper for threading
    def classify_worker(t_id, t_title, t_content):
        # Check cache (read-only access is thread-safe enough for this script)
        cached_data = llm_cache.get(t_id)
        # Validate cache format (must be dict with 'categories', 'is_cli', 'description')
        if cached_data and isinstance(cached_data, dict) and 'categories' in cached_data and 'is_cli' in cached_data:
            return t_id, cached_data, "cached"
        
        # Call LLM
        result = call_llm_classify(t_title, t_content, list(KALI_CATEGORIES.keys()))
        return t_id, result, "llm"

    # Create a map for easy update
    tool_map_obj = {t['id']: t for t in tools}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit tasks
        future_to_tool = {
            executor.submit(classify_worker, t['id'], t['title'], t['content']): t['id'] 
            for t in tools
        }
        
        completed_count = 0
        total_count = len(tools)
        
        for future in concurrent.futures.as_completed(future_to_tool):
            t_id = future_to_tool[future]
            completed_count += 1
            if completed_count % 10 == 0:
                print(f"Progress: {completed_count}/{total_count}")
                
            try:
                _, result, source = future.result()
                
                if result and 'categories' in result:
                    new_cats = result['categories']
                    is_cli = result.get('is_cli')
                    description = result.get('description', '')

                    # Validate
                    valid_cats = [c for c in new_cats if c in KALI_CATEGORIES]
                    if not valid_cats:
                        valid_cats = ["utilities"] # Fallback
                    
                    tool_map_obj[t_id]['categories'] = valid_cats
                    tool_map_obj[t_id]['is_cli'] = is_cli
                    tool_map_obj[t_id]['description'] = description
                    tool_map_obj[t_id]['category_source'] = f"llm-classified ({source})"
                    
                    # Update cache with full object
                    cache_entry = {
                        "categories": valid_cats,
                        "is_cli": is_cli,
                        "description": description
                    }
                    
                    if source == "cached":
                        cache_hits += 1
                    else:
                        llm_cache[t_id] = cache_entry
                else:
                    print(f"  -> Failed to classify {t_id}")
                    failed_list.append(t_id)
                    
            except Exception as exc:
                print(f"  -> Exception for {t_id}: {exc}")
                failed_list.append(f"{t_id} error: {exc}")

    # Final save
    save_cache(llm_cache)
    print(f"Classification complete. Cache hits: {cache_hits}")
    
    # Write failures
    if failed_list:
        print(f"Writing {len(failed_list)} failures to {FAILED_LOG}")
        with open(FAILED_LOG, "w", encoding="utf-8") as f:
            for item in failed_list:
                f.write(f"{item}\n")

    # 4. Organize Data
    categories_map = defaultdict(list)
    for tool in tools:
        for cat in tool['categories']:
            cat_slug = slugify(cat)
            categories_map[cat_slug].append(tool)

    # 5. Generate Files
    if not args.dry_run:
        # Helper for YAML lists
        def to_yaml_list(lst):
            return json.dumps(lst) # Simple JSON array is valid YAML flow style

        # Helper to extract Install section
        def extract_install_section(body):
            # Simple extraction: look for ## Install or similar
            match = re.search(r'(##\s+(?:Installation|Install).*?)(?=\n##|\Z)', body, re.IGNORECASE | re.DOTALL)
            if match:
                return match.group(1)
            return "*(No installation information found)*"

        # Generate Tool MDs
        for tool in tools:
            t_id = tool['id']
            t_title = tool['title']
            t_cats = tool['categories']
            t_body = tool['content']
            t_fm = tool['front_matter']
            
            # Fix links
            t_body = fix_links(t_body, tool_map)
            
            # Extract Install Section (and remove from body to avoid duplication if desired, 
            # but for now we just extract it. If we want to remove it from body, we'd need more complex logic)
            # For now, let's keep body as is, or maybe try to strip it? 
            # The template has {{CONTENT_BODY}}, so if we duplicate, it appears twice.
            # Let's try to remove it from t_body if found.
            install_section = extract_install_section(t_body)
            # t_body = t_body.replace(install_section, "") # Risky if exact match fails due to whitespace
            
            # Prepare Metadata Fields
            homepage = t_fm.get('Homepage', t_fm.get('homepage', ''))
            repo = t_fm.get('Source', t_fm.get('source', '')) # Often 'Source' in kali docs
            version = t_fm.get('Version', t_fm.get('version', ''))
            arch = t_fm.get('Architectures', t_fm.get('architectures', ''))
            license_ = t_fm.get('License', t_fm.get('license', ''))
            binaries = t_fm.get('Binaries', t_fm.get('binaries', '')) # Usually not in FM, maybe need to extract?
            metapackages = t_fm.get('Metapackages', t_fm.get('metapackages', ''))
            icon = t_fm.get('Icon', t_fm.get('icon', ''))

            # Format Lists
            cat_slugs = [slugify(c) for c in t_cats]
            
            # Generate Category Links
            cat_links = ""
            for cat in t_cats:
                cat_slug = slugify(cat)
                cat_links += f"- [{cat}](../{cat_slug}.md)\n"

            # Generate Metadata Section (Official Info)
            meta_section = ""
            for k, v in t_fm.items():
                if k.lower() not in ['title', 'categories', 'tags', 'homepage', 'source', 'version', 'architectures', 'license', 'metapackages', 'icon']:
                    meta_section += f"- **{k}**: {v}\n"

            # Fill Template
            md_content = tool_tmpl.replace("{{TOOL_ID}}", t_id) \
                                  .replace("{{TOOL_TITLE}}", t_title) \
                                  .replace("{{TOOL_CATEGORIES_YAML}}", to_yaml_list(t_cats)) \
                                  .replace("{{TOOL_CATEGORY_SLUGS_YAML}}", to_yaml_list(cat_slugs)) \
                                  .replace("{{TOOL_HOMEPAGE}}", str(homepage)) \
                                  .replace("{{TOOL_REPOSITORY}}", str(repo)) \
                                  .replace("{{TOOL_VERSION}}", str(version)) \
                                  .replace("{{TOOL_ARCHITECTURES}}", str(arch)) \
                                  .replace("{{TOOL_LICENSE}}", str(license_)) \
                                  .replace("{{TOOL_BINARIES_YAML}}", to_yaml_list(binaries if isinstance(binaries, list) else [binaries] if binaries else [])) \
                                  .replace("{{TOOL_METAPACKAGES_YAML}}", to_yaml_list(metapackages if isinstance(metapackages, list) else [metapackages] if metapackages else [])) \
                                  .replace("{{TOOL_ICON}}", str(icon)) \
                                  .replace("{{SOURCE_PATH}}", tool['source_path']) \
                                  .replace("{{SOURCE_COMMIT}}", git_info['commit']) \
                                  .replace("{{GENERATED_AT}}", datetime.now().isoformat()) \
                                  .replace("{{CATEGORY_LINKS}}", cat_links) \
                                  .replace("{{TOOL_HOMEPAGE_LINK}}", f"[{homepage}]({homepage})" if homepage else "") \
                                  .replace("{{TOOL_REPOSITORY_LINK}}", f"[{repo}]({repo})" if repo else "") \
                                  .replace("{{TOOL_BINARIES_INLINE}}", str(binaries)) \
                                  .replace("{{TOOL_METAPACKAGES_INLINE}}", str(metapackages)) \
                                  .replace("{{TOOL_ICON_INLINE}}", str(icon)) \
                                  .replace("{{TOOL_INSTALL_SECTION}}", install_section) \
                                  .replace("{{METADATA_SECTION}}", meta_section) \
                                  .replace("{{CONTENT_BODY}}", t_body)

            with open(tools_dir / f"{t_id}.md", 'w', encoding='utf-8') as f:
                f.write(md_content)

        # Generate Category MDs
        for cat_slug, cat_tools in categories_map.items():
            # Find a display name
            display_name = cat_slug
            for t in cat_tools:
                for c in t['categories']:
                    if slugify(c) == cat_slug:
                        display_name = c
                        break
                if display_name != cat_slug:
                    break
            
            # Sort tools: CLI first, then by ID
            # is_cli might be None, False, or True. Treat None as False.
            cat_tools.sort(key=lambda x: (not x.get('is_cli', False), x['id']))

            # Generate Table Rows
            table_rows = ""
            for t in cat_tools:
                # Try to find binaries in FM
                bins = t['front_matter'].get('Binaries', '')
                if isinstance(bins, list):
                    bins = ", ".join(bins)
                
                is_cli = t.get('is_cli', False)
                cli_mark = "✅" if is_cli else "❌"
                desc = t.get('description', '')
                # Escape pipes in description just in case
                desc = desc.replace("|", "\|")

                table_rows += f"| {t['title']} | {cli_mark} | {desc} | {bins} | {t['category_source']} | [View](tools/{t['id']}.md) |\n"

            md_content = cat_tmpl.replace("{{CATEGORY_NAME}}", display_name) \
                                 .replace("{{CATEGORY_SLUG}}", cat_slug) \
                                 .replace("{{CATEGORY_ALIASES_YAML}}", "[]") \
                                 .replace("{{TOOLS_COUNT}}", str(len(cat_tools))) \
                                 .replace("{{GENERATED_AT}}", datetime.now().isoformat()) \
                                 .replace("{{SOURCE_COMMIT}}", git_info['commit']) \
                                 .replace("{{CATEGORY_DESCRIPTION}}", KALI_CATEGORIES.get(cat_slug, f"Tools related to {display_name}.")) \
                                 .replace("{{TOOL_TABLE_ROWS}}", table_rows)
            
            with open(ref_dir / f"{cat_slug}.md", 'w', encoding='utf-8') as f:
                f.write(md_content)

        # Generate SKILL.md
        skill_content = "---\n"
        skill_content += "name: kali-tools\n"
        skill_content += "description: Comprehensive reference for Kali Linux tools. Use this skill to find, understand, and use security tools in Kali Linux. It provides a categorized index of all available tools.\n"
        # Generate SKILL.md
        cat_rows = ""
        for cat_slug, cat_tools in sorted(categories_map.items()):
            display_name = cat_slug # Simplified
            # Try to get better display name
            for t in cat_tools:
                 for c in t['categories']:
                    if slugify(c) == cat_slug:
                        display_name = c
                        break
            # Aliases placeholder
            aliases_str = display_name 
            description = KALI_CATEGORIES.get(cat_slug, "")
            cat_rows += f"| {display_name} | {description} | {aliases_str} | {len(cat_tools)} | [View](references/{cat_slug}.md) |\n"
            
        tool_index_rows = ""
        for tool in sorted(tools, key=lambda x: x['id']):
            cats_str = ", ".join(tool['categories'])
            tool_index_rows += f"| {tool['id']} | {tool['title']} | {cats_str} | [View](references/tools/{tool['id']}.md) |\n"

        uncategorized_count = len(categories_map.get('uncategorized', []))
        multi_cat_count = sum(1 for t in tools if len(t['categories']) > 1)

        skill_content = skill_tmpl.replace("{{SOURCE_REPO_URL}}", git_info['url']) \
                                  .replace("{{SOURCE_DIR}}", str(src_dir)) \
                                  .replace("{{SOURCE_COMMIT}}", git_info['commit']) \
                                  .replace("{{SOURCE_BRANCH}}", git_info['branch']) \
                                  .replace("{{GENERATED_AT}}", datetime.now().isoformat()) \
                                  .replace("{{GENERATED_BY}}", GENERATED_BY) \
                                  .replace("{{TOOLS_TOTAL}}", str(len(tools))) \
                                  .replace("{{CATEGORIES_TOTAL}}", str(len(categories_map))) \
                                  .replace("{{MULTI_CATEGORY_TOOLS}}", str(multi_cat_count)) \
                                  .replace("{{UNCATEGORIZED_TOOLS}}", str(uncategorized_count)) \
                                  .replace("{{CATEGORY_SLUG}}", "uncategorized") \
                                  .replace("{{TOOL_ID}}", "nmap") \
                                  .replace("{{CATEGORY_TABLE_ROWS}}", cat_rows) \
                                  .replace("{{TOOL_INDEX_ROWS}}", tool_index_rows)
        
        with open(out_dir / "SKILL.md", 'w', encoding='utf-8') as f:
            f.write(skill_content)

        # Removed JSON Metadata generation as requested

    # 6. Statistics
    print("-" * 30)
    print("Build Statistics:")
    print(f"Tools Total: {len(tools)}")
    print(f"Categories Total: {len(categories_map)}")
    
    uncategorized_count = len(categories_map.get('uncategorized', []))
    print(f"Tools Uncategorized: {uncategorized_count}")
    
    multi_cat_count = sum(1 for t in tools if len(t['categories']) > 1)
    print(f"Multi-category Tools: {multi_cat_count}")
    
    if args.limit and count >= args.limit:
        print(f"(Stopped after limit {args.limit})")

if __name__ == "__main__":
    main()
