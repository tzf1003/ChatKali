---
tool_id: shellter
title: shellter
categories: ["exploitation-tools", "post-exploitation"]
category_slugs: ["exploitation-tools", "post-exploitation"]
homepage: https://www.shellterproject.com/
repository: 
version: 7.2-0kali3
architectures: i386 amd64
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-post-exploitation kali-tools-windows-resources"]
icon: images/shellter-logo.svg
source_path: kali-tools\shellter\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.103954
---

# Tool: shellter (shellter)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.shellterproject.com/](https://www.shellterproject.com/) |
| Repository |  |
| Version | 7.2-0kali3 |
| Architectures | i386 amd64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-post-exploitation kali-tools-windows-resources |
| Icon | images/shellter-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/shellter
- **PackagesInfo**: |
- ****Installed size**: ** `726 KB`
- ****How to install**: ** `sudo apt install shellter`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# shellter -h
- **┃ You may need to install the wine32 package first**: []
- **ShellExecuteEx failed**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![shellter](images/shellter.png)

## shellter Usage Examples

```console
root@kali:~# dpkg --add-architecture i386
root@kali:~# apt update && apt install wine32
root@kali:~# shellter
```


## Source
- Path: kali-tools\shellter\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.103954
