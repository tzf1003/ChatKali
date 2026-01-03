---
tool_id: foremost
title: foremost
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: https://sourceforge.net/projects/foremost/
repository: 
version: 1.5.7-11
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: images/foremost-logo.svg
source_path: kali-tools\foremost\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.901942
---

# Tool: foremost (foremost)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/foremost/](https://sourceforge.net/projects/foremost/) |
| Repository |  |
| Version | 1.5.7-11 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | images/foremost-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/rul/foremost/tree/debian/sid
- **PackagesInfo**: |
- ****Installed size**: ** `102 KB`
- ****How to install**: ** `sudo apt install foremost`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# foremost -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## foremost Usage Example

Search for a selection of file types (`-t doc,jpg,pdf,xls`) in the given image file (`-i image.dd`):

```console
root@kali:~# foremost -t doc,jpg,pdf,xls -i image.dd
Processing: image.dd
|*|
root@kali:~# ls output/
audit.txt  jpg  pdf
```


## Source
- Path: kali-tools\foremost\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.901942
