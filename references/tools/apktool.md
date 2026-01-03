---
tool_id: apktool
title: apktool
categories: ["reverse-engineering"]
category_slugs: ["reverse-engineering"]
homepage: https://ibotpeaches.github.io/Apktool/
repository: 
version: 2.7.0+dfsg-7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering"]
icon: images/apktool-logo.svg
source_path: kali-tools\apktool\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.784312
---

# Tool: apktool (apktool)

## Categories
- [reverse-engineering](../reverse-engineering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://ibotpeaches.github.io/Apktool/](https://ibotpeaches.github.io/Apktool/) |
| Repository |  |
| Version | 2.7.0+dfsg-7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering |
| Icon | images/apktool-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/android-tools-team/apktool
- **PackagesInfo**: |
- ****Installed size**: ** `269 KB`
- ****How to install**: ** `sudo apt install apktool`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# apktool -h
- **usage**: apktool b[uild] [options] <app_path>
- **For additional info, see**: https://ibotpeaches.github.io/Apktool/
- **For smali/baksmali info, see**: https://github.com/JesusFreke/smali


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## apktool Usage Example

Use debug mode (`d`) to decode the given apk file (`/root/SdkControllerApp.apk)`:

```console
root@kali:~# apktool d Facebook\ Lite_v121.0.0.8.97_apkpure.com.apk
I: Using Apktool 2.3.4-dirty on Facebook Lite_v121.0.0.8.97_apkpure.com.apk
I: Loading resource table...
I: Decoding AndroidManifest.xml with resources...
I: Loading resource table from file: /root/.local/share/apktool/framework/1.apk
I: Regular manifest package...
I: Decoding file-resources...
I: Decoding values */* XMLs...
I: Baksmaling classes.dex...
I: Copying assets and libs...
I: Copying unknown files...
I: Copying original files...
```


## Source
- Path: kali-tools\apktool\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.784312
