---
tool_id: seclists
title: seclists
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/danielmiessler/SecLists
repository: 
version: 2025.2-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-passwords"]
icon: images/seclists-logo.svg
source_path: kali-tools\seclists\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.098874
---

# Tool: seclists (seclists)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) |
| Repository |  |
| Version | 2025.2-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-passwords |
| Icon | images/seclists-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/seclists
- **PackagesInfo**: |
- ****Installed size**: ** `1.83 GB`
- ****How to install**: ** `sudo apt install seclists`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# seclists -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## SecLists Usage Examples

```console
root@kali:~# ls -lh /usr/share/seclists/
total 40K
drwxr-xr-x  6 root root 4.0K Mar 23 09:56 Discovery
drwxr-xr-x  3 root root 4.0K Mar 23 09:56 Fuzzing
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 IOCs
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Miscellaneous
drwxr-xr-x 11 root root 4.0K Mar 23 09:56 Passwords
drwxr-xr-x  2 root root 4.0K Mar 23 09:56 Pattern-Matching
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Payloads
-rwxr-xr-x  1 root root 3.5K Mar  7 16:02 README.md
drwxr-xr-x  4 root root 4.0K Mar 23 09:56 Usernames
drwxr-xr-x  7 root root 4.0K Mar 23 09:56 Web-Shells
root@kali:~#
root@kali:~# tree -d /usr/share/seclists/
/usr/share/seclists/
├── Discovery
│   ├── DNS
│   ├── Infrastructure
│   ├── SNMP
│   └── Web-Content
│       ├── CMS
│       ├── SVNDigger
│       │   ├── cat
│       │   │   ├── Conf
│       │   │   ├── Database
│       │   │   ├── Language
│       │   │   └── Project
│       │   └── context
│       ├── URLs
│       └── Web-Services
├── Fuzzing
│   └── Polyglots
├── IOCs
├── Miscellaneous
├── Passwords
│   ├── Common-Credentials
│   ├── Cracked-Hashes
│   ├── Default-Credentials
│   ├── Honeypot-Captures
│   ├── Leaked-Databases
│   ├── Malware
│   ├── Permutations
│   ├── Software
│   └── WiFi-WPA
├── Pattern-Matching
├── Payloads
│   ├── Anti-Virus
│   ├── File-Names
│   ├── Images
│   ├── PHPInfo
│   └── Zip-Bombs
├── Usernames
│   ├── Honeypot-Captures
│   └── Names
└── Web-Shells
    ├── FuzzDB
    ├── JSP
    ├── laudanum-0.8
    │   ├── asp
    │   ├── aspx
    │   ├── cfm
    │   ├── jsp
    │   │   └── warfiles
    │   │       ├── META-INF
    │   │       └── WEB-INF
    │   └── php
    ├── PHP
    └── WordPress

53 directories
root@kali:~#
```


## Source
- Path: kali-tools\seclists\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.098874
