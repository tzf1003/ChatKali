---
tool_id: thc-ipv6
title: thc-ipv6
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: http://www.thc.org/thc-ipv6/
repository: 
version: 3.8-2
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\thc-ipv6\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.141150
---

# Tool: thc-ipv6 (thc-ipv6)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.thc.org/thc-ipv6/](http://www.thc.org/thc-ipv6/) |
| Repository |  |
| Version | 3.8-2 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/thc-ipv6
- **PackagesInfo**: |
- **Some of the tools included**: []
- **alive6**: an effective alive scanning.
- **denial6**: try a collection of denial-of-service tests against a
- **detect-new-ip6**: detect new ip6 devices which join the network.
- **dnsdict6**: parallelized dns ipv6 dictionary bruteforcer.
- **dos-new-ip6**: detect new ip6 devices and tell them that their chosen
- **exploit6**: test known ipv6 vulnerabilities against a target.
- **fake_mld6**: announce yourself in a multicast group of your choice on
- **fake_router6**: announce yourself as a router on the network.
- **flood_advertise6**: flood a target with random neighbor advertisements.
- **flood_router6**: flood a target with random router advertisements.
- **implementation6**: performs various implementation checks on ipv6.
- **parasite6**: icmp neighbor solitication/advertisement spoofer.
- **redir6**: redirect traffic to you intelligently (man-in-the-middle)
- **rsmurf6**: remote smurfer (known to work only against Linux at the
- **thcping6**: sends a hand crafted ping6 packet.
- **toobig6**: mtu decreaser with the same intelligence as redir6.
- ****Installed size**: ** `3.68 MB`
- ****How to install**: ** `sudo apt install thc-ipv6`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# atk6-trace6 -h
- **Syntax**: atk6-trace6 [-abdtu] [-s src6] interface targetaddress [port]
- **Options**: []
- **Output Options**: []
- **-v         verbose information (twice**: detailed, thrice: dumping packets)
- **Enumerate Options**: []
- **Alive Technique Options**: []
- **-e dst,hop send an errornous packets**: destination (default), hop-by-hop
- **-F         firewall mode**: -p -e dst -u 53 -s 22,25,80,443,9511 -a 9511
- **-n number  how often to send each packet (default**: local 1, remote 2)
- **-W time    time in ms to wait after sending a packet (default**: 1)
- **Help Options**: []
- **of 2001**: db8::1-fff or 2001:db8::1-2:0-ffff:0:0-ffff, etc.
- **-w ms    wait time for connect in ms (default**: 1000)
- **-m mtu     specifies the maximum MTU (default**: interface MTU, min: 1000)
- **-s resend  send each packet RESEND number of times, default**: 1
- **The following test cases are currently implemented**: []
- **1**: large hop-by-hop header with router-alert and filled with unknown options
- **2**: large destination header filled with unknown options
- **3**: hop-by-hop header with router alert option plus 180 headers
- **4**: hop-by-hop header with router alert option plus 178 headers + ping
- **5**: AH header + ping
- **6**: first fragments of a ping with a hop-by-hop header with router alert
- **7**: large hop-by-hop header filled with unknown options (no router alert)
- **-t NO   specify the number of threads to use (default**: 8, max: 32).
- **Examples**: -E H111, -E D
- **atk6-dnsrevenum6 dns.test.com 2001**: db8:42a8::/48
- **atk6-dnssecwalk 3.8 (c) 2020 by Marc Heuse <mh@mh-sec.de> http**: //www.mh-sec.de
- **Example**: atk6-sendpeesmp6 eth0 2048 fe80:: fe80::1
- **-N           use fe80**: : as source
- **The hello command takes optionally the DR priority (default**: 0).
- **server is offering. Note**: if the pool  is  very  large,  this  is
- **Smurfs  the local network of the victim. Note**: this depends on an
- **current versions).  Evil**: "ff02::1" as victim will DOS your local
- **The  homepage for this toolkit is**: https://github.com/vanhauser-thc/thc-
- **Sending options**: []
- **-n count    send how many packets (default**: forever)
- **-w seconds  wait time between the packets sent (default**: 5)
- **Flag options**: []
- **-O  do NOT set the override flag (default**: on)
- **-r  DO set the router flag (default**: off)
- **-s  DO set the solicitate flag (default**: off)
- **ND Security evasion options (can be combined)**: []
- **Note**: very simple server. Does not honor multiple queries in a packet, norNS, MX, etc. lookups.
- **-F flags           Set one or more of the following flags**: managed, other,
- **-E type            Router Advertisement Guard Evasion option. Types**: []
- **-i interval        time between RA packets (default**: 5)
- **-n number          number of RAs to send (default**: unlimited)
- **-X                 clean up by de-announcing fake router (default**: disabled)
- **offering. Note**: if the pool is very large, this is rather senseless. :-)
- **Modes**: []
- **if not supplied, target is random and query address is ff02**: :1
- **Evasion Methods**: []
- **Option 1024 can be used with 1..31 and 64. The evasion methods are processed in the following order**: 256, 512, 2048, 1..31/33..63 then either 64 or 128 then 1024.
- **-o options DHCPv6 message options to send (default**: abcdefghijklmonpqr)
- **-n number  how many times to send each packet (default**: 1)
- **-w sec     wait number of seconds between packets (default**: 0)
- **-p number  perform an alive check every number of tests (default**: none)
- **Note that the -P fuzzing target should be ff02**: :d
- **! Please note**: ndpexhaust6 is deprecated, please use ndpexhaust26!
- **NS security bypass**: -F fragment, -H hop-by-hop and -D large destination header
- **Smurfs the local network of the victim. Note**: this depends on an
- **Evil**: "ff02::1" as victim will DOS your local LAN completely
- **-w ms           wait time between packets in ms (default**: 1000, if -n not 1)
- **-H t**: l:v        add a hop-by-hop header with special content
- **-D t**: l:v        add a destination header with special content
- **-t ttl          specify TTL (default**: 255)
- **-T number       ICMPv6 type to send (default**: 128 = ping)
- **-C number       ICMPv6 code to send (default**: 0)
- **-n count        how often to send the packet (default**: 1)
- **t**: l:v syntax: type:length:value, value is in hex, e.g. 1:2:0eab
- **Maximum hop reach**: 31


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## address6 Usage Example

Convert an IPv6 address to a MAC address and vice-versa:

```console
root@kali:~# address6 fe80::76d4:35ff:fe4e:39c8
74:d4:35:4e:39:c8
root@kali:~# address6 74:d4:35:4e:39:c8
fe80::76d4:35ff:fe4e:39c8
```

## alive6 Usage Example

```console
root@kali:~# alive6 eth0
Alive: fd77:7c68:420a:1:426c:8fff:fe1b:cb90 [ICMP parameter problem]
Alive: fd77:7c68:420a:1:20c:29ff:fee5:5bf4 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:75d9:4f39:a46a:6f83 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:6912:8e80:e02f:1969 [ICMP echo-reply]
Alive: fd77:7c68:420a:1:201:6cff:fe6f:ddd1 [ICMP echo-reply]
```

## detect-new-ip6 Usage Example

```console
root@kali:~# detect-new-ip6 eth0
Started ICMP6 DAD detection (Press Control-C to end) ...
Detected new ip6 address: fe80::85d:9879:9251:853a
```

## dnsdict6 Usage Example

```console
root@kali:~# dnsdict6 example.com
Starting DNS enumeration work on example.com. ...
Starting enumerating example.com. - creating 8 threads for 798 words...
Estimated time to completion: 1 to 2 minutes
www.example.com. => 2606:2800:220:6d:26bf:1447:1097:aa7
```


## Source
- Path: kali-tools\thc-ipv6\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.141150
