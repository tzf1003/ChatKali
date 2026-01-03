---
tool_id: sqlninja
title: sqlninja
categories: ["web-application-analysis", "exploitation-tools", "vulnerability-analysis", "information-gathering"]
category_slugs: ["web-application-analysis", "exploitation-tools", "vulnerability-analysis", "information-gathering"]
homepage: https://sqlninja.sourceforge.net/
repository: 
version: 0.2.6-r1-1kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/sqlninja-logo.svg
source_path: kali-tools\sqlninja\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.123652
---

# Tool: sqlninja (sqlninja)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [exploitation-tools](../exploitation-tools.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sqlninja.sourceforge.net/](https://sqlninja.sourceforge.net/) |
| Repository |  |
| Version | 0.2.6-r1-1kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/sqlninja-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sqlninja
- **PackagesInfo**: |
- ****Installed size**: ** `1.00 MB`
- ****How to install**: ** `sudo apt install sqlninja`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sqlninja --help
- **/usr/bin/sqlninja version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **Usage**: /usr/bin/sqlninja
- **The following single-character options are accepted**: []
- **With arguments**: -m -f -p -w -u -d
- **Boolean (without arguments)**: -g -v
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
- **-m <mode>**: Required. Available modes are:
- **-f <file>**: configuration file (default: sqlninja.conf)
- **-p <password>**: sa password
- **-w <wordlist>**: wordlist to use in bruteforce mode (dictionary method
- **-g**: generate debug script and exit (only valid in upload mode)
- **-v**: verbose output
- **-d <mode>**: activate debug


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sqlninja Usage Example

Connect to the target in test mode (`-m t`) with the specified config file (`-f /root/sqlninja.conf`):

```console
root@kali:~# sqlninja -m t -f /root/sqlninja.conf
Sqlninja rel. 0.2.6-r1
Copyright (C) 2006-2011 icesurfer <r00t@northernfortress.net>
[+] Parsing /root/sqlninja.conf...
[+] Target is: 192.168.1.51:80
[+] Trying to inject a 'waitfor delay'....
```


## Source
- Path: kali-tools\sqlninja\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.123652
