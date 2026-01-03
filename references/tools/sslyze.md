---
tool_id: sslyze
title: sslyze
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://github.com/nabla-c0d3/sslyze
repository: 
version: 6.2.0-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/sslyze-logo.svg
source_path: kali-tools\sslyze\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.128283
---

# Tool: sslyze (sslyze)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/nabla-c0d3/sslyze](https://github.com/nabla-c0d3/sslyze) |
| Repository |  |
| Version | 6.2.0-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/sslyze-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sslyze
- **PackagesInfo**: |
- ****Installed size**: ** `2.20 MB`
- ****How to install**: ** `sudo apt install sslyze`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sslyze -h
- **usage**: sslyze [-h] [--update_trust_stores] [--cert CERTIFICATE_FILE]
- **positional arguments**: []
- **options**: []
- **Trust stores options**: []
- **latest stores will be downloaded from https**: //github.c
- **Client certificate options**: []
- **Input and output options**: []
- **described in SSLyze's Python API**: the nodes and
- **attributes will be the same. See https**: //nabla-
- **TARGET_FILE. It should contain one host**: port per line.
- **Connectivity options**: []
- **URL**: 'http://USER:PW@HOST:PORT/'. For proxies
- **target server(s). StartTLS should be one of**: auto,
- **Scan commands**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sslyze Usage Example

Launch a regular scan type (`–regular`) against the target host (`www.example.com`):

```console
root@kali:~# sslyze --regular www.example.com

 REGISTERING AVAILABLE PLUGINS
 -----------------------------

  PluginCompression
  PluginCertInfo
  PluginSessionResumption
  PluginSessionRenegotiation
  PluginOpenSSLCipherSuites



 CHECKING HOST(S) AVAILABILITY
 -----------------------------

   www.example.com:443                 => 93.184.216.119:443



 SCAN RESULTS FOR WWW.EXAMPLE.COM:443 - 93.184.216.119:443
 ---------------------------------------------------------

  * Compression :
        Compression Support:      Disabled

  * Certificate :
      Validation w/ Mozilla's CA Store:  Certificate is Trusted
```


## Source
- Path: kali-tools\sslyze\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.128283
