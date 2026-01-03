---
tool_id: wapiti
title: wapiti
categories: ["web-application-analysis", "vulnerability-analysis", "information-gathering"]
category_slugs: ["web-application-analysis", "vulnerability-analysis", "information-gathering"]
homepage: https://wapiti.sourceforge.net/
repository: 
version: 3.2.8+dfsg-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-identify kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/wapiti-logo.svg
source_path: kali-tools\wapiti\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.163661
---

# Tool: wapiti (wapiti)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://wapiti.sourceforge.net/](https://wapiti.sourceforge.net/) |
| Repository |  |
| Version | 3.2.8+dfsg-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-identify kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/wapiti-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/wapiti
- **PackagesInfo**: |
- **Wapiti can detect the following vulnerabilities**: ['Database Injection (PHP/ASP/JSP SQL Injections and XPath Injections)', 'Cross Site Scripting (XSS) reflected and permanent', 'File disclosure detection (local and remote include, require, fopen,']
- ****Installed size**: ** `3.33 MB`
- ****How to install**: ** `sudo apt install wapiti`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wapiti-getcookie -h
- **usage**: wapiti-getcookie [-h] -u URL -c COOKIE [-p PROXY] [--tor]
- **Wapiti 3.2.8**: Web application vulnerability scanner
- **options**: []
- **Set the HTTP(S) proxy to use. Supported**: http(s) and
- **--tor                 Use Tor listener (127.0.0.1**: 9050)
- **URLs. Possible values**: paranoid, sneaky, polite,
- **-v, --verbose LEVEL   Set verbosity level (0**: quiet, 1: normal, 2: verbose)
- **-f, --format FORMAT   Set output format. Supported**: csv, html, json, txt,
- **level 1**: include only the HTTP requests, level 2 :
- **--cms CMS_LIST        Choose the CMS to scan. Possible choices**: drupal,
- **Wapiti-getcookie**: An utility to grab cookies from a webpage


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\wapiti\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.163661
