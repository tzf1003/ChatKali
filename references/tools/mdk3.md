---
tool_id: mdk3
title: mdk3
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/aircrack-ng/mdk3
repository: 
version: 6.0-9
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless"]
icon: images/mdk3-logo.svg
source_path: kali-tools\mdk3\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.985585
---

# Tool: mdk3 (mdk3)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/aircrack-ng/mdk3](https://github.com/aircrack-ng/mdk3) |
| Repository |  |
| Version | 6.0-9 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless |
| Icon | images/mdk3-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/mdk3
- **PackagesInfo**: |
- **Features**: []
- ****Installed size**: ** `174 KB`
- ****How to install**: ** `sudo apt install mdk3`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# mdk3 --help
- **And with lots of help from the great aircrack-ng community**: []
- **IMPORTANT**: It is your responsibility to make sure you have permission from the
- **MDK USAGE**: []
- **TEST MODES**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## mdk3 Usage Example

Use the wireless interface (`wlan0`) to run the Authentication DoS mode test (`a`):

```console
root@kali:~# mdk3 wlan0 a

Trying to get a new target AP...
AP 9C:D3:6D:B8:FF:56 is responding!
Connecting Client: 00:00:00:00:00:00 to target AP: 9C:D3:6D:B8:FF:56
Connecting Client: 00:00:00:00:00:00 to target AP: 9C:D3:6D:B8:FF:56
AP 9C:D3:6D:B8:FF:56 seems to be INVULNERABLE!
Device is still responding with   500 clients connected!
Trying to get a new target AP...
AP E0:3F:49:6A:57:78 is responding!
Connecting Client: 00:00:00:00:00:00 to target AP: E0:3F:49:6A:57:78
AP E0:3F:49:6A:57:78 seems to be INVULNERABLE!
```


## Source
- Path: kali-tools\mdk3\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.985585
