---
tool_id: dumpzilla
title: dumpzilla
categories: ["information-gathering", "forensics"]
category_slugs: ["information-gathering", "forensics"]
homepage: http://www.dumpzilla.org/
repository: 
version: 20210311-0kali4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dumpzilla\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.880037
---

# Tool: dumpzilla (dumpzilla)

## Categories
- [information-gathering](../information-gathering.md)
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.dumpzilla.org/](http://www.dumpzilla.org/) |
| Repository |  |
| Version | 20210311-0kali4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dumpzilla
- **PackagesInfo**: |
- ****Installed size**: ** `136 KB`
- ****How to install**: ** `sudo apt install dumpzilla`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dumpzilla -h
- **usage**: python dumpzilla.py PROFILE_DIR [OPTIONS]
- **Options**: []
- **Wildcards (without RegExp option)**: []
- **Regular Expresions**: https://docs.python.org/3/library/re.html
- **Date syntax**: []
- **YYYY-MM-DD hh**: mi:ss (wildcards allowed)
- **Profile location**: []
- **WinXP profile -> 'C**: \Documents and Settings\%USERNAME%\Application Data\Mozilla\Firefox\Profiles\xxxx.default'
- **Win7 profile  -> 'C**: \Users\%USERNAME%\AppData\Roaming\Mozilla\Firefox\Profiles\xxxx.default'
- **dumpzilla**: error: ambiguous option: -h could match -hostcookie, -httponly, -host, -history_range


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dumpzilla Usage Example

Analyze the Mozilla profile folder (`/root/.mozilla/firefox/k780shir.default/`) and dump everything except the DOM data (`–All`):

```console
root@kali:~# dumpzilla '/root/.mozilla/firefox/k780shir.default/' --All

====================================================================================================
Cookies              [SHA256 hash: 18d35b51ec9865ea3dd21e9bc69dc3d286d4e20373bbb0b350a0e41c8bf2da42]
====================================================================================================


Domain: google.com
Host: .google.com
Name: PREF
Value: ID=ddcc3d04cf65b33f:TM=1400253352:LM=1400253352:S=LrFq_HXVbaconjt0l
Path: /
Expiry: 2016-05-15 11:15:52
Last acess: 2014-05-16 11:15:52
Creation Time: 2014-05-16 11:15:52
Secure: No
HttpOnly: No


Domain: kali.org
Host: .kali.org
Name: __utma
Value: 24402336.1888242215.144BAC0N56.1400253356.14322255.1
Path: /
Expiry: 2016-05-15 11:15:55
Last acess: 2014-05-16 11:15:55
Creation Time: 2014-05-16 11:15:55
```


## Source
- Path: kali-tools\dumpzilla\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.880037
