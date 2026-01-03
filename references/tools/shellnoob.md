---
tool_id: shellnoob
title: shellnoob
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://github.com/reyammer/shellnoob
repository: 
version: 2.1+git20170425-0kali5
architectures: amd64 armel armhf i386
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-exploitation"]
icon: images/shellnoob-logo.svg
source_path: kali-tools\shellnoob\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.103527
---

# Tool: shellnoob (shellnoob)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/reyammer/shellnoob](https://github.com/reyammer/shellnoob) |
| Repository |  |
| Version | 2.1+git20170425-0kali5 |
| Architectures | amd64 armel armhf i386 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-exploitation |
| Icon | images/shellnoob-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/shellnoob
- **PackagesInfo**: |
- **Features**: []
- **currently supported**: asm, bin, hex, obj, exe, C, Python, ruby, pretty,
- *** in-place development**: you run ShellNoob directly on the target
- *** uber cheap debugging**: check the --to-strace and --to-gdb option!
- *** Verbose mode shows the low-level steps of the conversion**: useful to
- *** Extra plugins**: binary patching made easy with the --file-patch,
- ****Installed size**: ** `96 KB`
- ****How to install**: ** `sudo apt install shellnoob`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# shellnoob -h
- **shellnoob.py -c (prepend a breakpoint (Warning**: only few platforms/OS are supported!)
- **shellnoob.py --64 (64 bits mode, default**: 32 bits)
- **shellnoob.py --intel (intel syntax mode, default**: att)
- **shellnoob.py --file-patch <exe_fp> <file_offset> <data> (in hex). (Warning**: tested only on x86/x86_64)
- **shellnoob.py --vm-patch <exe_fp> <vm_address> <data> (in hex). (Warning**: tested only on x86/x86_64)
- **shellnoob.py --fork-nopper <exe_fp> (this nops out the calls to fork(). Warning**: tested only on x86/x86_64)
- **Supported INPUT format**: asm, obj, bin, hex, c, shellstorm
- **Supported OUTPUT format**: asm, obj, exe, bin, hex, c, completec, python, bash, ruby, pretty, safeasm


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## shellnoob Usage Example

Start in interactive mode (`-i`) in asm to opcode mode (`–to-opcode`):

```console
root@kali:~# shellnoob -i --to-opcode
asm_to_opcode selected (type "quit" or ^C to end)
>> xchg %eax, %esp
xchg %eax, %esp ~> 94
>> ret
ret ~> c3
>>
```


## Source
- Path: kali-tools\shellnoob\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.103527
