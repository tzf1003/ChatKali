---
tool_id: blueranger
title: blueranger
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: http://www.hackfromacave.com/projects/blueranger.html
repository: 
version: 0.1-1kali6
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\blueranger\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.810926
---

# Tool: blueranger (blueranger)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.hackfromacave.com/projects/blueranger.html](http://www.hackfromacave.com/projects/blueranger.html) |
| Repository |  |
| Version | 0.1-1kali6 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/blueranger
- **PackagesInfo**: |
- ****Installed size**: ** `13 KB`
- ****How to install**: ** `sudo apt install blueranger`
- **root@kali**: ~# blueranger -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## blueranger Usage Example

Use the Bluetooth interface (`hci1`) to scan for the specified remote address (`20:C9:D0:43:4B:D8`):

```console
root@kali:~# blueranger hci1 20:C9:D0:43:4B:D8

Starting ...

Close with 2 X Crtl+C


      (((B(l(u(e(R)a)n)g)e)r)))

By JP Dunning (.ronin)
www.hackfromacave.com

Locating: ares (20:C9:D0:43:4B:D8)
Ping Count: 1

Proximity Change    Link Quality
----------------    ------------
FOUND           255/255

Range
------------------------------------
|*
------------------------------------
```


## Source
- Path: kali-tools\blueranger\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.810926
