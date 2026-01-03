---
tool_id: smbmap
title: smbmap
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://github.com/ShawnDEvans/smbmap
repository: 
version: 1.10.7-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords"]
icon: images/smbmap-logo.svg
source_path: kali-tools\smbmap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.113033
---

# Tool: smbmap (smbmap)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ShawnDEvans/smbmap](https://github.com/ShawnDEvans/smbmap) |
| Repository |  |
| Version | 1.10.7-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords |
| Icon | images/smbmap-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/smbmap
- **PackagesInfo**: |
- **Features**: []
- ****Installed size**: ** `134 KB`
- ****How to install**: ** `sudo apt install smbmap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# smbmap -h
- **usage**: smbmap [-h] (-H HOST | --host-file FILE) [-u USERNAME] [-p PASSWORD |
- **(**: \___/  \   \  //   |(. |_)  :) \   \  //   |    /    \      (. |__) :)
- **\___  \    /\  \/.    ||**: \/   /\   \/.    |   /' /\  \     |:  ____/
- **__/  \   |**: \.        |(|  _  \  |: \.        |  //  __'  \    (|  /
- **/" \**: ) |.  \    /:  ||: |_)  :)|.  \    /:  | /   /  \   \  /|__/ \


## Documentation (Upstream)
--------------------------------------------------------------------------
 SMBMap - Samba Share Enumerator v1.10.7 | Shawn Evans - ShawnDEvans@gmail.com
                      https://github.com/ShawnDEvans/smbmap
 
 options:
   -h, --help            show this help message and exit
 
 Main arguments:
   -H HOST               IP or FQDN
   --host-file FILE      File containing a list of hosts
   -u, --username USERNAME
                         Username, if omitted null session assumed
   -p, --password PASSWORD
                         Password or NTLM hash, format is LMHASH:NTHASH
   --prompt              Prompt for a password
   -s SHARE              Specify a share (default C$), ex 'C$'
   -d DOMAIN             Domain name (default WORKGROUP)
   -P PORT               SMB port (default 445)
   -v, --version         Return the OS version of the remote host
   --signing             Check if host has SMB signing disabled, enabled, or
                         required
   --admin               Just report if the user is an admin
   --no-banner           Removes the banner from the top of the output
   --no-color            Removes the color from output
   --no-update           Removes the "Working on it" message
   --timeout SCAN_TIMEOUT
                         Set port scan socket timeout. Default is .5 seconds
 
 Kerberos settings:
   -k, --kerberos        Use Kerberos authentication
   --no-pass             Use CCache file (export KRB5CCNAME='~/current.ccache')
   --dc-ip IP or Host    IP or FQDN of DC
 
 Command Execution:
   Options for executing commands on the specified host
 
   -x COMMAND            Execute a command ex. 'ipconfig /all'
   --mode CMDMODE        Set the execution method, wmi or psexec, default wmi
 
 Shard drive Search:
   Options for searching/enumerating the share of the specified host(s)
 
   -L                    List all drives on the specified host, requires ADMIN
                         rights.
   -r [PATH]             Recursively list dirs and files (no share\path lists
                         the root of ALL shares), ex. 'email/backup'
   -g FILE               Output to a file in a grep friendly format, used with
                         -r (otherwise it outputs nothing), ex -g grep_out.txt
   --csv FILE            Output to a CSV file, ex --csv shares.csv
   --dir-only            List only directories, ommit files.
   --no-write-check      Skip check to see if drive grants WRITE access.
   -q                    Quiet verbose output. Only shows shares you have READ
                         or WRITE on, and suppresses file listing when
                         performing a search (-A).
   --depth DEPTH         Traverse a directory tree to a specific depth. Default
                         is 1 (root node).
   --exclude SHARE [SHARE ...]
                         Exclude share(s) from searching and listing, ex.
                         --exclude ADMIN$ C$'
   -A PATTERN            Define a file name pattern (regex) that auto downloads
                         a file on a match (requires -r), not case sensitive,
                         ex '(web|global).(asax|config)'
 
 File Content Search:
   Options for searching the content of files (must run as root), kind of experimental
 
   -F PATTERN            File content search, -F '[Pp]assword' (requires admin
                         access to execute commands, and PowerShell on victim
                         host)
   --search-path PATH    Specify drive/path to search (used with -F, default
                         C:\Users), ex 'D:\HR\'
   --search-timeout TIMEOUT
                         Specifcy a timeout (in seconds) before the file search
                         job gets killed. Default is 300 seconds.
 
 Filesystem interaction:
   Options for interacting with the specified host's filesystem
 
   --download PATH       Download a file from the remote system,
                         ex.'C$\temp\passwords.txt'
   --upload SRC DST      Upload a file to the remote system ex.
                         '/tmp/payload.exe C$\temp\payload.exe'
   --delete PATH TO FILE
                         Delete a remote file, ex. 'C$\temp\msf.exe'
   --skip                Skip delete file confirmation prompt
 
 Examples:
 
 $ smbmap -u jsmith -p password1 -d workgroup -H 192.168.0.1
 $ smbmap -u jsmith -p 'aad3b435b51404eeaad3b435b51404ee:da76f2c4c96028b7a6111aef4a50a94d' -H 172.16.0.20
 $ smbmap -u 'apadmin' -p 'asdf1234!' -d ACME -Hh 10.1.3.30 -x 'net group "Domain Admins" /domain'
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## smbmap Usage Examples

Check for shares on the specified host with the username and password provided:

```console
root@kali:~# smbmap -u victim -p s3cr3t -H 192.168.86.61
[+] Finding open SMB ports....
[+] User SMB session establishd on 192.168.86.61...
[+] IP: 192.168.86.61:445   Name: win7-x86.lan
    Disk                                                    Permissions
    ----                                                    -----------
    ADMIN$                                              NO ACCESS
    C$                                                  NO ACCESS
    IPC$                                                NO ACCESS
    Users                                               READ ONLY
```


## Source
- Path: kali-tools\smbmap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.113033
