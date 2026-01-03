---
tool_id: unix-privesc-check
title: unix-privesc-check
categories: ["utilities", "information-gathering", "vulnerability-analysis"]
category_slugs: ["utilities", "information-gathering", "vulnerability-analysis"]
homepage: http://pentestmonkey.net/tools/audit/unix-privesc-check
repository: 
version: 1.4-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-vulnerability"]
icon: images/unix-privesc-check-logo.svg
source_path: kali-tools\unix-privesc-check\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.154913
---

# Tool: unix-privesc-check (unix-privesc-check)

## Categories
- [utilities](../utilities.md)
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://pentestmonkey.net/tools/audit/unix-privesc-check](http://pentestmonkey.net/tools/audit/unix-privesc-check) |
| Repository |  |
| Version | 1.4-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-vulnerability |
| Icon | images/unix-privesc-check-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/unix-privesc-check
- **PackagesInfo**: |
- ****Installed size**: ** `85 KB`
- ****How to install**: ** `sudo apt install unix-privesc-check`
- **root@kali**: ~# unix-privesc-check -h
- **unix-privesc-check v1.4 ( http**: //pentestmonkey.net/tools/unix-privesc-check )
- **Usage**: unix-privesc-check { standard | detailed }
- **"standard" mode**: Speed-optimised check of lots of security settings.
- **"detailed" mode**: Same as standard mode, but also checks perms of open file


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## unix-privesc-check Usage Example

```console
root@kali:~# unix-privesc-check standard
Assuming the OS is: linux
Starting unix-privesc-check v1.4 ( http://pentestmonkey.net/tools/unix-privesc-check )

This script checks file permissions and other settings that could allow
local users to escalate privileges.

Use of this script is only permitted on systems which you have been granted
legal permission to perform a security assessment of.  Apart from this
condition the GPL v2 applies.

Search the output below for the word 'WARNING'.  If you don't see it then
this script didn't find any problems.


############################################
Recording hostname
############################################
kali

############################################
Recording uname
############################################
Linux kali 3.12-kali1-amd64 #1 SMP Debian 3.12.9-1kali1 (2014-05-13) x86_64 GNU/Linux

############################################
Recording Interface IP addresses
```


## Source
- Path: kali-tools\unix-privesc-check\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.154913
