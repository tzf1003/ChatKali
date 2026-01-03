---
tool_id: ubertooth
title: ubertooth
categories: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
category_slugs: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
homepage: https://github.com/greatscottgadgets/ubertooth/
repository: 
version: 2020.12.R1-0kali3
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-bluetooth kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ubertooth\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.149537
---

# Tool: ubertooth (ubertooth)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/greatscottgadgets/ubertooth/](https://github.com/greatscottgadgets/ubertooth/) |
| Repository |  |
| Version | 2020.12.R1-0kali3 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-bluetooth kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/ubertooth
- **PackagesInfo**: |
- ****Installed size**: ** `252 KB`
- ****How to install**: ** `sudo apt install ubertooth-firmware-source`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ubertooth-util -h
- **Determine the AFH map for piconet ??**: ??:22:44:66:88:
- **Main options**: []
- **-m <int> threshold for channel removal (default**: 5)
- **-r print AFH channel map once every second (default**: print on update)
- **-e maximum access code errors (default**: 2, range: 0-4)
- **Usage**: []
- **Major modes**: []
- **-p promiscuous**: sniff active connections
- **-a[address] get/set access address (example**: -a8e89bed6)
- **-s<address> faux slave mode, using MAC addr (example**: -s22:44:66:88:aa:cc)
- **-t<address> set connection following target (example**: -t22:44:66:88:aa:cc/48)
- **Interference (use with -f or -p)**: []
- **Data source**: []
- **Misc**: []
- **To update firmware, run**: []
- **Miscellaneous**: []
- **-A <index> advertising channel index (default**: 38)
- **-a <BD ADDR> Bluetooth address (default**: random)
- **For more information on Uberducky, visit**: []
- **https**: //github.com/mikeryan/uberducky
- **Options**: []
- **-l <1-48> capture length (default**: 18)
- **-a <access_code> access code (default**: 630f9ffe)
- **-w USB delay in 625us timeslots (default**: 5)
- **Example usage**: []
- **ubertooth-rx -z -t 20 -- survey mode**: discover all LAPs+UAPs for 20 seconds
- **Configuration**: []
- **-c <BT Channel> set a fixed bluetooth channel [Default**: 39]
- **-e max_ac_errors (default**: 2, range: 0-4)
- **-t <SECONDS> sniff timeout - 0 means no timeout [Default**: 0]
- **Output options**: []
- **-t scan Time (seconds) - length of time to sniff packets. [Default**: 20s]
- **NOTE**: you probably want ubertooth-specan-ui
- **Common options**: []
- **Radio options**: []
- **Range test**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\ubertooth\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.149537
