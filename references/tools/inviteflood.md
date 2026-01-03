---
tool_id: inviteflood
title: inviteflood
categories: ["exploitation-tools", "utilities"]
category_slugs: ["exploitation-tools", "utilities"]
homepage: http://www.hackingvoip.com/sec_tools.html
repository: 
version: 2.0-1kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\inviteflood\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.947988
---

# Tool: inviteflood (inviteflood)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackingvoip.com/sec_tools.html](http://www.hackingvoip.com/sec_tools.html) |
| Repository |  |
| Version | 2.0-1kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/inviteflood
- **PackagesInfo**: |
- ****Installed size**: ** `33 KB`
- ****How to install**: ** `sudo apt install inviteflood`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# inviteflood -h
- **Usage**: []
- **-a flood tool "From**: " alias (e.g. jane.doe)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## inviteflood Usage Example

Using the eth0 interface (`eth0`) and the provided user (`5000`), flood the target domain (`example.local`) and flood target (`192.168.1.5`) using 100 packets (`100`):

```console
root@kali:~# inviteflood eth0 5000 example.local 192.168.1.5 100

inviteflood - Version 2.0
              June 09, 2006

source IPv4 addr:port   = 192.168.1.202:9
dest   IPv4 addr:port   = 192.168.1.5:5060
targeted UA             = 5000@192.168.1.1

Flooding destination with 100 packets
sent: 100
```


## Source
- Path: kali-tools\inviteflood\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.947988
