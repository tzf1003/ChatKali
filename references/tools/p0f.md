---
tool_id: p0f
title: p0f
categories: ["information-gathering", "sniffing-spoofing"]
category_slugs: ["information-gathering", "sniffing-spoofing"]
homepage: https://lcamtuf.coredump.cx/p0f3/
repository: 
version: 3.09b-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-information-gathering"]
icon: images/p0f-logo.svg
source_path: kali-tools\p0f\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.034971
---

# Tool: p0f (p0f)

## Categories
- [information-gathering](../information-gathering.md)
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://lcamtuf.coredump.cx/p0f3/](https://lcamtuf.coredump.cx/p0f3/) |
| Repository |  |
| Version | 3.09b-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-information-gathering |
| Icon | images/p0f-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/p0f
- **PackagesInfo**: |
- ****Installed size**: ** `218 KB`
- ****How to install**: ** `sudo apt install p0f`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# p0f -h
- **p0f**: invalid option -- 'h'
- **Usage**: p0f [ ...options... ] [ 'filter rule' ]
- **Network interface options**: []
- **Operating mode and output settings**: []
- **Performance-related options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## p0f Usage Example

Use interface eth0 (`-i eth0`) in promiscuous mode (`-p`), saving the results to a file (`-o /tmp/p0f.log`):

```console
root@kali:~# p0f -i eth0 -p -o /tmp/p0f.log
-- p0f 3.09b by Michal Zalewski <lcamtuf@coredump.cx> ---

[+] Closed 1 file descriptor.
[+] Loaded 322 signatures from '/etc/p0f/p0f.fp'.
[+] Intercepting traffic on interface 'eth0'.
[+] Default packet filtering configured [+VLAN].
[+] Log file '/tmp/p0f.log' opened for writing.
[+] Entered main event loop.

.-[ 192.168.1.15/35834 -> 173.246.39.185/873 (syn) ]-
|
| client   = 192.168.1.15/35834
| os       = Linux 3.11 and newer
| dist     = 0
| params   = none
| raw_sig  = 4:64+0:0:1460:mss*20,7:mss,sok,ts,nop,ws:df,id+:0
```


## Source
- Path: kali-tools\p0f\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.034971
