---
tool_id: massdns
title: massdns
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/blechschmidt/massdns
repository: 
version: 1.0.0-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\massdns\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.983609
---

# Tool: massdns (massdns)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/blechschmidt/massdns](https://github.com/blechschmidt/massdns) |
| Repository |  |
| Version | 1.0.0-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/massdns
- **PackagesInfo**: |
- ****Installed size**: ** `101 KB`
- ****How to install**: ** `sudo apt install massdns`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# massdns -h
- **Usage**: massdns [options] [domainlist]
- **-b  --bindto           Bind to IP address and port. (Default**: 0.0.0.0:0)
- **-c  --resolve-count    Number of resolves for a name before giving up. (Default**: 50)
- **--drop-group       Group to drop privileges to when running as root. (Default**: nogroup)
- **--drop-user        User to drop privileges to when running as root. (Default**: nobody)
- **domain. (Default**: 500)
- **-l  --error-log        Error log file path. (Default**: /dev/stderr)
- **--processes        Number of processes to be used for resolving. (Default**: 1)
- **--retry            Unacceptable DNS response codes. (Default**: REFUSED)
- **-s  --hashmap-size     Number of concurrent lookups. (Default**: 10000)
- **--status-format    Format for real-time status updates, json or ansi (Default**: ansi)
- **--socket-count     Socket count per process. (Default**: 1)
- **-t  --type             Record type to be resolved. (Default**: A)
- **Output flags**: []
- **Advanced flags for the simple output mode**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\massdns\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.983609
