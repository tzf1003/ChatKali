---
tool_id: crunch
title: crunch
categories: ["utilities", "password-attacks"]
category_slugs: ["utilities", "password-attacks"]
homepage: http://sourceforge.net/projects/crunch-wordlist/
repository: 
version: 3.6-3.1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: images/crunch-logo.svg
source_path: kali-tools\crunch\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.856200
---

# Tool: crunch (crunch)

## Categories
- [utilities](../utilities.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://sourceforge.net/projects/crunch-wordlist/](http://sourceforge.net/projects/crunch-wordlist/) |
| Repository |  |
| Version | 3.6-3.1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | images/crunch-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/crunch
- **PackagesInfo**: |
- ****Installed size**: ** `84 KB`
- ****How to install**: ** `sudo apt install crunch`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# crunch -h
- **Usage**: crunch <min> <max> [options]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## crunch Usage Example

Generate a dictionary file containing words with a minimum and maximum length of 6 (`6 6`) using the given characters (`0123456789abcdef`), saving the output to a file (`-o 6chars.txt`):

```console
root@kali:~# crunch 6 6 0123456789abcdef -o 6chars.txt
Crunch will now generate the following amount of data: 117440512 bytes
112 MB
0 GB
0 TB
0 PB
Crunch will now generate the following number of lines: 16777216
```


## Source
- Path: kali-tools\crunch\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.856200
