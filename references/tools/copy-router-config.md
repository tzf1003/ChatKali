---
tool_id: copy-router-config
title: copy-router-config
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.offsec.com
repository: 
version: 1.0-1kali5
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\copy-router-config\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.851332
---

# Tool: copy-router-config (copy-router-config)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.offsec.com](https://www.offsec.com) |
| Repository |  |
| Version | 1.0-1kali5 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/copy-router-config
- **PackagesInfo**: |
- ****Installed size**: ** `12 KB`
- ****How to install**: ** `sudo apt install copy-router-config`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# merge-router-config.pl -h
- **Usage**: ./merge-copy-config.pl <router-ip> <tftp-serverip> <community>


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## copy-router-config Usage Example

Copy the config from the router (`192.168.1.1`) to the TFTP server (`192.168.1.15`), authenticating with the community string (`private`):

```console
root@kali:~# copy-router-config.pl 192.168.1.1 192.168.1.15 private
```

## merge-router-config Usage Example

Merge the config with the router (`192.168.1.1`), copying from the TFTP server (`192.168.1.15`), using the community string (`private`):

```console
root@kali:~# merge-router-config.pl 192.168.1.1 192.168.1.15 private
```


## Source
- Path: kali-tools\copy-router-config\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.851332
