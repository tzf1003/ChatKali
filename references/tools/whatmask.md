---
tool_id: whatmask
title: whatmask
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://www.laffeycomputer.com/whatmask.html
repository: 
version: 1.2-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\whatmask\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.170053
---

# Tool: whatmask (whatmask)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.laffeycomputer.com/whatmask.html](http://www.laffeycomputer.com/whatmask.html) |
| Repository |  |
| Version | 1.2-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/whatmask
- **PackagesInfo**: |
- **will echo back the following**: ['The netmask in the following formats: CIDR, Netmask, Netmask (Hex)']
- ****Installed size**: ** `40 KB`
- ****How to install**: ** `sudo apt install whatmask`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man whatmask
- **Netmask Notations supported**: []
- **Whatmask will echo back the following**: ['The netmask in the following formats: CIDR, Netmask, Netmask (Hex),']
- **Examples of how Whatmask works**: []


## Documentation (Upstream)
------------------------------------------
                     TCP/IP SUBNET MASK EQUIVALENTS
             ---------------------------------------------
             CIDR = .....................: /26
             Netmask = ..................: 255.255.255.192
             Netmask (hex) = ............: 0xffffffc0
             Wildcard Bits = ............: 0.0.0.63
             Usable IP Addresses = ......: 62
 
             myhost> whatmask 255.255.192.0
 
             ---------------------------------------------
                     TCP/IP SUBNET MASK EQUIVALENTS
             ---------------------------------------------
             CIDR = .....................: /18
             Netmask = ..................: 255.255.192.0
             Netmask (hex) = ............: 0xffffc000
             Wildcard Bits = ............: 0.0.63.255
             Usable IP Addresses = ......: 16,382
 
             myhost> whatmask 0xffffffe0
 
             ---------------------------------------------
                     TCP/IP SUBNET MASK EQUIVALENTS
             ---------------------------------------------
             CIDR = .....................: /27
             Netmask = ..................: 255.255.255.224
             Netmask (hex) = ............: 0xffffffe0
             Wildcard Bits = ............: 0.0.0.31
             Usable IP Addresses = ......: 30
 
             myhost> whatmask 0.0.0.31
 
             ---------------------------------------------
                     TCP/IP SUBNET MASK EQUIVALENTS
             ---------------------------------------------
             CIDR = .....................: /27
             Netmask = ..................: 255.255.255.224
             Netmask (hex) = ............: 0xffffffe0
             Wildcard Bits = ............: 0.0.0.31
             Usable IP Addresses = ......: 30
 
             myhost> whatmask 192.168.165.23/19
 
             ------------------------------------------------
                          TCP/IP NETWORK INFORMATION
             ------------------------------------------------
             IP Entered = ..................: 192.168.165.23
             CIDR = ........................: /19
             Netmask = .....................: 255.255.224.0
             Netmask (hex) = ...............: 0xffffe000
             Wildcard Bits = ...............: 0.0.31.255
             ------------------------------------------------
             Network Address = .............: 192.168.160.0
             Broadcast Address = ...........: 192.168.191.255
             Usable IP Addresses = .........: 8,190
             First Usable IP Address = .....: 192.168.160.1
             Last Usable IP Address = ......: 192.168.191.254
 
             myhost> whatmask 192.168.0.13/255.255.255.0
 
             ------------------------------------------------
                          TCP/IP NETWORK INFORMATION
             ------------------------------------------------
             IP Entered = ..................: 192.168.0.13
             CIDR = ........................: /24
             Netmask = .....................: 255.255.255.0
             Netmask (hex) = ...............: 0xffffff00
             Wildcard Bits = ...............: 0.0.0.255
             ------------------------------------------------
             Network Address = .............: 192.168.0.0
             Broadcast Address = ...........: 192.168.0.255
             Usable IP Addresses = .........: 254
             First Usable IP Address = .....: 192.168.0.1
             Last Usable IP Address = ......: 192.168.0.254
 
             myhost> whatmask 192.168.0.113/0xffffffe0
 
             ------------------------------------------------
                          TCP/IP NETWORK INFORMATION
             ------------------------------------------------
             IP Entered = ..................: 192.168.0.113
             CIDR = ........................: /27
             Netmask = .....................: 255.255.255.224
             Netmask (hex) = ...............: 0xffffffe0
             Wildcard Bits = ...............: 0.0.0.31
             ------------------------------------------------
             Network Address = .............: 192.168.0.96
             Broadcast Address = ...........: 192.168.0.127
             Usable IP Addresses = .........: 30
             First Usable IP Address = .....: 192.168.0.97
             Last Usable IP Address = ......: 192.168.0.126
 
             myhost> whatmask 192.168.0.169/0.0.0.127
 
             ------------------------------------------------
                          TCP/IP NETWORK INFORMATION
             ------------------------------------------------
             IP Entered = ..................: 192.168.0.169
             CIDR = ........................: /25
             Netmask = .....................: 255.255.255.128
             Netmask (hex) = ...............: 0xffffff80
             Wildcard Bits = ...............: 0.0.0.127
             ------------------------------------------------
             Network Address = .............: 192.168.0.128
             Broadcast Address = ...........: 192.168.0.255
             Usable IP Addresses = .........: 126
             First Usable IP Address = .....: 192.168.0.129
             Last Usable IP Address = ......: 192.168.0.254
 
 BUGS
        Report bugs to <software@laffeycomputer.com>
 
 CONTRIBUTORS
        Original code:
               Joe Laffey <software@laffeycomputer.com>
 
        Assistance with Manpage and Packaging:
               David Wirch <kuma@linuxboxen.org>
 
        Many thanks to the beta testers and users who sent in valuable feedback!
 
 UPDATES
        Official Whatmask website:
               http://www.laffeycomputer.com/whatmask.html
 
 LAFFEY Computer Imaging           Nov 14, 2003                      Whatmask(1)
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\whatmask\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.170053
