---
tool_id: bluesnarfer
title: bluesnarfer
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: http://www.alighieri.org/
repository: 
version: 0.1-1kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\bluesnarfer\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.811424
---

# Tool: bluesnarfer (bluesnarfer)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.alighieri.org/](http://www.alighieri.org/) |
| Repository |  |
| Version | 0.1-1kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-bluetooth kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bluesnarfer
- **PackagesInfo**: |
- ****Installed size**: ** `30 KB`
- ****How to install**: ** `sudo apt install bluesnarfer`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bluesnarfer --help
- **bluesnarfer**: invalid option -- '-'
- **usage**: bluesnarfer [options] [ATCMD] -b bt_addr
- **ATCMD**: valid AT+CMD (GSM EXTENSION)
- **TYPE**: valid phonebook type ..
- **example**: "DC" (dialed call list)
- **-b bdaddr**: bluetooth device address
- **-C chan**: bluetooth rfcomm channel
- **-c ATCMD**: custom action
- **-r N-M**: read phonebook entry N to M
- **-w N-M**: delete phonebook entry N to M
- **-f name**: search "name" in phonebook address
- **-s TYPE**: select phonebook memory storage
- **-l**: list aviable phonebook memory storage
- **-i**: device info


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


bluesnarfer Usage Example

Scan the remote device address (`-b 20:C9:D0:43:4B:D8`) and get the device info (`-i`):

```console
root@kali:~# bluesnarfer -b 20:C9:D0:43:4B:D8 -i
device name: ares
```


## Source
- Path: kali-tools\bluesnarfer\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.811424
