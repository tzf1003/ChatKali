---
tool_id: google-nexus-tools
title: google-nexus-tools
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/corbindavenport/nexus-tools
repository: 
version: 2.3-0kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\google-nexus-tools\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.916056
---

# Tool: google-nexus-tools (google-nexus-tools)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/corbindavenport/nexus-tools](https://github.com/corbindavenport/nexus-tools) |
| Repository |  |
| Version | 2.3-0kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/google-nexus-tools
- **PackagesInfo**: |
- ****Installed size**: ** `1.38 MB`
- ****How to install**: ** `sudo apt install google-nexus-tools`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# nexus-fastboot -h
- **-H                            - Name of adb server host (default**: localhost)
- **-P                            - Port of adb server (default**: 5037)
- **connect <host>[**: <port>]       - connect to a device via TCP/IP
- **disconnect [<host>[**: <port>]]  - disconnect from a TCP/IP device.
- **device commands**: []
- **the format is a list of lines with the following format**: []
- **forward specs are one of**: []
- **tcp**: <port>
- **localabstract**: <unix domain socket name>
- **localreserved**: <unix domain socket name>
- **localfilesystem**: <unix domain socket name>
- **dev**: <character device name>
- **jdwp**: <process pid> (remote only)
- **scripting**: []
- **adb get-state                - prints**: offline | bootloader | device
- **adb get-serialno             - prints**: <serial-number>
- **adb get-devpath              - prints**: <device-path>
- **networking**: []
- **Note**: you should not automatically start a PPP connection.
- **<tty> refers to the tty for PPP stream. Eg. dev**: /dev/omap_csmi_tty1
- **adb sync notes**: adb sync [ <directory> ]
- **<localdir> can be interpreted in several ways**: ['If <directory> is not specified, both /system and /data partitions will be updated.', 'If it is "system" or "data", only the corresponding partition']
- **environmental variables**: []
- **usage**: fastboot [ <option> ] <command>
- **commands**: []
- **flash**: raw boot <kernel> [ <ramdisk> ]    create bootimage and flash it
- **options**: []
- **-b <base_addr>                           specify a custom kernel base address. default**: 0x10000000
- **-n <page size>                           specify the nand page size. default**: 2048


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\google-nexus-tools\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.916056
