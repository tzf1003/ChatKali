---
tool_id: iw
title: iw
categories: ["wireless-attacks", "information-gathering", "utilities"]
category_slugs: ["wireless-attacks", "information-gathering", "utilities"]
homepage: https://wireless.wiki.kernel.org/en/users/documentation/iw
repository: 
version: 6.17-1
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\iw\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.951492
---

# Tool: iw (iw)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://wireless.wiki.kernel.org/en/users/documentation/iw](https://wireless.wiki.kernel.org/en/users/documentation/iw) |
| Repository |  |
| Version | 6.17-1 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/kernel-team/iw
- **PackagesInfo**: |
- ****Installed size**: ** `332 KB`
- ****How to install**: ** `sudo apt install iw`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# iw -h
- **Usage**: iw [options] command
- **Options**: []
- **Commands**: []
- **dev <devname> ap start <SSID> <SSID> <freq> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz|160MHz|320MHz] [punct <bitmap>] <beacon interval in TU> <DTIM period> [hidden-ssid|zeroed-ssid] head <beacon head in hexadecimal> [tail <beacon tail in hexadecimal>] [inactivity-time <inactivity time in seconds>] [key0**: abcde d:1:6162636465]
- **dev <devname> ap start <SSID> <control freq> [5|10|20|40|80|80+80|160|320] [<center1_freq> [<center2_freq>]] [punct <bitmap>] <beacon interval in TU> <DTIM period> [hidden-ssid|zeroed-ssid] head <beacon head in hexadecimal> [tail <beacon tail in hexadecimal>] [inactivity-time <inactivity time in seconds>] [key0**: abcde d:1:6162636465]
- **The configuration file contains coalesce rules**: []
- **delay**: maximum coalescing delay in msec.
- **condition**: 1/0 i.e. 'not match'/'match' the patterns
- **patterns**: each pattern is given as a bytestring with '-' in
- **places where any byte may be present, e.g. 00**: 11:22:-:44 will
- **match 00**: 11:22:33:44 and 00:11:22:33:ff:44 etc. Offset and
- **pattern should be separated by '+', e.g. 18+43**: 34:00:12 will
- **match '43**: 34:00:12' after 18 bytes of offset in Rx packet.
- **dev <devname> auth <SSID> <bssid> <type**: open|shared> <freq in MHz> [key 0:abcde d:1:6162636465]
- **dev <devname> connect [-w] <SSID> [<freq in MHz>] [<bssid>] [auth open|shared] [key 0**: abcde d:1:6162636465] [mfp:req/opt/no]
- **dev <devname> ibss join <SSID> <freq in MHz> [NOHT|HT20|HT40+|HT40-|5MHz|10MHz|80MHz] [fixed-freq] [<fixed bssid>] [beacon-interval <TU>] [basic-rates <rate in Mbps,rate2,...>] [mcast-rate <rate in Mbps>] [key d**: 0:abcde]
- **Valid interface types are**: managed, ibss, monitor, mesh, wds.
- **The flags are only used for monitor interfaces, valid flags are**: []
- **none**: no special flags
- **fcsfail**: show frames with FCS errors
- **control**: show control frames
- **otherbss**: show frames from other BSSes
- **cook**: use cooked mode
- **active**: use active mode (ACK incoming unicast packets)
- **mumimo-groupid <GROUP_ID>**: use MUMIMO according to a group id
- **mumimo-follow-mac <MAC_ADDRESS>**: use MUMIMO according to a MAC address
- **Each line in the file represents a target, with the following format**: []
- **dev <devname> mgmt dump frame <type as hex ab> <pattern as hex ab**: cd:..> [frame <type> <pattern>]* [count <frames>]
- **Example**: iw dev wlan0 mgmt dump frame 40 00 frame 40 01:02 count 10
- **.Example**: iw dev wlan0 mpath probe xx:xx:xx:xx:xx:xx frame 01:xx:xx:00
- **wdev <idx> nan add_func type <publish|subscribe|followup> [active] [solicited] [unsolicited] [bcast] [close_range] name <name> [info <info>] [flw_up_id <id> flw_up_req_id <id> flw_up_dest <mac>] [ttl <ttl>] [srf <include|exclude> <bf|list> [bf_idx] [bf_len] <mac1;mac2...>] [rx_filter <str1**: str2...>] [tx_filter <str1:str2...>]
- **dev <devname> scan [-u] [freq <freq>*] [duration <dur>] [ies <hex as 00**: 11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
- **dev <devname> scan sched_start [interval <in_msecs> | scan_plans [<interval_secs**: iterations>*] <interval_secs>] [delay <in_secs>] [freqs <freq>+] [matches [ssid <ssid>]+]] [active [ssid <ssid>]+|passive] [randomise[=<addr>/<mask>]] [coloc] [flush]
- **dev <devname> scan trigger [freq <freq>*] [duration <dur>] [ies <hex as 00**: 11:..>] [meshid <meshid>] [lowpri,flush,ap-force,duration-mandatory,coloc] [randomise[=<addr>/<mask>]] [ssid <ssid>*|passive]
- **dev <devname> set bitrates [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> [he-mcs-<2.4|5|6> <NSS**: MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5] [he-gi-<2.4|5|6> <0.8|1.6|3.2>] [he-ltf-<2.4|5|6> <1|2|4>]
- **dev <devname> set tidconf [peer <MAC address>] tids <mask> [override] [sretry <num>] [lretry <num>] [ampdu [on|off]] [amsdu [on|off]] [noack [on|off]] [rtscts [on|off]][bitrates <type [auto|fixed|limit]> [legacy-<2.4|5> <legacy rate in Mbps>*] [ht-mcs-<2.4|5> <MCS index>*] [vht-mcs-<2.4|5> <NSS**: MCSx,MCSy... | NSS:MCSx-MCSy>*] [sgi-2.4|lgi-2.4] [sgi-5|lgi-5]]
- **Examples**: []
- **$ iw dev wlan0 set tidconf peer xx**: xx:xx:xx:xx:xx tids 0x2 bitrates limit vht-mcs-5 4:9
- **Set monitor flags. Valid flags are**: []
- **Valid values**: 0 - 255.
- **Put this wireless device into a different network namespace**: []
- **phy <phyname> set sar_specs <sar type> <range index**: sar power>*
- **Example subtype values**: 0xA (disassociation), 0xC (deauthentication)
- **phy <phyname> wowlan enable [any] [disconnect] [magic-packet] [gtk-rekey-failure] [eap-identity-request] [4way-handshake] [rfkill-release] [net-detect [interval <in_msecs> | scan_plans [<interval_secs**: iterations>*] <interval_secs>] [delay <in_secs>] [freqs <freq>+] [matches [ssid <ssid>]+]] [active [ssid <ssid>]+|passive] [randomise[=<addr>/<mask>]] [coloc] [flush]] [tcp <config-file>] [patterns [offset1+]<pattern1> ...]
- **may be present, e.g. 00**: 11:22:-:44 will match 00:11:22:33:44 and
- **00**: 11:22:33:ff:44 etc.
- **Offset and pattern should be separated by '+', e.g. 18+43**: 34:00:12 will match '43:34:00:12' after 18 bytes of offset in Rx packet.
- **The TCP configuration file contains**: []
- **source=ip[**: port]
- **dest=ip**: port@mac
- **Net-detect configuration example**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\iw\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.951492
