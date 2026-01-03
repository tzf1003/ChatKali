---
tool_id: pwncat
title: pwncat
categories: ["post-exploitation", "exploitation-tools"]
category_slugs: ["post-exploitation", "exploitation-tools"]
homepage: https://github.com/cytopia/pwncat
repository: 
version: 0.1.2-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\pwncat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.061212
---

# Tool: pwncat (pwncat)

## Categories
- [post-exploitation](../post-exploitation.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/cytopia/pwncat](https://github.com/cytopia/pwncat) |
| Repository |  |
| Version | 0.1.2-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/pwncat
- **PackagesInfo**: |
- ****Installed size**: ** `5.63 MB`
- ****How to install**: ** `sudo apt install pwncat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pwncat -h
- **usage**: pwncat [options] hostname port
- **pwncat [options] -L [addr**: ]port hostname port
- **pwncat [options] -R addr**: port hostname port
- **positional arguments**: []
- **Specify multiple ports to scan**: []
- **Via list**: --self-inject /bin/sh:10.0.0.1:4444,4445,4446
- **Via range**: --self-inject /bin/sh:10.0.0.1:4444-4446
- **Via incr**: --self-inject /bin/sh:10.0.0.1:4444+2
- **mode arguments**: []
- **-l, --listen          [Listen mode]**: []
- **-z, --zero            [Zero-I/0 mode]**: []
- **-L, --local [addr**: ]port
- **[Local forward mode]**: []
- **addr/port (given by --local [addr**: ]port).
- **(I.e.**: proxies a remote service to a local address)
- **-R, --remote addr**: port
- **[Remote forward mode]**: []
- **-R/--remote addr**: port and the connection to the
- **optional arguments**: []
- **color on Windows by default. (default**: auto)
- **--safe-word str       All modes**: []
- **protocol arguments**: []
- **-4                    Only Use IPv4 (default**: IPv4 and IPv6 dualstack).
- **-6                    Only Use IPv6 (default**: IPv4 and IPv6 dualstack).
- **--http                Connect / Listen mode (TCP and UDP)**: []
- **--https               Connect / Listen mode (TCP and UDP)**: []
- **command & control arguments**: []
- **--self-inject cmd**: host:port[s]
- **Listen mode (TCP only)**: []
- **Example**: --self-inject /bin/bash:10.0.0.1:4444
- **Note**: this is currently an experimental feature and does
- **pwncat scripting engine**: []
- **--script-send file    All modes (TCP and UDP)**: []
- **contain the exact following function which will**: []
- **be applied as the transformer**: []
- **def transform(data, pse)**: []
- **--script-recv file    All modes (TCP and UDP)**: []
- **zero-i/o mode arguments**: []
- **--banner              Zero-I/O (TCP and UDP)**: []
- **listen mode arguments**: []
- **-k, --keep-open       Listen mode (TCP only)**: []
- **(default**: quit if the remote is not available or the
- **--rebind [x]          Listen mode (TCP and UDP)**: []
- **--rebind-wait s       Listen mode (TCP and UDP)**: []
- **Wait x seconds between re-initialization. (default**: 1)
- **--rebind-robin port   Listen mode (TCP and UDP)**: []
- **If the server is unable to initialize (e.g**: cannot bind
- **connect mode arguments**: []
- **--reconn [x]          Connect mode (TCP and UDP)**: []
- **Note on UDP**: []
- **--reconn-wait s       Connect mode (TCP and UDP)**: []
- **Wait x seconds between re-connects. (default**: 1)
- **--reconn-robin port   Connect mode (TCP and UDP)**: []
- **--ping-init           Connect mode (TCP and UDP)**: []
- **ping packet (default**: '\0')
- **--ping-intvl s        Connect mode (TCP and UDP)**: []
- **--ping-word str       Connect mode (TCP and UDP)**: []
- **--ping-robin port     Connect mode (TCP and UDP)**: []
- **--udp-sconnect        Connect mode (UDP only)**: []
- **Connect mode (UDP only)**: []
- **The default is to send a null byte sting**: '\0'.
- **misc arguments**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\pwncat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.061212
