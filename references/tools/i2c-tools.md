---
tool_id: i2c-tools
title: i2c-tools
categories: ["utilities", "hardware-hacking"]
category_slugs: ["utilities", "hardware-hacking"]
homepage: https://www.kernel.org/pub/software/utils/i2c-tools/
repository: 
version: 4.4-2
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\i2c-tools\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.941741
---

# Tool: i2c-tools (i2c-tools)

## Categories
- [utilities](../utilities.md)
- [hardware-hacking](../hardware-hacking.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.kernel.org/pub/software/utils/i2c-tools/](https://www.kernel.org/pub/software/utils/i2c-tools/) |
| Repository |  |
| Version | 4.4-2 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/aurel32/i2c-tools
- **PackagesInfo**: |
- **This package contains a heterogeneous set of I2C tools for Linux**: a bus
- ****Installed size**: ** `50 KB`
- ****How to install**: ** `sudo apt install python3-smbus`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# i2ctransfer -h
- **Usage**: i2ctransfer [OPTIONS] I2CBUS DESC [DATA] [DESC [DATA]]...
- **MODE is one of**: []
- **OPTIONS**: -a allow even reserved addresses
- **DESC describes the transfer in the form**: {r|w}LENGTH[@address]
- **DATA are LENGTH bytes for a write message. They can be shortened by a suffix**: []
- **Example (bus 0, read 8 byte at offset 0x64 from EEPROM at 0x50)**: []
- **Example (same EEPROM, at offset 0x42 write 0xff 0xfe ... 0xf0)**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\i2c-tools\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.941741
