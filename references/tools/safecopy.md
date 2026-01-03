---
tool_id: safecopy
title: safecopy
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://safecopy.sf.net
repository: 
version: 1.7-7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\safecopy\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.091911
---

# Tool: safecopy (safecopy)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://safecopy.sf.net](http://safecopy.sf.net) |
| Repository |  |
| Version | 1.7-7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/safecopy
- **PackagesInfo**: |
- ****Installed size**: ** `93 KB`
- ****How to install**: ** `sudo apt install safecopy`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# safecopy -h
- **Usage**: safecopy [options] <source> <target>
- **Options**: []
- **--stage1**: Preset to rescue most of the data fast,
- **Presets**: -f 1* -r 1* -R 4 -Z 1 -L 2
- **--stage2**: Preset to rescue more data, using no retries
- **--stage3**: Preset to rescue everything that can be rescued
- **-b <size>**: Blocksize for default read operations.
- **Default**: none
- **-f <size>**: Blocksize when skipping over badblocks.
- **-r <size>**: Resolution in bytes when searching for the exact
- **-R <number>**: At least that many read attempts are made on the first
- **-Z <number>**: On each error, force seek the read head from start to
- **-L <mode>**: Use low level device calls as specified:
- **Supported low level features in this version are**: []
- **--sync**: Use synchronized read calls (disable driver buffering).
- **--forceopen**: Keep trying to reopen the source after a read errer
- **Warning**: When used in combination with
- **-s <blocks>**: Start position where to start reading.
- **-l <blocks>**: Maximum length of data to be read.
- **-I <badblockfile>**: Incremental mode. Assume the target file already
- **Implies**: -I /dev/null if -I is not specified
- **-i <bytes>**: Blocksize to interpret the badblockfile given with -I.
- **-c <blocks>**: Continue copying at this position.
- **-X <badblockfile>**: Exclusion mode. If used together with -I,
- **-x <bytes>**: Blocksize to interpret the badblockfile given with -X.
- **-o <badblockfile>**: Write a badblocks/e2fsck compatible bad block file.
- **-S <seekscript>**: Use external script for seeking in input file.
- **-M <string>**: Mark unrecovered data with this string instead of
- **--debug <level>**: Enable debug output. Level is a bit field,
- **add values together for more information**: []
- **program flow**: 1
- **IO control**: 2
- **badblock marking**: 4
- **seeking**: 8
- **incremental mode**: 16
- **exclude mode**: 32
- **or for all debug output**: 255
- **-T <timingfile>**: Write sector read timing information into
- **-h | --help**: Show this text
- **Valid parameters for -f -r -b <size> options are**: []
- **Description of output**: []
- **.**: Between 1 and 1024 blocks successfully read.
- **_**: Read of block was incomplete. (possibly end of file)
- **|/|**: Seek failed, source can only be read sequentially.
- **>**: Read failed, reducing blocksize to read partial data.
- **!**: A low level error on read attempt of smallest allowed size
- **[xx](+yy){**: Current block and number of bytes continuously
- **X**: Read failed on a block with minimum blocksize and is skipped.
- **<**: Successful read after the end of a bad area causes
- **}[xx](+yy)**: current block and number of bytes of recent
- **<http**: //www.gnu.org/licenses/gpl2.html>.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\safecopy\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.091911
