---
tool_id: sqlsus
title: sqlsus
categories: ["vulnerability-analysis", "web-application-analysis", "information-gathering"]
category_slugs: ["vulnerability-analysis", "web-application-analysis", "information-gathering"]
homepage: https://sqlsus.sourceforge.net/
repository: 
version: 0.7.2-1kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/sqlsus-logo.svg
source_path: kali-tools\sqlsus\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.124067
---

# Tool: sqlsus (sqlsus)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sqlsus.sourceforge.net/](https://sqlsus.sourceforge.net/) |
| Repository |  |
| Version | 0.7.2-1kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/sqlsus-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sqlsus
- **PackagesInfo**: |
- ****Installed size**: ** `156 KB`
- ****How to install**: ** `sudo apt install sqlsus`
- **{{< spoiler "Dependencies**: " >}}


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sqlsus Usage Example

Generate a configuration file for the scan (`-g sqlsus.cfg`):

```console
root@kali:~# sqlsus -g sqlsus.cfg

              sqlsus version 0.7.2

  Copyright (c) 2008-2011 Jérémy Ruffet (sativouf)

[+] Configuration successfully saved to sqlsus.cfg
root@kali:~# nano sqlsus.cfg
```

```console
root@kali:~# sqlsus sqlsus.cfg

              sqlsus version 0.7.2

  Copyright (c) 2008-2011 Jérémy Ruffet (sativouf)

[+] Session "192.168.1.25" created
sqlsus> start
```


## Source
- Path: kali-tools\sqlsus\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.124067
