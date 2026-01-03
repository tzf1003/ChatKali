---
tool_id: donut-shellcode
title: donut-shellcode
categories: ["exploitation-tools", "post-exploitation"]
category_slugs: ["exploitation-tools", "post-exploitation"]
homepage: https://github.com/TheWover/donut
repository: 
version: 1.1-0kali3
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: images/donut-shellcode-logo.svg
source_path: kali-tools\donut-shellcode\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.874844
---

# Tool: donut-shellcode (donut-shellcode)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/TheWover/donut](https://github.com/TheWover/donut) |
| Repository |  |
| Version | 1.1-0kali3 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | images/donut-shellcode-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/donut-shellcode
- **PackagesInfo**: |
- **The generator and loader support the following features**: ['Compression of input files with aPLib and LZNT1, Xpress, Xpress Huffman']
- ****Installed size**: ** `93 KB`
- ****How to install**: ** `sudo apt install python3-donut`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# donut -h
- **[ Donut shellcode generator v1 (built Mar 10 2025 15**: 50:28)
- **usage**: donut [options] <EXE/DLL/VBS/JS>
- **-n,--modname**: <name>                    Module name for HTTP staging. If entropy is enabled, this is generated randomly.
- **-s,--server**: <server>                   Server that will host the Donut module. Credentials may be provided in the following format: https://username:password@192.168.0.1/
- **-e,--entropy**: <level>                   Entropy. 1=None, 2=Use random names, 3=Random names + symmetric encryption (default)
- **-a,--arch**: <arch>,--cpu: <arch>         Target architecture : 1=x86, 2=amd64, 3=x86+amd64(default).
- **-o,--output**: <path>                     Output file to save loader. Default is "loader.bin"
- **-f,--format**: <format>                   Output format. 1=Binary (default), 2=Base64, 3=C, 4=Ruby, 5=Python, 6=Powershell, 7=C#, 8=Hex
- **-y,--fork**: <offset>                     Create a new thread for the loader and continue execution at <offset> relative to the host process's executable.
- **-x,--exit**: <action>                     Exit behaviour. 1=Exit thread (default), 2=Exit process, 3=Do not exit or cleanup and block indefinitely
- **-c,--class**: <namespace.class>           Optional class name. (required for .NET DLL)
- **-d,--domain**: <name>                     AppDomain name to create for .NET assembly. If entropy is enabled, this is generated randomly.
- **-i,--input**: <path>,--file: <path>       Input file to execute in-memory.
- **-m,--method**: <method>,--function: <api> Optional method or function for DLL. (a method is required for .NET DLL)
- **-p,--args**: <arguments>                  Optional parameters/command line inside quotations for DLL method/function or EXE.
- **-r,--runtime**: <version>                 CLR runtime version. MetaHeader used by default or v4.0.30319 if none available.
- **-z,--compress**: <engine>                 Pack/Compress file. 1=None
- **-b,--bypass**: <level>                    Bypass AMSI/WLDP/ETW : 1=None, 2=Abort on fail, 3=Continue on fail.(default)
- **-k,--headers**: <level>                   Preserve PE headers. 1=Overwrite (default), 2=Keep all
- **-j,--decoy**: <level>                     Optional path of decoy module for Module Overloading.
- **examples**: []
- **donut --arch**: x86 --class:TestClass --method:RunProcess --args:notepad.exe --input:loader.dll
- **donut -iloader.dll -c TestClass -m RunProcess -p"calc notepad" -s http**: //remote_server.com/modules/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\donut-shellcode\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.874844
