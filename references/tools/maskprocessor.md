---
tool_id: maskprocessor
title: maskprocessor
categories: ["password-attacks", "utilities"]
category_slugs: ["password-attacks", "utilities"]
homepage: https://github.com/hashcat/maskprocessor
repository: 
version: 0.73+git20170609.1708898-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\maskprocessor\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.982906
---

# Tool: maskprocessor (maskprocessor)

## Categories
- [password-attacks](../password-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/hashcat/maskprocessor](https://github.com/hashcat/maskprocessor) |
| Repository |  |
| Version | 0.73+git20170609.1708898-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/maskprocessor
- **PackagesInfo**: |
- ****Installed size**: ** `44 KB`
- ****How to install**: ** `sudo apt install maskprocessor`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# mp64 -h
- **Usage**: mp64 [options]... mask
- *** Startup**: []
- *** Increment**: []
- **-i,  --increment=NUM**: NUM   Enable increment mode. 1st NUM=start, 2nd NUM=stop
- **Example**: -i 4:8 searches lengths 4-8 (inclusive)
- *** Misc**: []
- *** Resources**: []
- *** Files**: []
- *** Custom charsets**: []
- **-2,  --custom-charset2=CS  Example**: []
- *** Built-in charsets**: []
- **?s =  !"#$%&'()*+,-./**: ;<=>?@[\]^_`{|}~


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## maskprocessor Usage Example

Generate a list of words beginning with (`pass`) and append one digit (`?d`) and one lowercase letter (`?l`):

```console
root@kali:~# maskprocessor pass?d?l
pass0a
pass0b
pass0c
pass0d
pass0e
pass0f
pass0g
```


## Source
- Path: kali-tools\maskprocessor\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.982906
