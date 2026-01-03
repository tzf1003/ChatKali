---
tool_id: medusa
title: medusa
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: http://foofus.net/?page_id=51
repository: 
version: 2.3-3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-vulnerability kali-tools-web"]
icon: images/medusa-logo.svg
source_path: kali-tools\medusa\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.986638
---

# Tool: medusa (medusa)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://foofus.net/?page_id=51](http://foofus.net/?page_id=51) |
| Repository |  |
| Version | 2.3-3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-vulnerability kali-tools-web |
| Icon | images/medusa-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/medusa
- **PackagesInfo**: |
- **the key features of this application**: []
- ****Installed size**: ** `843 KB`
- ****How to install**: ** `sudo apt install medusa`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# medusa -h
- **Medusa v2.3 [http**: //www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>
- **Syntax**: Medusa [-h host|-H file] [-u username|-U file] [-p password|-P file] [-C file] -M module [OPT]
- **-h [TEXT]**: Target hostname or IP address
- **-H [FILE]**: File containing target hostnames or IP addresses
- **-u [TEXT]**: Username to test
- **-U [FILE]**: File containing usernames to test
- **-p [TEXT]**: Password to test
- **-P [FILE]**: File containing passwords to test
- **-C [FILE]**: File containing combo entries. See README for more information.
- **-O [FILE]**: File to append log information to
- **-e [n/s/ns]**: Additional password checks ([n] No Password, [s] Password = Username)
- **-M [TEXT]**: Name of the module to execute (without the .mod extension)
- **-m [TEXT]**: Parameter to pass to the module. This can be passed multiple times with a
- **-d**: Dump all known modules
- **-n [NUM]**: Use for non-default TCP port number
- **-s**: Enable SSL
- **-g [NUM]**: Give up after trying to connect for NUM seconds (default 3)
- **-r [NUM]**: Sleep NUM seconds between retry attempts (default 3)
- **-R [NUM]**: Attempt NUM retries before giving up. The total number of attempts will be NUM + 1.
- **-c [NUM]**: Time to wait in usec to verify socket is available (default 500 usec).
- **-t [NUM]**: Total number of logins to be tested concurrently
- **-T [NUM]**: Total number of hosts to be tested concurrently
- **-L**: Parallelize logins using one username per thread. The default is to process
- **-f**: Stop scanning host after first valid username/password found.
- **-F**: Stop audit after first valid username/password found on any host.
- **-b**: Suppress startup banner
- **-q**: Display module's usage information
- **-v [NUM]**: Verbose level [0 - 6 (more)]
- **-w [NUM]**: Error debug level [0 - 10 (more)]
- **-V**: Display version
- **-Z [TEXT]**: Resume scan based on map of previous scan


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\medusa\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.986638
