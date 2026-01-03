---
tool_id: xmount
title: xmount
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: https://www.sits.lu/xmount
repository: 
version: 1.2.1+ds-1
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\xmount\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.180668
---

# Tool: xmount (xmount)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.sits.lu/xmount](https://www.sits.lu/xmount) |
| Repository |  |
| Version | 1.2.1+ds-1 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/xmount
- **PackagesInfo**: |
- ****Installed size**: ** `327 KB`
- ****How to install**: ** `sudo apt install xmount`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# xmount -h
- **Usage**: []
- **Options**: []
- **fopts**: []
- **-d**: Enable FUSE's and xmount's debug mode.
- **-h**: Display this help message.
- **-s**: Run single threaded.
- **-o no_allow_other**: Disable automatic addition of FUSE's allow_other option.
- **-o <fopts>**: Specify fuse mount options. Will also disable automatic addition of FUSE's allow_other option!
- **xopts**: []
- **--cache <cfile>**: Enable virtual write support.
- **--in <itype> <ifile>**: Input image format and source file(s). May be specified multiple times.
- **--inopts <iopts>**: Specify input library specific options.
- **--info**: Print out infos about used compiler and libraries.
- **--morph <mtype>**: Morphing function to apply to input image(s). If not specified, defaults to "combine".
- **--morphopts <mopts>**: Specify morphing library specific options.
- **--offset <off>**: Move the output image data start <off> bytes into the input image(s).
- **--out <otype>**: Output image format. If not specified, defaults to "raw".
- **--owcache <file>**: Same as --cache <file> but overwrites existing cache file.
- **--rocache <file>**: Same as --cache <file> but does **not** allow further writes.
- **--sizelimit <size>**: The data end of input image(s) is set to no more than <size> bytes after the data start.
- **--version**: Same as --info.
- **mntp**: []
- **Infos**: []
- **Input / Morphing library specific options**: []
- **aewfmaxmem**: Maximum amount of RAM cache, in MiB, for image offset tables. Default: 10 MiB
- **aewfmaxfiles**: Maximum number of concurrently opened image segment files. Default: 10
- **aewfstats**: Output statistics at regular intervals to this directory (must exist).
- **aewfrefresh**: The update interval, in seconds, for the statistics (aewfstats must be set). Default: 10s.
- **aewflog**: Path for writing log file (must exist).
- **aewfthreads**: Max. number of threads for parallelized decompression. Default: System CPUs (6)
- **vdilog**: Path for writing log file(must exist).
- **aaffmaxmem**: Maximum amount of RAM cache, in MiB, for image seek offsets. Default: 10 MiB
- **aafflog**: Log file name.
- **raid_chunksize**: Specify the chunk size to use in bytes. Defaults to 524288 (512k).
- **unallocated_fs**: Specify the filesystem to extract unallocated blocks from. Supported filesystems are: 'hfs', 'fat'. Default: autodetect.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\xmount\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.180668
