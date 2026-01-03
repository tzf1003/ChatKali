---
tool_id: sublist3r
title: sublist3r
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/aboul3la/Sublist3r
repository: 
version: 1.1-4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sublist3r\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.132508
---

# Tool: sublist3r (sublist3r)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/aboul3la/Sublist3r](https://github.com/aboul3la/Sublist3r) |
| Repository |  |
| Version | 1.1-4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/sublist3r
- **PackagesInfo**: |
- ****Installed size**: ** `1.85 MB`
- ****How to install**: ** `sudo apt install sublist3r`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sublist3r -h
- **usage**: sublist3r [-h] -d DOMAIN [-b [BRUTEFORCE]] [-p PORTS] [-v [VERBOSE]]
- **OPTIONS**: []
- **Example**: python3 /usr/bin/sublist3r -d google.com


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sublist3r Usage Examples

Search for subdomains of kali.org (`-d kali.org`) using the Bing search engine (`-e bing`) with 3 threads (`-t 3`).

```console
root@kali:~# sublist3r -d kali.org -t 3 -e bing

                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|

                # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for kali.org
[-] Searching now in Bing..
[-] Total Unique Subdomains Found: 19
www.kali.org
archive-3.kali.org
archive-4.kali.org
archive-5.kali.org
bugs.kali.org
cdimage.kali.org
docs.kali.org
ar.docs.kali.org
he.docs.kali.org
id.docs.kali.org
tr.docs.kali.org
forums.kali.org
git.kali.org
http.kali.org
images.kali.org
pkg.kali.org
repo.kali.org
security.kali.org
tools.kali.org
```


## Source
- Path: kali-tools\sublist3r\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.132508
