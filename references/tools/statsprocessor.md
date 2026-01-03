---
tool_id: statsprocessor
title: statsprocessor
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://github.com/hashcat/statsprocessor
repository: 
version: 0.11+git20160316-5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\statsprocessor\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.129140
---

# Tool: statsprocessor (statsprocessor)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/hashcat/statsprocessor](https://github.com/hashcat/statsprocessor) |
| Repository |  |
| Version | 0.11+git20160316-5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/statsprocessor
- **PackagesInfo**: |
- ****Installed size**: ** `45 KB`
- ****How to install**: ** `sudo apt install statsprocessor`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sp64 -h
- **Usage**: sp64 [options]... hcstat-file [filter-mask]
- *** Startup**: []
- *** Increment**: []
- *** Markov**: []
- *** Misc**: []
- *** Resources**: []
- *** Files**: []
- *** Custom charsets**: []
- **-2,  --custom-charset2=CS  Example**: []
- *** Built-in charsets**: []
- **?s =  !"#$%&'()*+,-./**: ;<=>?@[\]^_`{|}~


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## statsprocessor Usage Example

Generate passwords with a minimum length of 6 (`–pw-min=6`) and a maximum length of 8 (`–pw-max=8`) using the stats in the provided file (`/usr/share/oclhashcat/hashcat.hcstat`):

```console
root@kali:~# statsprocessor --pw-min=6 --pw-max=8 /usr/share/oclhashcat/hashcat.hcstat
13nger
13aner
13rina
13erer
13ller
131200
13ster
13iner
```


## Source
- Path: kali-tools\statsprocessor\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.129140
