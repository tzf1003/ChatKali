---
tool_id: cifs-utils
title: cifs-utils
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://wiki.samba.org/index.php/LinuxCIFS_utils
repository: 
version: 2:7.4-1
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\cifs-utils\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.841802
---

# Tool: cifs-utils (cifs-utils)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://wiki.samba.org/index.php/LinuxCIFS_utils](https://wiki.samba.org/index.php/LinuxCIFS_utils) |
| Repository |  |
| Version | 2:7.4-1 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/samba-team/cifs-utils
- **PackagesInfo**: |
- ****Installed size**: ** `351 KB`
- ****How to install**: ** `sudo apt install cifs-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# smbinfo -h
- **Usage**: setcifsacl option [<list_of_ACEs>|<SID>] <file_name>
- **ent key types**: []
- **entry for each key type**: []
- **cifscreds**: invalid option -- 'h'
- **getcifsacl**: Display CIFS/NTFS ACL in a security descriptor of a file object
- **Valid options**: []
- **Options**: []
- **Less commonly used options**: []
- **(e.g. unneeded for mounts to most Samba versions)**: []
- **Rarely used options**: []
- **To display the version number of the mount helper**: []
- **setcifsacl**: Alter components of CIFS/NTFS security descriptor of a file object
- **setcifsacl -a "ACL**: Administrator:ALLOWED/0x0/FULL" <file_name>
- **setcifsacl -A "ACL**: Administrator:ALLOWED/0x0/FULL" <file_name>
- **setcifsacl -D "ACL**: Administrator:DENIED/0x0/D" <file_name>
- **setcifsacl -M "ACL**: user1:ALLOWED/0x0/0x1e01ff" <file_name>
- **setcifsacl -S "ACL**: Administrator:ALLOWED/0x0/D" <file_name>
- **usage**: smbinfo [-h] [-V]
- **positional arguments**: []
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\cifs-utils\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.841802
