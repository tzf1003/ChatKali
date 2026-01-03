---
tool_id: patator
title: patator
categories: ["password-attacks", "utilities"]
category_slugs: ["password-attacks", "utilities"]
homepage: https://github.com/lanjelot/patator
repository: 
version: 1.0-4
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-web"]
icon: images/patator-logo.svg
source_path: kali-tools\patator\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.040917
---

# Tool: patator (patator)

## Categories
- [password-attacks](../password-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/lanjelot/patator](https://github.com/lanjelot/patator) |
| Repository |  |
| Version | 1.0-4 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-web |
| Icon | images/patator-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/patator
- **PackagesInfo**: |
- **Currently it supports the following modules**: []
- **+ ftp_login**: Brute-force FTP
- **+ ssh_login**: Brute-force SSH
- **+ telnet_login**: Brute-force Telnet
- **+ smtp_login**: Brute-force SMTP
- **+ smtp_vrfy**: Enumerate valid users using SMTP VRFY
- **+ smtp_rcpt**: Enumerate valid users using SMTP RCPT TO
- **+ finger_lookup**: Enumerate valid users using Finger
- **+ http_fuzz**: Brute-force HTTP
- **+ ajp_fuzz**: Brute-force AJP
- **+ pop_login**: Brute-force POP3
- **+ pop_passd**: Brute-force poppassd (http://netwinsite.com/poppassd/)
- **+ imap_login**: Brute-force IMAP4
- **+ ldap_login**: Brute-force LDAP
- **+ dcom_login**: Brute-force DCOM
- **+ smb_login**: Brute-force SMB
- **+ smb_lookupsid**: Brute-force SMB SID-lookup
- **+ rlogin_login**: Brute-force rlogin
- **+ vmauthd_login**: Brute-force VMware Authentication Daemon
- **+ mssql_login**: Brute-force MSSQL
- **+ mysql_login**: Brute-force MySQL
- **+ mysql_query**: Brute-force MySQL queries
- **+ rdp_login**: Brute-force RDP (NLA)
- **+ pgsql_login**: Brute-force PostgreSQL
- **+ vnc_login**: Brute-force VNC
- **+ dns_forward**: Forward DNS lookup
- **+ dns_reverse**: Reverse DNS lookup
- **+ snmp_login**: Brute-force SNMP v1/2/3
- **+ ike_enum**: Enumerate IKE transforms
- **+ unzip_pass**: Brute-force the password of encrypted ZIP files
- **+ keystore_pass**: Brute-force the password of Java keystore files
- **+ umbraco_crack**: Crack Umbraco HMAC-SHA1 password hashes
- **+ tcp_fuzz**: Fuzz TCP services
- **+ dummy_test**: Testing module
- ****Installed size**: ** `187 KB`
- ****How to install**: ** `sudo apt install patator`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# patator -h
- **Patator 1.0 (https**: //github.com/lanjelot/patator) with python-3.13.9
- **Usage**: patator module --help
- **Available modules**: []
- **+ rdp_gateway**: Brute-force RDP Gateway
- **+ oracle_login**: Brute-force Oracle
- **+ sqlcipher_pass**: Brute-force the password of SQLCipher-encrypted databases


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## patator Usage Example

Do a MySQL brute force attack (`mysql_login`) with the root user (`user=root`) and passwords contained in a file (`password=FILE0 0=/root/passes.txt`) against the given host (`host=127.0.0.1`), ignoring the specified string (`-x ignore:fgrep=’Access denied for user’`):

```console
root@kali:~# patator mysql_login user=root password=FILE0 0=/root/passes.txt host=127.0.0.1 -x ignore:fgrep='Access denied for user'
12:30:36 patator    INFO - Starting Patator v0.5 (http://code.google.com/p/patator/) at 2014-05-19 12:30 EDT
12:30:36 patator    INFO -
12:30:36 patator    INFO - code  size | candidate                          |   num | mesg
12:30:36 patator    INFO - ----------------------------------------------------------------------
12:30:37 patator    INFO - 0     16   | toor                               |  4493 | 5.5.37-0+wheezy1
12:30:37 patator    INFO - Hits/Done/Skip/Fail/Size: 1/4493/0/0/4493, Avg: 3582 r/s, Time: 0h 0m 1s
```


## Source
- Path: kali-tools\patator\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.040917
