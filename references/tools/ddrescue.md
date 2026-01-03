---
tool_id: ddrescue
title: ddrescue
categories: ["utilities", "forensics"]
category_slugs: ["utilities", "forensics"]
homepage: http://www.garloff.de/kurt/linux/ddrescue/
repository: 
version: 1.99.13-0kali2
architectures: amd64 arm64
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-recover kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ddrescue\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.863256
---

# Tool: ddrescue (ddrescue)

## Categories
- [utilities](../utilities.md)
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.garloff.de/kurt/linux/ddrescue/](http://www.garloff.de/kurt/linux/ddrescue/) |
| Repository |  |
| Version | 1.99.13-0kali2 |
| Architectures | amd64 arm64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-recover kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/ddrescue
- **PackagesInfo**: |
- ****Installed size**: ** `411 KB`
- ****How to install**: ** `sudo apt install ddrescue`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dd_rescue -h
- **(compiled May 21 2025 11**: 21:52 by gcc (Debian 14.2.0-19) 14.2.0)
- **(features**: O_DIRECT dl/libfallocate fallocate splice fitrim xattr rdrnd sse4.2)
- **USAGE**: dd_rescue [options] infile outfile
- **Options**: -s ipos    start position in  input file (default=0),
- **-L plug1[=par1[**: par2]][,plug2[,..]]    load plugins,
- **-i         interactive**: ask before overwriting data (def=no),
- **-f         force**: skip some sanity checks (def=no),
- **-p         preserve**: preserve ownership, perms, times, attrs (def=no),
- **-C limit   rateControl**: avoid xfer data faster than limit B/s


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dd_rescue Usage Example

Start at position 100 of the input file (`-s 100 /var/log/messages`) and write, beginning at position 0 of the destination file (`-S 0 /tmp/ddrescue-out`):

```console
root@kali:~# dd_rescue -s 100 /var/log/messages -S 0 /tmp/ddrescue-out
dd_rescue: (info): Using softbs=65536, hardbs=4096
dd_rescue: (info) expect to copy 1766kB from /var/log/messages
dd_rescue: (info): ipos:      1024.1k, opos:      1024.0k, xferd:      1024.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1024.0k
             +curr.rate:  1122807kB/s, avg.rate:  1018906kB/s, avg.load:  0.0%
             >.......................-.................<  57%  ETA:  0:00:00
dd_rescue: (info): read /var/log/messages (1767.0k): EOF
dd_rescue: (info): Summary for /var/log/messages -> /tmp/ddrescue-out:
dd_rescue: (info): ipos:      1767.0k, opos:      1767.0k, xferd:      1767.0k
                   errs:      0, errxfer:         0.0k, succxfer:      1767.0k
             +curr.rate:   352945kB/s, avg.rate:   568151kB/s, avg.load:  0.0%
             >.......................-................-< 100%  ETA:  0:00:00
```


## Source
- Path: kali-tools\ddrescue\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.863256
