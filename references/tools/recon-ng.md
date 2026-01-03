---
tool_id: recon-ng
title: recon-ng
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://github.com/lanmaster53/recon-ng
repository: 
version: 5.1.2-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-information-gathering"]
icon: images/recon-ng-logo.svg
source_path: kali-tools\recon-ng\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.074817
---

# Tool: recon-ng (recon-ng)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/lanmaster53/recon-ng](https://github.com/lanmaster53/recon-ng) |
| Repository |  |
| Version | 5.1.2-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-information-gathering |
| Icon | images/recon-ng-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/recon-ng
- **PackagesInfo**: |
- ****Installed size**: ** `271 KB`
- ****How to install**: ** `sudo apt install recon-ng`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# recon-web -h
- **usage**: recon-web [-h] [--host HOST] [--port PORT]
- **options**: []
- *** Workspace initialized**: default


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## recon-ng Usage Example

Search for results on xssed.com (`use recon/domains-vulnerabilities/xssed`) for the target domain (`set SOURCE cisco.com`):

```console
root@kali:~# recon-ng

    _/_/_/    _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/
   _/    _/  _/        _/        _/      _/  _/_/    _/            _/_/    _/  _/
  _/_/_/    _/_/_/    _/        _/      _/  _/  _/  _/  _/_/_/_/  _/  _/  _/  _/  _/_/_/
 _/    _/  _/        _/        _/      _/  _/    _/_/            _/    _/_/  _/      _/
_/    _/  _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/


                                          /\
                                         / \\ /\
        Sponsored by...           /\  /\/  \\V  \/\
                                 / \\/ // \\\\\ \\ \/\
                                // // BLACK HILLS \/ \\
                               www.blackhillsinfosec.com

                      [recon-ng v4.9.4, Tim Tomes (@LaNMaSteR53)]

[76] Recon modules
[8]  Reporting modules
[2]  Import modules
[2]  Exploitation modules
[2]  Discovery modules

[recon-ng][default] > use recon/domains-vulnerabilities/xssed
[recon-ng][default][xssed] > set SOURCE cisco.com
SOURCE => cisco.com
[recon-ng][default][xssed] > run

---------
CISCO.COM
---------
[*] Category: Redirect
[*] Example: http://www.cisco.com/survey/exit.html?http://xssed.com/
[*] Host: www.cisco.com
[*] Publish_Date: 2012-02-16 00:00:00
[*] Reference: http://xssed.com/mirror/76478/
[*] Status: unfixed
[*] --------------------------------------------------
[*] Category: XSS
[*] Example: http://developer.cisco.com/web/webdialer/wikidocs?p_p_id=1_WAR_wikinavigationportlet_INSTANCE_veD7&p<br>_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&p_r_p_185834411_no<br>deId=803209&p_r_p_185834411_title=%22%3E%3Ch1%3ECross-Site%20Scripting%20@matiaslonigro%3C/h1%3E%3Cs<br>cript%3Ealert%28/xss/%29%3C/script%3E
[*] Host: developer.cisco.com
[*] Publish_Date: 2012-02-13 00:00:00
[*] Reference: http://xssed.com/mirror/76294/
[*] Status: unfixed
[...]
```


## Source
- Path: kali-tools\recon-ng\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.074817
