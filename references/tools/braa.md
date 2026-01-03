---
tool_id: braa
title: braa
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/mteg/braa
repository: 
version: 0.82-8
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\braa\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.813515
---

# Tool: braa (braa)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/mteg/braa](https://github.com/mteg/braa) |
| Repository |  |
| Version | 0.82-8 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/braa
- **PackagesInfo**: |
- ****Installed size**: ** `62 KB`
- ****How to install**: ** `sudo apt install braa`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# braa -h
- **usage**: braa [options] [query1] [query2] ...
- **-r <rc>   Retry count (default**: 3).
- **Query format**: []
- **GET**: ['community@]iprange[:port]:oid[/id']
- **WALK**: ['community@]iprange[:port]:oid.*[/id']
- **SET**: ['community@]iprange[:port]:oid=value[/id']
- **Examples**: []
- **public@10.253.101.1**: 161:.1.3.6.*
- **10.253.101.1-10.253.101.255**: .1.3.6.1.2.1.1.4.0=sme,.1.3.6.*
- **10.253.101.1**: .1.3.6.1.2.1.1.1.0/description
- **It is also possible to specify multiple queries at once**: []
- **Values for SET queries have to be prepended with a character specifying the value type**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## braa Usage Example

Walk the SNMP tree on `192.168.1.215` using the community string of `public`, querying all OIDs under `.1.3.6`:

```console
root@kali:~# braa public@192.168.1.215:.1.3.6.*
192.168.1.215:122ms:.1.3.6.1.2.1.1.1.0:Linux redhat.biz.local 2.4.20-8 #1 Thu Mar 13 17:54:28 EST 2003 i686
192.168.1.215:143ms:.1.3.6.1.2.1.1.2.0:.1.3.6.1.4.1.8072.3.2.10
192.168.1.215:122ms:.1.3.6.1.2.1.1.3.0:4051218219
192.168.1.215:122ms:.1.3.6.1.2.1.1.4.0:Root <root@localhost> (configure /etc/snmp/snmp.local.conf)
192.168.1.215:143ms:.1.3.6.1.2.1.1.5.0:redhat.biz.local
```


## Source
- Path: kali-tools\braa\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.813515
