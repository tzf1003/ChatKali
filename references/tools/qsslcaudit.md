---
tool_id: qsslcaudit
title: qsslcaudit
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://github.com/gremwell/qsslcaudit
repository: 
version: 0.8.3-0kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\qsslcaudit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.069182
---

# Tool: qsslcaudit (qsslcaudit)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/gremwell/qsslcaudit](https://github.com/gremwell/qsslcaudit) |
| Repository |  |
| Version | 0.8.3-0kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/qsslcaudit
- **PackagesInfo**: |
- ****Installed size**: ** `1.11 MB`
- ****How to install**: ** `sudo apt install qsslcaudit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# qsslcaudit -h
- **Usage**: qsslcaudit [options]
- **SSL client tests**: []
- **1**: (certs) custom certificate trust
- **2**: (certs) self-signed certificate for target domain trust
- **3**: (certs) self-signed certificate for invalid domain trust
- **4**: (certs) custom certificate for target domain trust
- **5**: (certs) custom certificate for invalid domain trust
- **6**: (certs) certificate for target domain signed by custom CA trust
- **7**: (certs) certificate for invalid domain signed by custom CA trust
- **8**: (protos) SSLv2 protocol support
- **9**: (protos) SSLv3 protocol support
- **10**: (ciphers) SSLv3 protocol and EXPORT grade ciphers support
- **11**: (ciphers) SSLv3 protocol and LOW grade ciphers support
- **12**: (ciphers) SSLv3 protocol and MEDIUM grade ciphers support
- **13**: (protos) TLS 1.0 protocol support
- **14**: (ciphers) TLS 1.0 protocol and EXPORT grade ciphers support
- **15**: (ciphers) TLS 1.0 protocol and LOW grade ciphers support
- **16**: (ciphers) TLS 1.0 protocol and MEDIUM grade ciphers support
- **17**: (ciphers) TLS 1.1 protocol and EXPORT grade ciphers support
- **18**: (ciphers) TLS 1.1 protocol and LOW grade ciphers support
- **19**: (ciphers) TLS 1.1 protocol and MEDIUM grade ciphers support
- **20**: (ciphers) TLS 1.2 protocol and EXPORT grade ciphers support
- **21**: (ciphers) TLS 1.2 protocol and LOW grade ciphers support
- **22**: (ciphers) TLS 1.2 protocol and MEDIUM grade ciphers support
- **23**: (ciphers) DTLS 1.0 protocol and EXPORT grade ciphers support
- **24**: (ciphers) DTLS 1.0 protocol and LOW grade ciphers support
- **25**: (ciphers) DTLS 1.0 protocol and MEDIUM grade ciphers support
- **26**: (ciphers) DTLS 1.2 protocol and EXPORT grade ciphers support
- **27**: (ciphers) DTLS 1.2 protocol and LOW grade ciphers support
- **28**: (ciphers) DTLS 1.2 protocol and MEDIUM grade ciphers support
- **29**: (certs) CVE-2020-0601 ECC cert trust
- **Options**: []
- **--server <https**: //example.com>  grab certificate information from <server>
- **--forward <127.0.0.1**: 6666>      forward connection to upstream proxy


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\qsslcaudit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.069182
