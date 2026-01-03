---
tool_id: dmitry
title: dmitry
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/
repository: 
version: 1.3a-8
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/dmitry-logo.svg
source_path: kali-tools\dmitry\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.869188
---

# Tool: dmitry (dmitry)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/](https://mor-pah.net/software/dmitry-deepmagic-information-gathering-tool/) |
| Repository |  |
| Version | 1.3a-8 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/dmitry-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/dmitry
- **PackagesInfo**: |
- ****Installed size**: ** `50 KB`
- ****How to install**: ** `sudo apt install dmitry`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dmitry -h
- **Usage**: dmitry [-winsepfb] [-t 0-9] [-o %host.txt] host


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script id="asciicast-31154" src="https://asciinema.org/a/31154.js" async type="text/javascript"></script>

## dmitry Usage Example

Run a domain whois lookup (`w`), an IP whois lookup (`i`), retrieve Netcraft info (`n`), search for subdomains (`s`), search for email addresses (`e`), do a TCP port scan (`p`), and save the output to example.txt (`o`) for the domain `example.com`:

```console
root@kali:~# dmitry -winsepo example.txt example.com
Deepmagic Information Gathering Tool
"There be some deep magic going on"

Writing output to 'example.txt'

HostIP:93.184.216.119
HostName:example.com

Gathered Inet-whois information for 93.184.216.119
---------------------------------
```


## Source
- Path: kali-tools\dmitry\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.869188
