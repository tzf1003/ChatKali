---
tool_id: usbutils
title: usbutils
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/gregkh/usbutils
repository: 
version: 1:014-1
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-arm kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\usbutils\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.157263
---

# Tool: usbutils (usbutils)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/gregkh/usbutils](https://github.com/gregkh/usbutils) |
| Repository |  |
| Version | 1:014-1 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-arm kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `325 KB`
- ****How to install**: ** `sudo apt install usbutils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# usbhid-dump -h
- **Usage**: usbhid-dump [OPTION]...
- **-s [[bus]**: ][devnum]
- **-d vendor**: ['product']
- **T**: Bus=01 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  2 Spd=12  MxCh= 0
- **D**: Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS= 8 #Cfgs=  1
- **P**: Vendor=80ee ProdID=0021 Rev=01.00
- **S**: Product=USB Tablet
- **C**: #Ifs= 1 Cfg#= 1 Atr=80 MxPwr=100mA
- **I**: If#= 0 Alt= 0 #EPs= 1 Cls=03(HID  ) Sub=00 Prot=00 Driver=usbhid
- **E**: Ad=81(I) Atr=03(Int.) MxPS=   8 Ivl=10ms
- **Options**: []
- **-s, -a, --address=bus[**: dev]      limit interfaces by bus number
- **-d, -m, --model=vid[**: pid]        limit interfaces by vendor and
- **-e, --entity=STRING              what to dump**: either "descriptor",
- **-f, --stream-feedback            enable stream dumping feedback**: for
- **Default options**: --stream-timeout=60000 --entity=descriptor
- **Signals**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\usbutils\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.157263
