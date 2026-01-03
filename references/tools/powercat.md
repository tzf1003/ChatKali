---
tool_id: powercat
title: powercat
categories: ["post-exploitation", "exploitation-tools"]
category_slugs: ["post-exploitation", "exploitation-tools"]
homepage: https://github.com/besimorhino/powercat
repository: 
version: 0.0~git20240305.4e33fdf-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-windows-resources"]
icon: images/powercat-logo.svg
source_path: kali-tools\powercat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.054874
---

# Tool: powercat (powercat)

## Categories
- [post-exploitation](../post-exploitation.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/besimorhino/powercat](https://github.com/besimorhino/powercat) |
| Repository |  |
| Version | 0.0~git20240305.4e33fdf-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-windows-resources |
| Icon | images/powercat-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/powercat
- **PackagesInfo**: |
- ****Installed size**: ** `55 KB`
- ****How to install**: ** `sudo apt install powercat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# powercat -h
- **Github Repository**: https://github.com/besimorhino/powercat
- **Usage**: powercat [-c or -l] [-p port] [options]
- **Client Relay Format**: -r <protocol>:<ip addr>:<port>
- **Listener Relay Format**: -r <protocol>:<port>
- **DNSCat2 Relay Format**: -r dns:<dns server>:<dns port>:<domain>
- **Get the server here**: https://github.com/iagox86/dnscat2
- **connecting. Default**: 60
- **can be executed in this way**: powershell -E <encoded string>
- **Examples**: []
- **powercat -c 10.1.1.15 -p 8000 -i C**: \inputfile
- **Write the data sent to the local listener on port 4444 to C**: \outfile
- **powercat -l -p 4444 -of C**: \outfile
- **powercat -l -p 8000 -r tcp**: 10.1.1.1:9000
- **powercat -l -p 8000 -r dns**: 10.1.1.1:53:c2.example.com


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\powercat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.054874
