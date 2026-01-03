---
tool_id: rizin
title: rizin
categories: ["reverse-engineering"]
category_slugs: ["reverse-engineering"]
homepage: https://rizin.re/
repository: 
version: 0.8.1-0kali2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-forensics kali-tools-hardware kali-tools-respond kali-tools-reverse-engineering"]
icon: images/rizin-logo.svg
source_path: kali-tools\rizin\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.083625
---

# Tool: rizin (rizin)

## Categories
- [reverse-engineering](../reverse-engineering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://rizin.re/](https://rizin.re/) |
| Repository |  |
| Version | 0.8.1-0kali2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-forensics kali-tools-hardware kali-tools-respond kali-tools-reverse-engineering |
| Icon | images/rizin-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rizin
- **PackagesInfo**: |
- ****Installed size**: ** `270 KB`
- ****How to install**: ** `sudo apt install rizin`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rz-test -h
- **Usage**: rz-test [-qvVnL] [-j threads] [test file/dir | @test-type]
- **=            Same as 'rizin malloc**: //512
- **-C           File is host**: port (alias for -cR+http://%%s/cmd/)
- **[-f file] [-F fil**: ter] [-i skip] [-l len] 'code'|hex|-
- **-F [in**: out]   Specify input and/or output filters (att2intel, x86.pseudo, ...)
- **-L            List Asm plugins**: (a=asm, d=disasm, A=analyze, e=ESIL)
- **Environment**: []
- **[-C F**: C:D] [-f str] [-m addr] [-n str] [-N m:M] [-P pdb]
- **-C [fmt**: C:D]    Create [elf,mach0,pe] with Code and Data hexpairs (see -a)
- **-k [sdb-query]  Run sdb query. for example**: *
- **-N [min**: max]    Force min:max number of chars per string (see -z and -zz)
- **RZ_BIN_CODESIGN_VERBOSE**: # make code signatures verbose
- **RZ_BIN_DEBASE64**: e bin.debase64                # try to debase64 all strings
- **RZ_BIN_DEBUGINFOD_URLS**: e bin.dbginfo.debuginfod_urls # use alternative debuginfod server
- **RZ_BIN_DEMANGLE=0**: e bin.demangle                # do not demangle symbols
- **RZ_BIN_LANG**: e bin.lang                    # assume lang for demangling
- **RZ_BIN_MAXSTRBUF**: e search.str.max_length       # specify maximum buffer size
- **RZ_BIN_PDBSERVER**: e pdb.server                  # use alternative PDB server
- **RZ_BIN_PREFIX**: e bin.prefix                  # prefix symbols/sections/relocs with a specific string
- **RZ_BIN_STRFILTER**: e bin.str.filter              # rizin -qc 'e bin.str.filter=??' -
- **RZ_BIN_STRPURGE**: e bin.str.purge               # try to purge false positives
- **RZ_BIN_SYMSTORE**: e pdb.symstore                # path to downstream PDB symbol store
- **RZ_CONFIG**: # config file
- **RZ_NOPLUGINS**: # do not load plugins
- **-d [algo] Compute edit distance based on the chosen algorithm**: []
- **-t [type] Compute the difference between two files based on its type**: []
- **[-S string] [-f fmt] [-nN dword] [-dDw off**: hex] file|f.asm|-
- **-d [off**: dword] Patch dword (4 bytes) at given offset
- **-D [off**: qword] Patch qword (8 bytes) at given offset
- **ntas**: begin nop, trap, 'a', sequence
- **NTAS**: same as above, but at the end
- **-w [off**: hex]   Patch hexpairs at given offset
- **Appending a comma (example**: sha1,md4,md5,sha256)
- **-e endian Set the endianness (default**: 'big' accepted: 'big' or 'little')
- **If 's**: ' prefix is specified
- **Examples**: []
- **Supported test types**: @json @unit @fuzz @cmds
- **OS/Arch for archos tests**: linux-x64


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\rizin\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.083625
