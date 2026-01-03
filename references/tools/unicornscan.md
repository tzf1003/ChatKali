---
tool_id: unicornscan
title: unicornscan
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://www.unicornscan.org/
repository: 
version: 0.4.7-1kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/unicornscan-logo.svg
source_path: kali-tools\unicornscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.153822
---

# Tool: unicornscan (unicornscan)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.unicornscan.org/](http://www.unicornscan.org/) |
| Repository |  |
| Version | 0.4.7-1kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/unicornscan-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/unicornscan
- **PackagesInfo**: |
- **Benefits**: []
- **abilities include**: ['Asynchronous stateless TCP scanning with all variations of TCP Flags.', 'Asynchronous stateless TCP banner grabbing', 'Asynchronous protocol specific UDP Scanning (sending enough of a signature']
- ****Installed size**: ** `3.61 MB`
- ****How to install**: ** `sudo apt install unicornscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# us -h
- **Usage**: unibrow:
- **-H		Hardware address like XX**: XX:XX:XX:XX:XX (otherwise use nics hwaddr)
- *****: options with `*' require an argument following them
- **Example**: fantaip -i eth0 192.168.1.7
- **unibrow**: invalid option -- '-'
- **usage**: unicornscan [options `b:B:cd:De:EFG:hHi:Ij:l:L:m:M:o:p:P:q:Qr:R:s:St:T:u:Uw:W:vVzZ:' ] X.X.X.X/YY:S-E
- **-d, --delay-type     *set delay type (numeric value, valid options are `1**: tsc 2:gtod 3:sleep')
- **6=linux 7**: strangetcp
- **example**: unicornscan -i eth1 -Ir 160 -E 192.168.1.0/24:1-4000 gateway:a


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Unicornscan Usage Example

```console
root@kali:~# unicornscan -mTsf -Iv -r 1000 192.168.0.102:a
adding 192.168.0.102/32 mode `TCPscan' ports `a' pps 1000
using interface(s) eth0
scaning 1.00e+00 total hosts with 6.55e+04 total packets, should take a little longer than 1 Minutes, 12 Seconds
connected 192.168.103.227:23221 -> 192.168.0.102:445
TCP open 192.168.0.102:445  ttl 128
connected 192.168.103.227:50006 -> 192.168.0.102:443
TCP open 192.168.0.102:443  ttl 128
connected 192.168.103.227:54487 -> 192.168.0.102:161
TCP open 192.168.0.102:161  ttl 128
connected 192.168.103.227:47765 -> 192.168.0.102:80
TCP open 192.168.0.102:80  ttl 128
connected 192.168.103.227:4267 -> 192.168.0.102:1884
TCP open 192.168.0.102:139  ttl 128
sender statistics 963.9 pps with 65536 packets sent total
listener statistics 131180 packets recieved 0 packets droped and 0 interface drops
TCP open                http[   80]     from 192.168.0.102  ttl 128
TCP open         netbios-ssn[  139]     from 192.168.0.102  ttl 128
TCP open                snmp[  161]     from 192.168.0.102  ttl 128
TCP open               https[  443]     from 192.168.0.102  ttl 128
TCP open        microsoft-ds[  445]     from 192.168.0.102  ttl 128
root@kali:~#
```


## Source
- Path: kali-tools\unicornscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.153822
