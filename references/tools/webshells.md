---
tool_id: webshells
title: webshells
categories: ["post-exploitation"]
category_slugs: ["post-exploitation"]
homepage: https://www.kali.org
repository: 
version: 1.1+kali8
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web"]
icon: images/webshells-logo.svg
source_path: kali-tools\webshells\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.166558
---

# Tool: webshells (webshells)

## Categories
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.kali.org](https://www.kali.org) |
| Repository |  |
| Version | 1.1+kali8 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web |
| Icon | images/webshells-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/webshells
- **PackagesInfo**: |
- ****Installed size**: ** `71 KB`
- ****How to install**: ** `sudo apt install webshells`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# webshells -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Webshells Usage Examples

```console
root@kali:~# tree /usr/share/webshells/
/usr/share/webshells/
├── asp
│   ├── cmd-asp-5.1.asp
│   └── cmdasp.asp
├── aspx
│   └── cmdasp.aspx
├── cfm
│   └── cfexec.cfm
├── jsp
│   ├── cmdjsp.jsp
│   └── jsp-reverse.jsp
├── perl
│   ├── perlcmd.cgi
│   └── perl-reverse-shell.pl
└── php
    ├── findsock.c
    ├── php-backdoor.php
    ├── php-findsock-shell.php
    ├── php-reverse-shell.php
    ├── qsd-php-backdoor.php
    └── simple-backdoor.php

6 directories, 14 files
root@kali:~#
```


## Source
- Path: kali-tools\webshells\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.166558
