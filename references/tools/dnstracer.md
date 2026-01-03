---
tool_id: dnstracer
title: dnstracer
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://www.mavetju.org/unix/dnstracer.php
repository: 
version: 1.9-8
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dnstracer\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.873156
---

# Tool: dnstracer (dnstracer)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.mavetju.org/unix/dnstracer.php](http://www.mavetju.org/unix/dnstracer.php) |
| Repository |  |
| Version | 1.9-8 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/creekorful/dnstracer
- **PackagesInfo**: |
- ****Installed size**: ** `59 KB`
- ****How to install**: ** `sudo apt install dnstracer`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnstracer -h
- **dnstracer**: invalid option -- 'h'
- **DNSTRACER version 1.8.1 - (c) Edwin Groothuis - http**: //www.mavetju.org
- **Usage**: dnstracer [options] [host]
- **-c**: disable local caching, default enabled
- **-C**: enable negative caching, default disabled
- **-o**: enable overview of received answers, default disabled
- **-q <querytype>**: query-type to use for the DNS requests, default A
- **-r <retries>**: amount of retries for DNS requests, default 3
- **-s <server>**: use this server for the initial request, default localhost
- **-t <maximum timeout>**: Limit time to wait per try
- **-v**: verbose
- **-S <ip address>**: use this source address.
- **-4**: don't query IPv6 servers


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dnstracer Usage Example

Scan a domain (`example.com`), retry up to 3 times (`-r 3`), and display verbose output (`-v`):

```console
root@kali:~# dnstracer -r 3 -v example.com
Tracing to example.com[a] via 192.168.1.1, maximum of 3 retries
192.168.1.1 (192.168.1.1) IP HEADER
- Destination address:  192.168.1.1
DNS HEADER (send)
```


## Source
- Path: kali-tools\dnstracer\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.873156
