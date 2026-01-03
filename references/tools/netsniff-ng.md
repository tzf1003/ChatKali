---
tool_id: netsniff-ng
title: netsniff-ng
categories: ["sniffing-spoofing", "defensive-tools", "utilities", "information-gathering"]
category_slugs: ["sniffing-spoofing", "defensive-tools", "utilities", "information-gathering"]
homepage: http://netsniff-ng.org/
repository: 
version: 0.6.9-1.1
architectures: any
license: GNU GPL version 2.0
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-respond kali-tools-sniffing-spoofing"]
icon: images/netsniff-ng-logo.svg
source_path: kali-tools\netsniff-ng\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.012991
---

# Tool: netsniff-ng (netsniff-ng)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [defensive-tools](../defensive-tools.md)
- [utilities](../utilities.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://netsniff-ng.org/](http://netsniff-ng.org/) |
| Repository |  |
| Version | 0.6.9-1.1 |
| Architectures | any |
| License | GNU GPL version 2.0 |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-respond kali-tools-sniffing-spoofing |
| Icon | images/netsniff-ng-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/netsniff-ng
- **PackagesInfo**: |
- **netsniff-ng toolkit currently consists of the following utilities**: []
- *** netsniff-ng**: a zero-copy packet analyzer, pcap capturing/replaying tool
- *** trafgen**: a multithreaded low-level zero-copy network packet generator
- *** mausezahn**: high-level packet generator for appliances with Cisco-CLI
- *** ifpps**: a top-like kernel networking and system statistics tool
- *** curvetun**: a lightweight curve25519-based multiuser IP tunnel
- *** astraceroute**: an autonomous system trace route and DPI testing utility
- *** flowtop**: a top-like netfilter connection tracking tool
- *** bpfc**: a [seccomp-]BPF (Berkeley packet filter) compiler, JIT disassembler
- ****Installed size**: ** `2.06 MB`
- ****How to install**: ** `sudo apt install netsniff-ng`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# trafgen -h
- **http**: //www.netsniff-ng.org
- **Usage**: trafgen [options] [packet]
- **Options**: []
- **-m|--max-ttl <ttl>      Set maximum TTL (def**: 30)
- **-q|--num-probes <num>   Number of max probes for each hop (def**: 2)
- **-x|--timeout <sec>      Probe response timeout in sec (def**: 3)
- **Examples**: []
- **IPv4 trace of AS with TCP SYN probe (this will most-likely pass)**: []
- **IPv4 trace of AS with TCP ECN SYN probe**: []
- **IPv4 trace of AS with TCP FIN probe**: []
- **IPv4 trace of AS with Xmas probe**: []
- **IPv4 trace of AS with Null probe with ASCII payload**: []
- **IPv6 trace of AS up to www.6bone.net**: []
- **Note**: []
- **Please report bugs at https**: //github.com/netsniff-ng/netsniff-ng/issues
- **This is free software**: you are free to change and redistribute it.
- **-f|--format <format>    Output format**: C|netsniff-ng|xt_bpf|tcpdump
- **Options, general**: []
- **Example**: []
- **Secret ingredient**: 7647-14-5
- **If netfilter is not running, you can activate it with e.g.**: []
- **-n|--num-cpus <num>    Number of top hitter CPUs in ncurses mode (def**: 5)
- **-x <port>             Interactive mode with telnet CLI, default port**: 25542
- **-l <ip>               Listen address to bind to when in interactive mode, default**: 0.0.0.0
- **-c <count>            Send packet count times, default**: 1, infinite:0
- **-b <dstmac|keyword>   Same with destination mac address; keywords**: []
- **-Q <[CoS**: ]vlan>       Specify 802.1Q VLAN tag and optional Class of Service, you can
- **via a comma or a period (e.g. '5**: 10,20,2:30')
- **Currently supported types**: arp, bpdu, cdp, ip, icmp, udp, tcp,
- **-S                    Simulation mode**: DOES NOT put anything on the wire, this is
- **-K|--fanout-type <type>        Apply fanout discipline**: hash|lb|cpu|rnd|roll|qm
- **-L|--fanout-opts <opts>        Additional fanout options**: defrag|roll
- **-t|--type <type>               Filter for**: host|broadcast|multicast|others|outgoing
- **-F|--interval <size|time>      Dump interval if -o is a dir**: <num>KiB/MiB/GiB/s/sec/min/hrs
- **-n|--num <0|uint>              Number of packets until exit (def**: 0)
- **-S|--ring-size <size>          Specify ring size to**: <num>KiB/MiB/GiB
- **-k|--kernel-pull <uint>        Kernel pull from user interval in us (def**: 10us)
- **-J|--jumbo-support             Support replay/fwd 64KB Super Jumbo Frames (def**: 2048B)
- **-J|--jumbo-support                    Support 64KB super jumbo frames (def**: 2048B)
- **-n|--num <uint>                       Number of packets until exit (def**: 0)
- **-r|--rand                             Randomize packet selection (def**: round robin)
- **-P|--cpus <uint>[-<uint>]             Specify number of forks(<= CPUs) (def**: #CPUs)
- **-t|--gap <time>                       Set approx. interpacket gap (s/ms/us/ns, def**: us)
- **Arbitrary packet config examples (e.g. trafgen -e > trafgen.cfg)**: []
- **Run packet on  all CPUs**: { fill(0xff, 64) csum16(0, 64) }
- **Run packet only on CPU1**: cpu(1):   { rnd(64), 0b11001100, 0xaa }
- **Run packet only on CPU1-2**: cpu(1-2): { drnd(64),'a',csum16(1, 8),'b',42 }
- **Generate config files from existing pcap using netsniff-ng**: []
- **Smoke/fuzz test example**: machine A, 10.0.0.2 (trafgen) is directly
- **to generate a trafgen config file with packet ratios as**: []
- **IMIX             64**: 7,  570:4,  1518:1
- **Tolly            64**: 55,  78:5,   576:17, 1518:23
- **Cisco            64**: 7,  594:4,  1518:1
- **RPR Trimodal     64**: 60, 512:20, 1518:20
- **RPR Quadrimodal  64**: 50, 512:15, 1518:15, 9218:20


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\netsniff-ng\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.012991
