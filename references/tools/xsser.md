---
tool_id: xsser
title: xsser
categories: ["vulnerability-analysis", "web-application-analysis", "exploitation-tools"]
category_slugs: ["vulnerability-analysis", "web-application-analysis", "exploitation-tools"]
homepage: https://xsser.03c8.net/
repository: 
version: 1.8.4-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\xsser\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.183039
---

# Tool: xsser (xsser)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://xsser.03c8.net/](https://xsser.03c8.net/) |
| Repository |  |
| Version | 1.8.4-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/xsser
- **PackagesInfo**: |
- ****Installed size**: ** `23.98 MB`
- ****How to install**: ** `sudo apt install xsser`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# xsser -h
- **Usage**: []
- **Options**: []
- ***Special Features***: []
- **'Cross Site Tracing' [CAPEC-107]**: []
- **--xst=XST           XST - Cross Site Tracing (--xst http(s)**: //host.com)
- ***Select Target(s)***: []
- **to get target(s) urls from**: []
- **-d DORK             Search target(s) using a query (ex**: 'news.php?id=')
- **--De=DORK_ENGINE    Use this search engine (default**: DuckDuckGo)
- ***Select type of HTTP/HTTPS Connection(s)***: []
- **inject**: []
- **-g GETDATA          Send payload using GET (ex**: '/menu.php?id=XSS')
- **-p POSTDATA         Send payload using POST (ex**: 'foo=1&bar=XSS')
- **-c CRAWLING         Number of urls to crawl on target(s)**: 1-99999
- **--Cw=CRAWLER_WIDTH  Deeping level of crawler**: 1-5 (default: 2)
- **--Cl                Crawl only local target(s) urls (default**: FALSE)
- ***Configure Request(s)***: []
- **payload(s). You can choose multiple**: []
- **--user-agent=AGENT  Change your HTTP User-Agent header (default**: SPOOFED)
- **--referer=REFERER   Use another HTTP Referer header (default**: NONE)
- **--auth-cred=ACRED   HTTP Authentication credentials (name**: password)
- **--proxy=PROXY       Use proxy server (tor**: http://localhost:8118)
- **--timeout=TIMEOUT   Select your timeout (default**: 30)
- **--retries=RETRIES   Retries when connection timeout (default**: 1)
- **--threads=THREADS   Maximum number of concurrent requests (default**: 5)
- **--delay=DELAY       Delay in seconds between each request (default**: 0)
- **--follow-redirects  Follow server redirections (default**: FALSE)
- **--follow-limit=FLI  Set limit for redirection requests (default**: 50)
- ***Checker Systems***: []
- **against XSS attacks**: []
- **--checkaturl=ALT    Check reply using**: <alternative url> [aka BLIND-XSS]
- **--checkmethod=ALTM  Check reply using**: GET or POST (default: GET)
- **--checkatdata=ALD   Check reply using**: <alternative payload>
- ***Select Vector(s)***: []
- **only one option**: []
- ***Select Payload(s)***: []
- **XSSer. Choose only if required**: []
- **--auto-set=FZZ_NUM  ASET  - Limit of vectors to inject (default**: 1293)
- **--auto-info         AINFO - Select ONLY vectors with INFO (default**: FALSE)
- **--auto-random       ARAND - Set random to order (default**: FALSE)
- ***Anti-antiXSS Firewall rules***: []
- **and some anti-XSS browser filters. Choose only if required**: []
- ***Select Bypasser(s)***: []
- **possible anti-XSS filters. They can be combined with other techniques**: []
- **(reversing obfuscators) (ex**: 'Mix,Une,Str,Hex')
- ***Special Technique(s)***: []
- **techniques and fuzzing vectors. You can choose multiple**: []
- ***Select Final injection(s)***: []
- **the vulnerabilities found. Choose only one option**: []
- ***Special Final injection(s)***: []
- **your final code (except with DCP exploits)**: []
- ***Reporting***: []
- ***Miscellaneous***: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

```console
xsser --gtk
```

![xsser](images/xsser.png)


## Source
- Path: kali-tools\xsser\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.183039
