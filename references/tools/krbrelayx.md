---
tool_id: krbrelayx
title: krbrelayx
categories: ["post-exploitation", "exploitation-tools"]
category_slugs: ["post-exploitation", "exploitation-tools"]
homepage: https://github.com/dirkjanm/krbrelayx
repository: 
version: 0.0~git20250127.aef69a7-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\krbrelayx\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.961709
---

# Tool: krbrelayx (krbrelayx)

## Categories
- [post-exploitation](../post-exploitation.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/dirkjanm/krbrelayx](https://github.com/dirkjanm/krbrelayx) |
| Repository |  |
| Version | 0.0~git20250127.aef69a7-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/krbrelayx
- **PackagesInfo**: |
- ****Installed size**: ** `172 KB`
- ****How to install**: ** `sudo apt install krbrelayx`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# printerbug -h
- **usage**: printerbug.py [-h] [--verbose] [-target-file file]
- **Required options**: []
- **HOSTNAME              Hostname/ip or ldap**: //host:port connection string to
- **Main options**: []
- **Password or LM**: NTLM hash, will prompt if not specified
- **-s, --spn SPN         servicePrincipalName to add (for example**: []
- **Record options**: []
- **Action to perform. Options**: add (add a new record),
- **cache), delete (delete from LDAP). Default**: query
- **--ttl TTL             TTL for record (default**: 180)
- **[-hp HEXPASSWORD] [-s USERNAME] [-hashes LMHASH**: NTHASH]
- **HOSTNAMES are valid. Example**: smb://server:445 If
- **-r SMBSERVER          Redirect HTTP requests to a file**: // path on SMBSERVER
- **will be stored (default**: current directory).
- **Format to store tickets in. Valid**: ccache (Impacket)
- **or kirbi (Mimikatz format) default**: ccache
- **https**: //docs.python.org/2.4/lib/standard-
- **Kerberos Keys (of your account with unconstrained delegation)**: []
- **-hashes LMHASH**: NTHASH
- **NTLM hashes, format is LMHASH**: NTHASH
- **SMB attack options**: []
- **LDAP attack options**: []
- **AD CS attack options**: []
- **[-hashes LMHASH**: NTHASH] [-no-pass] [-k]
- **positional arguments**: []
- **target                [[domain/]username[**: password]@]<targetName or address>
- **options**: []
- **connection**: []
- **authentication**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\krbrelayx\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.961709
