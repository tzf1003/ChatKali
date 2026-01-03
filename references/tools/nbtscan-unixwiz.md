---
tool_id: nbtscan-unixwiz
title: nbtscan-unixwiz
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://unixwiz.net/tools/nbtscan.html
repository: 
version: 1.0.35-0kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\nbtscan-unixwiz\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.002395
---

# Tool: nbtscan-unixwiz (nbtscan-unixwiz)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://unixwiz.net/tools/nbtscan.html](http://unixwiz.net/tools/nbtscan.html) |
| Repository |  |
| Version | 1.0.35-0kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/nbtscan-unixwiz
- **PackagesInfo**: |
- ****Installed size**: ** `53 KB`
- ****How to install**: ** `sudo apt install nbtscan-unixwiz`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# nbtscan-unixwiz -h
- **nbtscan-unixwiz**: invalid option -- 'h'
- **nbtscan 1.0.35 - 2008-04-08 - http**: //www.unixwiz.net/tools/
- **usage**: nbtscan-unixwiz [options] target [targets...]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/104243.js" id="asciicast-104243" async></script>

## nbtscan-unixwiz Usage Examples

Scan a range of IP addresses (`192.168.0.100-110`) without doing inverse name lookups (`-n`):

```console
root@kali:~# nbtscan-unixwiz -n 192.168.0.100-110
192.168.0.105   WORKGROUP\RETROPIE              SHARING
*timeout (normal end of scan)
```


Scan a single IP address (`192.168.0.38`) and show Full NBT resource record responses (`-f`):

```console
root@kali:~# nbtscan-unixwiz -f 192.168.0.38
192.168.0.38    WORKGROUP\DOOKOSSEL             SHARING
  DOOKOSSEL      <00> UNIQUE Workstation Service
  DOOKOSSEL      <03> UNIQUE Messenger Service<3>
  DOOKOSSEL      <20> UNIQUE File Server Service
  ..__MSBROWSE__.<01> GROUP  Master Browser
  WORKGROUP      <00> GROUP  Domain Name
  WORKGROUP      <1d> UNIQUE Master Browser
  WORKGROUP      <1e> GROUP  Browser Service Elections
  00:00:00:00:00:00   ETHER
```


## Source
- Path: kali-tools\nbtscan-unixwiz\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.002395
