---
tool_id: rtpmixsound
title: rtpmixsound
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://www.hackingvoip.com/sec_tools.html
repository: 
version: 3.0-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\rtpmixsound\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.089853
---

# Tool: rtpmixsound (rtpmixsound)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackingvoip.com/sec_tools.html](http://www.hackingvoip.com/sec_tools.html) |
| Repository |  |
| Version | 3.0-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rtpmixsound
- **PackagesInfo**: |
- ****Installed size**: ** `231 KB`
- ****How to install**: ** `sudo apt install rtpmixsound`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rtpmixsound -h
- **Usage**: []
- **RIFF formatted WAVE file meeting these constraints**: []
- **1) header 'chunks' must be in one of two sequences**: []
- **Note**: If you are running the tool from a host with multiple
- **-f spoof factor - amount by which to**: []
- **[ range**: 0 - 80, default: 80 = output spoof ASAP ]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rtpmixsound Usage Example

Mix the given audio file (`/usr/share/rtpmixsound/stapler.wav`) through the network displaying verbose output (`-v`):

```console
root@kali:~# rtpmixsound /usr/share/rtpmixsound/stapler.wav -v
Targeting interface eth0
libfindrtp_find_rtp(): using pcap filter "ip".
State: ip_a ==  | port_a == 0 | ip_b ==  | port_b == 0
```


## Source
- Path: kali-tools\rtpmixsound\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.089853
