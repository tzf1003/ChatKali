---
tool_id: sippts
title: sippts
categories: ["information-gathering", "vulnerability-analysis", "exploitation-tools", "sniffing-spoofing", "utilities"]
category_slugs: ["information-gathering", "vulnerability-analysis", "exploitation-tools", "sniffing-spoofing", "utilities"]
homepage: https://github.com/Pepelux/sippts
repository: 
version: 4.1.2-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sippts\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.108678
---

# Tool: sippts (sippts)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [exploitation-tools](../exploitation-tools.md)
- [sniffing-spoofing](../sniffing-spoofing.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/Pepelux/sippts](https://github.com/Pepelux/sippts) |
| Repository |  |
| Version | 4.1.2-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sippts
- **PackagesInfo**: |
- ****Installed size**: ** `762 KB`
- ****How to install**: ** `sudo apt install sippts`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sippts -h
- **usage**: sippts [-h]


## Documentation (Upstream)
---------| |
           .-'| |            | |`-.
         .'   | |   SIPPTS   | |   `.
      .-'      \ \          / /      `-.
    .'        _.| |--------| |._        `.
   /    -.  .'  | |        | |  `.  .-    \
  /       `(    | |________| |    )'       \
 |          \  .i------------i.  /          |
 |        .-')/                \(`-.        |
 \    _.-'.-'/     ________     \`-.`-._    /
  \.-'_.-'  /   .-' ______ `-.   \  `-._`-./\
   `-'     /  .' .-' _   _`-. `.  \     `-' \\
          | .' .' _ (3) (2) _`. `. |        //
         / /  /  (4)  ___  (1)_\  \ \       \\                                   SIPPTS version 4.1.2 (updated)
         | | |  _   ,'   `.==' `| | |       //                                        CVE version 0.1 (updated)
         | | | (5)  |     | (O) | | |      //                       https://github.com/Pepelux/sippts
         | | |   _  `.___.' _   | | |      \\               by Pepelux - https://twitter.com/pepeluxx
         | \  \ (6)  _   _ (9) /  / |      //
         /  `. `.   (7) (8)  .' .'  \      \\
        /     `. `-.______.-' .'     \     //
       /        `-.________.-'        \ __//
      |                                |--'
      |================================|
      "--------------------------------"
 
  -= SIPPTS is a set of tools for auditing VoIP systems based on the SIP protocol =- 
 
 Commands:
   {video,astami,scan,exten,rcrack,send,wssend,enumerate,leak,ping,invite,dump,dcrack,flood,sniff,spoof,pcapdump,rtpbleed,rtcpbleed,rtpbleedflood,rtpbleedinject}
     video                                         Animated help
     astami                                        Asterisk AMI pentest
     scan                                          Fast SIP scanner
     exten                                         Search SIP extensions of a
                                                   PBX
     rcrack                                        Remote password cracker
     send                                          Send a customized message
     wssend                                        Send a customized message
                                                   over WS
     enumerate                                     Enumerate methods of a SIP
                                                   server
     leak                                          Exploit SIP Digest Leak
                                                   vulnerability
     ping                                          SIP ping
     invite                                        Try to make calls through a
                                                   PBX
     dump                                          Dump SIP digest
                                                   authentications from a PCAP
                                                   file
     dcrack                                        SIP digest authentication
                                                   cracking
     flood                                         Flood a SIP server
     sniff                                         SIP network sniffing
     spoof                                         ARP Spoofing tool
     pcapdump                                      Extract data from a PCAP
                                                   file
     rtpbleed                                      Detect RTPBleed
                                                   vulnerability (send RTP
                                                   streams)
     rtcpbleed                                     Detect RTPBleed
                                                   vulnerability (send RTCP
                                                   streams)
     rtpbleedflood                                 Exploit RTPBleed
                                                   vulnerability (flood RTP)
     rtpbleedinject                                Exploit RTPBleed
                                                   vulnerability (inject WAV
                                                   file)
 
 Options:
   -h, --help                                      show this help message and
                                                   exit
 
 Command help:
   sippts <command> -h
 ```
 
 - - -
 
 ##### sippts-gui
 
 
 ```
 root@kali:~# sippts-gui -h
 
 
 
                __ _
              .: .' '.
             /: /     \_
            ;: ;  ,-'/`:\
            |: | |  |() :|
            ;: ;  '-.\_:/
             \: \     /`
              ':_'._.'
                 ||
                /__\
     .---.     |====|
   .'   _,"-,__|::  |
  /    ((O)=;--.::  |
 ;      `|: |  |::  |
 |       |: |  |::  |
 |       |: |  |::  |                                                   SIPPTS version 4.1.2 (updated)
 |       |: |  |::  |                                                        CVE version 0.1 (updated)
 |      /:'__\ |::  |                                      https://github.com/Pepelux/sippts
 |     [______]|::  |                              by Pepelux - https://twitter.com/pepeluxx
 |      `----` |::  |__
 |         _.--|::  |  ''--._
 ;       .'  __|====|__      '.
  \    .'_.-'._ `""` _.'-._    '.
   '--'/`      `'' ''`     `\    '.__
       '._     SIPPTS     _.'
         # `""--......--""`
 
 Welcome to SIPPTS! Type ? or help to list commands
 
 [!] Client interface: eth0
 [!] Client IP address: 10.0.2.15
 [!] Network mask: 255.255.255.0
 [!] Gateway: 10.0.2.2
 
 Type ? or help to list commands
 
 SIPPTS> 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sippts\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.108678
