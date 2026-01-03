---
tool_id: enum4linux
title: enum4linux
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://labs.portcullis.co.uk/tools/enum4linux/
repository: 
version: 0.9.1-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/enum4linux-logo.svg
source_path: kali-tools\enum4linux\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.883658
---

# Tool: enum4linux (enum4linux)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://labs.portcullis.co.uk/tools/enum4linux/](https://labs.portcullis.co.uk/tools/enum4linux/) |
| Repository |  |
| Version | 0.9.1-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/enum4linux-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/enum4linux
- **PackagesInfo**: |
- **Features include**: []
- ****Installed size**: ** `58 KB`
- ****How to install**: ** `sudo apt install enum4linux`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# enum4linux -h
- **enum4linux v0.9.1 (http**: //labs.portcullis.co.uk/application/enum4linux/)
- **Usage**: ./enum4linux.pl [options] ip
- **Options are (like "enum")**: []
- **The following options from enum.exe aren't implemented**: -L, -N, -D, -f
- **Additional options**: []
- **-R range  RID ranges to enumerate (default**: 500-550,1000-1050, implies -r)
- **-k user   User(s) that exists on remote system (default**: administrator,guest,krbtgt,domain admins,root,bin,none)
- **Use commas to try several users**: -k admin,user1,user2
- **access**: Allow anonymous SID/Name translation" enabled (XP, 2003).
- **NB**: Samba servers often seem to have RIDs in the range 3000-3050.
- **Dependancy info**: You will need to have the samba package installed as this
- **smbclient.  Polenum from http**: //labs.portcullis.co.uk/application/polenum/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## enum4linux Usage Example

Attempt to get the userlist (`-U`) and OS information (`-o`) from the target (`192.168.1.200`):

```console
root@kali:~# enum4linux -U -o 192.168.1.200
Starting enum4linux v0.8.9 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Sun Aug 17 12:17:32 2014

 ==========================
|    Target Information    |
 ==========================
Target ........... 192.168.1.200
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ======================================================
|    Enumerating Workgroup/Domain on 192.168.1.200   |
 ======================================================
[+] Got domain/workgroup name: KALI
```


## Source
- Path: kali-tools\enum4linux\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.883658
