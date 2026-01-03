---
tool_id: arjun
title: arjun
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://github.com/s0md3v/Arjun
repository: 
version: 2.2.7-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\arjun\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.787893
---

# Tool: arjun (arjun)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/s0md3v/Arjun](https://github.com/s0md3v/Arjun) |
| Repository |  |
| Version | 2.2.7-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/arjun
- **PackagesInfo**: |
- **http**: //api.example.com/v1/userinfo?id=751634589
- **Some features**: ['Supports GET/POST/POST-JSON/POST-XML requests;', 'Automatically handles rate limits and timeouts;', 'Export results to: BurpSuite, text or JSON file;', 'Import targets from: BurpSuite, text file or a raw request file;', 'Can passively extract parameters from JS or 3 external sources.']
- ****Installed size**: ** `348 KB`
- ****How to install**: ** `sudo apt install arjun`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# arjun -h
- **usage**: arjun [-h] [-u URL] [-o JSON_FILE] [-oT TEXT_FILE] [-oB [BURP_PROXY]]
- **options**: []
- **-oB [BURP_PROXY]      Output to Burp Suite Proxy. Default is 127.0.0.1**: 8080.
- **-d DELAY              Delay between requests in seconds. (default**: 0)
- **-t THREADS            Number of concurrent threads. (default**: 5)
- **-w WORDLIST           Wordlist file path. (default**: {arjundir}/db/large.txt)
- **-m METHOD             Request method to use**: GET/POST/XML/JSON. (default:
- **-T TIMEOUT            HTTP request timeout in seconds. (default**: 15)
- **(default**: 9999)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\arjun\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.787893
