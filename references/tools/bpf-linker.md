---
tool_id: bpf-linker
title: bpf-linker
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/aya-rs/bpf-linker
repository: 
version: 0.9.14-0kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\bpf-linker\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.813129
---

# Tool: bpf-linker (bpf-linker)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/aya-rs/bpf-linker](https://github.com/aya-rs/bpf-linker) |
| Repository |  |
| Version | 0.9.14-0kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bpf-linker
- **PackagesInfo**: |
- ****Installed size**: ** `3.40 MB`
- ****How to install**: ** `sudo apt install bpf-linker`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bpf-linker -h
- **Usage**: bpf-linker [OPTIONS] --output <OUTPUT> <INPUTS>...
- **Arguments**: []
- **Options**: []
- **--cpu <CPU>                       Target BPF processor. Can be one of `generic`, `probe`, `v1`, `v2`, `v3` [default**: generic]
- **--cpu-features <features>         Enable or disable CPU features. The available features are**: alu32, dummy, dwarfris. Use +feature to enable a feature, or -feature to disable it.  For example --cpu-features=+alu32,-dwarfris [default: ]
- **--emit <EMIT>                     Output type. Can be one of `llvm-bc`, `asm`, `llvm-ir`, `obj` [default**: obj]
- **-O <OPTIMIZE>                         Optimization level. 0-3, s, or z [default**: 2]
- **--fatal-errors <FATAL_ERRORS>     Whether to treat LLVM errors as fatal [default**: true] [possible values: true, false]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\bpf-linker\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.813129
