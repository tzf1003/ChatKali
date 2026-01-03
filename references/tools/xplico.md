---
tool_id: xplico
title: xplico
categories: ["forensics"]
category_slugs: ["forensics"]
homepage: https://www.xplico.org
repository: 
version: 1.2.2-0kali6
architectures: amd64 i386
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-forensics kali-tools-respond"]
icon: images/xplico-logo.svg
source_path: kali-tools\xplico\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.181102
---

# Tool: xplico (xplico)

## Categories
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.xplico.org](https://www.xplico.org) |
| Repository |  |
| Version | 1.2.2-0kali6 |
| Architectures | amd64 i386 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-forensics kali-tools-respond |
| Icon | images/xplico-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/xplico
- **PackagesInfo**: |
- ****Installed size**: ** `10.00 MB`
- ****How to install**: ** `sudo apt install xplico`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# xplico-webui-stop -h
- **See http**: //www.xplico.org for more information.
- **This product includes GeoLite data created by MaxMind, available from http**: //www.maxmind.com/.
- **usage**: xplico [-v] [-c <config_file>] [-h] [-s] [-g] [-l] [-i <prot>] -m <capute_module>
- **NOTE**: parameters MUST respect this order!
- **[*]  Web UI**: http://127.0.0.1:9876
- **Loaded**: loaded (/usr/lib/systemd/system/xplico.service; disabled; preset: disabled)
- **Active**: inactive (dead)
- **Invocation**: 1f7ff40bc6734c05a4d414aaab79e788
- **Docs**: https://www.xplico.org/docs
- **Process**: 1819556 ExecStart=/usr/sbin/apachectl start (code=exited, status=1/FAILURE)
- **Mem peak**: 3.2M
- **CPU**: 62ms
- **Nov 27 12**: 11:38 kali systemd[1]: Stopped xplico.service - Xplico.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## xplico Usage Examples

Use the rltm module (`-m rltm`) and analyze traffic on interface eth0 (`-i eth0`):

```console
root@kali:~# xplico -m rltm -i eth0
xplico v1.0.1
Internet Traffic Decoder (NFAT).
See http://www.xplico.org for more information.

Copyright 2007-2012 Gianluca Costa & Andrea de Franceschi and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

This product includes GeoLite data created by MaxMind, available from http://www.maxmind.com/.
Configuration file (/opt/xplico/cfg/xplico_cli.cfg) found!
GeoLiteCity.dat found!
pcapf: running: 0/0, subflow:0/0, tot pkt:1
pol: running: 0/0, subflow:0/0, tot pkt:0
eth: running: 0/0, subflow:0/0, tot pkt:1
pppoe: running: 0/0, subflow:0/0, tot pkt:0
ppp: running: 0/0, subflow:0/0, tot pkt:0
ip: running: 0/0, subflow:0/0, tot pkt:0
```


## Source
- Path: kali-tools\xplico\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.181102
