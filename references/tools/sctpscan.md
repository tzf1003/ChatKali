---
tool_id: sctpscan
title: sctpscan
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/philpraxis/sctpscan
repository: 
version: 0.1-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sctpscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.098515
---

# Tool: sctpscan (sctpscan)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/philpraxis/sctpscan](https://github.com/philpraxis/sctpscan) |
| Repository |  |
| Version | 0.1-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sctpscan
- **PackagesInfo**: |
- ****Installed size**: ** `78 KB`
- ****How to install**: ** `sudo apt install sctpscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sctpscan -h
- **Usage**: sctpscan [options]
- **Options**: []
- **-p, --port <port>           (default**: 10000)
- **-P, --loc_port <port>           (default**: 10000)
- **-l, --loc_host <loc_host>   (default**: 127.0.0.1)
- **-r, --rem_host <rem_host>   (default**: 127.0.0.2)
- **Frequent SCTP ports**: 1, 7, 9, 20, 21, 22, 80, 100, 128, 179, 260, 250, 443, 1167, 1812, 2097, 2000, 2001, 2010, 2011, 2020, 2021, 2100, 2110, 2120, 2225, 2427, 2477, 2577, 2904, 2905, 2906, 2907, 2908, 2909, 2944, 2945, 3000, 3097, 3565, 3740, 3863, 3864, 3868, 4000, 4739, 4740, 5000, 5001, 5060, 5061, 5090, 5091, 5672, 5675, 6000, 6100, 6110, 6120, 6130, 6140, 6150, 6160, 6170, 6180, 6190, 6529, 6700, 6701, 6702, 6789, 6790, 7000, 7001, 7102, 7103, 7105, 7551, 7626, 7701, 7800, 8000, 8001, 8471, 8787, 9006, 9084, 9899, 9911, 9900, 9901, 9902, 10000, 10001, 11146, 11997, 11998, 11999, 12205, 12235, 13000, 13001, 14000, 14001, 20049, 29118, 29168, 30000, 32905, 32931, 32768
- **Send both checksum**: new crc32 and old legacy-driven adler32
- **Execution arguments**: <script_name> host_ip sctp_port
- **sctpscan -s -F -r 172.22 -l `ifconfig eth0 | grep 'inet addr**: ' |  cut -d: -f2 | cut -d ' ' -f 1 `
- **Simple verification end to end on the local machine**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sctpscan Usage Example

Scan (`-s`) for frequently used ports (`-F`) on the remote network (`-r 192.168.1.*`):

```console
root@kali:~# sctpscan -s -F -r 192.168.1.*
SCTPscan - Copyright (C) 2002 - 2009 Philippe Langlois.
Netscanning with Crc32 checksumed packet
Portscanning Frequent Ports on 192.168.1.*.
```


## Source
- Path: kali-tools\sctpscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.098515
