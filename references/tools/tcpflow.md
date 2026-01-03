---
tool_id: tcpflow
title: tcpflow
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: https://github.com/simsong/tcpflow
repository: 
version: 1.6.1-3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-sniffing-spoofing"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\tcpflow\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.136372
---

# Tool: tcpflow (tcpflow)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/simsong/tcpflow](https://github.com/simsong/tcpflow) |
| Repository |  |
| Version | 1.6.1-3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-sniffing-spoofing |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/tcpflow
- **PackagesInfo**: |
- ****Installed size**: ** `658 KB`
- ****How to install**: ** `sudo apt install tcpflow-nox`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# tcpflow -h
- **usage**: tcpflow [-aBcCDhIpsvVZ] [-b max_bytes] [-d debug_level]
- **-a**: do ALL post-processing.
- **-b max_bytes**: max number of bytes per flow to save
- **-d debug_level**: debug level; default is 1
- **-f**: maximum number of file descriptors to use
- **-h**: print this help message (-hh for more help)
- **-H**: print detailed information about each scanner
- **-i**: network interface on which to listen
- **-I**: write for each flow another file *.findx to provide byte-indexed timestamps
- **-g**: output each flow in alternating colors (note change!)
- **-l**: treat non-flag arguments as input files rather than a pcap expression
- **-p**: don't use promiscuous mode
- **-q**: quiet mode - do not print warnings
- **-r file**: read packets from tcpdump pcap file (may be repeated)
- **-R file**: read packets from tcpdump pcap file TO FINISH CONNECTIONS
- **-v**: verbose operation equivalent to -d 10
- **-V**: print version number and exit
- **-w  file**: write packets not processed to file
- **-o  outdir**: specify output directory (default '.')
- **-X  filename**: DFXML output to filename
- **-m  bytes**: specifies skip that starts a new stream (default 16777216).
- **-F{p}**: filename prefix/suffix (-hh for options)
- **-T{t}**: filename template (-hh for options; default %A.%a-%B.%b%V%v%C%c)
- **-K**: output|keep pcap flow structure.
- **Security**: []
- **Control of Scanners**: []
- **Console output options**: []
- **-B**: binary output, even with -c or -C (normally -c or -C turn it off)
- **-c**: console print only (don't create files)
- **-C**: console print only, but without the display of source/dest header
- **-0**: don't print newlines after packets when printing to console
- **-s**: strip non-printable characters (change to '.')
- **-J**: output json format.
- **-D**: output in hex (useful to combine with -c or -C)
- **expression**: tcpdump-like filtering expression


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\tcpflow\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.136372
