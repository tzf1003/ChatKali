---
tool_id: sidguesser
title: sidguesser
categories: ["password-attacks", "information-gathering"]
category_slugs: ["password-attacks", "information-gathering"]
homepage: http://www.cqure.net/wp/tools/database/sidguesser/
repository: 
version: 1.0.5-1kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/sidguesser-logo.svg
source_path: kali-tools\sidguesser\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.105288
---

# Tool: sidguesser (sidguesser)

## Categories
- [password-attacks](../password-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.cqure.net/wp/tools/database/sidguesser/](http://www.cqure.net/wp/tools/database/sidguesser/) |
| Repository |  |
| Version | 1.0.5-1kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/sidguesser-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sidguesser
- **PackagesInfo**: |
- ****Installed size**: ** `25 KB`
- ****How to install**: ** `sudo apt install sidguesser`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sidguess -h


## Documentation (Upstream)
----------------------------------
 sidguess -i <ip> -d <dictionary> [options]
 
 options:
     -p <portnr> Use specific port (default 1521)
     -r <report> Report to file
     -m <mode>   findfirst OR findall(default)
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sidguess Usage Example

Attack the server (`-i 192.168.1.205`) using a dictionary file (`-d /usr/share/wordlists/metasploit/unix_users.txt`):

```console
root@kali:~# sidguess -i 192.168.1.205 -d /usr/share/wordlists/metasploit/unix_users.txt

SIDGuesser v1.0.5 by patrik@cqure.net
-------------------------------------

Starting Dictionary Attack (<space> for stats, Q for quit) ...
```


## Source
- Path: kali-tools\sidguesser\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.105288
