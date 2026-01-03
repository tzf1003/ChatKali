---
tool_id: vboot-utils
title: vboot-utils
categories: ["utilities", "defensive-tools", "forensics"]
category_slugs: ["utilities", "defensive-tools", "forensics"]
homepage: https://chromium.googlesource.com/chromiumos/platform/vboot_reference
repository: 
version: 0~R106-15054.B+dfsg-0.1
architectures: amd64 arm64 armel armhf i386
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\vboot-utils\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.158432
---

# Tool: vboot-utils (vboot-utils)

## Categories
- [utilities](../utilities.md)
- [defensive-tools](../defensive-tools.md)
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://chromium.googlesource.com/chromiumos/platform/vboot_reference](https://chromium.googlesource.com/chromiumos/platform/vboot_reference) |
| Repository |  |
| Version | 0~R106-15054.B+dfsg-0.1 |
| Architectures | amd64 arm64 armel armhf i386 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/vboot-utils
- **PackagesInfo**: |
- ****Installed size**: ** `281 KB`
- ****How to install**: ** `sudo apt install vboot-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# vbutil_keyblock --help
- **Usage**: futility vbutil_keyblock <--pack|--unpack> <file> [OPTIONS]
- **Supported COMMANDs**: []
- **Global options**: []
- **The following commands are built-in**: []
- **Required parameters**: []
- **Optional**: []
- **and the verified version of u-boot. Namely**: []
- **The programs previously included in this package**: dump_fmap dump_kernel_config
- **ERROR**: You must put a test image on a USB stick and boot it in recovery mode (this means Esc+Refresh+Power, *not* Ctrl-U!) to run this
- **Valid parameters**: []
- **For more information, please see**: []
- **https**: //chromium.googlesource.com/chromiumos/docs/+/HEAD/os_config.md#crossystem
- **Options**: []
- **GET MODE**: []
- **-g, --get   (default)	Get (read) from bios_file, with following options**: []
- **SET MODE**: []
- **-s, --set            	Set (write) to bios_file, with following options**: []
- **CREATE MODE**: []
- **SAMPLE**: []
- **For '--vblock <file>', required OPTIONS are**: []
- **optional OPTIONS are**: []
- **For '--verify <file>', required OPTIONS are**: []
- **For '--verify <file>', optional OPTIONS are**: []
- **--algorithm <number>        Signing algorithm to use with key**: []
- **Optional parameters**: []
- **For '--pack <file>', required OPTIONS are**: []
- **Optional OPTIONS are**: []
- **For '--unpack <file>', optional OPTIONS are**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\vboot-utils\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.158432
