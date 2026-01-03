---
tool_id: joomscan
title: joomscan
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
homepage: https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project
repository: 
version: 0.0.7-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\joomscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.954940
---

# Tool: joomscan (joomscan)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project](https://www.owasp.org/index.php/Category:OWASP_Joomla_Vulnerability_Scanner_Project) |
| Repository |  |
| Version | 0.0.7-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/joomscan
- **PackagesInfo**: |
- ****Installed size**: ** `274 KB`
- ****How to install**: ** `sudo apt install joomscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# joomscan -h


## Documentation (Upstream)
++---==[Version : 0.0.7
     +---++---==[Update Date : [2018/09/23]
     +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
     --=[Code name : Self Challenge
     @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP
 
    
 
 Help :
 
 Usage:	joomscan [options]
 
 --url | -u <URL>                |   The Joomla URL/domain to scan.
 --enumerate-components | -ec    |   Try to enumerate components.
 
 --cookie <String>               |   Set cookie.
 --user-agent | -a <User-Agent>  |   Use the specified User-Agent.
 --random-agent | -r             |   Use a random User-Agent.
 --timeout <Time-Out>            |   Set timeout.
 --proxy=PROXY                   |   Use a proxy to connect to the target URL
            Proxy example: --proxy http://127.0.0.1:8080
                                   https://127.0.0.1:443
                                   socks://127.0.0.1:414
                                   
 --about                         |   About Author
 --help | -h                     |   This help screen.
 --version                       |   Output the current version and exit.
 
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## joomscan Usage Example

Scan the Joomla installation at the given URL (`-u http://192.168.1.202/joomla`) for vulnerabilities:

```console
root@kali:~# joomscan -u http://localhost/
    ____  _____  _____  __  __  ___   ___    __    _  _
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  (
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
      (1337.today)

    --=[OWASP JoomScan
    +---++---==[Version : 0.0.5
    +---++---==[Update Date : [2018/03/13]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : KLOT
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://localhost/ ...



[+] Detecting Joomla Version
[++] Joomla 3.8.6

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking Directory Listing
[++] directory has directory listing :
http://localhost/administrator/components
http://localhost/administrator/modules
http://localhost/administrator/templates
http://localhost/images/banners


[+] Checking apache info/status files
[++] Interesting file is found
http://localhost/server-status

[+] admin finder
[++] Admin page : http://localhost/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://localhost/robots.txt

Interesting path found from robots.txt
http://localhost/joomla/administrator/
http://localhost/administrator/
http://localhost/bin/
http://localhost/cache/
http://localhost/cli/
http://localhost/components/
http://localhost/includes/
http://localhost/installation/
http://localhost/language/
http://localhost/layouts/
http://localhost/libraries/
http://localhost/logs/
http://localhost/modules/
http://localhost/plugins/
http://localhost/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found


Your Report : reports/localhost/
root@kali:~#
root@kali:~# ls /usr/share/joomscan/reports/localhost/
localhost_report_2018-3-19_at_8.37.58.html  localhost_report_2018-3-19_at_8.37.58.txt
root@kali:~#
```


## Source
- Path: kali-tools\joomscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.954940
