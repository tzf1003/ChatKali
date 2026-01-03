---
tool_id: winexe
title: winexe
categories: ["exploitation-tools", "post-exploitation"]
category_slugs: ["exploitation-tools", "post-exploitation"]
homepage: https://sourceforge.net/projects/winexe
repository: 
version: 1.1~20140107-0kali21
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\winexe\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.174846
---

# Tool: winexe (winexe)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/winexe](https://sourceforge.net/projects/winexe) |
| Repository |  |
| Version | 1.1~20140107-0kali21 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://gitlab.com/kalilinux/packages/winexe
- **PackagesInfo**: |
- ****Installed size**: ** `158 KB`
- ****How to install**: ** `sudo apt install winexe`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# winexe -h
- **Usage**: winexe [OPTION]... //HOST COMMAND
- **Options**: []
- **--runas=[DOMAIN\]USERNAME%PASSWORD      Run as the given user (BEWARE**: []
- **--interactive=0|1                       Desktop interaction**: 0 -
- **--ostype=0|1|2                          OS type**: 0 - 32-bit, 1 - 64-bit,


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## winexe Usage Example

With the given credentials (`-U ‘Administrator%s3cr3t’`), connect to the remote server (`//192.168.1.225`), and execute the given command (`cmd.exe /c echo “this is running on windows”`):

```console
root@kali:~# winexe -U 'Administrator%s3cr3t' //192.168.1.225 'cmd.exe /c echo "this is running on windows"'
"this is running on windows"
```


## Source
- Path: kali-tools\winexe\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.174846
