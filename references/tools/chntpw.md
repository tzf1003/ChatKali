---
tool_id: chntpw
title: chntpw
categories: ["password-attacks", "utilities"]
category_slugs: ["password-attacks", "utilities"]
homepage: http://pogostick.net/~pnh/ntpasswd/
repository: 
version: 140201-1.2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: images/chntpw-logo.svg
source_path: kali-tools\chntpw\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.839759
---

# Tool: chntpw (chntpw)

## Categories
- [password-attacks](../password-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://pogostick.net/~pnh/ntpasswd/](http://pogostick.net/~pnh/ntpasswd/) |
| Repository |  |
| Version | 140201-1.2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | images/chntpw-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/chntpw
- **PackagesInfo**: |
- ****Installed size**: ** `486 KB`
- ****How to install**: ** `sudo apt install chntpw`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# samusrgrp -h
- **chntpw**: change password of a user in a Windows SAM file,
- **NOTE**: This program is somewhat hackish! You are on your own!
- **Modes**: []
- **Options**: []
- **-L**: Log changed filenames to /tmp/changed, also auto-saves
- **-C**: Auto-save (commit) changed hives without asking
- **-N**: No allocate mode, only allow edit of existing values with same size
- **-E**: No expand mode, do not expand hive file (safe mode)
- **-t**: Debug trace of allocated blocks
- **-v**: Some more verbose messages/debug
- **Mode**: -a = add user to group
- **Parameters**: []
- **Example**: []
- **-H**: Human readable output, else parsable
- **Multi call binary, if program is named**: []
- **samusrtogrp -- Assume -a mode**: Add a user into a group
- **samusrfromgrp -- Assume -r mode**: Remove user from a group


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\chntpw\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.839759
