---
tool_id: sipsak
title: sipsak
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/nils-ohlmeier/sipsak
repository: 
version: 0.9.8.1-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sipsak\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.109197
---

# Tool: sipsak (sipsak)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/nils-ohlmeier/sipsak](https://github.com/nils-ohlmeier/sipsak) |
| Repository |  |
| Version | 0.9.8.1-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-voip-team/sipsak
- **PackagesInfo**: |
- ****Installed size**: ** `134 KB`
- ****How to install**: ** `sudo apt install sipsak`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sipsak --help
- **shoot**: sipsak [-f FILE] [-L] -s SIPURI
- **trace**: sipsak -T -s SIPURI
- **usrloc**: sipsak -U [-C SIPURI] [-x NUMBER] -s SIPURI
- **message**: sipsak -M [-B STRING] [-O STRING] [-c SIPURI] -s SIPURI
- **flood**: sipsak -F [-e NUMBER] -s SIPURI
- **random**: sipsak -R [-t NUMBER] -s SIPURI
- **additional parameter in every mode**: []
- **sip**: ['user@]servername[:port']
- **--appendix-begin=NUMBER    the starting number appendix to the user name (default**: 0)
- **--expires=NUMBER           the expires header field value (default**: 15)
- **(default**: request length)
- **--local-port=PORT          the local port to use (default**: any)
- **--remote-port=PORT         the remote port to use (default**: 5060)
- **on non-reliable transports (default**: 64)
- **--timer-t1=NUMBER          timeout T1 in ms (default**: 500)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sipsak\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.109197
