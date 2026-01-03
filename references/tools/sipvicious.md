---
tool_id: sipvicious
title: sipvicious
categories: ["information-gathering", "vulnerability-analysis", "password-attacks", "sniffing-spoofing"]
category_slugs: ["information-gathering", "vulnerability-analysis", "password-attacks", "sniffing-spoofing"]
homepage: https://github.com/EnableSecurity/sipvicious
repository: 
version: 0.3.3-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-passwords kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sipvicious\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.109851
---

# Tool: sipvicious (sipvicious)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [password-attacks](../password-attacks.md)
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/EnableSecurity/sipvicious](https://github.com/EnableSecurity/sipvicious) |
| Repository |  |
| Version | 0.3.3-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-passwords kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/sipvicious
- **PackagesInfo**: |
- **tools**: svmap, svwar, svcrack, svreport, svcrash.
- ****Installed size**: ** `197 KB`
- ****How to install**: ** `sudo apt install sipvicious`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# svwar -h
- **Usage**: svwar [options] target
- **examples**: []
- **svcrack -u100 -d dictionary.txt udp**: //10.0.0.1:5080
- **Options**: []
- **specify a range of numbers. example**: []
- **sip**: 999@example.org
- **Supported commands**: ['list:\tlists all scans', 'export:\texports the given scan to a given format', 'delete:\tdeletes the scan', 'stats:\tprint out some statistics of interest', 'search:\tsearch for a specific string in the user agent (svmap)']
- **svwar -e100-999 udp**: //10.0.0.1:5080
- **specify an extension or extension range  example**: -e


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## svmap Usage Example

Scan the given network range (`192.168.1.0/24`) and display verbose output (`-v`):

```console
root@kali:~# svmap 192.168.1.0/24 -v
INFO:DrinkOrSip:trying to get self ip .. might take a while
INFO:root:start your engines
INFO:DrinkOrSip:Looks like we received a SIP request from 192.168.1.202:5060
INFO:DrinkOrSip:Looks like we received a SIP request from 192.168.1.202:5060
INFO:DrinkOrSip:Looks like we received a SIP request from 192.168.1.202:5060
```


## Source
- Path: kali-tools\sipvicious\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.109851
