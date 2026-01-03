---
tool_id: enumiax
title: enumiax
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://enumiax.sourceforge.net/
repository: 
version: 0.4a-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\enumiax\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.884643
---

# Tool: enumiax (enumiax)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://enumiax.sourceforge.net/](https://enumiax.sourceforge.net/) |
| Repository |  |
| Version | 0.4a-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/enumiax
- **PackagesInfo**: |
- ****Installed size**: ** `35 KB`
- ****How to install**: ** `sudo apt install enumiax`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# enumiax --help
- **enumiax**: invalid option -- '-'
- **Usage**: enumiax [options] target
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## enumiax Usage Example

Run a dictionary attack (`-d /usr/share/wordlists/metasploit/unix_users.txt`) against the target host (`192.168.1.1`):

```console
root@kali:~# enumiax -d /usr/share/wordlists/metasploit/unix_users.txt 192.168.1.1
```


## Source
- Path: kali-tools\enumiax\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.884643
