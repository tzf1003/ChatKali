---
tool_id: fragrouter
title: fragrouter
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: http://www.anzen.com/research/nidsbench/fragrouter.html
repository: 
version: 1.7-3kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\fragrouter\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.903464
---

# Tool: fragrouter (fragrouter)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.anzen.com/research/nidsbench/fragrouter.html](http://www.anzen.com/research/nidsbench/fragrouter.html) |
| Repository |  |
| Version | 1.7-3kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/fragrouter
- **PackagesInfo**: |
- ****Installed size**: ** `72 KB`
- ****How to install**: ** `sudo apt install fragrouter`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fragrouter --help
- **fragrouter**: invalid option -- '-'
- **Usage**: fragrouter [-i interface] [-p] [-g hop] [-G hopcount] ATTACK
- **where ATTACK is one of the following**: []
- **-B1**: base-1: normal IP forwarding
- **-F1**: frag-1: ordered 8-byte IP fragments
- **-F2**: frag-2: ordered 24-byte IP fragments
- **-F3**: frag-3: ordered 8-byte IP fragments, one out of order
- **-F4**: frag-4: ordered 8-byte IP fragments, one duplicate
- **-F5**: frag-5: out of order 8-byte fragments, one duplicate
- **-F6**: frag-6: ordered 8-byte fragments, marked last frag first
- **-F7**: frag-7: ordered 16-byte fragments, fwd-overwriting
- **-T1**: tcp-1:  3-whs, bad TCP checksum FIN/RST, ordered 1-byte segments
- **-T3**: tcp-3:  3-whs, ordered 1-byte segments, one duplicate
- **-T4**: tcp-4:  3-whs, ordered 1-byte segments, one overwriting
- **-T5**: tcp-5:  3-whs, ordered 2-byte segments, fwd-overwriting
- **-T7**: tcp-7:  3-whs, ordered 1-byte segments, interleaved null segments
- **-T8**: tcp-8:  3-whs, ordered 1-byte segments, one out of order
- **-T9**: tcp-9:  3-whs, out of order 1-byte segments
- **-C2**: tcbc-2: 3-whs, ordered 1-byte segments, interleaved SYNs
- **-C3**: tcbc-3: ordered 1-byte null segments, 3-whs, ordered 1-byte segments
- **-R1**: tcbt-1: 3-whs, RST, 3-whs, ordered 1-byte segments
- **-I2**: ins-2:  3-whs, ordered 1-byte segments, bad TCP checksums
- **-I3**: ins-3:  3-whs, ordered 1-byte segments, no ACK set
- **-M1**: misc-1: Windows NT 4 SP2 - http://www.dataprotect.com/ntfrag/
- **-M2**: misc-2: Linux IP chains - http://www.dataprotect.com/ipchains/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## fragrouter Usage Example

Using interface eth0 (`-i eth0`), send ordered 8-byte IP fragments (`-F1`):

```console
root@kali:~# fragrouter -i eth0 -F1
fragrouter: frag-1: ordered 8-byte IP fragments
```


## Source
- Path: kali-tools\fragrouter\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.903464
