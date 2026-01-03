---
tool_id: binwalk
title: binwalk
categories: ["reverse-engineering"]
category_slugs: ["reverse-engineering"]
homepage: https://github.com/ReFirmLabs/binwalk
repository: 
version: 2.4.3+dfsg1-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-hardware kali-tools-respond"]
icon: images/binwalk-logo.svg
source_path: kali-tools\binwalk\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.805299
---

# Tool: binwalk (binwalk)

## Categories
- [reverse-engineering](../reverse-engineering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ReFirmLabs/binwalk](https://github.com/ReFirmLabs/binwalk) |
| Repository |  |
| Version | 2.4.3+dfsg1-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-hardware kali-tools-respond |
| Icon | images/binwalk-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/binwalk
- **PackagesInfo**: |
- ****Installed size**: ** `659 KB`
- ****How to install**: ** `sudo apt install python3-binwalk`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# binwalk -h
- **Original author**: Craig Heffner, ReFirmLabs
- **https**: //github.com/OSPG/binwalk
- **Usage**: binwalk [OPTIONS] [FILE1] [FILE2] [FILE3] ...
- **Disassembly Scan Options**: []
- **-T, --minsn=<int>            Minimum number of consecutive instructions to be considered valid (default**: 500)
- **Signature Scan Options**: []
- **Extraction Options**: []
- **-D, --dd=<type[**: ext[:cmd]]>  Extract <type> signatures (regular expression), give the files an extension of <ext>, and execute <cmd>
- **-d, --depth=<int>            Limit matryoshka recursion depth (default**: 8 levels deep)
- **-C, --directory=<str>        Extract files/folders to a custom directory (default**: current working directory)
- **Entropy Options**: []
- **-H, --high=<float>           Set the rising edge entropy trigger threshold (default**: 0.95)
- **-L, --low=<float>            Set the falling edge entropy trigger threshold (default**: 0.85)
- **Binary Diffing Options**: []
- **Raw Compression Options**: []
- **General Options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## binwalk Usage Example

Run a file signature scan (`-B`) on the given firmware file (`ddwrt-linksys-wrt1200ac-webflash.bin`):

```console
root@kali:~# binwalk -B ddwrt-linksys-wrt1200ac-webflash.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             TRX firmware header, little endian, image size: 37883904 bytes, CRC32: 0x95C5DF32, flags: 0x1, version: 1, header size: 28 bytes, loader offset: 0x1C, linux kernel offset: 0x0, rootfs offset: 0x0
28            0x1C            uImage header, header size: 64 bytes, header CRC: 0x780C2742, created: 2018-10-10 02:12:20, image size: 2150281 bytes, Data Address: 0x8000, Entry Point: 0x8000, data CRC: 0xA097CFEA, OS: Linux, CPU: ARM, image type: OS Kernel Image, compression type: none, image name: "DD-WRT"
92            0x5C            Linux kernel ARM boot executable zImage (little-endian)
2460          0x99C           device tree image (dtb)
23432         0x5B88          xz compressed data
23776         0x5CE0          xz compressed data
2117484       0x204F6C        device tree image (dtb)
3145756       0x30001C        UBI erase count header, version: 1, EC: 0x0, VID header offset: 0x800, data offset: 0x1000
```


## Source
- Path: kali-tools\binwalk\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.805299
