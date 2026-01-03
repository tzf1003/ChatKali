---
tool_id: amap
title: amap
categories: ["information-gathering", "system-services"]
category_slugs: ["information-gathering", "system-services"]
homepage: https://www.thc.org
repository: 
version: 5.4-4kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\amap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.779849
---

# Tool: amap (amap)

## Categories
- [information-gathering](../information-gathering.md)
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.thc.org](https://www.thc.org) |
| Repository |  |
| Version | 5.4-4kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/amap
- **PackagesInfo**: |
- ****Installed size**: ** `282 KB`
- ****How to install**: ** `sudo apt install amap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# amapcrap -h
- **Syntax**: amapcrap [-S] [-u] [-m 0ab] [-M min,max] [-n connects] [-N delay] [-w delay] [-e] [-v] TARGET PORT
- **Modes**: []
- **-A         Map applications**: send triggers and analyse responses (default)
- **Options**: []
- **-v         Verbose mode, use twice (or more!) for debug (not recommended**: -)
- **Usage hint**: Options "-bqv" are recommended, add "-1" for fast/rush checks.
- **-u           use UDP protocol (default**: TCP) (not usable with -c)
- **-n connects  maximum number of connects (default**: unlimited)
- **-N delay     delay between connects in ms (default**: 0)
- **-w delay     delay before closing the port (default**: 250)
- **-m 0ab       send as random crap**: 0-nullbytes, a-letters+spaces, b-binary
- **appdefs definitions. Note**: by default all modes are activated (0:10%, a:40%,
- **b**: 50%). Mode 'a' always sends one line with letters and spaces which end with
- **\r\n. Visit our homepage at http**: //www.thc.org


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## amap Usage Example

Scan port `80` on `192.168.1.15`. Display the received banners (`b`), do not display closed ports (`q`), and use verbose output (`v`):

```console
root@kali:~# amap -bqv 192.168.1.15 80
Using trigger file /etc/amap/appdefs.trig ... loaded 30 triggers
Using response file /etc/amap/appdefs.resp ... loaded 346 responses
Using trigger file /etc/amap/appdefs.rpc ... loaded 450 triggers

amap v5.4 (www.thc.org/thc-amap) started at 2014-05-13 19:07:16 - APPLICATION MAPPING mode

Total amount of tasks to perform in plain connect mode: 23
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http - banner: \n\n501 Method Not Implemented\n\n
<h1>Method Not Implemented</h1>
\n

to /index.html not supported.
\n

\n

<hr />

\n

<address>Apache/2.2.22 (Debian) Server at 12
Protocol on 192.168.1.15:80/tcp (by trigger ssl) matches http-apache-2 - banner: \n\n501 Method Not Implemented\n\n</address>
<h1>Method Not Implemented</h1>
\n

to /index.html not supported.
\n

\n

<hr />

\n

<address>Apache/2.2.22 (Debian) Server at 12
Waiting for timeout on 19 connections ...</address>amap v5.4 finished at 2014-05-13 19:07:22
```


## Source
- Path: kali-tools\amap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.779849
