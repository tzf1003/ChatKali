---
tool_id: dirbuster
title: dirbuster
categories: ["web-application-analysis", "information-gathering"]
category_slugs: ["web-application-analysis", "information-gathering"]
homepage: https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project
repository: 
version: 1.0-1kali6
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/dirbuster-logo.svg
source_path: kali-tools\dirbuster\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.867344
---

# Tool: dirbuster (dirbuster)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project](https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project) |
| Repository |  |
| Version | 1.0-1kali6 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/dirbuster-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dirbuster
- **PackagesInfo**: |
- ****Installed size**: ** `10.75 MB`
- ****How to install**: ** `sudo apt install dirbuster`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dirbuster -h
- **Usage**: java -jar DirBuster-1.0-RC1 -u <URL http://example.com/> [Options]
- **Options**: []
- **-h**: Display this help message
- **-H**: Start DirBuster in headless mode (no gui), report will be auto saved on exit
- **-l <Word list to use>**: The Word list to use for the list based brute force. Default: /home/kali/kali-www/bin/kali-tools/tool-output/dirbuster/directory-list-2.3-small.txt
- **-g**: Only use GET requests. Default Not Set
- **-e <File Extention list>**: File Extention list eg asp,aspx. Default: php
- **-t <Number of Threads>**: Number of connection threads to use. Default: 10
- **-s <Start point>**: Start point of the scan. Default: /
- **-v**: Verbose output, Default: Not set
- **-P**: Don't Parse html, Default: Not Set
- **-R**: Don't be recursive, Default: Not Set
- **-r <location>**: File to save report to. Default: /home/kali/kali-www/bin/kali-tools/tool-output/dirbuster/DirBuster-Report-[hostname]-[port].txt
- **Examples**: []
- **java -jar DirBuster-1.0-RC1.jar -H -u https**: //www.target.com/
- **java -jar DirBuster-1.0-RC1.jar -u https**: //www.target.com/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

```console
dirbuster
```

![dirbuster](images/dirbuster.png)


## Source
- Path: kali-tools\dirbuster\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.867344
