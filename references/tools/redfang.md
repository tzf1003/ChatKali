---
tool_id: redfang
title: redfang
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: []
repository: 
version: 2.5-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\redfang\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.077230
---

# Tool: redfang (redfang)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage |  |
| Repository |  |
| Version | 2.5-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/redfang
- **PackagesInfo**: |
- ****Installed size**: ** `40 KB`
- ****How to install**: ** `sudo apt install redfang`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fang -h
- **author**: Ollie Whitehouse <ollie@atstake.com>
- **enhanced**: device info discovery by Stephen Kapp <skapp@atstake.com>
- **usage**: []
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## redfang Usage Example

Scan the given range (`-r 00803789EE76-00803789EEff`) and discover Bluetooth devices (`-s`):

```console
root@kali:~# fang -r 00803789EE76-00803789EEff -s
redfang - the bluetooth hunter ver 2.5
(c)2003 @stake Inc
author:   Ollie Whitehouse <ollie@atstake.com>
enhanced: threads by Simon Halsall <s.halsall@eris.qinetiq.com>
enhanced: device info discovery by Stephen Kapp <skapp@atstake.com>
Scanning 138 address(es)
Address range 00:80:37:89:ee:76 -> 00:80:37:89:ee:ff
Performing Bluetooth Discovery...
```


## Source
- Path: kali-tools\redfang\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.077230
