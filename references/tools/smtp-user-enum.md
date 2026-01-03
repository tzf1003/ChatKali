---
tool_id: smtp-user-enum
title: smtp-user-enum
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum
repository: 
version: 1.2-1kali4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: images/smtp-user-enum-logo.svg
source_path: kali-tools\smtp-user-enum\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.113724
---

# Tool: smtp-user-enum (smtp-user-enum)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum](http://pentestmonkey.net/tools/user-enumeration/smtp-user-enum) |
| Repository |  |
| Version | 1.2-1kali4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | images/smtp-user-enum-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/smtp-user-enum
- **PackagesInfo**: |
- ****Installed size**: ** `98 KB`
- ****How to install**: ** `sudo apt install smtp-user-enum`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# smtp-user-enum -h
- **smtp-user-enum v1.2 ( http**: //pentestmonkey.net/tools/smtp-user-enum )
- **Usage**: smtp-user-enum [options] ( -u username | -U file-of-usernames ) ( -t host | -T file-of-targets )
- **options are**: []
- **-m n     Maximum number of processes (default**: 5)
- **-M mode  Method to use for username guessing EXPN, VRFY or RCPT (default**: VRFY)
- **-f addr  MAIL FROM email address.  Used only in "RCPT TO" mode (default**: user@example.com)
- **-D dom   Domain to append to supplied user list to make email addresses (Default**: none)
- **-p port  TCP port on which smtp service runs (default**: 25)
- **-w n     Wait a maximum of n seconds for reply (default**: 5)
- **Examples**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## smtp-user-enum Usage Example

Use the VRFY method (`-M VRFY`) to search for the specified user (`-u root`) on the target server (`-t 192.168.1.25`):

```console
root@kali:~# smtp-user-enum -M VRFY -u root -t 192.168.1.25
Starting smtp-user-enum v1.2 ( http://pentestmonkey.net/tools/smtp-user-enum )

 ----------------------------------------------------------
|                   Scan Information                       |
 ----------------------------------------------------------

Mode ..................... VRFY
Worker Processes ......... 5
Target count ............. 1
Username count ........... 1
Target TCP port .......... 25
Query timeout ............ 5 secs
Target domain ............

######## Scan started at Tue May 13 16:06:28 2014 #########
192.168.1.25: root exists
######## Scan completed at Tue May 13 16:06:29 2014 #########
1 results.

1 queries in 1 seconds (1.0 queries / sec)
```


## Source
- Path: kali-tools\smtp-user-enum\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.113724
