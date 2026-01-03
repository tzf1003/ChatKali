---
tool_id: reaver
title: reaver
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/t6x/reaver-wps-fork-t6x
repository: 
version: 1.6.6-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless"]
icon: images/reaver-logo.svg
source_path: kali-tools\reaver\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.074005
---

# Tool: reaver (reaver)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/t6x/reaver-wps-fork-t6x](https://github.com/t6x/reaver-wps-fork-t6x) |
| Repository |  |
| Version | 1.6.6-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless |
| Icon | images/reaver-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/reaver
- **PackagesInfo**: |
- ****Installed size**: ** `851 KB`
- ****How to install**: ** `sudo apt install reaver`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wash -h
- **Required Arguments**: []
- **Optional Arguments**: []
- **Advanced Options**: []
- **-r, --recurring-delay=<x**: y>     Sleep for y seconds every x pin attempts
- **Example**: []
- **reaver -i wlan0mon -b 00**: 90:4C:C1:AC:21 -vv


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## wash Usage Example

Scan for networks using the monitor mode interface (`-i wlan0mon`) on channel 6 (`-c 6`), while ignoring frame checksum errors (`-C`):

```console
root@kali:~# wash -i wlan0mon -c 6 -C
BSSID               Ch  dBm  WPS  Lck  Vendor    ESSID
--------------------------------------------------------------------------------
E0:3F:49:6A:57:78    6  -73  1.0  No   Unknown   ASUS
```

## reaver Usage Example

Use the monitor mode interface (`-i mon0`) to attack the access point (`-b E0:3F:49:6A:57:78`), displaying verbose output (`-v`):

```console
root@kali:~# reaver -i wlan0mon -b E0:3F:49:6A:57:78 -v

Reaver v1.6.5 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Waiting for beacon from E0:3F:49:6A:57:78
[+] Associated with E0:3F:49:6A:57:78 (ESSID: ASUS)
[+] Trying pin 12345670
```


## Source
- Path: kali-tools\reaver\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.074005
