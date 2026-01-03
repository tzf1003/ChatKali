---
tool_id: dnswalk
title: dnswalk
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://github.com/davebarr/dnswalk
repository: 
version: 2.0.2.dfsg.1-3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dnswalk\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.874047
---

# Tool: dnswalk (dnswalk)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/davebarr/dnswalk](https://github.com/davebarr/dnswalk) |
| Repository |  |
| Version | 2.0.2.dfsg.1-3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/dnswalk
- **PackagesInfo**: |
- ****Installed size**: ** `46 KB`
- ****How to install**: ** `sudo apt install dnswalk`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnswalk --help
- **/usr/bin/dnswalk version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **Usage**: dnswalk domain
- **The following single-character options are accepted**: []
- **With arguments**: -D
- **Boolean (without arguments)**: -r -f -i -a -d -m -F -l
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dnswalk Usage Example

Attempt to get DNS zone information from the target domain (`example.com.`):

```console
root@kali:~# dnswalk example.com.
Checking example.com.
```

```console
root@kali:~# dnswalk -r -d example.com.
Checking example.com.
```


## Source
- Path: kali-tools\dnswalk\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.874047
