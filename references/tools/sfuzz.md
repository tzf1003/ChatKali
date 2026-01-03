---
tool_id: sfuzz
title: sfuzz
categories: ["vulnerability-analysis"]
category_slugs: ["vulnerability-analysis"]
homepage: http://aconole.brad-x.com/programs/sfuzz.html
repository: 
version: 0.7.0-1kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-fuzzing kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sfuzz\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.101563
---

# Tool: sfuzz (sfuzz)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://aconole.brad-x.com/programs/sfuzz.html](http://aconole.brad-x.com/programs/sfuzz.html) |
| Repository |  |
| Version | 0.7.0-1kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-fuzzing kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sfuzz
- **PackagesInfo**: |
- ****Installed size**: ** `191 KB`
- ****How to install**: ** `sudo apt install sfuzz`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sfuzz -h
- **By**: Aaron Conole
- **url**: http://aconole.brad-x.com/programs/sfuzz.html
- **EMAIL**: apconole@yahoo.com
- **Build-prefix**: /usr
- **networking / output**: []
- **-R	 Refrain from closing connections (ie**: "leak" them)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sfuzz Usage Example

Fuzz the target server (`-S 192.168.1.1`) on port 10443 (`-p 10443`) with TCP output mode (`-T`), using the basic HTTP config (`-f /usr/share/sfuzz/sfuzz-sample/basic.http`):

```console
root@kali:~# sfuzz -S 192.168.1.1 -p 10443 -T -f /usr/share/sfuzz/sfuzz-sample/basic.http
[12:53:47] dumping options:
    filename: </usr/share/sfuzz/sfuzz-sample/basic.http>
    state:    <8>
    lineno:   <56>
    literals:  [74]
    sequences: [34]
    symbols: [0]
    req_del:  <200>
    mseq_len: <10024>
    plugin: <none>
    s_syms: <0>
    literal[1] = [AREALLYBADSTRING]
```


## Source
- Path: kali-tools\sfuzz\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.101563
