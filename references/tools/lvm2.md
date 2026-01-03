---
tool_id: lvm2
title: lvm2
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://sourceware.org/lvm2/
repository: 
version: 2.03.31-2
architectures: linux-any all
license: 
binaries: []
metapackages: ["kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-linux-wsl kali-tools-forensics kali-tools-information-gathering kali-tools-protect kali-tools-respond kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\lvm2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.974665
---

# Tool: lvm2 (lvm2)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceware.org/lvm2/](https://sourceware.org/lvm2/) |
| Repository |  |
| Version | 2.03.31-2 |
| Architectures | linux-any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-linux-wsl kali-tools-forensics kali-tools-information-gathering kali-tools-protect kali-tools-respond kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/lvm-team/lvm2
- **PackagesInfo**: |
- ****Installed size**: ** `572 KB`
- ****How to install**: ** `sudo apt install lvm2-lockd`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# lvmlockd -h
- **Usage**: []
- **blkdeactivate**: Utility to deactivate block devices
- **Options**: []
- **Device specific options**: []
- **DM_OPTIONS**: []
- **LVM_OPTIONS**: []
- **MDRAID_OPTIONS**: []
- **MPATH_OPTIONS**: []
- **VDO_OPTIONS**: []
- **<concise_device_specification> has single-device entries separated by semi-colons**: []
- **E.g.**: dev1,,,,0 100 linear 253:1 0,100 100 error;dev2,,,ro,0 1 error
- **Options are**: devno, devname, blkdevname.
- **Tree specific options are**: ascii, utf, vt100; compact, inverted, notrunc;
- **fsadm**: Utility to resize or check the filesystem on a device
- **--writemostly PV[**: t|n|y] )
- **Common options for command**: []
- **Common options for lvm**: []
- **Available lvm commands**: []
- **/usr/sbin/lvmdump**: unknown option -
- **-a advanced collection - warning**: if lvm is already hung,
- **usage**: lvmdbusd [-h] [--udev] [--debug] [--nojson] [--lvmshell]
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\lvm2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.974665
