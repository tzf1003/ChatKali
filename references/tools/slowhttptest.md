---
tool_id: slowhttptest
title: slowhttptest
categories: ["web-application-analysis", "vulnerability-analysis", "defensive-tools"]
category_slugs: ["web-application-analysis", "vulnerability-analysis", "defensive-tools"]
homepage: https://github.com/shekyan/slowhttptest
repository: 
version: 1.9.0-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-vulnerability kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\slowhttptest\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.112184
---

# Tool: slowhttptest (slowhttptest)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [defensive-tools](../defensive-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/shekyan/slowhttptest](https://github.com/shekyan/slowhttptest) |
| Repository |  |
| Version | 1.9.0-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-vulnerability kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/slowhttptest
- **PackagesInfo**: |
- ****Installed size**: ** `89 KB`
- ****How to install**: ** `sudo apt install slowhttptest`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# slowhttptest -h
- **Usage**: slowhttptest [options ...]
- **Test modes**: []
- **Reporting options**: []
- **-v level         verbosity level 0-4**: Fatal, Info, Error, Warning, Debug
- **General options**: []
- **-u URL           absolute URL of target (http**: //localhost/)
- **X-xx**: xx for header or &xx=xx for body, where x
- **Probe/Proxy options**: []
- **-d host**: port     all traffic directed through HTTP proxy at host:port (off)
- **-e host**: port     probe traffic directed through HTTP proxy at host:port (off)
- **-j cookies       value of Cookie header (ex.**: -j "user_id=1001; timeout=9000")
- **Range attack specific options**: []
- **Slow read specific options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## slowhttptest Usage Example

Use 1000 connections (`-c 1000`) with the Slowloris mode (`-H`), and generate statistics (`-g>` with the output file name (-`o slowhttp`). Use 10 seconds to wait for data (`-i 10`), 200 connections (`-r 200`) with GET requests (`-t GET`) against the target URL (`-u http://192.168.1.202/index.php`) with a maximum of length of 24 bytes (`-x 24)` and a 3 second time out (`-p 3`):

```console
root@kali:~# slowhttptest -c 1000 -H -g -o slowhttp -i 10 -r 200 -t GET -u http://192.168.1.202/index.php -x 24 -p 3
Sat May 17 10:45:26 2014:
Sat May 17 10:45:26 2014:
    slowhttptest version 1.6
 - https://code.google.com/p/slowhttptest/ -
test type:                        SLOW HEADERS
number of connections:            1000
URL:                              http://192.168.1.202/index.php
verb:                             GET
Content-Length header value:      4096
follow up data max size:          52
interval between follow up data:  10 seconds
connections per seconds:          200
probe connection timeout:         3 seconds
test duration:                    240 seconds
using proxy:                      no proxy

Sat May 17 10:45:26 2014:
slow HTTP test status on 0th second:

initializing:        0
pending:             1
connected:           0
error:               0
closed:              0
service available:   YES
```


## Source
- Path: kali-tools\slowhttptest\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.112184
