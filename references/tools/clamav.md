---
tool_id: clamav
title: clamav
categories: ["defensive-tools", "utilities"]
category_slugs: ["defensive-tools", "utilities"]
homepage: https://www.clamav.net/
repository: 
version: 1.4.3+dfsg-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-protect"]
icon: images/clamav-logo.svg
source_path: kali-tools\clamav\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.846802
---

# Tool: clamav (clamav)

## Categories
- [defensive-tools](../defensive-tools.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.clamav.net/](https://www.clamav.net/) |
| Repository |  |
| Version | 1.4.3+dfsg-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-protect |
| Icon | images/clamav-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/clamav-team/clamav
- **PackagesInfo**: |
- **This package contains the command line interface. Features**: ['built-in support for various archive formats, including Zip, Tar,']
- **for getting it**: ['clamav-freshclam: updates the database from Internet. This is']
- ****Installed size**: ** `33.05 MB`
- ****How to install**: ** `sudo apt install libclamav12`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# clamav-config -h
- **Clam AntiVirus**: Daemon Client 1.4.3
- **By The ClamAV Team**: https://www.clamav.net/about.html#credits
- ****Caution****: You should NEVER run bytecode signatures from untrusted sources.
- **When building a CVD. Default**: 3000
- **Default**: 213
- **prompt.  NOTE**: If a CVD is found in the
- **This package contains the daemon featuring**: ['fast, multi-threaded daemon;', "easy integration with MTA's;", 'support for on-access scanning;', 'remote scanning;', 'able to be run supervised by daemon.']
- **clamdtop [-hVc] [host[**: port] /path/to/clamd.sock ...]
- **host[**: port]                       Connect to clamd on host at port (default 3310)
- **ClamAV**: On Access Scanning Application and Client 1.4.3
- **--ping                 -p A[**: I]    Ping clamd up to [A] times at optional interval [I] until it responds.
- **NOTE**: DIRECTORY must already exist, be an absolute path, and                                         be writeable by freshclam and readable by clamd/clamscan.    --daemon-notify[=/path/clamd.conf]   Send RELOAD command to clamd
- **Environment Variables**: []
- **--ping              -p A[**: I]       Ping clamd up to [A] times at optional interval [I] until it responds.
- **Usage**: clamav-config [OPTION]
- **Known values for OPTION are**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\clamav\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.846802
