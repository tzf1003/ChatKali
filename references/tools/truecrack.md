---
tool_id: truecrack
title: truecrack
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://github.com/lvaccaro/truecrack
repository: 
version: 3.6+git20150326-0kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-gpu kali-tools-passwords kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\truecrack\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.146894
---

# Tool: truecrack (truecrack)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/lvaccaro/truecrack](https://github.com/lvaccaro/truecrack) |
| Repository |  |
| Version | 3.6+git20150326-0kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-gpu kali-tools-passwords kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/truecrack
- **PackagesInfo**: |
- ****Installed size**: ** `2.62 MB`
- ****How to install**: ** `sudo apt install truecrack`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# truecrack -h
- **Website**: https://github.com/lvaccaro/truecrack
- **Contact us**: infotruecrack@gmail.com
- **Based on TrueCrypt, freely available at http**: //www.truecrypt.org/
- **Usage for Dictionary attack**: []
- **Usage for Alphabet attack**: []
- **Options**: []
- **Sample for Dictionary attack**: []
- **Sample for Alphabet attack**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## truecrack Usage Example

```console
root@kali:~# truecrack -t truecrypt_vol -k ripemd160 -w passes.txt
TrueCrack v3.0
Website: http://code.google.com/p/truecrack
Contact us: infotruecrack@gmail.com
Found password:     "s3cr3t"
Password length:    "7"
Total computations: "78"
```


## Source
- Path: kali-tools\truecrack\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.146894
