---
tool_id: sniffjoke
title: sniffjoke
categories: ["defensive-tools"]
category_slugs: ["defensive-tools"]
homepage: https://github.com/vecna/sniffjoke
repository: 
version: 0.4.1-1kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-sniffing-spoofing"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sniffjoke\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.114754
---

# Tool: sniffjoke (sniffjoke)

## Categories
- [defensive-tools](../defensive-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/vecna/sniffjoke](https://github.com/vecna/sniffjoke) |
| Repository |  |
| Version | 0.4.1-1kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-sniffing-spoofing |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sniffjoke
- **PackagesInfo**: |
- ****Installed size**: ** `518 KB`
- ****How to install**: ** `sudo apt install sniffjoke`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sniffjokectl -h
- **usage**: /usr/bin/sniffjoke-autotest options
- **OPTIONS**: []
- **by hand this script should accept these argument**: []
- **(eg**: /tmp/home/, where sniffjoke-autotest is running)
- **Usage**: sniffjokectl [OPTIONS]... [COMMANDS]...
- **--location <name>	specify the network environment (suggested) [default**: generic]
- **--dir <name>		specify the base directory where the location reside [default**: /usr/local/var/sniffjoke/]
- **--user <username>	downgrade priviledge to the specified user [default**: nobody]
- **--group <groupname>	downgrade priviledge to the specified group [default**: nogroup]
- **--no-tcp		disable tcp mangling [default**: tcp mangled]
- **--no-udp		disable udp mangling [default**: udp mangled]
- **--start		if present, evasion i'ts activated immediatly [default**: not present]
- **--chain		enable chained hacking, powerful and entropic effects [default**: disabled]
- **--debug <level 0-5>	set verbosity level [default**: 2]
- **0**: suppress log, 1: common, 2: verbose, 3: debug, 4: session 5: packets
- **--foreground		running in foreground [default**: background]
- **--admin <ip>[**: port]	specify administration IP address [default: 127.0.0.1:8844]
- **--gw-mac-addr		specify default gateway mac address [default**: is autodetected]
- **http**: //www.delirandom.net/sniffjoke
- **technical details will be found in**: []
- **-g      specify the group to privilege downgrade            (default**: nogroup)
- **-u      specify the user to privilege downgrade             (default**: nobody)
- **--address <ip>[**: port]	specify administration IP address [default: 127.0.0.1:8844]
- **--timeout		set milliseconds timeout when contacting SniffJoke service [default**: 500]
- **when sniffjoke is running, you should send commands with a command line argument**: []
- **set start**: end value	set the injection's strogness over selected port [not supported!]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sniffjoke\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.114754
