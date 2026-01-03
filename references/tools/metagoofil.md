---
tool_id: metagoofil
title: metagoofil
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/opsdisk/metagoofil
repository: 
version: 1:1.2.0+git20221009-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-information-gathering kali-tools-reporting"]
icon: images/metagoofil-logo.svg
source_path: kali-tools\metagoofil\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.989733
---

# Tool: metagoofil (metagoofil)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/opsdisk/metagoofil](https://github.com/opsdisk/metagoofil) |
| Repository |  |
| Version | 1:1.2.0+git20221009-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-information-gathering kali-tools-reporting |
| Icon | images/metagoofil-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/metagoofil
- **PackagesInfo**: |
- ****Installed size**: ** `126 KB`
- ****How to install**: ** `sudo apt install metagoofil`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# metagoofil -h
- **usage**: metagoofil.py [-h] -d DOMAIN [-e DELAY] [-f [SAVE_FILE]]
- **options**: []
- **take a while. Default**: 30.0
- **unreachable/stale pages. Default**: 15
- **-l SEARCH_MAX         Maximum results to search. Default**: 100
- **Default**: 100
- **-r NUMBER_OF_THREADS  Number of downloader threads. Default**: 8
- **no -u = "Mozilla/5.0 (compatible; Googlebot/2.1; +http**: //www.google.com/bot.html)"


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## metagoofil Usage Example

Scan for documents from a domain (`-d kali.org)` that are PDF files (`-t pdf`), searching 100 results (`-l 100`), download 25 files (`-n 25`), saving the downloads to a directory (`-o kalipdf`), and saving the output to a file (`-f kalipdf.html`):

```console
root@kali:~# metagoofil -d kali.org -t pdf -l 100 -n 25 -o kalipdf -f kalipdf.html

******************************************************
*     /\/\   ___| |_ __ _  __ _  ___   ___  / _(_) | *
*    /    \ / _ \ __/ _` |/ _` |/ _ \ / _ \| |_| | | *
*   / /\/\ \  __/ || (_| | (_| | (_) | (_) |  _| | | *
*   \/    \/\___|\__\__,_|\__, |\___/ \___/|_| |_|_| *
*                         |___/                      *
* Metagoofil Ver 2.2                                 *
* Christian Martorella                               *
* Edge-Security.com                                  *
* cmartorella_at_edge-security.com                   *
******************************************************
['pdf']

[-] Starting online search...

[-] Searching for pdf files, with a limit of 100
        Searching 100 results...
Results: 21 files found
Starting to download 25 of them:
```


## Source
- Path: kali-tools\metagoofil\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.989733
