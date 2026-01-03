---
tool_id: voiphopper
title: voiphopper
categories: ["sniffing-spoofing", "information-gathering"]
category_slugs: ["sniffing-spoofing", "information-gathering"]
homepage: https://sourceforge.net/projects/voiphopper
repository: 
version: 2.04-1kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: images/voiphopper-logo.svg
source_path: kali-tools\voiphopper\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.161574
---

# Tool: voiphopper (voiphopper)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/voiphopper](https://sourceforge.net/projects/voiphopper) |
| Repository |  |
| Version | 2.04-1kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | images/voiphopper-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/voiphopper
- **PackagesInfo**: |
- ****Installed size**: ** `130 KB`
- ****How to install**: ** `sudo apt install voiphopper`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# voiphopper -h
- **VoIP Hopper Extended Usage**: []
- **Miscellaneous Options**: []
- **Example**: voiphopper -i eth0 -t 2 -v 800 -m 00:80:9f:ad:42:42
- **MAC Address Spoofing Options (used with -a, -v, or -c options)**: []
- **CDP Spoof Mode (-c 1)**: []
- **Example Usage for SIP Firmware Phone**: []
- **Example Usage for SCCP Firmware Phone**: []
- **Example Usage for Phone with MAC Spoofing**: []
- **voiphopper -i eth0 -m 00**: 07:0E:EA:50:86 -c 1 -E 'SEP00070EEA5086' -P 'Port 1' -C Host -L 'Cisco IP Phone 7940' -S 'P003-08-8-00' -U 1
- **Avaya DHCP Option Mode (-a)**: []
- **VLAN Hop Mode (-v VLAN ID)**: []
- **Alcatel VLAN Discovery (-t 0|1|2)**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## voiphopper Usage Example

```console
root@kali:~# voiphopper -i eth0 -z
VoIP Hopper assessment mode ~ Select 'q' to quit and 'h' for help menu.
Main Sniffer:  capturing packets on eth0
a
Analyzing ARP packets on default interface: eth0
New host #1 learned on eth0: (MAC): 78:ca:39:fe:0b:4c   (IP): 192.168.1.229
New host #2 learned on eth0: (MAC): 60:6b:bd:5a:b6:6c   (IP): 192.168.1.213
New host #3 learned on eth0: (MAC): 40:6c:8f:1b:cb:90   (IP): 192.168.1.232
a
Disabling analysis of ARP packets on default interface:  eth0
```


## Source
- Path: kali-tools\voiphopper\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.161574
