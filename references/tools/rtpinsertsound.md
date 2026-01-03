---
tool_id: rtpinsertsound
title: rtpinsertsound
categories: ["sniffing-spoofing", "exploitation-tools"]
category_slugs: ["sniffing-spoofing", "exploitation-tools"]
homepage: http://www.hackingvoip.com/sec_tools.html
repository: 
version: 3.0-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\rtpinsertsound\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.089451
---

# Tool: rtpinsertsound (rtpinsertsound)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackingvoip.com/sec_tools.html](http://www.hackingvoip.com/sec_tools.html) |
| Repository |  |
| Version | 3.0-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rtpinsertsound
- **PackagesInfo**: |
- ****Installed size**: ** `239 KB`
- ****How to install**: ** `sudo apt install rtpinsertsound`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rtpinsertsound -h
- **Usage**: []
- **RIFF formatted WAVE file meeting these constraints**: []
- **1) header 'chunks' must be in one of two sequences**: []
- **Note**: If you are running the tool from a host with multiple
- **-f spoof factor - amount by which to**: []
- **[ range**: 0 - 80, default: 80 = output spoof ASAP ]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rtpinsertsound Usage Example

Insert an audio file (`/usr/share/rtpinsertsound/stapler.wav`) through the network and use verbose output (`-v`):

```console
root@kali:~# rtpinsertsound /usr/share/rtpinsertsound/stapler.wav -v
Targeting interface eth0
libfindrtp_find_rtp(): using pcap filter "ip".
```


## Source
- Path: kali-tools\rtpinsertsound\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.089451
