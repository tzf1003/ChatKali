---
tool_id: plecost
title: plecost
categories: ["web-application-analysis", "vulnerability-analysis", "information-gathering"]
category_slugs: ["web-application-analysis", "vulnerability-analysis", "information-gathering"]
homepage: https://github.com/iniqua/plecost
repository: 
version: 1.1.2-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\plecost\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.051445
---

# Tool: plecost (plecost)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/iniqua/plecost](https://github.com/iniqua/plecost) |
| Repository |  |
| Version | 1.1.2-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://gitlab.com/kalilinux/packages/plecost
- **PackagesInfo**: |
- ****Installed size**: ** `5.86 MB`
- ****How to install**: ** `sudo apt install plecost`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# plecost -h
- **usage**: plecost [-h] [-v] [-o OUTPUT_FILE] [--hostname HOSTNAME] [-np] [-nc]
- **Plecost**: Wordpress finger printer tool
- **positional arguments**: []
- **options**: []
- **-v, --verbosity       verbosity level**: -v, -vv, -vvv.
- **-o OUTPUT_FILE        report file with extension**: xml|json
- **scanner options**: []
- **-j, --jackass-modes   jackass mode**: unlimited connections to remote host
- **wordlist options**: []
- **advanced options**: []
- **update options**: []
- **database search**: []
- **Examples**: []
- *** Scan target using default 50 most common plugins**: []
- *** Update vulnerability database**: []
- *** List available word lists**: []
- *** Use embedded 1000 most common word list**: []
- **or**: plecost -w plugin_list_1000 TARGET
- *** Scan, using 10 concurrent network connections**: []
- *** Scan using verbose mode and generate xml report**: []
- *** Scan using verbose mode and generate json report**: []
- *** Not show banner, and only test wordpress connectivity, without plugin or wordpress testing**: []
- *** Update CVE database**: []
- *** Update plugins list**: []
- *** List plugins with associated vulnerabilities in local database**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## plecost Usage Example

Use 100 plugins (`-n 100`), sleep for 10 seconds between probes (`-s 10`) but no more than 15 (`-M 15`) and use the plugin list (`-i /usr/share/plecost/wp_plugin_list.txt`) to scan the given URL (`192.168.1.202/wordpress`):

```console
root@kali:~# plecost -n 100 -s 10 -M 15 -i /usr/share/plecost/wp_plugin_list.txt 192.168.1.202/wordpress
[*] Num of checks set to: 100

-------------------------------------------------
[*] Input plugin list set to: /usr/share/plecost/wp_plugin_list.txt
[*] Min sleep time set to: 10
[*] Max sleep time set to: 15
-------------------------------------------------

==> Results for: 192.168.1.202/wordpress <==

[i] Wordpress version found:  3.9.1
[i] Wordpress last public version: 3.9.1


[*] Search for installed plugins


[i] Plugin found: akismet
    |_Latest version:  2.4.0
    |_ Installed version: 3.0.0
    |_CVE list:
    |___CVE-2009-2334: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-2334)
    |___CVE-2007-2714: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-2714)
    |___CVE-2006-4743: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-4743)
    |___CVE-2009-2334: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-2334)
    |___CVE-2007-2714: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2007-2714)
    |___CVE-2006-4743: (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-4743)
```


## Source
- Path: kali-tools\plecost\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.051445
