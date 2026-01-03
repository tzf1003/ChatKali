---
tool_id: ident-user-enum
title: ident-user-enum
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://pentestmonkey.net/tools/user-enumeration/ident-user-enum
repository: 
version: 1.0-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ident-user-enum\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.942925
---

# Tool: ident-user-enum (ident-user-enum)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://pentestmonkey.net/tools/user-enumeration/ident-user-enum](https://pentestmonkey.net/tools/user-enumeration/ident-user-enum) |
| Repository |  |
| Version | 1.0-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/ident-user-enum
- **PackagesInfo**: |
- ****Installed size**: ** `12 KB`
- ****How to install**: ** `sudo apt install ident-user-enum`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ident-user-enum -h
- **ident-user-enum v1.0 ( http**: //pentestmonkey.net/tools/ident-user-enum )
- **Usage**: ident-user-enum.pl ip port [ port [ port ... ] ]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/107704.js" id="asciicast-107704" async></script>

## ident-user-enum Usage Examples

Scan the remote host (`192.168.1.13`) and determine which user is running the service on the specified ports (`22 139 445`).

```console
root@kali:~# ident-user-enum 192.168.1.13 22 139 445
ident-user-enum v1.0 ( http://pentestmonkey.net/tools/ident-user-enum )

192.168.1.13:22 root
192.168.1.13:139    root
192.168.1.13:445    root
```


## Source
- Path: kali-tools\ident-user-enum\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.942925
