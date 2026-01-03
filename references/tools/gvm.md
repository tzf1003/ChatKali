---
tool_id: gvm
title: gvm
categories: ["vulnerability-analysis"]
category_slugs: ["vulnerability-analysis"]
homepage: https://www.greenbone.net/
repository: 
version: 25.04.1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-vulnerability"]
icon: images/gvm-logo.svg
source_path: kali-tools\gvm\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.924302
---

# Tool: gvm (gvm)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.greenbone.net/](https://www.greenbone.net/) |
| Repository |  |
| Version | 25.04.1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-vulnerability |
| Icon | images/gvm-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/gvm
- **PackagesInfo**: |
- ****Installed size**: ** `47 KB`
- ****How to install**: ** `sudo apt install gvm`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# gvm-stop -h
- **Step 1**: Checking OpenVAS (Scanner)...
- **OK**: the mqtt_server_uri is defined in /etc/openvas/openvas.conf
- **ERROR**: Your GVM-25.04.0 installation is not yet complete!
- **FIX**: Run the NVT synchronization script greenbone-feed-sync.
- **IMPORTANT NOTE**: this script is provided and maintained by Debian and Kali.
- **[>]  Web UI (Greenbone Security Assistant)**: https://127.0.0.1:9392
- **Loaded**: loaded (/usr/lib/systemd/system/notus-scanner.service; disabled; preset: disabled)
- **Active**: inactive (dead)
- **Docs**: https://github.com/greenbone/notus-scanner
- **https**: //www.greenbone.net
- **Nov 27 09**: 51:54 kali systemd[1]: Stopped notus-scanner.service - Notus Scanner.
- **man**: openvas(8)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![gvm](images/openvas.png)


## Source
- Path: kali-tools\gvm\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.924302
