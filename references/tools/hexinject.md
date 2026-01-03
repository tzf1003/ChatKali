---
tool_id: hexinject
title: hexinject
categories: ["sniffing-spoofing"]
category_slugs: ["sniffing-spoofing"]
homepage: https://hexinject.sourceforge.net/
repository: 
version: 1.6-0kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-sniffing-spoofing"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\hexinject\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.932164
---

# Tool: hexinject (hexinject)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://hexinject.sourceforge.net/](https://hexinject.sourceforge.net/) |
| Repository |  |
| Version | 1.6-0kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-sniffing-spoofing |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/hexinject
- **PackagesInfo**: |
- ****Installed size**: ** `100 KB`
- ****How to install**: ** `sudo apt install hexinject`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# prettypacket -h
- **written by**: Emanuele Acri <crossbower@tuta.io>
- **Usage**: []
- **Options**: []
- **hexinject**: invalid option -- '-'
- **Injection options**: []
- **Interface options**: []
- **(experimental**: use airmon-ng instead of this...)
- **Other options**: []
- **APD-like data format**: http://wiki.hping.org/26
- **usage**: []
- **example packets**: []
- **ethernet(dst=ff**: ff:ff:ff:ff:ff,src=ff:ff:ff:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=00,totlen=30,id=60976,fragoff=0,mf=0,df=1,rf=0,ttl=64,proto=tcp,cksum=0x40c9,saddr=192.168.1.9,daddr=173.194.44.95)+tcp(sport=32857,dport=80,seq=1804471615,ack=0,ns=0,off=8,flags=s,win=62694,cksum=0xda46,urp=0)+tcp.nop()+tcp.nop()+tcp.timestamp(val=54111314,ecr=1049055856)+data(str=f0a)
- **(types**: tcp, udp, icmp, igmp, arp, stp,


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hexinject Usage Example

Start in sniffing mode (`-s`) through the eth0 interface (`-i eth0`):

```console
root@kali:~# hexinject -s -i eth0
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 E4 36 00 00 40 11 11 4E C0 A8 01 E8 C0 A8 01 FF D3 C6 7E 9C 00 1D B1 DA 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 A1 63 00 00 40 11 54 21 C0 A8 01 E8 C0 A8 01 FF FF 69 7E 9E 00 1D 86 35 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 BF 94 00 00 40 11 35 FC C0 A8 01 DC C0 A8 01 FF E3 ED 7E 9C 00 1D A1 BF 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 7C C3 A1 A4 B4 70 08 00 45 00 00 31 2F DE 00 00 40 11 C5 B2 C0 A8 01 DC C0 A8 01 FF C5 16 7E 9E 00 1D C0 94 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
```

## prettypacket Usage Example

Print an example of a UDP packet (`-x udp`):

```console
root@kali:~# prettypacket -x udp

Ethernet Header:
 1C AF F7 6B 0E 4D        Destination hardware address
 AA 00 04 00 0A 04        Source hardware address
 08 00                    Lenght/Type

IP Header:
 45                       Version / Header length
 00                       ToS / DFS
 00 3C                    Total length
 9B 23                    ID
 00 00                    Flags / Fragment offset
 40                       TTL
 11                       Protocol
 70 BC                    Checksum
 C0 A8 01 09              Source address
 D0 43 DC DC              Destination address

UDP Header:
 91 02                    Source port
 00 35                    Destination port
 00 28                    Length
 6F 0B                    Checksum

Payload or Trailer:
 AE 9C 01 00 00 01 00 00 00 00 00 00 03 77 77 77 06 67 6F 6F 67 6C 65 03 63 6F
 6D 00 00 01 00 01
```

## hex2raw Usage Example

```console
root@kali:~# hex2raw
 FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 E4 36 00 00 40 11 11 4E C0 A8 01 E8 C0 A8 01 FF D3 C6 7E 9C 00 1D B1 DA 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
FF FF FF FF FF FF 40 6C 8F 1B CB 90 08 00 45 00 00 31 A1 63 00 00 40 11 54 21 C0 A8 01 E8 C0 A8 01 FF FF 69 7E 9E 00 1D 86 35 4D 2D 53 45 41 52 43 48 20 2A 20 48 54 54 50 2F 31 2E 31 0D 0A
������@lE1�c@T!�������i~��5M-SEARCH * HTTP/1.1
```

## packets.tcl Usage Example

```console
root@kali:~# packets.tcl 'ethernet(dst=ff:ff:ff:ff:ee:ee,src=aa:aa:ee:ff:ff:ff,type=0x0800)+ip(ihl=5,ver=4,tos=0xc0,totlen=58,id=62912,fragoff=0,mf=0,df=0,rf=0,ttl=64,proto=1,cksum=0xe500,saddr=192.168.1.7,daddr=192.168.1.6)+icmp(type=3,code=3,unused=0)+data(str=aaaa)+udp(sport=33169,dport=10,len=10,cksum=0x94d6)+data(str=aaaa)+arp(htype=ethernet,ptype=ip,hsize=6,psize=4,op=request,shard=00:11:22:33:44:55,sproto=192.168.1.1,thard=22:22:22:22:22:22,tproto=10.0.0.1)' > packet-out
```


## Source
- Path: kali-tools\hexinject\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.932164
