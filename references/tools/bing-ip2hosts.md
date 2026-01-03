---
tool_id: bing-ip2hosts
title: bing-ip2hosts
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://www.morningstarsecurity.com/research/bing-ip2hosts
repository: 
version: 1.0.5-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\bing-ip2hosts\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.804072
---

# Tool: bing-ip2hosts (bing-ip2hosts)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.morningstarsecurity.com/research/bing-ip2hosts](https://www.morningstarsecurity.com/research/bing-ip2hosts) |
| Repository |  |
| Version | 1.0.5-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bing-ip2hosts
- **PackagesInfo**: |
- ****Installed size**: ** `29 KB`
- ****How to install**: ** `sudo apt install bing-ip2hosts`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bing-ip2hosts -h
- **m,                   .,recon**: ,        ,,
- **j#          https**: //morningstarsecurity.com/research/bing-ip2hosts
- **https**: //github.com/urbanadventurer/bing-ip2hosts
- **Usage**: /usr/bin/bing-ip2hosts [OPTIONS] IP|hostname
- **OPTIONS are**: []
- **-n NUM	Stop after NUM scraped pages return no new results (Default**: 5).
- **-l	Select the language for use in the setlang parameter (Default**: en-us).


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## bing-ip2hosts Usage Examples

```console
root@kali:~# bing-ip2hosts -p microsoft.com
[ 65.55.58.201 | Scraping 1 | Found 0 | / ]
http://microsoft.com
http://research.microsoft.com
http://www.answers.microsoft.com
http://www.microsoft.com
http://www.msdn.microsoft.com
```

```console
root@kali:~# bing-ip2hosts -p 173.194.33.80
[ 173.194.33.80 | Scraping 60-69 of 73 | Found 41 | | ]| / ]
http://asia.google.com
http://desktop.google.com
http://ejabat.google.com
http://google.netscape.com
http://partner-client.google.com
http://picasa.google.com
```


## Source
- Path: kali-tools\bing-ip2hosts\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.804072
