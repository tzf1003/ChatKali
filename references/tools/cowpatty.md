---
tool_id: cowpatty
title: cowpatty
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://www.willhackforsushi.com/?page_id=50
repository: 
version: 4.8-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-802-11 kali-tools-wireless"]
icon: images/cowpatty-logo.svg
source_path: kali-tools\cowpatty\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.852690
---

# Tool: cowpatty (cowpatty)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.willhackforsushi.com/?page_id=50](https://www.willhackforsushi.com/?page_id=50) |
| Repository |  |
| Version | 4.8-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-802-11 kali-tools-wireless |
| Icon | images/cowpatty-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/cowpatty
- **PackagesInfo**: |
- ****Installed size**: ** `73 KB`
- ****How to install**: ** `sudo apt install cowpatty`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# genpmk -h
- **Usage**: genpmk [options]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## genpmk Usage Example

Use the provided dictionary file (`-f /usr/share/wordlists/nmap.lst`) to generate a hashfile, saving it to a file (`-d cowpatty_dict`) for the given ESSID (`-s securenet`):

```console
root@kali:~# genpmk -f /usr/share/wordlists/nmap.lst -d cowpatty_dict -s securenet
genpmk 1.3 - WPA-PSK precomputation attack. \&lt;jwright@hasborg.com\&gt;
File cowpatty_dict does not exist, creating.
key no. 1000: pinkgirl
1641 passphrases tested in 3.60 seconds: 456.00 passphrases/second
```

## cowpatty Usage Example

Use the provided hashfile (`-d cowpatty_dict`), read the packet capture (`-r Kismet-20181113-13-37-00-1.pcapdump`), and crack the password for the given ESSID (`-s 6F36E6`):

```console
root@kali:~# cowpatty -d cowpatty_dict -r Kismet-20181113-13-37-00-1.pcapdump -s 6F36E6
cowpatty 4.8 - WPA-PSK dictionary attack. <jwright@hasborg.com>

Collected all necessary data to mount crack against WPA2/PSK passphrase.
Starting dictionary attack. Please be patient.

The PSK is "12345678".

5 passphrases tested in 0.00 seconds: 50000.00 passphrases/second
```


## Source
- Path: kali-tools\cowpatty\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.852690
