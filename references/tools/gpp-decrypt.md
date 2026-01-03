---
tool_id: gpp-decrypt
title: gpp-decrypt
categories: ["information-gathering", "password-attacks"]
category_slugs: ["information-gathering", "password-attacks"]
homepage: http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html
repository: 
version: 0.1-1kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\gpp-decrypt\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.919409
---

# Tool: gpp-decrypt (gpp-decrypt)

## Categories
- [information-gathering](../information-gathering.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html](http://carnal0wnage.attackresearch.com/2012/10/group-policy-preferences-and-getting.html) |
| Repository |  |
| Version | 0.1-1kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/gpp-decrypt
- **PackagesInfo**: |
- ****Installed size**: ** `11 KB`
- ****How to install**: ** `sudo apt install gpp-decrypt`
- **{{< spoiler "Dependencies**: " >}}


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## gpp-decrypt Usage Example

Decrypt the given Group Policy Preferences string (`j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw`):

```console
root@kali:~# gpp-decrypt j1Uyj3Vx8TY9LtLZil2uAuZkFQA/4latT76ZwgdHdhw
Local*P4ssword!
```


## Source
- Path: kali-tools\gpp-decrypt\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.919409
