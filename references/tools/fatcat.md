---
tool_id: fatcat
title: fatcat
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/Gregwar/fatcat
repository: 
version: 1.1.1-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\fatcat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.895485
---

# Tool: fatcat (fatcat)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/Gregwar/fatcat](https://github.com/Gregwar/fatcat) |
| Repository |  |
| Version | 1.1.1-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/fatcat
- **PackagesInfo**: |
- **Its features**: ['Get information about FAT filesystem;', 'Explore FAT file system;', 'Read file or extract directories;', 'Retrieve file & directories that are deleted;', 'Backup & restore the FAT tables;', 'Hack the FAT table by writing on it;', 'Hack the entries by changing clusters and file sizes;', 'Perform a search for orphaned files & directories;', 'Compare and merge the FAT tables;', 'Repair unallocated directories &  files;', 'Supports FAT12, FAT16 and FAT32.']
- ****Installed size**: ** `141 KB`
- ****How to install**: ** `sudo apt install fatcat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fatcat -h
- **Usage**: fatcat disk.img [options]
- **-i**: display information about disk
- **-O [offset]**: global offset (may be partition place)
- **-F [format]**: output format (default, json)
- **Browsing & extracting**: []
- **-l [dir]**: list files and directories in the given path
- **-L [cluster]**: list files and directories in the given cluster
- **-r [path]**: reads the file given by the path
- **-R [cluster]**: reads the data from given cluster
- **-s [size]**: specify the size of data to read from the cluster
- **-d**: enable listing of deleted files
- **-x [directory]**: extract all files to a directory, deleted files included if -d
- *** -S**: write scamble data in unallocated sectors
- *** -z**: write scamble data in unallocated sectors
- **-@ [cluster]**: Get the cluster address and information
- **-2**: analysis & compare the 2 FATs
- **-b [file]**: backup the FATs (see -t)
- *** -p [file]**: restore (patch) the FATs (see -t)
- *** -w [cluster] -v [value]**: write next cluster (see -t)
- **-t [table]**: specify which table to write (0:both, 1:first, 2:second)
- *** -m**: merge the FATs
- **-o**: search for orphan files and directories
- *** -f**: try to fix reachable directories
- **-e [path]**: sets the entry to hack, combined with:
- *** -c [cluster]**: sets the entry cluster
- *** -s [size]**: sets the entry size
- *** -a [attributes]**: sets the entry attributes
- **-k [cluster]**: try to find an entry that point to that cluster
- *****: These flags writes on the disk, and may damage it, be careful


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\fatcat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.895485
