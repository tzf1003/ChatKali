---
tool_id: kalibrate-rtl
title: kalibrate-rtl
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: https://github.com/steve-m/kalibrate-rtl
repository: 
version: 0.4.1+git20191125-0kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-sdr kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\kalibrate-rtl\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.959217
---

# Tool: kalibrate-rtl (kalibrate-rtl)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/steve-m/kalibrate-rtl](https://github.com/steve-m/kalibrate-rtl) |
| Repository |  |
| Version | 0.4.1+git20191125-0kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-sdr kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/kalibrate-rtl
- **PackagesInfo**: |
- ****Installed size**: ** `62 KB`
- ****How to install**: ** `sudo apt install kalibrate-rtl`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# kal -h
- **Usage**: []
- **GSM Base Station Scan**: []
- **Clock Offset Calculation**: []
- **Where options are**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## kal Usage Example

Scan for GSM base stations in the GSM-850 band (`-s GSM850`), then use channel 128 (`-c 128`) to get the frequency offset:

```console
root@kali:~# kal -s GSM850
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Scanning for GSM-850 base stations.
GSM-850:
    chan: 128 (869.2MHz - 3.988kHz) power: 486634.32
    chan: 143 (872.2MHz - 3.760kHz) power: 56331.63

root@kali:~# kal -c 128
Found 1 device(s):
  0:  ezcap USB 2.0 DVB-T/DAB/FM dongle

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Exact sample rate is: 270833.002142 Hz
kal: Calculating clock frequency offset.
Using GSM-850 channel 128 (869.2MHz)
average     [min, max]  (range, stddev)
- 4.093kHz      [-4102, -4083]  (20, 5.314593)
overruns: 0
not found: 0
average absolute error: 4.709 ppm
```


## Source
- Path: kali-tools\kalibrate-rtl\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.959217
