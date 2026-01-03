---
tool_id: berate-ap
title: berate-ap
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: https://github.com/sensepost/berate_ap
repository: 
version: 0.4.6+git20240824-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\berate-ap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.799848
---

# Tool: berate-ap (berate-ap)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sensepost/berate_ap](https://github.com/sensepost/berate_ap) |
| Repository |  |
| Version | 0.4.6+git20240824-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/berate-ap
- **PackagesInfo**: |
- ****Installed size**: ** `103 KB`
- ****How to install**: ** `sudo apt install berate-ap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# berate_ap -h
- **Usage**: berate_ap [options] <wifi-interface> [<interface-with-internet>] [<access-point-name> [<passphrase>]]
- **Options**: []
- **-c <channel>            Channel number (default**: 1)
- **Use**: 'nat' for NAT (default)
- **--ht_capab <HT>         HT capabilities (default**: [HT40+])
- **--country <code>        Set two-letter country code for regularity (example**: US)
- **--freq-band <GHz>       Set frequency band. Valid inputs**: 2.4, 5 (default: 2.4)
- **--driver                Choose your WiFi adapter driver (default**: nl80211)
- **Enterprise Options**: []
- **Name of the certs at the location**: ['hostapd.ca.pem', 'hostapd.dh.pem', 'hostapd.cert.pem', 'hostapd.key.pem']
- **--remote-radius <ip address>[**: port]
- **Mana WPE Options**: []
- **Mana/Karma Options**: []
- **MANA Other Options**: []
- **PLEASE NOTE**: This attack currently does not work with mana enabled so the correct
- **wpa_sycophant Options**: []
- **This option needs to be used in conjunction with https**: //github.com/sensepost/wpa_sycophant
- **Non-Bridging Options**: []
- **-g <gateway>            IPv4 Gateway for the Access Point (default**: 192.168.12.1)
- **Useful informations**: []
- **Examples**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\berate-ap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.799848
