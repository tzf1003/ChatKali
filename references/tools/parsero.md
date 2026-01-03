---
tool_id: parsero
title: parsero
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://github.com/behindthefirewalls/Parsero
repository: 
version: 0.81~git20140929-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/parsero-logo.svg
source_path: kali-tools\parsero\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.038944
---

# Tool: parsero (parsero)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/behindthefirewalls/Parsero](https://github.com/behindthefirewalls/Parsero) |
| Repository |  |
| Version | 0.81~git20140929-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/parsero-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/parsero
- **PackagesInfo**: |
- **indexed. For example, "Disallow**: /portal/login" means that the content on
- ****Installed size**: ** `20 KB`
- ****How to install**: ** `sudo apt install parsero`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# parsero -h
- **usage**: parsero [-h] [-u URL] [-o] [-sb] [-f FILE]
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script id="asciicast-31995" src="https://asciinema.org/a/31995.js" async type="text/javascript"></script>

## parsero Usage Example

Search for results from a website (`-u www.bing.com`) using Bing indexed Disallows (`-sb`):

```console
root@kali:~# parsero -u www.bing.com -sb

____
| _ \ __ _ _ __ ___ ___ _ __ ___
| |_) / _` | '__/ __|/ _ \ '__/ _ \
| __/ (_| | | \__ \ __/ | | (_) |
|_| \__,_|_| |___/\___|_| \___/

Starting Parsero v0.75 (https://github.com/behindthefirewalls/Parsero) at 06/09/14 12:48:25
Parsero scan report for www.bing.com
http://www.bing.com/travel/secure 301 Moved Permanently
http://www.bing.com/travel/flight/flightSearchAction 301 Moved Permanently
http://www.bing.com/travel/css 301 Moved Permanently
http://www.bing.com/results 404 Not Found
http://www.bing.com/spbasic 404 Not Found
http://www.bing.com/entities/search 302 Found
http://www.bing.com/translator/? 200 OK
http://www.bing.com/Proxy.ashx 404 Not Found
http://www.bing.com/images/search? 200 OK
http://www.bing.com/travel/hotel/hotelSearch 301 Moved Permanently
http://www.bing.com/static/ 404 Not Found
http://www.bing.com/offers/proxy/dealsserver/api/log 405 Method Not Allowed
http://www.bing.com/shenghuo 301 Moved Permanently
http://www.bing.com/widget/render 200 OK
````


## Source
- Path: kali-tools\parsero\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.038944
