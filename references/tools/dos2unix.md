---
tool_id: dos2unix
title: dos2unix
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://waterlan.home.xs4all.nl/dos2unix.html
repository: 
version: 7.5.2-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dos2unix\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.875637
---

# Tool: dos2unix (dos2unix)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://waterlan.home.xs4all.nl/dos2unix.html](https://waterlan.home.xs4all.nl/dos2unix.html) |
| Repository |  |
| Version | 7.5.2-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/dos2unix
- **PackagesInfo**: |
- **at the end of each line**: CR (carriage return) followed by LF (line
- ****Installed size**: ** `1.82 MB`
- ****How to install**: ** `sudo apt install dos2unix`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# unix2mac -h
- **Usage**: unix2mac [options] [file ...] [-n infile outfile ...]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## unix2dos Usage Example

```console
root@kali:~# unix2dos -n unix.txt dos.txt
unix2dos: converting file unix.txt to file dos.txt in DOS format ...
```

## unix2mac Usage Example

```console
root@kali:~# unix2mac -n unix.txt mac.txt
unix2mac: converting file unix.txt to file mac.txt in Mac format ...
```

## dos2unix Usage Example

```console
root@kali:~# dos2unix -n dos.txt unix2.txt
dos2unix: converting file dos.txt to file unix2.txt in Unix format ...
```

## mac2unix Usage Example

```console
root@kali:~# mac2unix -n mac.txt unix3.txt
mac2unix: converting file mac.txt to file unix3.txt in Unix format ...
```


## Source
- Path: kali-tools\dos2unix\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.875637
