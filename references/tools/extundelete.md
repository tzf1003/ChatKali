---
tool_id: extundelete
title: extundelete
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: http://extundelete.sourceforge.net/
repository: 
version: 0.2.4-3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-recover kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\extundelete\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.892926
---

# Tool: extundelete (extundelete)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://extundelete.sourceforge.net/](http://extundelete.sourceforge.net/) |
| Repository |  |
| Version | 0.2.4-3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-recover kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/extundelete
- **PackagesInfo**: |
- ****Installed size**: ** `152 KB`
- ****How to install**: ** `sudo apt install extundelete`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# extundelete --help
- **Usage**: extundelete [options] [--] device-file
- **Options**: []
- **Actions**: []
- **Examples below**: list of options.  Dn must be one of info, warn, or


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## extundelete Usage Example

Read the partition (`/dev/sda1`) and restore (`–restore-file`) the given file name (root/importantfile):

```console
root@kali:~# extundelete /dev/sda1 --restore-file root/importantfile
WARNING: Extended attributes are not restored.
WARNING: EXT3_FEATURE_INCOMPAT_RECOVER is set.
The partition should be unmounted to undelete any files without further data loss.
If the partition is not currently mounted, this message indicates
it was improperly unmounted, and you should run fsck before continuing.
If you decide to continue, extundelete may overwrite some of the deleted
files and make recovering those files impossible.  You should unmount the
file system and check it with fsck before using extundelete.
Would you like to continue? (y/n)
y
Loading filesystem metadata ... 192 groups loaded.
Loading journal descriptors ... 29495 descriptors loaded.
Writing output to directory RECOVERED_FILES/
```


## Source
- Path: kali-tools\extundelete\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.892926
