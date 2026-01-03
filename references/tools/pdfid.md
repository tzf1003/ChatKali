---
tool_id: pdfid
title: pdfid
categories: ["information-gathering", "malware-analysis", "forensics"]
category_slugs: ["information-gathering", "malware-analysis", "forensics"]
homepage: https://blog.didierstevens.com/programs/pdf-tools/
repository: 
version: 0.2.10-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: images/pdfid-logo.svg
source_path: kali-tools\pdfid\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.043024
---

# Tool: pdfid (pdfid)

## Categories
- [information-gathering](../information-gathering.md)
- [malware-analysis](../malware-analysis.md)
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://blog.didierstevens.com/programs/pdf-tools/](https://blog.didierstevens.com/programs/pdf-tools/) |
| Repository |  |
| Version | 0.2.10-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | images/pdfid-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/pdfid
- **PackagesInfo**: |
- ****Installed size**: ** `106 KB`
- ****How to install**: ** `sudo apt install pdfid`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pdfid -h
- **Usage**: pdfid [options] [pdf-file|zip-file|url|@file] ...
- **Arguments**: []
- **@file**: run PDFiD on each file listed in the text file specified
- **https**: //DidierStevens.com
- **Options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## pdfid Usage Example

```console
root@kali:~# pdfid /usr/share/doc/texmf/fonts/lm/lm-info.pdf
PDFiD 0.0.12 /usr/share/doc/texmf/fonts/lm/lm-info.pdf
 PDF Header: %PDF-1.4
 obj                  526
 endobj               526
 stream               151
 endstream            151
 xref                   1
 trailer                1
 startxref              1
 /Page                 26
 /Encrypt               0
 /ObjStm                0
 /JS                    0
 /JavaScript            0
 /AA                    0
 /OpenAction            0
 /AcroForm              0
 /JBIG2Decode           0
 /RichMedia             0
 /Launch                0
 /EmbeddedFile          0
 /Colors > 2^24         0
 ```


## Source
- Path: kali-tools\pdfid\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.043024
