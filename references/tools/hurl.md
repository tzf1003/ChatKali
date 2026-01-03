---
tool_id: hurl
title: hurl
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/fnord0/hURL
repository: 
version: 2.1-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\hurl\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.940474
---

# Tool: hurl (hurl)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/fnord0/hURL](https://github.com/fnord0/hURL) |
| Repository |  |
| Version | 2.1-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/hurl
- **PackagesInfo**: |
- ****Installed size**: ** `187 KB`
- ****How to install**: ** `sudo apt install hurl`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hURL -h
- **.**: :[ hURL - hexadecimal & URL (en/de)coder ]::.
- **USAGE**: /usr/bin/hURL [ -flag|--flag ] [ -f <file1>,<file2> ] [ string ]
- **--esc**: : output in escaped string	    ; "\x00\x01\x02\x03 ..."
- **--pair**: : output in hexpair format	    ; 00010203 ...
- **--ansiC**: : output in C format		    ; 0x00, 0x01, 0x02, 0x03 ...


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hurl Usage Examples

Decode the given base64-encoded string (`-b “S2FsaSBMaW51eAo=”`) and display the result:

```console
root@kali:~# hURL -b "S2FsaSBMaW51eAo="

Original string       :: S2FsaSBMaW51eAo=
base64 DEcoded string :: Kali Linux
```


## Source
- Path: kali-tools\hurl\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.940474
