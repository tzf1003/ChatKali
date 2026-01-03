---
tool_id: dhcpig
title: dhcpig
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/kamorin/DHCPig
repository: 
version: 1.6-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dhcpig\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.866531
---

# Tool: dhcpig (dhcpig)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/kamorin/DHCPig](https://github.com/kamorin/DHCPig) |
| Repository |  |
| Version | 1.6-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/dhcpig
- **PackagesInfo**: |
- ****Installed size**: ** `85 KB`
- ****How to install**: ** `sudo apt install dhcpig`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dhcpig -h
- **Doc**: []
- **http**: //github.com/kamorin/DHCPig
- **Usage**: []
- **Options**: []
- **-h, --help                     <-- you are here**: )
- **-s, --client-src               ... a list of client macs 00**: 11:22:33:44:55,00:11:22:33:44:56 (Default: <random>)
- **-O, --request-options          ... option-codes to request e.g. 21,22,23 or 12,14-19,23 (Default**: 0-80)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dhcpig Usage Example

Exhaust all of the available DHCP addresses using the eth0 interface (`eth0`):

```console
root@kali:~# pig.py eth0
WARNING: No route found for IPv6 destination :: (no default route?)

Sending DHCPDISCOVER on eth0
waiting for first DHCP Server response on eth0
```


## Source
- Path: kali-tools\dhcpig\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.866531
