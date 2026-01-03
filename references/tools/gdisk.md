---
tool_id: gdisk
title: gdisk
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://sourceforge.net/projects/gptfdisk/
repository: 
version: 1.0.10-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\gdisk\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.909134
---

# Tool: gdisk (gdisk)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://sourceforge.net/projects/gptfdisk/](http://sourceforge.net/projects/gptfdisk/) |
| Repository |  |
| Version | 1.0.10-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/gdisk
- **PackagesInfo**: |
- **Features**: ['Edit GUID partition table definitions', 'In place conversion of BSD disklabels to GPT', 'In place conversion of MBR to GPT', 'In place conversion of GPT to MBR', 'Create hybrid MBR/GPT layouts', 'Repair damaged GPT data structures', 'Repair damaged MBR structures', 'Back up GPT data to a file (and restore from file)']
- ****Installed size**: ** `940 KB`
- ****How to install**: ** `sudo apt install gdisk`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sgdisk --help
- **ture, see the extended  GPT  fdisk  documentation  at  https**: //www.rods-
- **order**: []
- **name**: -a.  This option alters the highlighting of partitions and blocks
- **of free space**: Instead of using ncurses, when -a is used cgdisk  uses  a
- **The display is broken into two interactive parts**: []
- **select among them**: []
- **Known bugs and limitations include**: []
- **Primary author**: Roderick W. Smith (rodsmith@rodsbooks.com)
- **Contributors**: []
- **https**: //www.rodsbooks.com/fixparts/
- **tures are supported, as well**: []
- **In the MBR scheme, partitions come in three varieties**: []
- **menu. Specific functions are**: []
- **Usage**: sgdisk  [OPTION...] <device>
- **-A, --attributes=list|[partnum**: show|or|nand|xor|=|set|clear|toggle|get[:bitnum|hexbitmask]]     operate on partition attributes
- **-c, --change-name=partnum**: name                                                                  change partition's name
- **-h, --hybrid=partnum[**: partnum...][:EE]                                                          create hybrid MBR
- **-m, --gpttombr=partnum[**: partnum...]                                                             convert GPT to MBR
- **-n, --new=partnum**: start:end                                                                     create new partition
- **-r, --transpose=partnum**: partnum                                                                 transpose two partitions
- **-t, --typecode=partnum**: {hexcode|GUID}                                                           change partition type code
- **-u, --partition-guid=partnum**: guid                                                               set partition GUID
- **Help options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\gdisk\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.909134
