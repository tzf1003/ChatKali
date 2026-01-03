---
tool_id: ohrwurm
title: ohrwurm
categories: ["vulnerability-analysis", "utilities"]
category_slugs: ["vulnerability-analysis", "utilities"]
homepage: http://mazzoo.de/blog/2006/08/25#ohrwurm
repository: 
version: 0.1-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ohrwurm\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.024481
---

# Tool: ohrwurm (ohrwurm)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://mazzoo.de/blog/2006/08/25#ohrwurm](http://mazzoo.de/blog/2006/08/25#ohrwurm) |
| Repository |  |
| Version | 0.1-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/ohrwurm
- **PackagesInfo**: |
- **Features**: ['reads SIP messages to get information of the RTP port']
- ****Installed size**: ** `33 KB`
- ****How to install**: ** `sudo apt install ohrwurm`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ohrwurm -h
- **usage**: ohrwurm -a <IP target a> -b <IP target b> [-s <randomseed>] [-e <bit error ratio in %>] [-i <interface>] [-A <RTP port a> -B <RTP port b>]
- **-s <integer> randomseed (default**: read from /dev/urandom)
- **-e <double> bit error ratio in % (default**: 1.230000)
- **-i <interfacename> network interface (default**: eth0)
- **-t suppress RTCP packets (default**: dont suppress)
- **note**: using -A and -B skips SIP sniffing, any RTP can be fuzzed


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## ohrwurm Usage Example

Fuzz two hosts (`-a 192.168.1.123 -b 192.168.1.15`), both on port 6970 (`-A 6970 -B 6970`), through interface eth0 (`-i eth0`):

```console
root@kali:~# ohrwurm -a 192.168.1.123 -b 192.168.1.15 -A 6970 -B 6970 -i eth0
ohrwurm-0.1
using random seed 2978455466
```


## Source
- Path: kali-tools\ohrwurm\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.024481
