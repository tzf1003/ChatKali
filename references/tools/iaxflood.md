---
tool_id: iaxflood
title: iaxflood
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: http://www.hackingexposedvoip.com/sec_tools.html
repository: 
version: 0.1-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\iaxflood\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.942127
---

# Tool: iaxflood (iaxflood)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackingexposedvoip.com/sec_tools.html](http://www.hackingexposedvoip.com/sec_tools.html) |
| Repository |  |
| Version | 0.1-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/iaxflood
- **PackagesInfo**: |
- ****Installed size**: ** `25 KB`
- ****How to install**: ** `sudo apt install iaxflood`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# iaxflood -h
- **usage**: iaxflood sourcename destinationname numpackets


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## iaxflood Usage Example

Flood the VoIP server from the source (`192.168.1.202`) to the destination (`192.168.1.1`) by sending 500 packets (`500`):

```console
root@kali:~# iaxflood 192.168.1.202 192.168.1.1 500
Will flood port 4569 from port 4569 500 times
We have IP_HDRINCL
```


## Source
- Path: kali-tools\iaxflood\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.942127
