---
tool_id: websploit
title: websploit
categories: ["information-gathering", "web-application-analysis", "exploitation-tools"]
category_slugs: ["information-gathering", "web-application-analysis", "exploitation-tools"]
homepage: https://sourceforge.net/projects/websploit/
repository: 
version: 4.0.4-3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\websploit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.166978
---

# Tool: websploit (websploit)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/websploit/](https://sourceforge.net/projects/websploit/) |
| Repository |  |
| Version | 4.0.4-3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/websploit
- **PackagesInfo**: |
- ****Installed size**: ** `76 KB`
- ****How to install**: ** `sudo apt install websploit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man websploit
- **typing "websploit" as root and the prompt will change to this**: wsf >


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## websploit Usage Example

```console
root@kali:~# websploit
WARNING: No route found for IPv6 destination :: (no default route?)

     __          __  _               _       _ _
     \ \        / / | |             | |     (_) |
      \ \  /\  / /__| |__  ___ _ __ | | ___  _| |_
       \ \/  \/ / _ \ '_ \/ __| '_ \| |/ _ \| | __|
        \  /\  /  __/ |_) \__ \ |_) | | (_) | | |_
         \/  \/ \___|_.__/|___/ .__/|_|\___/|_|\__|
                              | |
                              |_|

        --=[WebSploit FrameWork
    +---**---==[Version :2.0.5 BETA
    +---**---==[Codename :We're Not Crying Wolf
    +---**---==[Available Modules : 19
        --=[Update Date : [r2.0.5-000 2.3.2014]



wsf > use web/dir_scanner
wsf:Dir_Scanner > set TARGET http://192.168.1.202
TARGET =>  192.168.1.202
wsf:Dir_Scanner > run
[*] Your Target : 192.168.1.202
[*]Loading Path List ... Please Wait ...
[index] ... [400 Bad Request]
[images] ... [400 Bad Request]
[download] ... [400 Bad Request]
[2006] ... [400 Bad Request]
[news] ... [400 Bad Request]
[crack] ... [400 Bad Request]
```


## Source
- Path: kali-tools\websploit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.166978
