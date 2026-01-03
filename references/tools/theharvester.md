---
tool_id: theharvester
title: theharvester
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/laramies/theHarvester
repository: 
version: 4.8.2-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/theharvester-logo.svg
source_path: kali-tools\theharvester\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.142636
---

# Tool: theharvester (theharvester)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/laramies/theHarvester](https://github.com/laramies/theHarvester) |
| Repository |  |
| Version | 4.8.2-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/theharvester-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/theharvester
- **PackagesInfo**: |
- ****Installed size**: ** `1.94 MB`
- ****How to install**: ** `sudo apt install theharvester`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# theharvester -h
- **usage**: theHarvester [-h] -d DOMAIN [-l LIMIT] [-S START] [-p] [-s]
- **options**: []
- **directory**: --screenshot output_directory


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## theharvester Usage Example

Search from email addresses from a domain (`-d kali.org`), limiting the results to 500 (`-l 500`), using DuckDuckGo (`-b duckduckgo`):

```console
root@kali:~# theHarvester -d kali.org -l 500 -b duckduckgo
*******************************************************************
*  _   _                                            _             *
* | |_| |__   ___    /\  /\__ _ _ ____   _____  ___| |_ ___ _ __  *
* | __|  _ \ / _ \  / /_/ / _` | '__\ \ / / _ \/ __| __/ _ \ '__| *
* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\__ \ ||  __/ |    *
*  \__|_| |_|\___| \/ /_/ \__,_|_|    \_/ \___||___/\__\___|_|    *
*                                                                 *
* theHarvester 4.4.3                                              *
* Coded by Christian Martorella                                   *
* Edge-Security Research                                          *
* cmartorella@edge-security.com                                   *
*                                                                 *
*******************************************************************

[*] Target: kali.org

[*] Searching Duckduckgo.

[*] No IPs found.

[*] No emails found.

[*] Hosts found: 14
---------------------
[...]

```console


## Source
- Path: kali-tools\theharvester\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.142636
