---
tool_id: urlcrazy
title: urlcrazy
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://www.morningstarsecurity.com/research/urlcrazy
repository: 
version: 0.7.3-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\urlcrazy\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.156831
---

# Tool: urlcrazy (urlcrazy)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.morningstarsecurity.com/research/urlcrazy](https://www.morningstarsecurity.com/research/urlcrazy) |
| Repository |  |
| Version | 0.7.3-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/urlcrazy
- **PackagesInfo**: |
- ****Installed size**: ** `1.31 MB`
- ****How to install**: ** `sudo apt install urlcrazy`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# urlcrazy -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/31882.js" id="asciicast-31882" async></script>

## urlcrazy Usage Example

Search for URLs using the dvorak layout (`-k dvorak`) and do no resolve hostnames (`-r`) for the given domain (`example.com`):

```console
root@kali:~# urlcrazy -k dvorak -r example.com
URLCrazy Domain Report
Domain    : example.com
Keyboard  : dvorak
At        : 2014-05-13 17:04:01 -0600

# Please wait. 95 hostnames to process

Typo Type              Typo            CC-A  Extn
---------------------------------------------------
Character Omission     eample.com      ?     com
Character Omission     examle.com      ?     com
Character Omission     exampe.com      ?     com
Character Omission     exampl.com      ?     com
Character Omission     example.cm      ?     cm
Character Omission     exaple.com      ?     com
```


## Source
- Path: kali-tools\urlcrazy\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.156831
