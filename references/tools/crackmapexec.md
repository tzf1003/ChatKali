---
tool_id: crackmapexec
title: crackmapexec
categories: ["information-gathering", "vulnerability-analysis", "password-attacks", "exploitation-tools", "post-exploitation"]
category_slugs: ["information-gathering", "vulnerability-analysis", "password-attacks", "exploitation-tools", "post-exploitation"]
homepage: https://github.com/mpgn/CrackMapExec
repository: 
version: 5.4.0-0kali6
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/crackmapexec-logo.svg
source_path: kali-tools\crackmapexec\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.853926
---

# Tool: crackmapexec (crackmapexec)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [password-attacks](../password-attacks.md)
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/mpgn/CrackMapExec](https://github.com/mpgn/CrackMapExec) |
| Repository |  |
| Version | 5.4.0-0kali6 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/crackmapexec-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/crackmapexec
- **PackagesInfo**: |
- **The biggest improvements over the above tools are**: ['Pure Python script, no external tools required', 'Fully concurrent threading', 'Uses **ONLY** native WinAPI calls for discovering sessions, users, dumping']
- ****Installed size**: ** `2.29 MB`
- ****How to install**: ** `sudo apt install crackmapexec`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# crackmapexec -h
- **usage**: crackmapexec [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]


## Documentation (Upstream)
-'|  |_)  |       /  ^  \    |  ,----'|  '  /  |  \  /  |    /  ^  \    |  |_)  | |  |__    \  V  /  |  |__   |  ,----'
     |  |     |      /       /  /_\  \   |  |     |    <   |  |\/|  |   /  /_\  \   |   ___/  |   __|    >   <   |   __|  |  |
     |  `----.|  |\  \----. /  _____  \  |  `----.|  .  \  |  |  |  |  /  _____  \  |  |      |  |____  /  .  \  |  |____ |  `----.
      \______|| _| `._____|/__/     \__\  \______||__|\__\ |__|  |__| /__/     \__\ | _|      |_______|/__/ \__\ |_______| \______|
 
                                                 A swiss army knife for pentesting networks
                                     Forged by @byt3bl33d3r and @mpgn_x64 using the powah of dank memes
 
                                            Exclusive release for Porchetta Industries users
                                                        https://porchetta.industries/
 
                                                    Version : 5.4.0
                                                    Codename: Indestructible G0thm0g
 
 options:
   -h, --help            show this help message and exit
   -t THREADS            set how many concurrent threads to use (default: 100)
   --timeout TIMEOUT     max timeout in seconds of each thread (default: None)
   --jitter INTERVAL     sets a random delay between each connection (default: None)
   --darrell             give Darrell a hand
   --verbose             enable verbose output
 
 protocols:
   available protocols
 
   {ssh,smb,ftp,ldap,mssql,winrm,rdp}
     ssh                 own stuff using SSH
     smb                 own stuff using SMB
     ftp                 own stuff using FTP
     ldap                own stuff using LDAP
     mssql               own stuff using MSSQL
     winrm               own stuff using WINRM
     rdp                 own stuff using RDP
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\crackmapexec\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.853926
