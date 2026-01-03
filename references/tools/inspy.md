---
tool_id: inspy
title: inspy
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/gojhonny/InSpy
repository: 
version: 3.0.0-0kali4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\inspy\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.946686
---

# Tool: inspy (inspy)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/gojhonny/InSpy](https://github.com/gojhonny/InSpy) |
| Repository |  |
| Version | 3.0.0-0kali4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/inspy
- **PackagesInfo**: |
- ****Installed size**: ** `45 KB`
- ****How to install**: ** `sudo apt install inspy`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# inspy -h
- **usage**: inspy [-h] [--domain DOMAIN] [--email EMAIL] [--titles [file]]
- **positional arguments**: []
- **options**: []
- **Formats**: first.last@xyz.com, last.first@xyz.com,
- **[Default**: title-list-small.txt]
- **Output Options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## inspy Usage Examples

Search LinkedIn for `google` employees (`–empspy`) with the provided wordlist of job titles (`/usr/share/inspy/wordlists/title-list-large.txt`).

```console
root@kali:~# inspy --empspy /usr/share/inspy/wordlists/title-list-large.txt google
```

Search for technologies (`–techspy`) in use at the target company (`cisco`) using the provided list of terms (`/usr/share/inspy/wordlists/tech-list-small.txt`).

```console
root@kali:~# inspy --techspy /usr/share/inspy/wordlists/tech-list-small.txt cisco
```


## Source
- Path: kali-tools\inspy\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.946686
