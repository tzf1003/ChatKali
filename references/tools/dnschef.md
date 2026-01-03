---
tool_id: dnschef
title: dnschef
categories: ["sniffing-spoofing"]
category_slugs: ["sniffing-spoofing"]
homepage: https://github.com/iphelix/dnschef
repository: 
version: 0.4+git20190327-0kali4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing kali-tools-windows-resources"]
icon: images/dnschef-logo.svg
source_path: kali-tools\dnschef\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.870923
---

# Tool: dnschef (dnschef)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/iphelix/dnschef](https://github.com/iphelix/dnschef) |
| Repository |  |
| Version | 0.4+git20190327-0kali4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing kali-tools-windows-resources |
| Icon | images/dnschef-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dnschef
- **PackagesInfo**: |
- ****Installed size**: ** `51 KB`
- ****How to install**: ** `sudo apt install dnschef`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dnschef -h
- **usage**: dnschef [options]:
- **options**: []
- **Fake DNS records**: :
- **--fakeipv6 2001**: db8::1
- **example**: google.com=1.1.1.1 will force all queries to
- **Optional runtime parameters.**: []
- **--nameservers 8.8.8.8#53 or 4.2.2.1#53#tcp or 2001**: 4860:4860::8888
- **IPv4 mode and 2001**: 4860:4860::8888 when running in
- **-i, --interface 127.0.0.1 or**: :1
- **default, the tool uses 127.0.0.1 for IPv4 mode and**: :1


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dnschef Usage Example

```console
root@kali:~# dnschef
          _                _          __
         | | version 0.1  | |        / _|
       __| |_ __  ___  ___| |__   ___| |_
      / _` | '_ \/ __|/ __| '_ \ / _ \  _|
     | (_| | | | \__ \ (__| | | |  __/ |
      \__,_|_| |_|___/\___|_| |_|\___|_|
                   iphelix@thesprawl.org

[*] DNS Chef started on interface: 127.0.0.1
[*] Using the following nameservers: 8.8.8.8
[*] No parameters were specified. Running in full proxy mode
```


## Source
- Path: kali-tools\dnschef\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.870923
