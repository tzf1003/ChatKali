---
tool_id: goshs
title: goshs
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/patrickhener/goshs
repository: 
version: 1.1.2-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/goshs-logo.svg
source_path: kali-tools\goshs\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.916846
---

# Tool: goshs (goshs)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/patrickhener/goshs](https://github.com/patrickhener/goshs) |
| Repository |  |
| Version | 1.1.2-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/goshs-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/goshs
- **PackagesInfo**: |
- ****Installed size**: ** `14.63 MB`
- ****How to install**: ** `sudo apt install goshs`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# goshs -h
- **Usage**: goshs [options]
- **Web server options**: []
- **-i,  --ip             IP or Interface to listen on            (default**: 0.0.0.0)
- **-p,  --port           The port to listen on                   (default**: 8000)
- **-d,  --dir            The web root directory                  (default**: current working path)
- **-w,  --webdav         Also serve using webdav protocol        (default**: false)
- **-wp, --webdav-port    The port to listen on for webdav        (default**: 8001)
- **-ro, --read-only      Read only mode, no upload possible      (default**: false)
- **-uo, --upload-only    Upload only mode, no download possible  (default**: false)
- **-uf, --upload-folder  Specify a different upload folder       (default**: current working path)
- **-nc, --no-clipboard   Disable the clipboard sharing           (default**: false)
- **-nd, --no-delete      Disable the delete option               (default**: false)
- **-si, --silent         Running without dir listing             (default**: false)
- **-c,  --cli            Enable cli (only with auth and tls)     (default**: false)
- **-e,  --embedded       Show embedded files in UI               (default**: false)
- **-o,  --output         Write output to logfile                 (default**: false)
- **TLS options**: []
- **-slh,   --le-http       Port to use for Let's Encrypt HTTP Challenge	(default**: 80)
- **-slt,   --le-tls        Port to use for Let's Encrypt TLS ALPN Challenge (default**: 443)
- **SFTP server options**: []
- **-sftp                        Activate SFTP server capabilities (default**: false)
- **-sp,    --sftp-port          The port SFTP listens on          (default**: 2022)
- **Authentication options**: []
- **-b,  --basic-auth     Use basic authentication (user**: pass - user can be empty)
- **Connection restriction**: []
- **Webhook options**: []
- **-W,  --webhook            Enable webhook support                                       (default**: false)
- **[all, upload, delete, download, view, webdav, sftp, verbose] (default**: all)
- **[Discord, Mattermost, Slack]                                 (default**: Discord)
- **Misc options**: []
- **-C  --config        Provide config file path                (default**: false)
- **-P  --print-config  Print sample config to STDOUT           (default**: false)
- **-u  --user          Drop privs to user (unix only)          (default**: current user)
- **-nm --no-mdns       Disable zeroconf mDNS registration      (default**: false)
- **-V  --verbose       Activate verbose log output             (default**: false)
- **Usage examples**: []
- **Start with default values**: ./goshs
- **Start with config file**: ./goshs -C /path/to/config.yaml
- **Start with wevdav support**: ./goshs -w
- **Start with different port**: ./goshs -p 8080
- **Start with self-signed cert**: ./goshs -s -ss
- **Start with let's encrypt**: ./goshs -s -sl -sle your@mail.com -sld your.domain.com,your.seconddomain.com
- **Start with custom cert**: ./goshs -s -sk <path to key> -sc <path to cert>
- **Start with basic auth**: ./goshs -b 'secret-user:$up3r$3cur3'
- **Start with basic auth bcrypt hash**: ./goshs -b 'secret-user:$2a$14$ydRJ//Ob4SctB/D7o.rvU.LmPs/vwXkeXCbtpCqzgOJDSShLgiY52'
- **Start with basic auth empty user**: ./goshs -b ':$up3r$3cur3'
- **Start with cli enabled**: ./goshs -b 'secret-user:$up3r$3cur3' -s -ss -c


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\goshs\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.916846
