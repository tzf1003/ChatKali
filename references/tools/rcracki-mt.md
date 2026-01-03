---
tool_id: rcracki-mt
title: rcracki-mt
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://freerainbowtables.com/
repository: 
version: 0.7.0-1kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-passwords"]
icon: images/rcracki-mt-logo.svg
source_path: kali-tools\rcracki-mt\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.072733
---

# Tool: rcracki-mt (rcracki-mt)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://freerainbowtables.com/](https://freerainbowtables.com/) |
| Repository |  |
| Version | 0.7.0-1kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-passwords |
| Icon | images/rcracki-mt-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rcracki-mt
- **PackagesInfo**: |
- ****Installed size**: ** `406 KB`
- ****How to install**: ** `sudo apt install rcracki-mt`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rcracki_mt -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rcracki_mt Usage Example

Crack the password hash (`-h 5d41402abc4b2a76b9719d911017c592`) using 4 CPU cores (`-t 4`) and the specified rainbow tables (`tables2/md5/`):

```console
root@kali:~# rcracki_mt -h 5d41402abc4b2a76b9719d911017c592 -t 4 tables2/md5/
Using 4 threads for pre-calculation and false alarm checking...
Found 440 rainbowtable files...

md5_mixalpha-numeric-space#1-8_0_60000x27443102_distrrtgen[p][i]_109.rti2:
Chain Position is now 27443102
192101714 bytes read, disk access time: 1.19 s
searching for 1 hash...
cryptanalysis time: 0.26 s
```


## Source
- Path: kali-tools\rcracki-mt\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.072733
