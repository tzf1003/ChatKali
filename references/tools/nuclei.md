---
tool_id: nuclei
title: nuclei
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
homepage: https://github.com/projectdiscovery/nuclei
repository: 
version: 3.4.10-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/nuclei-logo.svg
source_path: kali-tools\nuclei\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.020738
---

# Tool: nuclei (nuclei)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) |
| Repository |  |
| Version | 3.4.10-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/nuclei-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/nuclei
- **PackagesInfo**: |
- ****Installed size**: ** `94.09 MB`
- ****How to install**: ** `sudo apt install nuclei`
- **root@kali**: ~# nuclei -h
- **Usage**: []
- **Flags**: []
- **TARGET**: []
- **TARGET-FORMAT**: []
- **TEMPLATES**: []
- **FILTERING**: []
- **-s, -severity value[]              templates to run based on severity. Possible values**: info, low, medium, high, critical, unknown
- **-es, -exclude-severity value[]     templates to exclude based on severity. Possible values**: info, low, medium, high, critical, unknown
- **-pt, -type value[]                 templates to run based on protocol type. Possible values**: dns, file, http, headless, tcp, workflow, ssl, websocket, whois, code, javascript
- **-ept, -exclude-type value[]        templates to exclude based on protocol type. Possible values**: dns, file, http, headless, tcp, workflow, ssl, websocket, whois, code, javascript
- **OUTPUT**: []
- **CONFIGURATIONS**: []
- **-H, -header string[]                  custom header/cookie to include in all http request in header**: value format (cli, file)
- **-sni string                           tls sni hostname to use (default**: input domain name)
- **INTERACTSH**: []
- **-iserver, -interactsh-server string  interactsh server url for self-hosted instance (default**: oast.pro,oast.live,oast.site,oast.online,oast.fun,oast.me)
- **FUZZING**: []
- **-fuzz                               enable loading fuzzing templates (Deprecated**: use -dast instead)
- **-dtsa, -dast-server-address string  dast server address (default "localhost**: 9055")
- **UNCOVER**: []
- **-uf, -uncover-field string     uncover fields to return (ip,port,host) (default "ip**: port")
- **RATE-LIMIT**: []
- **OPTIMIZATIONS**: []
- **-ldp, -leave-default-ports       leave default HTTP/HTTPS ports (eg. host**: 80,host:443)
- **HEADLESS**: []
- **DEBUG**: []
- **UPDATE**: []
- **STATISTICS**: []
- **CLOUD**: []
- **AUTHENTICATION**: []
- **EXAMPLES**: []
- **Run nuclei on single host**: []
- **Run nuclei with specific template directories**: []
- **Run nuclei against a list of hosts**: []
- **Run nuclei with a JSON output**: []
- **Run nuclei with sorted Markdown outputs (with environment variables)**: []
- **Additional documentation is available at**: https://docs.nuclei.sh/getting-started/running


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\nuclei\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.020738
