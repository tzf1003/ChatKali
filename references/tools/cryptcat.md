---
tool_id: cryptcat
title: cryptcat
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://farm9.com/content/Free_Tools/cryptcat_linux2.tar
repository: 
version: 20031202-5kali8
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\cryptcat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.856568
---

# Tool: cryptcat (cryptcat)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://farm9.com/content/Free_Tools/cryptcat_linux2.tar](http://farm9.com/content/Free_Tools/cryptcat_linux2.tar) |
| Repository |  |
| Version | 20031202-5kali8 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/cryptcat
- **PackagesInfo**: |
- ****Installed size**: ** `80 KB`
- ****How to install**: ** `sudo apt install cryptcat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# cryptcat -h
- **connect to somewhere**: nc [-options] hostname port[s] [ports] ...
- **listen for inbound**: nc -l -p port [-options] [hostname] [port]
- **options**: []
- **-G num			source-routing pointer**: 4, 8, 12, ...
- **port numbers can be individual or ranges**: lo-hi [inclusive]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## cryptcat Usage Example

On the server, listen for a connection (`-l`) on port 4444 (`-p 4444`) and don’t do name resolution (`-n`). Redirect all data to a file (`> dataxfer`). On the client, connect to the remote IP address (`192.168.1.202`) on port 4444 (`4444`) and pipe in the data to be transferred (`< /tmp/juicyinfo)`:

```console
root@kali:~# cryptcat -l -p 4444 -n > dataxfer

root@kali:~# cryptcat 192.168.1.202 4444 < /tmp/juicyinfo
```


## Source
- Path: kali-tools\cryptcat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.856568
