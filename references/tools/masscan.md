---
tool_id: masscan
title: masscan
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/robertdavidgraham/masscan
repository: 
version: 2:1.3.2+ds1-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/masscan-logo.svg
source_path: kali-tools\masscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.983262
---

# Tool: masscan (masscan)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) |
| Repository |  |
| Version | 2:1.3.2+ds1-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/masscan-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/masscan
- **PackagesInfo**: |
- ****Installed size**: ** `516 KB`
- ****How to install**: ** `sudo apt install masscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# masscan --help
- **is the following, which scans the 10.x.x.x network for web servers**: []
- **example of all the parameters that are needed**: []
- **appear as follows in a configuration file**: []
- **To use the config file, type**: []
- **about. I suggest you try it now**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/31820.js" id="asciicast-31820" async></script>

## masscan Usage Example

Scan for a selection of ports (`-p22,80,445`) across a given subnet (`192.168.1.0/24`):

```console
root@kali:~# masscan -p22,80,445 192.168.1.0/24

Starting masscan 1.0.3 (http://bit.ly/14GZzcT) at 2014-05-13 21:35:12 GMT
 -- forced options: -sS -Pn -n --randomize-hosts -v --send-eth
Initiating SYN Stealth Scan
Scanning 256 hosts [3 ports/host]
Discovered open port 22/tcp on 192.168.1.217
Discovered open port 445/tcp on 192.168.1.220
Discovered open port 80/tcp on 192.168.1.230
```


## Source
- Path: kali-tools\masscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.983262
