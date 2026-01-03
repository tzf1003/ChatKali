---
tool_id: cisco-auditing-tool
title: cisco-auditing-tool
categories: ["password-attacks", "vulnerability-analysis"]
category_slugs: ["password-attacks", "vulnerability-analysis"]
homepage: http://www.scrypt.net/
repository: 
version: 1.0-1kali5
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-identify kali-tools-passwords kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\cisco-auditing-tool\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.843630
---

# Tool: cisco-auditing-tool (cisco-auditing-tool)

## Categories
- [password-attacks](../password-attacks.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.scrypt.net/](http://www.scrypt.net/) |
| Repository |  |
| Version | 1.0-1kali5 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-identify kali-tools-passwords kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/cisco-auditing-tool
- **PackagesInfo**: |
- ****Installed size**: ** `266 KB`
- ****How to install**: ** `sudo apt install cisco-auditing-tool`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# CAT --help
- **/usr/bin/CAT version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **Usage**: CAT [-OPTIONS [-MORE_OPTIONS]] [--] [PROGRAM_ARG1 ...]
- **The following single-character options are accepted**: []
- **With arguments**: -h -f -p -w -a -l
- **Boolean (without arguments)**: -i -q
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## cisco-auditing-tool Usage Example

Scan the host (`-h 192.168.99.230`) on port 23 (`-p 23`), using a password dictionary file (`-a /usr/share/wordlists/nmap.lst`):

```console
root@kali:~# CAT -h 192.168.99.230 -p 23 -a /usr/share/wordlists/nmap.lst

Cisco Auditing Tool - g0ne [null0]

Checking Host: 192.168.99.230


Guessing passwords:

Invalid Password: 123456
Invalid Password: 12345
```


## Source
- Path: kali-tools\cisco-auditing-tool\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.843630
