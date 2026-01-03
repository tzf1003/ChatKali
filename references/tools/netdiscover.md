---
tool_id: netdiscover
title: netdiscover
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/netdiscover-scanner/netdiscover
repository: 
version: 0.21-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/netdiscover-logo.svg
source_path: kali-tools\netdiscover\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.009186
---

# Tool: netdiscover (netdiscover)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/netdiscover-scanner/netdiscover](https://github.com/netdiscover-scanner/netdiscover) |
| Repository |  |
| Version | 0.21-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/netdiscover-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/netdiscover
- **PackagesInfo**: |
- ****Installed size**: ** `3.08 MB`
- ****How to install**: ** `sudo apt install netdiscover`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# netdiscover --help
- **Written by**: Jaime Penalba <jpenalbae@gmail.com>
- **Usage**: netdiscover [-i device] [-r range | -l file | -p] [-m file] [-F filter] [-s time] [-c count] [-n node] [-dfPLNS]
- **-i device**: your network device
- **-r range**: scan a given range instead of auto scan. 192.168.6.0/24,/16,/8
- **-l file**: scan the list of ranges contained into the given file
- **-p passive mode**: do not send anything, only sniff
- **-m file**: scan a list of known MACs and host names
- **-F filter**: customize pcap filter expression (default: "arp")
- **-s time**: time to sleep between each ARP request (milliseconds)
- **-c count**: number of times to send each ARP request (for nets with packet loss)
- **-n node**: last source IP octet used for scanning (from 2 to 253)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\netdiscover\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.009186
