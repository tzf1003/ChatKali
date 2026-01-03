---
tool_id: uniscan
title: uniscan
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
homepage: https://sourceforge.net/projects/uniscan/
repository: 
version: 6.3-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\uniscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.154345
---

# Tool: uniscan (uniscan)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/uniscan/](https://sourceforge.net/projects/uniscan/) |
| Repository |  |
| Version | 6.3-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/uniscan
- **PackagesInfo**: |
- ****Installed size**: ** `1.19 MB`
- ****How to install**: ** `sudo apt install uniscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# uniscan -h
- **OPTIONS**: []
- **-u 	<url> example**: https://www.example.com/
- **usage**: []
- **[1] perl ./uniscan.pl -u http**: //www.example.com/ -qweds
- **[4] perl ./uniscan.pl -i "ip**: xxx.xxx.xxx.xxx"
- **[5] perl ./uniscan.pl -o "inurl**: test"
- **[6] perl ./uniscan.pl -u https**: //www.example.com/ -r


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

```console
uniscan-gui
```

![uniscan](images/uniscan.png)

## uniscan Usage Example

Scan the given URL (`-u http://192.168.1.202/`) for vulnerabilities, enabling directory and dynamic checks (`-qd`):

```console
root@kali:~# uniscan -u http://192.168.1.202/ -qd
####################################
# Uniscan project                  #
# http://uniscan.sourceforge.net/  #
####################################
V. 6.2


Scan date: 16-5-2014 16:29:48
===================================================================================================
| Domain: http://192.168.1.202/
| Server: Apache/2.2.22 (Debian)
| IP: 192.168.1.202
===================================================================================================
|
| Directory check:
| [+] CODE: 200 URL: http://192.168.1.202/joomla/
| [+] CODE: 200 URL: http://192.168.1.202/wordpress/
===================================================================================================
|
| Crawler Started:
| Plugin name: FCKeditor upload test v.1 Loaded.
| Plugin name: Web Backdoor Disclosure v.1.1 Loaded.
| Plugin name: phpinfo() Disclosure v.1 Loaded.
| Plugin name: E-mail Detection v.1.1 Loaded.
| Plugin name: Timthumb <= 1.32 vulnerability v.1 Loaded.
| Plugin name: Code Disclosure v.1.1 Loaded.
| Plugin name: Upload Form Detect v.1.1 Loaded.
| Plugin name: External Host Detect v.1.2 Loaded.
| [+] Crawling finished, 27 URL's found!
```


## Source
- Path: kali-tools\uniscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.154345
