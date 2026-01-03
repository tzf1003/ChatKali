---
tool_id: polenum
title: polenum
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/Wh1t3Fox/polenum/
repository: 
version: 1.7-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-information-gathering kali-tools-passwords kali-tools-respond kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\polenum\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.053238
---

# Tool: polenum (polenum)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/Wh1t3Fox/polenum/](https://github.com/Wh1t3Fox/polenum/) |
| Repository |  |
| Version | 1.7-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-information-gathering kali-tools-passwords kali-tools-respond kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/polenum
- **PackagesInfo**: |
- ****Installed size**: ** `26 KB`
- ****How to install**: ** `sudo apt install polenum`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# polenum -h
- **usage**: polenum [-h] [--username USERNAME] [--password PASSWORD]
- **positional arguments**: []
- **enum4linux            username**: password@IPaddress
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## polenum Usage Example

Get the password policy of the system by logging in with the provided username and password (`victim:s3cr3t@192.168.1.200`) using SMB port 445 (`445/SMB`):

```console
root@kali:~# polenum victim:s3cr3t@192.168.1.200 '445/SMB'

[+] Attaching to 192.168.1.200 using victim:s3cr3t

    [+] Trying protocol 445/SMB...

[+] Found domain(s):

    [+] WIN7-X86
    [+] Builtin

[+] Password Info for Domain: WIN7-X86

    [+] Minimum password length: None
    [+] Password history length: None
    [+] Maximum password age: Not Set
    [+] Password Complexity Flags: 000000

        [+] Domain Refuse Password Change: 0
        [+] Domain Password Store Cleartext: 0
        [+] Domain Password Lockout Admins: 0
        [+] Domain Password No Clear Change: 0
        [+] Domain Password No Anon Change: 0
        [+] Domain Password Complex: 0

    [+] Minimum password age: None
    [+] Reset Account Lockout Counter: 30 minutes
    [+] Locked Account Duration: 30 minutes
    [+] Account Lockout Threshold: None
    [+] Forced Log off Time: Not Set
```


## Source
- Path: kali-tools\polenum\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.053238
