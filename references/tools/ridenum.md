---
tool_id: ridenum
title: ridenum
categories: ["information-gathering", "password-attacks"]
category_slugs: ["information-gathering", "password-attacks"]
homepage: https://github.com/trustedsec/ridenum
repository: 
version: 1.7-0kali4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\ridenum\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.082470
---

# Tool: ridenum (ridenum)

## Categories
- [information-gathering](../information-gathering.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/trustedsec/ridenum](https://github.com/trustedsec/ridenum) |
| Repository |  |
| Version | 1.7-0kali4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/ridenum
- **PackagesInfo**: |
- ****Installed size**: ** `32 KB`
- ****How to install**: ** `sudo apt install ridenum`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ridenum -h


## Documentation (Upstream)
-.|  | |  '--'  |      |  |____ |  |\   | |  `--'  | |  |  |  |
 | _| `._____||__| |_______/  _____|_______||__| \__|  \______/  |__|  |__|
                             |______|
 
 Written by: David Kennedy (ReL1K)
 Company: https://www.trustedsec.com
 Twitter: @TrustedSec
 Twitter: @HackingDave
 
 Rid Enum is a RID cycling attack that attempts to enumerate user accounts through
 null sessions and the SID to RID enum. If you specify a password file, it will
 automatically attempt to brute force the user accounts when its finished enumerating.
 
 - RIDENUM is open source and uses all standard python libraries minus python-pexpect. -
 
 You can also specify an already dumped username file, it needs to be in the DOMAINNAME\\USERNAME
 format.
 
 Example: ./ridenum.py 192.168.1.50 500 50000 /root/dict.txt /root/user.txt
 
 Usage: ./ridenum.py <server_ip> <start_rid> <end_rid> <optional_username> <optional_password> <optional_password_file> <optional_username_filename>
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## ridenum Usage Example

Connect to the remote server (`192.168.1.236`) and cycle from RID 500 to 50000 (`500 50000`), using the given password file (`/tmp/passes.txt`):

```console
root@kali:~# ridenum 192.168.1.236 500 50000 /tmp/passes.txt
[*] Attempting lsaquery first...This will enumerate the base domain SID
[*] Successfully enumerated base domain SID.. Moving on to extract via RID
[*] Enumerating user accounts.. This could take a little while.
```


## Source
- Path: kali-tools\ridenum\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.082470
