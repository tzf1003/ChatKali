---
tool_id: rebind
title: rebind
categories: ["exploitation-tools", "sniffing-spoofing"]
category_slugs: ["exploitation-tools", "sniffing-spoofing"]
homepage: []
repository: 
version: 0.3.4-1kali9
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing"]
icon: images/rebind-logo.svg
source_path: kali-tools\rebind\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.074401
---

# Tool: rebind (rebind)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage |  |
| Repository |  |
| Version | 0.3.4-1kali9 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing |
| Icon | images/rebind-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rebind
- **PackagesInfo**: |
- ****Installed size**: ** `2.64 MB`
- ****How to install**: ** `sudo apt install rebind`
- **root@kali**: ~# dns-rebind -h
- **Usage**: dns-rebind [OPTIONS]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rebind Usage Example

Use interface eth0 (`-i eth0`) to conduct the rebind attack with the specified domain (`-d kali.local`):

```console
root@kali:~# rebind -i eth0 -d kali.local

[+] Starting DNS server on port 53
[+] Starting attack Web server on port 80
[+] Starting callback Web server on port 81
[+] Starting proxy server on 192.168.1.202:664
[+] Services started and running!

> dns
[+] 192.168.1.202       kali.local.
[+] 192.168.1.202       www.kali.local.
[+] 192.168.1.202       ns1.kali.local.
[+] 192.168.1.202       ns2.kali.local.
```


## Source
- Path: kali-tools\rebind\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.074401
