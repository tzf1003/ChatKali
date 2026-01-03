---
tool_id: ipv6-toolkit
title: ipv6-toolkit
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://www.si6networks.com/tools/ipv6toolkit/
repository: 
version: 2.1+git20210331-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ipv6-toolkit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.948860
---

# Tool: ipv6-toolkit (ipv6-toolkit)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.si6networks.com/tools/ipv6toolkit/](https://www.si6networks.com/tools/ipv6toolkit/) |
| Repository |  |
| Version | 2.1+git20210331-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://gitlab.com/kalilinux/packages/ipv6-toolkit
- **PackagesInfo**: |
- **Included tools**: ['addr6: An IPv6 address analysis and manipulation tool.', 'flow6: A tool to perform a security asseessment of the IPv6 Flow Label.', 'frag6: A tool to perform IPv6 fragmentation-based attacks and to perform a']
- ****Installed size**: ** `3.46 MB`
- ****How to install**: ** `sudo apt install ipv6-toolkit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# udp6 -h
- **addr6**: An IPv6 address analysis and conversion tool
- **usage**: udp6 [-i INTERFACE] [-S LINK_SRC_ADDR] [-D LINK-DST-ADDR] [-s SRC_ADDR[/LEN]] [-d DST_ADDR] [-A HOP_LIMIT] [-y FRAG_SIZE] [-u DST_OPT_HDR_SIZE] [-U DST_OPT_U_HDR_SIZE] [-H HBH_OPT_HDR_SIZE] [-P PAYLOAD_SIZE] [-o SRC_PORT[/LEN]] [-a DST_PORT[/LEN]] [-N] [-f] [-j PREFIX[/LEN]] [-k PREFIX[/LEN]] [-J LINK_ADDR] [-K LINK_ADDR] [-b PREFIX[/LEN]] [-g PREFIX[/LEN]] [-B LINK_ADDR] [-G LINK_ADDR] [-F N_SOURCES] [-T N_PORTS] [-L | -l] [-z SECONDS] [-v] [-h]
- **OPTIONS**: []
- **Programmed by Fernando Gont for SI6 Networks <https**: //www.si6networks.com>
- **This script takes no further arguments, and operates as follows**: []
- **+ The format of the resulting output is**: []
- **tax**: []
- **lowing syntax**: []
- **2001**: db8:d::1. Firstly, script6 will obtain the output of path6 towards
- **Scan for IPv6 addresses of the network  2001**: db8::/64  that  embed  the
- **Scan  for  IPv6 addresses of the network 2001**: db8::/64, varying the two
- **fix fc00**: :/64. The tool will employ TCP segments as the  probe  packets
- **"66**: 55:44:33:22:11" ("-S" option). The probe packets will be IPv6 pack-
- **KNOWN_IIDS,  at  remote network 2001**: db8::/64. The target addresses are
- **obtaining by concatenating the network prefix  2001**: db8::/64  with  the
- **<http**: //www.si6networks.com>.
- **copy  of  the   license   is   available   at   <http**: //www.gnu.org/li-
- **flow6**: Security assessment tool for the IPv6 Flow Label field
- **--protocol, -P            IPv6 Payload protocol (valid**: TCP, UDP)
- **Programmed by Fernando Gont on behalf of SI6 Networks <https**: //www.si6networks.com>
- **frag6**: A security assessment tool for attack vectors based on IPv6 fragments
- **icmp6**: Security assessment tool for attack vectors based on ICMPv6 error messages
- **[-t TYPE[**: CODE] | -e CODE | -A CODE -V CODE -R CODE] [-r TARGET_ADDR]
- **[-P PAYLOAD_SIZE] [-n] [-a SRC_PORTL[**: SRC_PORTH]]
- **[-o DST_PORTL[**: DST_PORTH]] [-X TCP_FLAGS] [-q TCP_SEQ] [-Q TCP_ACK]
- **--icmp6, -t                 ICMPv6 Type**: Code
- **jumbo6**: Security assessment tool for attack vectors based on IPv6 jumbo packets
- **mldq6**: Security assessment tool for attack vectors based on MLD Query messages
- **na6**: Security Assessment tool for attack vectors based on NA messages
- **ni6**: Security assessment tool for attack vectors based on ICMPv6 NI messages
- **ns6**: Security assessment tool for attack vectors based on NS messages
- **path6**: A versatile IPv6 traceroute
- **[-H HBH_OPT_HDR_SIZE] [-y FRAG**: SIZE] [-f FLOW_LABEL]
- **ra6**: Security assessment tool for attack vectors based on RA messages
- **rd6**: Security assessment tool for attack vectors based on Redirect messages
- **rs6**: Security assessment tool for attack vectors based on RS messages
- **scan6**: An advanced IPv6 scanning tool
- **--port-scan, -j             Port scan type and range {tcp,udp}**: port_low[-port_hi]
- **--timeout, -O               Timeout in seconds (default**: 1 second)
- **of Alexa's Top 1M web sites. That is, lines with the following syntax**: []
- **Among the statistics produced by this command are**: []
- *** Packet drop rate**: That is, the percentage of destination IPv6
- ***  Packet  drop  rate  by  different  AS**: That is, the percentage of
- *** Packet drop rate by same AS**: That is, the percentage of packet
- *** Delta-Hops statistics**: Statistics  regarding  the  Delta-Hops  at
- **such destination**: []
- **1. 2001**: db8:1:1000::1
- **2. 2001**: db8:2:2000::4
- **3. 2001**: db8:2:4000::1
- **4. 2001**: db8:3:4000::1
- **5. 2001**: db8:3:1000::1
- **6. 2001**: db8:4:4000::1
- **7. 2001**: db8:4:1000::1
- **8. 2001**: db8:5:5000::1
- **9. 2001**: db8:5:6000::1
- **10. 2001**: db8:d::1
- **same destination**: []
- **the EH-enabled path6 ("2001**: db8:4:4000::1" in this case) as "M". Assum-
- **path6" ("2001**: db8:4:1000::1" in our case), as "M+1", etc.
- **is  "2001**: db8:4:4000::1",  and  therefore we assume the "node" dropping
- **node to be "2001**: db8:4:1000::1" ("M+1").
- **The resulting output will have the following syntax**: []
- **where**: []
- *** DEST**: Destination IPv6 address (as read from standard input).
- **In our example above, this would be 2001**: db8:d::1.
- *** LAST_NOEH**: Last responding IPv6 address for the path6 command
- **above, this would be 2001**: db8:d::1.
- *** HOPS_NOEH**: Number of hops to LAST_NOEH. In our example above,
- *** LAST_EH**: Last responding IPv6 address in the EH-enabled path6
- **command. In our example above, this would be 2001**: db8:4:4000::1.
- *** HOPS_EH**: Number of hops to LAST_EH. In our example above, this
- *** DROPN**: Node after the dropping node (M+2). In our example,
- **example above, this would be 2001**: db8:4:1000::1.
- **this would be 2001**: db8:5:5000::1.
- **$ script6 get-asn 2001**: db8::1
- **IPv6 address 2001**: db8::1.
- **$ script6 get-as 2001**: db8::1
- **ing to the IPv6 address 2001**: db8::1.
- **IETF RFC7872 (available at**: <http://tools.ietf.org/html/rfc7872>) for a
- **copy   of   the   license   is   available  at  <http**: //www.gnu.org/li-
- **tcp6**: Security assessment tool for attack vectors based on TCP/IPv6 packets
- **--win-modulation, -M      TCP Window modulation (WIN1**: TIME1:WIN2:TIME2)
- **udp6**: Security assessment tool for attack vectors based on UDP/IPv6 packets


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\ipv6-toolkit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.948860
