---
tool_id: dirb
title: dirb
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://dirb.sourceforge.net/
repository: 
version: 2.22+dfsg-7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web"]
icon: images/dirb-logo.svg
source_path: kali-tools\dirb\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.866936
---

# Tool: dirb (dirb)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://dirb.sourceforge.net/](https://dirb.sourceforge.net/) |
| Repository |  |
| Version | 2.22+dfsg-7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web |
| Icon | images/dirb-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/dirb
- **PackagesInfo**: |
- ****Installed size**: ** `1.44 MB`
- ****How to install**: ** `sudo apt install dirb`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man html2dic
- **Specify your custom USER_AGENT.  (Default is**: "Mozilla/4.0  (com-
- **-p <proxy[**: port]>
- **-P <proxy_username**: proxy_password>
- **-u <username**: password>
- **Usage**: dirb-gendict -type pattern
- **type**: -n numeric [0-9]
- **pattern**: Must be an ascii string in which every 'X' character wildcard
- **Example**: dirb-gendict -n thisword_X


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## dirb Usage Example

Scan the web server (`http://192.168.1.224/`) for directories using a dictionary file (`/usr/share/wordlists/dirb/common.txt`):

```console
root@kali:~# dirb http://192.168.1.224/ /usr/share/wordlists/dirb/common.txt

-----------------
DIRB v2.21
By The Dark Raver
-----------------

START_TIME: Fri May 16 13:41:45 2014
URL_BASE: http://192.168.1.224/
WORDLIST_FILES: /usr/share/wordlists/dirb/common.txt

-----------------

GENERATED WORDS: 4592

---- Scanning URL: http://192.168.1.224/ ----
==> DIRECTORY: http://192.168.1.224/.svn/
+ http://192.168.1.224/.svn/entries (CODE:200|SIZE:2726)
+ http://192.168.1.224/cgi-bin/ (CODE:403|SIZE:1122)
==> DIRECTORY: http://192.168.1.224/config/
==> DIRECTORY: http://192.168.1.224/docs/
==> DIRECTORY: http://192.168.1.224/external/
```


## Source
- Path: kali-tools\dirb\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.866936
