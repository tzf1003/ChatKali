---
tool_id: hoaxshell
title: hoaxshell
categories: ["post-exploitation", "web-application-analysis"]
category_slugs: ["post-exploitation", "web-application-analysis"]
homepage: https://github.com/t3l3machus/hoaxshell/
repository: 
version: 0.0~git20250119.e1bba89-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/hoaxshell-logo.svg
source_path: kali-tools\hoaxshell\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.934058
---

# Tool: hoaxshell (hoaxshell)

## Categories
- [post-exploitation](../post-exploitation.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/t3l3machus/hoaxshell/](https://github.com/t3l3machus/hoaxshell/) |
| Repository |  |
| Version | 0.0~git20250119.e1bba89-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/hoaxshell-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages//hoaxshell
- **PackagesInfo**: |
- ****Installed size**: ** `84 KB`
- ****How to install**: ** `sudo apt install hoaxshell`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hoaxshell -h
- **usage**: hoaxshell.py [-h] [-s SERVER_IP] [-c CERTFILE] [-k KEYFILE] [-p PORT]
- **options**: []
- **-p, --port PORT       Your hoaxshell server port (default**: 8080 over http, 443 over https).
- **Frequency of cmd execution queue cycle (A low value creates a faster shell but produces more http traffic. *Less than 0.8 will cause trouble. default**: 0.8s).
- **Provide a filename (absolute path) on the victim machine to write and execute commands from instead of using "Invoke-Expression". The path better be quoted. Be careful when using special chars in the path (e.g. $env**: USERNAME) as they must be properly escaped. See usage examples for details. CAUTION: you won't be able to change directory with this method. Your commands must include ablsolute paths to files etc.
- **Provide a value for the "Server" response header (default**: Microsoft-IIS/10)
- **-g, --grab            Attempts to restore a live session (default**: false).
- **Usage examples**: ['Basic shell session over http:']
- **hoaxshell -s <your_ip> -i -H "Authorization" -x "C**: \Users\\\$env:USERNAME\.local\hack.ps1"
- **openssl req -x509 -newkey rsa**: 2048 -keyout key.pem -out cert.pem -days 365


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\hoaxshell\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.934058
