---
tool_id: sipcrack
title: sipcrack
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: http://www.remote-exploit.org/codes_sipcrack.html
repository: 
version: 0.2-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-passwords kali-tools-voip"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sipcrack\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.107506
---

# Tool: sipcrack (sipcrack)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.remote-exploit.org/codes_sipcrack.html](http://www.remote-exploit.org/codes_sipcrack.html) |
| Repository |  |
| Version | 0.2-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-passwords kali-tools-voip |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/sipcrack
- **PackagesInfo**: |
- ****Installed size**: ** `72 KB`
- ****How to install**: ** `sudo apt install sipcrack`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sipcrack -h


## Documentation (Upstream)
-------------------------------------
 
 Usage: sipcrack [OPTIONS] [ -s | -w <wordlist> ] <dump file>
 
        <dump file>   = file containing logins sniffed by SIPdump 
 
        Options:                                                  
        -s            = use stdin for passwords                   
        -w wordlist   = file containing all passwords to try      
        -p num        = print cracking process every n passwords (for -w)
                        (ATTENTION: slows down heavily)           
 
 * Invalid arguments
 ```
 
 - - -
 
 ##### sipdump
 
 Part of SIPcrack, A suite of tools to sniff and crack the digest authentications within the SIP protocol.
 
 ```
 root@kali:~# sipdump -h
 
 SIPdump 0.2 
 ---------------------------------------
 
 Usage: sipdump [OPTIONS] <dump file>                           
 
        <dump file>    = file where captured logins will be written to
 
        Options:                                                  
        -i <interface> = interface to listen on                   
        -p <file>      = use pcap data file                       
        -m             = enter login data manually                
        -f "<filter>"  = set libpcap filter                       
 
 * Invalid arguments
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sipcrack\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.107506
