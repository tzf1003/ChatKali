---
tool_id: u-boot
title: u-boot
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.denx.de/wiki/U-Boot/
repository: 
version: 2022.04+dfsg-2
architectures: linux-any all
license: 
binaries: []
metapackages: ["kali-linux-arm kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\u-boot\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.149141
---

# Tool: u-boot (u-boot)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.denx.de/wiki/U-Boot/](https://www.denx.de/wiki/U-Boot/) |
| Repository |  |
| Version | 2022.04+dfsg-2 |
| Architectures | linux-any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-arm kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://salsa.debian.org/debian/u-boot
- **PackagesInfo**: |
- ****Installed size**: ** `758 KB`
- ****How to install**: ** `sudo apt install u-boot-tools`
- **Included platforms**: []
- **images in various formats**: ['mkimage', 'dumpimage', 'mksunxiboot', 'mkenvimage']
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# mkimage -h
- **dumpimage**: invalid option -- '-'
- **Usage**: mkimage [-T type] -l image
- **-b <image>**: boot <image> with preamble (Kirkwood, Avanta, Armada 370/XP/375/38x/39x)
- **-D <image>**: boot <image> without preamble (Dove)
- **-b**: enter xmodem boot mode
- **-d**: enter console debug mode
- **-a**: use timings for Armada XP
- **-s <resp-timeo>**: use specific response-timeout
- **-o <block-timeo>**: use specific xmodem block timeout
- **-t**: mini terminal
- **-B <baud>**: set baud rate
- **Options**: []
- **mkimage**: invalid option -- 'h'
- **Error**: Invalid option
- **mkimage [-x] -A arch -O os -T type -C comp -a addr -e ep -n name -d data_file[**: data_file...] image
- **Signing / verified boot options**: ['-k keydir] [-K dtb] [ -c <comment>] [-p addr] [-r] [-N engine']


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\u-boot\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.149141
