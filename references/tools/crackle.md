---
tool_id: crackle
title: crackle
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/mikeryan/crackle
repository: 
version: 0.1~git01282014-0kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-bluetooth kali-tools-passwords kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\crackle\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.853526
---

# Tool: crackle (crackle)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/mikeryan/crackle](https://github.com/mikeryan/crackle) |
| Repository |  |
| Version | 0.1~git01282014-0kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-bluetooth kali-tools-passwords kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/crackle
- **PackagesInfo**: |
- ****Installed size**: ** `54 KB`
- ****How to install**: ** `sudo apt install crackle`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# crackle -h
- **Usage**: crackle -i <input.pcap> [-o <output.pcap>] [-l <ltk>]
- **Major modes**: Crack TK // Decrypt with LTK
- **Crack TK**: []
- **Decrypt with LTK**: []
- **LTK format**: string of hex bytes, no separator, most-significant
- **Example**: -l 81b06facd90fe7a6e9bbd9cee59736a7
- **Optional arguments**: []
- **See web site for more info**: []
- **http**: //lacklustre.net/projects/crackle/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## crackle Usage Example
Read the input file (`-i ltk_exchange.pcap`) and write the decrypted output to disk (`-o ltk-decrypted.pcap`):

```console
root@kali:~# crackle -i ltk_exchange.pcap -o ltk-decrypted.pcap


!!!
TK found: 000000
ding ding ding, using a TK of 0! Just Cracks(tm)
!!!

Warning: packet is too short to be encrypted (1), skipping
LTK found: 7f62c053f104a5bbe68b1d896a2ed49c
Done, processed 712 total packets, decrypted 3
```


## Source
- Path: kali-tools\crackle\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.853526
