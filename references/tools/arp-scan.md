---
tool_id: arp-scan
title: arp-scan
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/royhills/arp-scan
repository: 
version: 1.10.0-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\arp-scan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.789533
---

# Tool: arp-scan (arp-scan)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/royhills/arp-scan](https://github.com/royhills/arp-scan) |
| Repository |  |
| Version | 1.10.0-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/arp-scan
- **PackagesInfo**: |
- ****Installed size**: ** `1.53 MB`
- ****How to install**: ** `sudo apt install arp-scan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# get-oui --help
- **Usage**: get-oui [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
- **'options' is one or more of**: []
- **arp-scan uses raw sockets, which requires privileges on some systems**: []
- **Linux with POSIX.1e capabilities support using libcap**: []
- **BSD and macOS**: []
- **Any operating system**: []
- **and network**: mask (10.0.0.0:255.255.255.0).
- **Options**: []
- **The data type for option arguments is shown by a letter in angle brackets**: []
- **<m> MAC address, e.g. 01**: 23:45:67:89:ab or 01-23-45-67-89-ab (case insensitive)
- **General Options**: []
- **Host Selection**: []
- **MAC/Vendor Mapping Files**: []
- **Output Format Control**: []
- **"(DUP**: n)" where n is the number of times this
- **insensitive field names are recognised**: []
- **MAC	Host MAC address xx**: xx:xx:xx:xx:xx
- **verbatim. "\" introduces escapes**: []
- **Example**: --format='${ip}\t${mac}\t${vendor}'
- **Host List Randomisation**: []
- **Output Timing and Retry**: []
- **DNS Resolution**: []
- **Output ARP Packet**: []
- **Output Ethernet Header**: []
- **address in the ARP packet**: use --arpsha to change
- **header. Default is ff**: ff:ff:ff:ff:ff (broadcast)
- **Misc Options**: []
- **Report bugs or send suggestions at https**: //github.com/royhills/arp-scan
- **See the arp-scan homepage at https**: //github.com/royhills/arp-scan
- **/usr/sbin/get-oui version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **The following single-character options are accepted**: []
- **With arguments**: -f -u
- **Boolean (without arguments)**: -h -v
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## arp-scan Usage Examples

Scan the local network, using the information from the primary network interface:

```console
root@kali:~# arp-scan -l
Interface: eth0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
172.16.193.1 00:50:56:c0:00:08 VMware, Inc.
172.16.193.2 00:50:56:f1:18:a8 VMware, Inc.
172.16.193.254 00:50:56:e5:7b:87 VMware, Inc.

3 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9: 256 hosts scanned in 2.327 seconds (110.01 hosts/sec). 3 responded
```

Scan a subnet, specifying the interface to use and a custom source MAC address:

```console
root@kali:~# arp-scan -I eth0 --srcaddr=DE:AD:BE:EF:CA:FE 192.168.86.0/24
Interface: eth0, datalink type: EN10MB (Ethernet)
Starting arp-scan 1.9 with 256 hosts (http://www.nta-monitor.com/tools/arp-scan/)
192.168.86.1 70:3a:cb:68:51:4c (Unknown)
192.168.86.3 00:08:9b:f6:f6:2f ICP Electronics Inc.
192.168.86.2 84:1b:5e:e5:66:af NETGEAR
192.168.86.4 00:11:32:4b:04:8a Synology Incorporated
192.168.86.7 b8:27:eb:89:ac:c3 Raspberry Pi Foundation
[...]
```


## Source
- Path: kali-tools\arp-scan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.789533
