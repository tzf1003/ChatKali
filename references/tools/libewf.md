---
tool_id: libewf
title: libewf
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: https://github.com/libyal/libewf-legacy
repository: the source file(s) or device
version: 20140816-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\libewf\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.965128
---

# Tool: libewf (libewf)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/libyal/libewf-legacy](https://github.com/libyal/libewf-legacy) |
| Repository | [the source file(s) or device](the source file(s) or device) |
| Version | 20140816-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/libewf
- **PackagesInfo**: |
- ****Installed size**: ** `157 KB`
- ****How to install**: ** `sudo apt install python3-libewf`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ewfverify -h
- **Usage**: ewfverify [ -A codepage ] [ -d digest_type ] [ -f format ]
- **-A**: codepage of header section, options: ascii (default),
- **-b**: specify the number of sectors to read at once (per chunk),
- **options**: sha1, sha256
- **-B**: specify the number of bytes to export (default is all bytes)
- **-c**: specify the compression values as: level or method:level
- **compression method options**: deflate (default)
- **compression level options**: none (default), empty-block,
- **-C**: specify the case number (default is case_number).
- **-d**: calculate additional digest (hash) types besides md5,
- **-D**: specify the description (default is description).
- **-e**: only show EWF read error information
- **-E**: specify the evidence number (default is evidence_number).
- **-f**: specify the input format, options: raw (default),
- **-h**: shows this help
- **-l**: logs verification errors and the digest (hash) to the
- **-m**: only show EWF media information
- **-M**: specify the media flags, options: logical, physical (default)
- **-N**: specify the notes (default is notes).
- **-o**: specify the offset to start the export (default is 0)
- **-p**: specify the process buffer size (default is the chunk size)
- **-P**: specify the number of bytes per sector (default is 512)
- **-q**: quiet shows minimal status information
- **-r**: specify the number of retries when a read error occurs (default
- **-R**: resume acquiry at a safe point
- **-s**: swap byte pairs of the media data (from AB to BA)
- **-S**: specify the segment file size in bytes (default is 1.4 GiB)
- **-t**: specify the target file to recover to (default is recover)
- **-T**: specify the file containing the table of contents (TOC) of
- **-u**: unattended mode (disables user interaction)
- **-v**: verbose output to stderr
- **-V**: print version
- **-w**: zero sectors on checksum error (mimic EnCase like behavior)
- **-x**: use the chunk data instead of the buffered read and write
- **-2**: specify the secondary target file (without extension) to write to
- **ewf_files**: the first or the entire set of EWF segment files
- **-i**: only show EWF acquiry information
- **image**: an Expert Witness Compression Format (EWF) image file
- **mount_point**: the directory to serve as mount point
- **-X**: extended options to pass to sub system


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\libewf\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.965128
