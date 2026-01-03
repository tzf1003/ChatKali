---
tool_id: de4dot
title: de4dot
categories: ["reverse-engineering", "malware-analysis"]
category_slugs: ["reverse-engineering", "malware-analysis"]
homepage: https://github.com/0xd4d/de4dot
repository: 
version: 3.1.41592.3405-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\de4dot\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.863630
---

# Tool: de4dot (de4dot)

## Categories
- [reverse-engineering](../reverse-engineering.md)
- [malware-analysis](../malware-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/0xd4d/de4dot](https://github.com/0xd4d/de4dot) |
| Repository |  |
| Version | 3.1.41592.3405-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://salsa.debian.org/pkg-security-team/de4dot
- **PackagesInfo**: |
- ****Installed size**: ** `1.40 MB`
- ****How to install**: ** `sudo apt install de4dot`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# de4dot -h
- **Latest version and source code**: https://github.com/0xd4d/de4dot
- **Options**: []
- **Default string decrypter method token or [type**: :][name][(args,...)]
- **Preserve rids in table**: tr (TypeRef), td (TypeDef), fd (Field), md (Method), pd (Param), mr (MemberRef), s (StandAloneSig), ed (Event), pr (Property), ts (TypeSpec), ms (MethodSpec), all (all previous tables). Use - to disable (eg. all,-pd). Can be combined: ed,fd,md
- **File options**: []
- **--strtok METHOD  String decrypter method token or [type**: :][name][(args,...)]
- **Deobfuscator options**: []
- **--co-name REGEX  Valid name regex pattern (!^(get_|set_|add_|remove_)?[A-Z]{1,3}(?**: `\d+)?$&!^(get_|set_|add_|remove_)?c[0-9a-f]{32}(?:`\d+)?$&^[\u2E80-\u9FFFa-zA-Z_<{$][\u2E80-\u9FFFa-zA-Z_0-9<>{}$.`-]*$)
- **--df-name REGEX  Valid name regex pattern (!^(?**: eval_)?[a-z][a-z0-9]{0,2}$&!^A_[0-9]+$&^[\u2E80-\u9FFFa-zA-Z_<{$][\u2E80-\u9FFFa-zA-Z_0-9<>{}$.`-]*$)
- **--go-name REGEX  Valid name regex pattern (!^[A-Za-z]{1,2}(?**: `\d+)?$&^[\u2E80-\u9FFFa-zA-Z_<{$][\u2E80-\u9FFFa-zA-Z_0-9<>{}$.`-]*$)
- **Use '!' if you want to invert the regex. Example**: !^[a-z\d]{1,2}$&!^[A-Z]_\d+$&^[\w.]+$
- **Examples**: []
- **de4dot.exe -r c**: \my\files -ro c:\my\output


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\de4dot\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.863630
