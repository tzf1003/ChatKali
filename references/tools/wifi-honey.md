---
tool_id: wifi-honey
title: wifi-honey
categories: ["wireless-attacks", "defensive-tools"]
category_slugs: ["wireless-attacks", "defensive-tools"]
homepage: https://www.digininja.org/projects/wifi_honey.php
repository: 
version: 1.0-1kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-802-11 kali-tools-sniffing-spoofing kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\wifi-honey\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.171555
---

# Tool: wifi-honey (wifi-honey)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [defensive-tools](../defensive-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.digininja.org/projects/wifi_honey.php](https://www.digininja.org/projects/wifi_honey.php) |
| Repository |  |
| Version | 1.0-1kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-802-11 kali-tools-sniffing-spoofing kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/wifi-honey
- **PackagesInfo**: |
- ****Installed size**: ** `16 KB`
- ****How to install**: ** `sudo apt install wifi-honey`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wifi-honey --help


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## wifi-honey Usage Example

Broadcast the given ESSID (`FreeWiFi`) on channel 6 (`6`) using the wireless interface (`wlan0`):

```console
root@kali:~# wifi-honey FreeWiFi 6 wlan0
```


## Source
- Path: kali-tools\wifi-honey\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.171555
