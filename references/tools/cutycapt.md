---
tool_id: cutycapt
title: cutycapt
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/Crystalix007/CutyCapt
repository: 
version: 0.0+20200623-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-reporting kali-tools-vulnerability kali-tools-web"]
icon: images/cutycapt-logo.svg
source_path: kali-tools\cutycapt\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.859649
---

# Tool: cutycapt (cutycapt)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/Crystalix007/CutyCapt](https://github.com/Crystalix007/CutyCapt) |
| Repository |  |
| Version | 0.0+20200623-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-reporting kali-tools-vulnerability kali-tools-web |
| Icon | images/cutycapt-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/cutycapt
- **PackagesInfo**: |
- ****Installed size**: ** `76 KB`
- ****How to install**: ** `sudo apt install cutycapt`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man cutycapt
- **cutycapt [options] --url=http**: //www.someurl.com --out=output.png
- **The URL to capture (http**: ...|file:...|...)
- **Minimal width for the image (default**: 800)
- **Minimal height for the image (default**: 600)
- **Don't wait more than (default**: 90000, infinite: 0)
- **After successful load, wait (default**: 0)
- **--header=<name>**: <value>
- **Specifies the request method (default**: get)
- **Unencoded request body (default**: none)
- **Base64-encoded request body (default**: none)
- **JavaScript execution (default**: on)
- **Java execution (default**: unknown)
- **Plugin execution (default**: unknown)
- **Private browsing (default**: unknown)
- **Automatic image loading (default**: on)
- **Script can open windows? (default**: unknown)
- **Script clipboard privs (default**: unknown)
- **Backgrounds in PDF/PS output (default**: off)
- **Page zoom factor (default**: no zooming)
- **Whether to zoom only the text (default**: off)
- **Address for HTTP proxy server (default**: none)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![cutycapt](images/cutycapt.png)

## cutycapt Usage Example

Take a capture of the URL (`–url=http://www.kali.org`) and save it to disk (`–out=kali.png`):

```console
root@kali:~# cutycapt --url=http://www.kali.org --out=kali.png
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
```


## Source
- Path: kali-tools\cutycapt\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.859649
