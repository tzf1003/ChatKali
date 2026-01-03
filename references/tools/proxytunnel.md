---
tool_id: proxytunnel
title: proxytunnel
categories: ["tunneling-exfiltration", "utilities"]
category_slugs: ["tunneling-exfiltration", "utilities"]
homepage: https://proxytunnel.sourceforge.io/
repository: 
version: 1.12.3-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web"]
icon: images/proxytunnel-logo.svg
source_path: kali-tools\proxytunnel\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.059106
---

# Tool: proxytunnel (proxytunnel)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://proxytunnel.sourceforge.io/](https://proxytunnel.sourceforge.io/) |
| Repository |  |
| Version | 1.12.3-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web |
| Icon | images/proxytunnel-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/proxytunnel
- **PackagesInfo**: |
- ****Installed size**: ** `102 KB`
- ****How to install**: ** `sudo apt install proxytunnel`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# proxytunnel -h
- **Usage**: proxytunnel [OPTIONS]...
- **Standard options**: []
- **-i, --inetd                Run from inetd (default**: off)
- **address**: port combination
- **-p, --proxy=STRING         Local proxy host**: port combination
- **-r, --remproxy=STRING      Remote proxy host**: port combination (using 2 proxies)
- **-d, --dest=STRING          Destination host**: port combination
- **Additional options for specific features**: []
- **-W, --wa-bug-29744         Workaround ASF Bugzilla 29744**: if SSL is active
- **-P, --proxyauth=STRING     Proxy auth credentials user**: pass combination
- **-R, --remproxyauth=STRING  Remote proxy auth credentials user**: pass combination
- **-t, --domain=STRING        NTLM domain (default**: autodetect)
- **Miscellaneous options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\proxytunnel\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.059106
