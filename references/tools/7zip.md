---
tool_id: 7zip
title: 7zip
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.7-zip.org/
repository: 
version: 25.01+dfsg-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering"]
icon: images/7zip-logo.svg
source_path: kali-tools\7zip\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.773334
---

# Tool: 7zip (7zip)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.7-zip.org/](https://www.7-zip.org/) |
| Repository |  |
| Version | 25.01+dfsg-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering |
| Icon | images/7zip-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/7zip
- **PackagesInfo**: |
- **of 7-Zip are**: []
- *** Supported formats**: []
- *** Packing / unpacking**: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM
- *** Unpacking only**: AR, ARJ, CAB, CHM, CPIO, CramFS, DMG, EXT, FAT,
- **"7zip" provides**: []
- *** /usr/bin/7z**: Full featured with plugin functionality.
- *** /usr/bin/7za**: Major formats/features only.
- *** /usr/bin/7zr**: LZMA (.7z, .lzma, .xz) only. Minimal executable.
- **Note**: []
- ****Installed size**: ** `2.70 MB`
- ****How to install**: ** `sudo apt install 7zip-standalone`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# 7zz -h
- **7-Zip 25.01 (x64)**: Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
- **64-bit locale=C.UTF-8 Threads**: 6 OPEN_MAX:1024, ASM
- **Usage**: 7zz <command> [<switches>...] <archive_name> [<file_names>...] [@listfile]
- **a**: Add files to archive
- **b**: Benchmark
- **d**: Delete files from archive
- **e**: Extract files from archive (without using directory names)
- **h**: Calculate hash values for files
- **i**: Show information about supported formats
- **l**: List contents of archive
- **rn**: Rename files in archive
- **t**: Test integrity of archive
- **u**: Update files to archive
- **x**: eXtract files with full paths
- **--**: Stop switches and @listfile parsing
- **-ai[r[-|0]][m[-|2]][w[-]]{@listfile|!wildcard}**: Include archives
- **-ax[r[-|0]][m[-|2]][w[-]]{@listfile|!wildcard}**: eXclude archives
- **-ao{a|s|t|u}**: set Overwrite mode
- **-an**: disable archive_name field
- **-bb[0-3]**: set output log level
- **-bd**: disable progress indicator
- **-bs{o|e|p}{0|1|2}**: set output stream for output/error/progress line
- **-bt**: show execution time statistics
- **-i[r[-|0]][m[-|2]][w[-]]{@listfile|!wildcard}**: Include filenames
- **-m{Parameters}**: set compression Method
- **-mmt[N]**: set number of CPU threads
- **-mx[N]**: set compression level: -mx1 (fastest) ... -mx9 (ultra)
- **-o{Directory}**: set Output directory
- **-p{Password}**: set Password
- **-r[-|0]**: Recurse subdirectories for name search
- **-sa{a|e|s}**: set Archive name mode
- **-scc{UTF-8|WIN|DOS}**: set charset for console input/output
- **-scs{UTF-8|UTF-16LE|UTF-16BE|WIN|DOS|{id}}**: set charset for list files
- **-scrc[CRC32|CRC64|SHA256|SHA1|XXH64|*]**: set hash function for x, e, h commands
- **-sdel**: delete files after compression
- **-seml[.]**: send archive by email
- **-sfx[{name}]**: Create SFX archive
- **-si[{name}]**: read data from stdin
- **-slp**: set Large Pages mode
- **-slt**: show technical information for l (List) command
- **-snh**: store hard links as links
- **-snl**: store symbolic links as links
- **-sni**: store NT security information
- **-sns[-]**: store NTFS alternate streams
- **-so**: write data to stdout
- **-spd**: disable wildcard matching for file names
- **-spe**: eliminate duplication of root folder for extract command
- **-spf[2]**: use fully qualified file paths
- **-ssc[-]**: set sensitive case mode
- **-sse**: stop archive creating, if it can't open some input file
- **-ssp**: do not change Last Access Time of source files while archiving
- **-ssw**: compress shared files
- **-stl**: set archive timestamp from the most recently modified file
- **-stm{HexMask}**: set CPU thread affinity mask (hexadecimal number)
- **-stx{Type}**: exclude archive type
- **-t{Type}**: Set type of archive
- **-u[-][p#][q#][r#][x#][y#][z#][!newArchiveName]**: Update options
- **-v{Size}[b|k|m|g]**: Create volumes
- **-w[{path}]**: assign Work directory. Empty path means a temporary directory
- **-x[r[-|0]][m[-|2]][w[-]]{@listfile|!wildcard}**: eXclude filenames
- **-y**: assume Yes on all queries
- **7-Zip (a) 25.01 (x64)**: Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
- **7-Zip (r) 25.01 (x64)**: Igor Pavlov : Public domain : 2025-08-03
- **-scrc[CRC32|CRC64|SHA256|*]**: set hash function for x, e, h commands
- **Options**: []
- **"7zip-standalone" provides**: []
- *** /usr/bin/7zz**: Full featured except plugins, standalone executable.
- **7-Zip (z) 25.01 (x64)**: Copyright (c) 1999-2025 Igor Pavlov : 2025-08-03
- **-scrc[CRC32|CRC64|SHA256|SHA1|XXH64|BLAKE2SP|*]**: set hash function for x, e, h commands


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\7zip\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.773334
