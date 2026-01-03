---
tool_id: bed
title: bed
categories: ["vulnerability-analysis", "web-application-analysis"]
category_slugs: ["vulnerability-analysis", "web-application-analysis"]
homepage: http://www.snake-basket.de
repository: 
version: 0.5-1kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability"]
icon: images/bed-logo.svg
source_path: kali-tools\bed\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.798184
---

# Tool: bed (bed)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.snake-basket.de](http://www.snake-basket.de) |
| Repository |  |
| Version | 0.5-1kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability |
| Icon | images/bed-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bed
- **PackagesInfo**: |
- ****Installed size**: ** `73 KB`
- ****How to install**: ** `sudo apt install bed`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bed -h
- **Usage**: []
- **<target>   = Host to check (default**: localhost)
- **<port>     = Port to connect to (default**: standard port)
- **<timeout>  = seconds to wait after each test (default**: 2 seconds)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## bed Usage Example

Use the HTTP plugin (`-s HTTP`) to fuzz the target server (`-t 192.168.1.15`):

```console
root@kali:~# bed -s HTTP -t 192.168.1.15

 BED 0.5 by mjm ( www.codito.de ) & eric ( www.snake-basket.de )

 + Buffer overflow testing:
        testing: 1  HEAD XAXAX HTTP/1.0
```


## Source
- Path: kali-tools\bed\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.798184
