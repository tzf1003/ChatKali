---
tool_id: dradis
title: dradis
categories: ["reporting-tools", "information-gathering"]
category_slugs: ["reporting-tools", "information-gathering"]
homepage: https://dradis.com/ce/
repository: 
version: 4.18.0-0kali1
architectures: amd64
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-reporting"]
icon: images/dradis-logo.svg
source_path: kali-tools\dradis\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.876968
---

# Tool: dradis (dradis)

## Categories
- [reporting-tools](../reporting-tools.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://dradis.com/ce/](https://dradis.com/ce/) |
| Repository |  |
| Version | 4.18.0-0kali1 |
| Architectures | amd64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-reporting |
| Icon | images/dradis-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dradis
- **PackagesInfo**: |
- ****Installed size**: ** `136.01 MB`
- ****How to install**: ** `sudo apt install dradis`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dradis-stop -h
- **lsof**: unacceptable port specification in: -i :
- **latest revision**: https://github.com/lsof-org/lsof
- **latest FAQ**: https://github.com/lsof-org/lsof/blob/master/00FAQ
- **latest (non-formatted) man page**: https://github.com/lsof-org/lsof/blob/master/Lsof.8
- **usage**: ['-?abhHKlnNoOPRtUvVX] [+|-c c] [+|-d s] [+D D] [+|-E] [+|-e s] [+|-f[gG]']
- **[+|-r [t]] [-s [p**: s]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]
- **Loaded**: loaded (/usr/lib/systemd/system/dradis.service; disabled; preset: disabled)
- **Active**: inactive (dead)
- **Nov 27 09**: 04:05 kali systemd[1]: dradis.service: Consumed 2.347s CPU time over 15.383s wall clock time, 133.3M memory peak.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


```console
service dradis start
```

## Screenshots

![Dradis login screen](images/dradis-01.png)
![Dradis dashboard](images/dradis-02.png)
![Dradis issue list](images/dradis-03.png)
![Dradis methodologies](images/dradis-04.png)


## Source
- Path: kali-tools\dradis\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.876968
