---
tool_id: udptunnel
title: udptunnel
categories: ["tunneling-exfiltration", "utilities"]
category_slugs: ["tunneling-exfiltration", "utilities"]
homepage: http://www1.cs.columbia.edu/~lennox/udptunnel/
repository: 
version: 1.1-12
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation"]
icon: images/udptunnel-logo.svg
source_path: kali-tools\udptunnel\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.149901
---

# Tool: udptunnel (udptunnel)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www1.cs.columbia.edu/~lennox/udptunnel/](http://www1.cs.columbia.edu/~lennox/udptunnel/) |
| Repository |  |
| Version | 1.1-12 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation |
| Icon | images/udptunnel-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/udptunnel
- **PackagesInfo**: |
- ****Installed size**: ** `37 KB`
- ****How to install**: ** `sudo apt install udptunnel`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# udptunnel --help
- **udptunnel**: invalid option -- '-'
- **Usage**: udptunnel -s TCP-port [-r] [-v] UDP-addr/UDP-port[/ttl]
- **-s**: Server mode.  Wait for TCP connections on the port.
- **-c**: Client mode.  Connect to the given address.
- **-r**: RTP mode.  Connect/listen on ports N and N+1 for both UDP and TCP.
- **-v**: Verbose mode.  Specify -v multiple times for increased verbosity.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\udptunnel\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.149901
