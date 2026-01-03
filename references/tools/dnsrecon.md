---
tool_id: dnsrecon
title: dnsrecon
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/darkoperator/dnsrecon
repository: 
version: 1.3.1-3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/dnsrecon-logo.svg
source_path: kali-tools\dnsrecon\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.872676
---

# Tool: dnsrecon (dnsrecon)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/darkoperator/dnsrecon](https://github.com/darkoperator/dnsrecon) |
| Repository |  |
| Version | 1.3.1-3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/dnsrecon-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/dnsrecon
- **PackagesInfo**: |
- **DNSRecon is a Python script that provides the ability to perform**: []
- ****Installed size**: ** `1.45 MB`
- ****How to install**: ** `sudo apt install dnsrecon`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnsrecon -h
- **usage**: dnsrecon [-h] [-d DOMAIN] [-iL INPUT_LIST] [-n NS_SERVER] [-r RANGE]
- **options**: []
- **Possible types**: []
- **std**: SOA, NS, A, AAAA, MX and SRV.
- **rvl**: Reverse lookup of a given CIDR or IP range.
- **brt**: Brute force domains and hosts using a given dictionary.
- **srv**: SRV records.
- **axfr**: Test all NS servers for a zone transfer.
- **bing**: Perform Bing search for subdomains and hosts.
- **yand**: Perform Yandex search for subdomains and hosts.
- **crt**: Perform crt.sh search for subdomains and hosts.
- **snoop**: Perform cache snooping against all NS servers for a given domain, testing
- **tld**: Remove the TLD of given domain and test against all TLDs registered in IANA.
- **zonewalk**: Perform a DNSSEC zone walk using NSEC records.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script id="asciicast-31190" src="https://asciinema.org/a/31190.js" async type="text/javascript"></script>

## dnsrecon Usage Example

Scan a domain (`-d example.com`), use a dictionary to brute force hostnames (`-D /usr/share/wordlists/dnsmap.txt)`, do a standard scan (`-t std`), and save the output to a file (`–xml dnsrecon.xml`):

```console
root@kali:~# dnsrecon -d example.com -D /usr/share/wordlists/dnsmap.txt -t std --xml dnsrecon.xml
[*] Performing General Enumeration of Domain:example.com
[*] DNSSEC is configured for example.com
[*] DNSKEYs:
```


## Source
- Path: kali-tools\dnsrecon\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.872676
