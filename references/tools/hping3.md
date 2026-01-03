---
tool_id: hping3
title: hping3
categories: ["information-gathering", "vulnerability-analysis", "utilities"]
category_slugs: ["information-gathering", "vulnerability-analysis", "utilities"]
homepage: http://www.hping.org/
repository: 
version: 3.a2.ds2-11~kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/hping3-logo.svg
source_path: kali-tools\hping3\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.936898
---

# Tool: hping3 (hping3)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hping.org/](http://www.hping.org/) |
| Repository |  |
| Version | 3.a2.ds2-11~kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/hping3-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/hping3
- **PackagesInfo**: |
- ****Installed size**: ** `255 KB`
- ****How to install**: ** `sudo apt install hping3`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hping3 -h
- **usage**: hping3 host [options]
- **Example**: hping --scan 1-30,70-90 -S www.target.host


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hping3 Usage Example

Use traceroute mode (`--traceroute`), be verbose (`-V`) in ICMP mode (`-1`) against the target (`www.example.com`):

```console
root@kali:~# hping3 --traceroute -V -1 www.example.com
using eth0, addr: 192.168.1.15, MTU: 1500
HPING www.example.com (eth0 93.184.216.119): icmp mode set, 28 headers + 0 data bytes
hop=1 TTL 0 during transit from ip=192.168.1.1 name=UNKNOWN
hop=1 hoprtt=0.3 ms
hop=2 TTL 0 during transit from ip=192.168.0.1 name=UNKNOWN
hop=2 hoprtt=3.3 ms
```


## Source
- Path: kali-tools\hping3\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.936898
