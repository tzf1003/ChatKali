---
tool_id: crack
title: crack
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://alecmuffett.com/alecm/software/crack/
repository: 
version: 5.0a-19
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\crack\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.853089
---

# Tool: crack (crack)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://alecmuffett.com/alecm/software/crack/](https://alecmuffett.com/alecm/software/crack/) |
| Repository |  |
| Version | 5.0a-19 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/crack
- **PackagesInfo**: |
- ****Installed size**: ** `153 KB`
- ****How to install**: ** `sudo apt install crack`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# Crack-Reporter -h
- **Crack**: unrecognised argument -h
- **Usage**: Crack [options] [bindir] [[-fmt format] files]...


## Documentation (Upstream)
- passwords cracked as of Thu Nov 27 08:51:44 EST 2025 ----
 
 
 ---- errors and warnings ----
 
 
 ---- done ----
 ```
 
 - - -
 
 ##### Crack-Reporter
 
 Programs to break password files
 
 ```
 root@kali:~# Crack-Reporter -h
 ---- passwords cracked as of Thu Nov 27 08:51:45 EST 2025 ----
 
 
 ---- errors and warnings ----
 
 
 ---- done ----
 ```
 
 - - -
 
 ### crack-common
 
 **Password guessing program (common files of all variants)**  
  Crack is program designed to quickly locate vulnerabilities
  in Unix (or other) password files by scanning the contents
  of a password file, looking for users who have misguidedly
  chosen a weak login password.
   
  This package provides the common files for the crypt() and
  MD5 versions.
 
 **Installed size:** `7.22 MB`  
 **How to install:** `sudo apt install crack-common`  
 
 {{< spoiler "Dependencies:" >}}
 * make
 {{< /spoiler >}}
 
 
 - - -
 
 ### crack-md5
 
 **Password guessing program (MD5 variant)**  
  Crack is program designed to quickly locate vulnerabilities
  in Unix (or other) password files by scanning the contents
  of a password file, looking for users who have misguidedly
  chosen a weak login password.
   
  This package provides the runtime files for the MD5 version.
 
 **Installed size:** `153 KB`  
 **How to install:** `sudo apt install crack-md5`  
 
 {{< spoiler "Dependencies:" >}}
 * crack-common
 * libc6 
 * libcrypt1 
 {{< /spoiler >}}
 
 ##### Crack
 
 Programs to break password files
 
 ```
 root@kali:~# Crack -h
 Crack: unrecognised argument -h
 Usage: Crack [options] [bindir] [[-fmt format] files]...
 ```
 
 - - -
 
 ##### Crack-Reporter
 
 Programs to break password files
 
 ```
 root@kali:~# Crack-Reporter -h
 ---- passwords cracked as of Thu Nov 27 08:51:57 EST 2025 ----
 
 
 ---- errors and warnings ----
 
 
 ---- done ----
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\crack\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.853089
