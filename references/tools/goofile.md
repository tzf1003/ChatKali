---
tool_id: goofile
title: goofile
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/sosukeinu/goofile
repository: 
version: 1.6+git20190819-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\goofile\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.915670
---

# Tool: goofile (goofile)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sosukeinu/goofile](https://github.com/sosukeinu/goofile) |
| Repository |  |
| Version | 1.6+git20190819-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/goofile
- **PackagesInfo**: |
- ****Installed size**: ** `37 KB`
- ****How to install**: ** `sudo apt install goofile`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# goofile -h
- **usage**: goofile [-h] [-d DOMAIN] [-f FILETYPE] [-k KEY] [-e ENGINE] [-q QUERY]
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/31264.js" id="asciicast-31264" async></script>

## goofile Usage Example

Search for files from a domain (`-d kali.org`) of the PDF filetype (`-f pdf)`:

```console
root@kali:~# goofile -d kali.org -f pdf

-------------------------------------
|Goofile v1.5                       |
|Coded by Thomas (G13) Richards     |
|www.g13net.com                     |
|code.google.com/p/goofile          |
-------------------------------------


Searching in kali.org for pdf
========================================

Files found:
====================

docs.kali.org/pdf/kali-book-fr.pdf
docs.kali.org/pdf/kali-book-es.pdf
docs.kali.org/pdf/kali-book-id.pdf
docs.kali.org/pdf/kali-book-de.pdf
docs.kali.org/pdf/kali-book-it.pdf
docs.kali.org/pdf/kali-book-ar.pdf
docs.kali.org/pdf/kali-book-ja.pdf
docs.kali.org/pdf/kali-book-nl.pdf
docs.kali.org/pdf/kali-book-ru.pdf
docs.kali.org/pdf/kali-book-en.pdf
docs.kali.org/pdf/kali-book-pt-br.pdf
docs.kali.org/pdf/kali-book-zh-hans.pdf
docs.kali.org/pdf/kali-book-sw.pdf
docs.kali.org/pdf/articles/kali-linux-live-usb-install-en.pdf
====================
```


## Source
- Path: kali-tools\goofile\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.915670
