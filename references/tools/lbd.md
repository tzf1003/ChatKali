---
tool_id: lbd
title: lbd
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://ge.mine.nu/code/
repository: 
version: 0.4-1kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-web"]
icon: images/lbd-logo.svg
source_path: kali-tools\lbd\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.963959
---

# Tool: lbd (lbd)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://ge.mine.nu/code/](http://ge.mine.nu/code/) |
| Repository |  |
| Version | 0.4-1kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-web |
| Icon | images/lbd-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/lbd
- **PackagesInfo**: |
- ****Installed size**: ** `15 KB`
- ****How to install**: ** `sudo apt install lbd`
- **root@kali**: ~# lbd -h
- **host**: illegal option -- h
- **Usage**: host [-aCdilrTvVw] [-c class] [-N ndots] [-t type] [-W time]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script id="asciicast-32257" src="https://asciinema.org/a/32257.js" async type="text/javascript"></script>

## lbd Usage Example

Test to see if the target domain (`example.com`) is using a load balancer:

```console
root@kali:~# lbd example.com

lbd - load balancing detector 0.1 - Checks if a given domain uses load-balancing.
Written by Stefan Behte (http://ge.mine.nu)
Proof-of-concept! Might give false positives.

Checking for DNS-Loadbalancing: NOT FOUND
Checking for HTTP-Loadbalancing [Server]:
ECS (sea/55ED)
ECS (sea/1C15)
FOUND
```


## Source
- Path: kali-tools\lbd\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.963959
