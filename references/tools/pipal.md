---
tool_id: pipal
title: pipal
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://www.digininja.org/projects/pipal.php
repository: 
version: 3.4.0-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-reporting"]
icon: images/pipal-logo.svg
source_path: kali-tools\pipal\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.049748
---

# Tool: pipal (pipal)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.digininja.org/projects/pipal.php](https://www.digininja.org/projects/pipal.php) |
| Repository |  |
| Version | 3.4.0-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-reporting |
| Icon | images/pipal-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/pipal
- **PackagesInfo**: |
- ****Installed size**: ** `243 KB`
- ****How to install**: ** `sudo apt install pipal`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pipal -h
- **pipal 3.4.0 Robin Wood (robin@digi.ninja) (http**: //digi.ninja)
- **Usage**: pipal [OPTION] ... FILENAME
- **--help, -h, -?**: show help
- **--top, -t X**: show the top X results (default 10)
- **--output, -o <filename>**: output to file
- **--gkey <Google Maps API key>**: to allow zip code lookups (optional)
- **--list-checkers**: Show the available checkers and which are enabled
- **--verbose, -v**: Verbose
- **FILENAME**: The file to count


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## pipal Usage Example

Analyze and display the top 5 passwords (`-t 5`), using the given file as input (`/usr/share/wordlists/nmap.lst`):

```console
root@kali:~# pipal -t 5 /usr/share/wordlists/nmap.lst
Generating stats, hit CTRL-C to finish early and dump stats on words already processed.
Please wait...
Processing:    100% |ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo| Time: 00:00:04


Total entries = 5085
Total unique entries = 5076

Top 5 passwords
#!comment:  *                                                                         * = 10 (0.2%)
cabrera = 1 (0.02%)
#!comment:  * The Nmap Security Scanner is (C) 1996-2010 Insecure.Com LLC. Nmap is    * = 1 (0.02%)
#!comment:  * also a registered trademark of Insecure.Com LLC.  This program is free  * = 1 (0.02%)
#!comment:  * software; you may redistribute and/or modify it under the terms of the  * = 1 (0.02%)

Top 5 base words
love = 26 (0.51%)
angel = 22 (0.43%)
password = 18 (0.35%)
soccer = 18 (0.35%)
princess = 13 (0.26%)

Password length (length ordered)
3 = 1 (0.02%)
4 = 11 (0.22%)
5 = 434 (8.53%)
6 = 1863 (36.64%)
7 = 1219 (23.97%)
8 = 865 (17.01%)
9 = 387 (7.61%)
10 = 156 (3.07%)
11 = 41 (0.81%)
12 = 13 (0.26%)
13 = 7 (0.14%)
14 = 1 (0.02%)
15 = 1 (0.02%)
16 = 1 (0.02%)
17 = 1 (0.02%)
87 = 83 (1.63%)
88 = 1 (0.02%)
```


## Source
- Path: kali-tools\pipal\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.049748
