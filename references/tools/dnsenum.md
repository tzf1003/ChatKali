---
tool_id: dnsenum
title: dnsenum
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/SparrowOchon/dnsenum2
repository: 
version: 1.3.2-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/dnsenum-logo.svg
source_path: kali-tools\dnsenum\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.871392
---

# Tool: dnsenum (dnsenum)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/SparrowOchon/dnsenum2](https://github.com/SparrowOchon/dnsenum2) |
| Repository |  |
| Version | 1.3.2-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/dnsenum-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/dnsenum
- **PackagesInfo**: |
- **currently performs the following operations**: ["Get the host's addresses (A record).", 'Get the namservers (threaded).', 'Get the MX record (threaded).', 'Perform axfr queries on nameservers and get BIND versions(threaded).', 'Get extra names and subdomains via google scraping (google query =']
- **"allinurl**: -www site:domain").
- ****Installed size**: ** `87 KB`
- ****How to install**: ** `sudo apt install dnsenum`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnsenum -h
- **dnsenum VERSION**: 1.3.1
- **Usage**: dnsenum [Options] <domain>
- **[Options]**: []
- **Note**: If no -f tag supplied will default to /usr/share/dnsenum/dns.txt or
- **GENERAL OPTIONS**: []
- **-t, --timeout <value>	The tcp and udp timeout values in seconds (default**: 10s).
- **-v, --verbose		Be verbose**: show all the progress and all the error messages.
- **GOOGLE SCRAPING OPTIONS**: []
- **BRUTE FORCE OPTIONS**: []
- **WHOIS NETRANGE OPTIONS**: []
- **-d, --delay <value>	The maximum value of seconds to wait between whois queries, the value is defined randomly, default**: 3s.
- ****Warning****: this can generate very large netranges and it will take lot of time to perform reverse lookups.
- **REVERSE LOOKUP OPTIONS**: []
- **OUTPUT OPTIONS**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dnsenum Usage Example

Don’t do a reverse lookup (`–noreverse`) and save the output to a file (`-o mydomain.xml`) for the domain `example.com`:

```console
root@kali:~# dnsenum --noreverse -o mydomain.xml example.com
dnsenum VERSION:1.2.4

-----   example.com   -----


Host's addresses:
__________________

example.com.                             392      IN    A        93.184.216.119


Name Servers:
______________

b.iana-servers.net.                      122      IN    A        199.43.133.53
a.iana-servers.net.                      122      IN    A        199.43.132.53


Mail (MX) Servers:
___________________
```


## Source
- Path: kali-tools\dnsenum\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.871392
