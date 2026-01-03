---
tool_id: intrace
title: intrace
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/robertswiecki/intrace
repository: 
version: 1.6-0kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\intrace\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.947590
---

# Tool: intrace (intrace)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/robertswiecki/intrace](https://github.com/robertswiecki/intrace) |
| Repository |  |
| Version | 1.6-0kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/intrace
- **PackagesInfo**: |
- ****Installed size**: ** `52 KB`
- ****How to install**: ** `sudo apt install intrace`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# intrace -h
- **2025/11/27 10**: 05:18.752862 <INFO> Usage: intrace <-h hostname> [-p <port>] [-d <debuglevel>] [-s <payloadsize>] [-4] [-6]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## intrace Usage Example

Run a trace to the target host (`-h www.example.com`) using port 80 (`-p 80`) with a packet size of 4 bytes (`-s 4`):

```console
root@kali:~# intrace -h www.example.com -p 80 -s 4
InTrace 1.5 -- R: 93.184.216.119/80 (80) L: 192.168.1.130/51654
Payload Size: 4 bytes, Seq: 0x0d6dbb02, Ack: 0x8605bff0
Status: Packets sent #8

  #  [src addr]         [icmp src addr]    [pkt type]
 1.  [192.168.1.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 2.  [192.168.0.1    ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 3.  [  ---          ]  [  ---          ]  [NO REPLY]
 4.  [64.59.184.185  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 5.  [66.163.70.25   ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 6.  [66.163.64.150  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 7.  [66.163.75.117  ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
 8.  [206.223.119.59 ]  [93.184.216.119 ]  [ICMP_TIMXCEED]
```


## Source
- Path: kali-tools\intrace\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.947590
