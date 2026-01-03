---
tool_id: siege
title: siege
categories: ["web-application-analysis", "utilities"]
category_slugs: ["web-application-analysis", "utilities"]
homepage: https://www.joedog.org/JoeDog/Siege
repository: 
version: 4.1.6-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\siege\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.105740
---

# Tool: siege (siege)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.joedog.org/JoeDog/Siege](https://www.joedog.org/JoeDog/Siege) |
| Repository |  |
| Version | 4.1.6-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/siege
- **PackagesInfo**: |
- **Note**: this package contains siege with HTTPS support turned on, thus it
- ****Installed size**: ** `282 KB`
- ****How to install**: ** `sudo apt install siege`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# siege.config -h
- **usage**: siege.config [no arguments]
- **Usage**: siege [options]
- **Options**: []
- **ex**: --time=1H, one hour test.
- **-b, --benchmark           BENCHMARK**: no delays between requests.
- **default is used**: /var/log/siege.log


## Documentation (Upstream)
-------------------------------
 Resource file already install as /root/.siege/siege.conf
 Use your favorite editor to change  your configuration by
 editing the values in that file or remove it and run this
 program again.
 
 ```
 
 - - -
 
 ##### siege2csv
 
 Run siege with an ever-increasing number of users
 
 ```
 root@kali:~# man siege2csv
 BOMBARDMENT(1)                     siege2csv                     BOMBARDMENT(1)
 
 NAME
        bombardment - Run siege with an ever-increasing number of users
 
    SYNOPSIS
        bombardment [urlfile] [clients] [increment] [trials] [delay] bombardment
        urls.txt 5 10 20 1
 
 DESCRIPTION
        bombardment is part of the siege distribution. It calls siege with an
        initial number of clients. When that run finishes, it immediately calls
        siege again with that number of clients plus the increment.  It does
        this the number of times specified in the fourth argument.
 
 OPTIONS
        urlfile
            The name of the file containing one or more URLs for siege to test.
 
        clients
            The initial number of clients to be used on the first run.
 
        increment
            The number of clients to add to each ensuing run.
 
        trials
            The number of times to run siege.
 
        delay
            The is the amount of time, in seconds, that each client will wait
            between requests.  The siege default is overridden by bombardment
 
 SEE ALSO
        siege(1), siege2csv(1)
 
 AUTHOR
        Written by Peter Hutnick, et al.
 
 JoeDog                             2023-01-05                    BOMBARDMENT(1)
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\siege\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.105740
