---
tool_id: tnscmd10g
title: tnscmd10g
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://www.red-database-security.com/
repository: 
version: 1.3-1kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/tnscmd10g-logo.svg
source_path: kali-tools\tnscmd10g\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.145781
---

# Tool: tnscmd10g (tnscmd10g)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.red-database-security.com/](http://www.red-database-security.com/) |
| Repository |  |
| Version | 1.3-1kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/tnscmd10g-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/tnscmd10g
- **PackagesInfo**: |
- ****Installed size**: ** `18 KB`
- ****How to install**: ** `sudo apt install tnscmd10g`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# tnscmd10g -h
- **usage**: /usr/bin/tnscmd10g [command] -h hostname


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## tnscmd10g Usage Example

Retrieve the version (`version`) from the target server (`-h 192.168.1.205`):

```console
root@kali:~# tnscmd10g version -h 192.168.1.205
sending (CONNECT_DATA=(COMMAND=version)) to 192.168.1.205:1521
writing 90 bytes
reading
.M.......6.........-. ..........(DESCRIPTION=(TMP=)(VSNNUM=153092352)(ERR=0)).7........TNSLSNR for 32-bit Windows: Version 9.2.0.1.0 - Production..TNS for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT Named Pipes NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production..Windows NT TCP/IP NT Protocol Adapter for 32-bit Windows: Version 9.2.0.1.0 - Production,,.........@
```


## Source
- Path: kali-tools\tnscmd10g\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.145781
