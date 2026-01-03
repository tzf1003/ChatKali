---
tool_id: dnscat2
title: dnscat2
categories: ["tunneling-exfiltration", "post-exploitation"]
category_slugs: ["tunneling-exfiltration", "post-exploitation"]
homepage: https://github.com/iagox86/dnscat2
repository: 
version: 0.07-0kali2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dnscat2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.870261
---

# Tool: dnscat2 (dnscat2)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/iagox86/dnscat2](https://github.com/iagox86/dnscat2) |
| Repository |  |
| Version | 0.07-0kali2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dnscat2
- **PackagesInfo**: |
- ****Installed size**: ** `268 KB`
- ****How to install**: ** `sudo apt install dnscat2-server`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnscat2-server --help
- **Usage**: dnscat [args] [domain]
- **General options**: []
- **--delay <ms>            Set the maximum delay between packets (default**: 1000).
- **and assuming the server is dead (default**: 20).
- **Input options**: []
- **Debug options**: []
- **Driver options**: []
- **host=<hostname>       The host to listen on (default**: 0.0.0.0).
- **port=<port>           The port to listen on (default**: 53).
- **multiple comma-separated (options**: TXT, MX,
- **CNAME, A, AAAA) (default**: TXT,CNAME,MX).
- **(default**: 0.0.0.0)
- **Examples**: []
- **passed on the commandline**: []
- **ERROR**: --help requested
- **New window created**: crypto-debug
- **Default host (0.0.0.0) and port (53), with no specific domain**: []
- **Default host/port, with a particular domain to listen on**: []
- **Or multiple domains**: []
- **can be done by passing the --dns argument**: []
- **-s, --dnsport=<i>         The DNS port to listen on [deprecated] (default**: []
- **host**: port (default: )
- **-a, --auto-command=<s>    Send this to each client that connects (default**: )
- **maintain (default**: 1000)
- **-l, --listener=<i>        DEBUG**: Start a listener driver on the given port


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\dnscat2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.870261
