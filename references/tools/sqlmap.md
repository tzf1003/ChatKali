---
tool_id: sqlmap
title: sqlmap
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis", "database-assessment", "exploitation-tools"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis", "database-assessment", "exploitation-tools"]
homepage: https://sqlmap.org/
repository: 
version: 1.9.11-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-database kali-tools-exploitation kali-tools-information-gathering kali-tools-top10 kali-tools-vulnerability kali-tools-web"]
icon: images/sqlmap-logo.svg
source_path: kali-tools\sqlmap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.122638
---

# Tool: sqlmap (sqlmap)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)
- [database-assessment](../database-assessment.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sqlmap.org/](https://sqlmap.org/) |
| Repository |  |
| Version | 1.9.11-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-database kali-tools-exploitation kali-tools-information-gathering kali-tools-top10 kali-tools-vulnerability kali-tools-web |
| Icon | images/sqlmap-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/sqlmap
- **PackagesInfo**: |
- ****Installed size**: ** `10.29 MB`
- ****How to install**: ** `sudo apt install sqlmap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sqlmapapi -h
- **|_|V...       |_|   https**: //sqlmap.org
- **Usage**: sqlmapapi [options]
- **Options**: []
- **-v VERBOSE            Verbosity level**: 0-6 (default 1)
- **Target**: []
- **-u URL, --url=URL   Target URL (e.g. "http**: //www.site.com/vuln.php?id=1")
- **Request**: []
- **Injection**: []
- **Detection**: []
- **Techniques**: []
- **Enumeration**: []
- **Operating system access**: []
- **General**: []
- **Miscellaneous**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sqlmap Usage Example

Attack the given URL (`-u “http://192.168.1.250/?p=1&forumaction=search”`) and extract the database names (`–dbs`):

```console
root@kali:~# sqlmap -u "http://192.168.1.250/?p=1&forumaction=search" --dbs
        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.2.11#stable}
|_ -| . ["]     | .'| . |
|___|_  ["]_|_|_|__,|  _|
      |_|V          |_|   http://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting at 13:37:00

[13:37:00] [INFO] testing connection to the target URL
```


## Source
- Path: kali-tools\sqlmap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.122638
