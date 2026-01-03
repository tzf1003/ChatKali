---
tool_id: spooftooph
title: spooftooph
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: http://www.hackfromacave.com/projects/spooftooph.html
repository: 
version: 0.5.2-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-bluetooth kali-tools-wireless"]
icon: images/spooftooph-logo.svg
source_path: kali-tools\spooftooph\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.119812
---

# Tool: spooftooph (spooftooph)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackfromacave.com/projects/spooftooph.html](http://www.hackfromacave.com/projects/spooftooph.html) |
| Repository |  |
| Version | 0.5.2-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-bluetooth kali-tools-wireless |
| Icon | images/spooftooph-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/spooftooph
- **PackagesInfo**: |
- ****Installed size**: ** `74 KB`
- ****How to install**: ** `sudo apt install spooftooph`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# spooftooph -h
- **-a <address>**: Specify new BD_ADDR
- **-b <num_lines>**: Number of Bluetooth profiles to display per page
- **-B**: Disable banner for smaller screens (like phones)
- **-c <class>**: Specify new CLASS
- **-h**: Help
- **-i <dev>**: Specify interface
- **-m**: Specify multiple interfaces during selection
- **-n <name>**: Specify new NAME
- **-r <file>**: Read in CSV logfile
- **-R**: Assign random NAME, CLASS, and ADDR
- **-s**: Scan for devices in local area
- **-t <time>**: Time interval to clone device in range
- **-u**: USB delay.  Interactive delay for reinitializing interface
- **-w <file>**: Write to CSV logfile


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## spooftooph Usage Example

Use the Bluetooth interface (`-i hci1`) to spoof itself as the given address (`-a 00803789EE76`):

```console
root@kali:~# spooftooph -i hci1 -a 00803789EE76
Manufacturer:   Broadcom Corporation (15)
Device address: 00:19:0E:0E:EA:4B
```


## Source
- Path: kali-tools\spooftooph\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.119812
