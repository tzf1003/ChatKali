---
tool_id: oscanner
title: oscanner
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://www.cqure.net/wp/tools/database/oscanner/
repository: 
version: 1.0.6-1kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/oscanner-logo.svg
source_path: kali-tools\oscanner\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.032172
---

# Tool: oscanner (oscanner)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.cqure.net/wp/tools/database/oscanner/](http://www.cqure.net/wp/tools/database/oscanner/) |
| Repository |  |
| Version | 1.0.6-1kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/oscanner-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/oscanner
- **PackagesInfo**: |
- **of plugins that currently do**: ['Sid Enumeration', 'Passwords tests (common & dictionary)', 'Enumerate Oracle version', 'Enumerate account roles', 'Enumerate account privileges', 'Enumerate account hashes', 'Enumerate audit information', 'Enumerate password policies', 'Enumerate database links']
- ****Installed size**: ** `1.46 MB`
- ****How to install**: ** `sudo apt install oscanner`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# oscanner -h


## Documentation (Upstream)
-----------------------------------
 	OracleScanner -s <ip> -r <repfile> [options]
 		-s	<servername>
 		-f	<serverlist>
 		-P	<portnr>
 		-v	be verbose
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## oscanner Usage Example

Scan the target server (`-s 192.168.1.15`) on port 1040 (`-P 1040`):

```console
root@kali:~# oscanner -s 192.168.1.15 -P 1040
Oracle Scanner 1.0.6 by patrik@cqure.net
--------------------------------------------------
[-] Checking host 192.168.1.15
[x] Failed to enumerate sids from host
[-] Loading services/sids from service file
```


## Source
- Path: kali-tools\oscanner\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.032172
