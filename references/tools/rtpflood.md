---
tool_id: rtpflood
title: rtpflood
categories: ["sniffing-spoofing"]
category_slugs: ["sniffing-spoofing"]
homepage: http://www.hackingvoip.com/sec_tools.html
repository: 
version: 1.0-1kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\rtpflood\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.089027
---

# Tool: rtpflood (rtpflood)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackingvoip.com/sec_tools.html](http://www.hackingvoip.com/sec_tools.html) |
| Repository |  |
| Version | 1.0-1kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rtpflood
- **PackagesInfo**: |
- ****Installed size**: ** `26 KB`
- ****How to install**: ** `sudo apt install rtpflood`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rtpflood -h
- **usage**: rtpflood sourcename destinationname srcport destport numpackets seqno timestamp SSID


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rtpflood Usage Example

Flood from the source IP (`192.168.1.202`) to the target IP (`192.168.1.1`) with source port 5060 (`5060`) and destination port 5061 (`5061`) using 1000 packets (`1000`) with the specified sequence number (`3`), timestamp (`123456789`), and SSID (`kali`):

```console
root@kali:~# rtpflood 192.168.1.202 192.168.1.1 5060 5061 1000 3 123456789 kali

Will flood port 5061 from port 5060 1000 times
Using sequence_number 3 timestamp 123456789 SSID 0

We have IP_HDRINCL

Number of Packets sent:

Sent 289 160 286
```


## Source
- Path: kali-tools\rtpflood\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.089027
