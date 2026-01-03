---
tool_id: dnsmap
title: dnsmap
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/resurrecting-open-source-projects/dnsmap
repository: 
version: 0.36-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/dnsmap-logo.svg
source_path: kali-tools\dnsmap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.872273
---

# Tool: dnsmap (dnsmap)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/resurrecting-open-source-projects/dnsmap](https://github.com/resurrecting-open-source-projects/dnsmap) |
| Repository |  |
| Version | 0.36-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/dnsmap-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/dnsmap
- **PackagesInfo**: |
- **Fun things that can happen**: []
- **(e.g.**: IP Cameras). This method is an alternative to finding devices via
- **This package provides two possible commands**: dnsmap and dnsmap-bulk.
- ****Installed size**: ** `259 KB`
- ****How to install**: ** `sudo apt install dnsmap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man dnsmap-bulk
- **1.  Finding interesting remote access servers (e.g.**: https://ex-
- **2.  Finding  badly  configured  and/or  unpatched  servers (e.g.**: []
- **vices  (e.g.**: IP  Cameras). This method is an alternative to
- **timestamp. e.g.**: dnsmap_example_com_br_2019_11_15_214812.txt. So,
- **your  online  experience.  i.e.**: killing your bandwidth. If used,
- **IP addresses. The maximum number of IPs to filter is 5.  Example**: []
- **Subdomain bruteforcing using dnsmap's built-in wordlist**: []
- **Subdomain bruteforcing using a user-supplied wordlist**: []
- **sults to /tmp/**: []
- **between each request**: []
- **wordlist**: []
- **New  bugs  should  be  reported at https**: //github.com/resurrecting-open-
- **tained by volunteers, inside dnsmap project, at  https**: //github.com/res-
- **WARNING**: using dnsmap-bulk, dnsmap will always use the default options,
- **results inside a directory**: []
- **https**: //github.com/resurrecting-open-source-projects/dnsmap/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dnsmap Usage Example

Scan example.com using a wordlist (`-w /usr/share/wordlists/dnsmap.txt`):

```console
root@kali:~# dnsmap example.com -w /usr/share/wordlists/dnsmap.txt
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)

[+] searching (sub)domains for example.com using /usr/share/wordlists/dnsmap.txt
[+] using maximum random delay of 10 millisecond(s) between requests
```

## dnsmap-bulk Usage Example

Create a file containing domain names to scan (domains.txt) and pass it to dnsmap-bulk.sh:

```console
root@kali:~# echo "example.com" >> domains.txt
root@kali:~# echo "example.org" >> domains.txt
root@kali:~# dnsmap-bulk.sh domains.txt
dnsmap 0.30 - DNS Network Mapper by pagvac (gnucitizen.org)

[+] searching (sub)domains for example.com using built-in wordlist
[+] using maximum random delay of 10 millisecond(s) between requests
```


## Source
- Path: kali-tools\dnsmap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.872273
