---
tool_id: apache-users
title: apache-users
categories: ["password-attacks", "web-application-analysis"]
category_slugs: ["password-attacks", "web-application-analysis"]
homepage: https://labs.portcullis.co.uk/downloads/
repository: 
version: 2.1-1kali6
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: images/apache-users-logo.svg
source_path: kali-tools\apache-users\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.782710
---

# Tool: apache-users (apache-users)

## Categories
- [password-attacks](../password-attacks.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://labs.portcullis.co.uk/downloads/](https://labs.portcullis.co.uk/downloads/) |
| Repository |  |
| Version | 2.1-1kali6 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | images/apache-users-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/apache-users
- **PackagesInfo**: |
- ****Installed size**: ** `13 KB`
- ****How to install**: ** `sudo apt install apache-users`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# apache-users -h
- **USAGE**: apache-users [-h 1.2.3.4] [-l names] [-p 80] [-s (SSL Support 1=true 0=false)] [-e 403 (http code)] [-t threads]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## apache-users Usage Example

Run against the remote host (`-h 192.168.1.202`), passing a dictionary of usernames (`-l /usr/share/wordlists/metasploit/unix_users.txt`), the port to use (`-p 80`), disable SSL (`-s 0`), specify the HTTP error code (`-e 403`), using 10 threads (`-t 10`):

```console
root@kali:~# apache-users -h 192.168.1.202 -l /usr/share/wordlists/metasploit/unix_users.txt -p 80 -s 0 -e 403 -t 10
```


## Source
- Path: kali-tools\apache-users\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.782710
