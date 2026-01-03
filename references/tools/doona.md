---
tool_id: doona
title: doona
categories: ["vulnerability-analysis"]
category_slugs: ["vulnerability-analysis"]
homepage: https://github.com/wireghoul/doona
repository: 
version: 1.0+git20190108-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\doona\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.875243
---

# Tool: doona (doona)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/wireghoul/doona](https://github.com/wireghoul/doona) |
| Repository |  |
| Version | 1.0+git20190108-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/doona
- **PackagesInfo**: |
- ****Installed size**: ** `128 KB`
- ****How to install**: ** `sudo apt install doona`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# doona -h
- **Usage**: []
- **-t <target>   = Host to check (default**: localhost)
- **-p <port>     = Port to connect to (default**: module specific standard port)
- **-o <timeout>  = seconds to wait after each test (default**: 2 seconds)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## doona Usage Example

Use the HTTP plugin (`-m HTTP`) to fuzz the target (`-t 192.168.1.15`), stopping after 5 cases (`-M 5`):

```console
root@kali:~# doona -m HTTP -t 192.168.1.15 -M 5

 Doona 1.0 by Wireghoul (www.justanotherhacker.com)

 + Buffer overflow testing
    1/37   [XAXAX] ......
Max requests (5) completed, index: 5
````


## Source
- Path: kali-tools\doona\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.875243
