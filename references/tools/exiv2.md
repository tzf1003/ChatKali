---
tool_id: exiv2
title: exiv2
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.exiv2.org/
repository: 
version: 0.28.7+dfsg-2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\exiv2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.889195
---

# Tool: exiv2 (exiv2)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.exiv2.org/](https://www.exiv2.org/) |
| Repository |  |
| Version | 0.28.7+dfsg-2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/qt-kde-team/3rdparty/exiv2
- **PackagesInfo**: |
- **Exiv2 command line utility to**: []
- *** print Exif, IPTC and XMP image metadata in different formats**: ['Exif summary info, interpreted values, or the plain data for each tag']
- ****Installed size**: ** `21.24 MB`
- ****How to install**: ** `sudo apt install libexiv2-doc`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# exiv2 -h
- **Usage**: exiv2 [ option [ arg ] ]+ [ action ] file ...
- **Actions**: []
- **Options**: []
- **-a time Time adjustment in the format [+|-]HH[**: MM[:SS]]. For 'adjust' action
- **-p mode Print mode for the 'print' action. Possible modes are**: []
- **s**: Size in bytes of vanilla value (may include NULL)
- **a**: All supported metadata (the default)
- **e**: Exif tags
- **t**: Exif thumbnail only (to <file>-thumb.jpg)
- **v**: Plain data value of untranslated (vanilla)
- **h**: Hex dump of the data
- **i**: IPTC tags
- **x**: XMP tags
- **c**: JPEG comment
- **p**: List available image preview, sorted by size
- **C**: ICC Profile, to <file>.icc
- **R**: Recursive print structure of image (debug build only)
- **S**: Print structure of image (limited file types)
- **X**: XMP sidecar to <file>.xmp
- **-P flgs Print flags for fine control of tag lists ('print' action)**: []
- **E**: Exif tags
- **I**: IPTC tags
- **g**: Group name (e.g. Exif.Photo.UserComment, Photo)
- **k**: Key (e.g. Exif.Photo.UserComment)
- **l**: Tag label (e.g. Exif.Photo.UserComment, 'User comment')
- **d**: Tag description
- **n**: Tag name (e.g. Exif.Photo.UserComment, UserComment)
- **y**: Type
- **V**: Plain data value, data type and the word 'set'
- **-d tgt1  Delete target(s) for the 'delete' action. Possible targets are**: []
- **XX**: "raw" metadata to <file>.exv. XMP default, optional Exif and IPTC
- **pN**: Extract N'th preview image to <file>-preview<N>.<ext>
- **follows strftime(3). The following keywords are also supported**: []
- ****: parentname: - name of parent directory
- **-M cmd  Command line for the modify action. The format is**: []
- **Examples**: []
- **exiv2 -g date/i https**: //clanmills.com/Stonehenge.jpg
- **Exiv2 library provides**: []
- *** Exif Makernote support**: ['Makernote tags can be read and written just like any other metadata', 'a sophisticated write algorithm avoids corrupting the Makernote']


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\exiv2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.889195
