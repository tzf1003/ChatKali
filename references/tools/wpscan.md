---
tool_id: wpscan
title: wpscan
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis"]
homepage: https://wpscan.com/wordpress-security-scanner
repository: 
version: 3.8.28-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/wpscan-logo.svg
source_path: kali-tools\wpscan\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.179289
---

# Tool: wpscan (wpscan)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://wpscan.com/wordpress-security-scanner](https://wpscan.com/wordpress-security-scanner) |
| Repository |  |
| Version | 3.8.28-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/wpscan-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/wpscan
- **PackagesInfo**: |
- ****Installed size**: ** `397 KB`
- ****How to install**: ** `sudo apt install wpscan`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wpscan -h
- **Usage**: wpscan [options]
- **Allowed Protocols**: http, https
- **Default Protocol if none provided**: http
- **Default**: 500
- **Available choices**: wp-login, xmlrpc, xmlrpc-multicall
- **--detection-mode MODE                     Default**: mixed
- **--http-auth login**: password
- **--proxy protocol**: //IP:port                Supported protocols depend on the cURL installed
- **--proxy-auth login**: password
- **--cookie-string COOKIE                    Cookie string to use in requests, format**: cookie1=value1[; cookie2=value2]
- **--api-token TOKEN                         The WPScan API Token to display vulnerability data, available at https**: //wpscan.com/profile
- **Available Choices**: []
- **u    User IDs range. e.g**: u1-5
- **Range separator to use**: -
- **Value if no argument supplied**: vp,vt,tt,cb,dbe,u,m
- **Note**: Permalink setting must be set to "Plain" for those to be detected
- **Separator to use between the values**: ,
- **Incompatible choices (only one of each group/s can be used)**: ['vp, ap, p', 'vt, at, t']
- **Examples**: a1', 'a1,a2,a3', '/tmp/a.txt


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## wpscan Usage Examples

Scan a target WordPress URL and enumerate any plugins that are installed:

```console
root@kali:~# wpscan --url http://wordpress.local --enumerate p
_______________________________________________________________
        __          _______   _____
        \ \        / /  __ \ / ____|
         \ \  /\  / /| |__) | (___   ___  __ _ _ __
          \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
           \  /\  /  | |     ____) | (__| (_| | | | |
            \/  \/   |_|    |_____/ \___|\__,_|_| |_|

        WordPress Security Scanner by the WPScan Team
                       Version 2.6
          Sponsored by Sucuri - https://sucuri.net
   @_WPScan_, @ethicalhack3r, @erwan_lr, pvdl, @_FireFart_
_______________________________________________________________

[+] URL: http://wordpress.local/
[+] Started: Mon Jan 12 14:07:40 2015

[+] robots.txt available under: 'http://wordpress.local/robots.txt'
[+] Interesting entry from robots.txt: http://wordpress.local/search
[+] Interesting entry from robots.txt: http://wordpress.local/support/search.php
[+] Interesting entry from robots.txt: http://wordpress.local/extend/plugins/search.php
[+] Interesting entry from robots.txt: http://wordpress.local/plugins/search.php
[+] Interesting entry from robots.txt: http://wordpress.local/extend/themes/search.php
[+] Interesting entry from robots.txt: http://wordpress.local/themes/search.php
[+] Interesting entry from robots.txt: http://wordpress.local/support/rss
[+] Interesting entry from robots.txt: http://wordpress.local/archive/
[+] Interesting header: SERVER: nginx
[+] Interesting header: X-FRAME-OPTIONS: SAMEORIGIN
[+] Interesting header: X-NC: HIT lax 249
[+] XML-RPC Interface available under: http://wordpress.local/xmlrpc.php

[+] WordPress version 4.2-alpha-31168 identified from rss generator

[+] Enumerating installed plugins  ...

   Time: 00:00:35 <======================================================> (2166 / 2166) 100.00% Time: 00:00:35

[+] We found 2166 plugins:
[...]
```


## Source
- Path: kali-tools\wpscan\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.179289
