---
tool_id: fierce
title: fierce
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/mschwager/fierce
repository: 
version: 1.6.0-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/fierce-logo.svg
source_path: kali-tools\fierce\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.898171
---

# Tool: fierce (fierce)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/mschwager/fierce](https://github.com/mschwager/fierce) |
| Repository |  |
| Version | 1.6.0-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/fierce-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/fierce
- **PackagesInfo**: |
- **Originally written by RSnake along with others at http**: //ha.ckers.org/.
- ****Installed size**: ** `239 KB`
- ****How to install**: ** `sudo apt install fierce`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fierce -h
- **usage**: fierce [-h] [--domain DOMAIN] [--connect] [--wide]
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## fierce Usage Example

Run a default scan against the target domain (`--domain example.com`):

```console
root@kali:~# fierce --domain example.com
DNS Servers for example.com:
    b.iana-servers.net
    a.iana-servers.net

Trying zone transfer first...
    Testing b.iana-servers.net
        Request timed out or transfer not allowed.
    Testing a.iana-servers.net
        Request timed out or transfer not allowed.

Unsuccessful in zone transfer (it was worth a shot)
Okay, trying the good old fashioned way... brute force

Checking for wildcard DNS...
Nope. Good.
Now performing 2280 test(s)...
```


## Source
- Path: kali-tools\fierce\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.898171
