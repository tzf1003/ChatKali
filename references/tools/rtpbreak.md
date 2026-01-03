---
tool_id: rtpbreak
title: rtpbreak
categories: ["sniffing-spoofing", "forensics", "information-gathering"]
category_slugs: ["sniffing-spoofing", "forensics", "information-gathering"]
homepage: http://dallachiesa.com/code/rtpbreak/
repository: 
version: 1.3a-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\rtpbreak\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.088558
---

# Tool: rtpbreak (rtpbreak)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [forensics](../forensics.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://dallachiesa.com/code/rtpbreak/](http://dallachiesa.com/code/rtpbreak/) |
| Repository |  |
| Version | 1.3a-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rtpbreak
- **PackagesInfo**: |
- ****Installed size**: ** `92 KB`
- ****How to install**: ** `sudo apt install rtpbreak`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rtpbreak -h
- **USAGE**: rtpbreak (-r|-i) <source> [options]
- **-d <str>      Set output directory to <str> (def**: .)
- **-t <float>    Set packet timeout to <float> seconds (def**: 10.00)
- **-T <float>    Set pattern timeout to <float> seconds (def**: 0.25)
- **-P <int>      Set pattern packets count to <int> (def**: 5)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rtpbreak Usage Example

Analyze RTP traffic using interface eth0 (`-i eth0`), fill in gaps (`-g`), sniff in promiscuous mode (`-m`), and save to the given directory (`-d rtplog`):

```console
root@kali:~# rtpbreak -i eth0 -g -m -d rtplog
 + rtpbreak v1.3a running here!
 + pid: 10951, date/time: 17/05/2014#13:40:02
 + Configuration
   + INPUT
     Packet source: iface 'eth0'
     Force datalink header length: disabled
   + OUTPUT
     Output directory: 'rtplog'
     RTP raw dumps: enabled
     RTP pcap dumps: enabled
     Fill gaps: enabled
     Dump noise: disabled
     Logfile: 'rtplog/rtp.0.txt'
     Logging to stdout: enabled
     Logging to syslog: disabled
     Be verbose: disabled
   + SELECT
     Sniff packets in promisc mode: enabled
     Add pcap filter: disabled
     Expecting even destination UDP port: disabled
     Expecting unprivileged source/destination UDP ports: disabled
     Expecting RTP payload type: any
     Expecting RTP payload length: any
     Packet timeout: 10.00 seconds
     Pattern timeout: 0.25 seconds
     Pattern packets: 5
   + EXECUTION
     Running as user/group: root/root
     Running daemonized: disabled
 * You can dump stats sending me a SIGUSR2 signal
 * Reading packets...
```


## Source
- Path: kali-tools\rtpbreak\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.088558
