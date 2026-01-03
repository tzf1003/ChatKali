---
tool_id: nikto
title: nikto
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
homepage: https://github.com/sullo/nikto
repository: 
version: 1:2.5.0+git20230114.90ff645-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/nikto-logo.svg
source_path: kali-tools\nikto\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.016601
---

# Tool: nikto (nikto)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sullo/nikto](https://github.com/sullo/nikto) |
| Repository |  |
| Version | 1:2.5.0+git20230114.90ff645-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/nikto-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/nikto
- **PackagesInfo**: |
- **Features**: ['Easily updatable CSV-format checks database', 'Output reports in plain text or HTML', 'Available HTTP versions automatic switching', 'Generic as well as specific server software checks', 'SSL support (through libnet-ssleay-perl)', 'Proxy support (with authentication)', 'Cookies support']
- ****Installed size**: ** `2.22 MB`
- ****How to install**: ** `sudo apt install nikto`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# replay -h
- **Options**: []
- **-Cgidirs+           Scan these CGI dirs**: none", "all", or values like "/cgi/ /cgi-a/
- **-Display+           Turn on/off display outputs**: []
- **-evasion+          Encoding technique**: []
- **-Format+           Save file (-o) format**: []
- **-id+               Host authentication to use, format is id**: pass or id:pass:realm
- **-mutate+           Guess additional file names**: []
- **-Plugins+          List of plugins to run (default**: ALL)
- **-Tuning+           Scan tuning**: []
- **-useproxy          Use the proxy defined in nikto.conf, or argument http**: //server:port
- **-proxy		Send request through this proxy (format**: host:port)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Nikto Usage Example

```console
root@kali:~# nikto -Display 1234EP -o report.html -Format htm -Tuning 123bde -host 192.168.0.102
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.0.102
+ Target Hostname:    192.168.0.102
+ Target Port:        80
+ Start Time:         2018-03-23 10:49:04 (GMT0)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ Server leaks inodes via ETags, header found with file /, inode: 287, size: 11832, mtime: Fri Feb  2 15:27:56 2018
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.12). Apache 2.0.65 (final release) and 2.2.29 are also current.
+ Allowed HTTP Methods: GET, HEAD, POST, OPTIONS
+ 371 requests: 0 error(s) and 9 item(s) reported on remote host
+ End Time:           2018-03-23 10:50:44 (GMT0) (100 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
root@kali:~#
root@kali:~# firefox report.html
```


## Source
- Path: kali-tools\nikto\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.016601
