---
tool_id: lynis
title: lynis
categories: ["defensive-tools", "information-gathering", "vulnerability-analysis"]
category_slugs: ["defensive-tools", "information-gathering", "vulnerability-analysis"]
homepage: https://cisofy.com/lynis/
repository: 
version: 3.1.6-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-vulnerability"]
icon: images/lynis-logo.svg
source_path: kali-tools\lynis\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.976059
---

# Tool: lynis (lynis)

## Categories
- [defensive-tools](../defensive-tools.md)
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://cisofy.com/lynis/](https://cisofy.com/lynis/) |
| Repository |  |
| Version | 3.1.6-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-vulnerability |
| Icon | images/lynis-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/lynis
- **PackagesInfo**: |
- ****Installed size**: ** `1.68 MB`
- ****How to install**: ** `sudo apt install lynis`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# lynis -h
- **2007-2025, CISOfy - https**: //cisofy.com/lynis/


## Documentation (Upstream)
---------------------------------
 
 
   Usage: lynis command [options]
 
 
   Command:
 
     audit
         audit system                  : Perform local security scan
         audit system remote <host>    : Remote security scan
         audit dockerfile <file>       : Analyze Dockerfile
 
     show
         show                          : Show all commands
         show version                  : Show Lynis version
         show help                     : Show help
 
     update
         update info                   : Show update details
 
 
   Options:
 
     Alternative system audit modes
     --forensics                       : Perform forensics on a running or mounted system
     --pentest                         : Non-privileged, show points of interest for pentesting
 
     Layout options
     --no-colors                       : Don't use colors in output
     --quiet (-q)                      : No output
     --reverse-colors                  : Optimize color display for light backgrounds
     --reverse-colours                 : Optimize colour display for light backgrounds
 
     Misc options
     --debug                           : Debug logging to screen
     --no-log                          : Don't create a log file
     --profile <profile>               : Scan the system with the given profile file
     --view-manpage (--man)            : View man page
     --verbose                         : Show more details on screen
     --version (-V)                    : Display version number and quit
     --wait                            : Wait between a set of tests
     --slow-warning <seconds>  : Threshold for slow test warning in seconds (default 10)
 
     Enterprise options
     --plugindir <path>                : Define path of available plugins
     --upload                          : Upload data to central node
 
     More options available. Run '/usr/sbin/lynis show options', or use the man page.
 
 
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## lynis Usage Example

Scan the system in quiet mode (`-Q`) and output in cronjob format (`–cronjob`):

```console
root@kali:~# lynis -Q --cronjob

[ Lynis 2.6.2 ]

################################################################################
  Lynis comes with ABSOLUTELY NO WARRANTY. This is free software, and you are
  welcome to redistribute it under the terms of the GNU General Public License.
  See the LICENSE file for details about using this software.

  2007-2018, CISOfy - https://cisofy.com/lynis/
  Enterprise support available (compliance, plugins, interface and tools)
################################################################################


[+] Initializing program
------------------------------------
- Detecting OS...  [ DONE ]
- Checking profiles... [ DONE ]

  ---------------------------------------------------
  Program version:           2.6.2
  Operating system:          Linux
  Operating system name:     Debian
  Operating system version:  kali-rolling
  Kernel version:            4.18.0
  Hardware platform:         x86_64
  Hostname:                  kali
  ---------------------------------------------------
  Profiles:                  /etc/lynis/default.prf
  Log file:                  /var/log/lynis.log
  Report file:               /var/log/lynis-report.dat
  Report version:            1.0
  Plugin directory:          /etc/lynis/plugins
  ---------------------------------------------------
  Auditor:                   [Not Specified]
  Language:                  en
  Test category:             all
  Test group:                all
  ---------------------------------------------------
[...]
```


## Source
- Path: kali-tools\lynis\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.976059
