---
tool_id: proxychains-ng
title: proxychains-ng
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/rofl0r/proxychains-ng
repository: 
version: 4.17-3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web"]
icon: images/proxychains-ng-logo.svg
source_path: kali-tools\proxychains-ng\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.058727
---

# Tool: proxychains-ng (proxychains-ng)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/rofl0r/proxychains-ng](https://github.com/rofl0r/proxychains-ng) |
| Repository |  |
| Version | 4.17-3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web |
| Icon | images/proxychains-ng-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/proxychains-ng
- **PackagesInfo**: |
- ****Installed size**: ** `67 KB`
- ****How to install**: ** `sudo apt install proxychains4`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# proxychains4-daemon -h
- **Usage**: proxychains4 -q -f config_file program_name [arguments]
- **for example**: proxychains telnet somehost.com


## Documentation (Upstream)
-----------------------------
 usage: proxychains4-daemon -i listenip -p port -r remotesubnet
 all arguments are optional.
 by default listenip is 127.0.0.1, port 1053 and remotesubnet 224.
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\proxychains-ng\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.058727
