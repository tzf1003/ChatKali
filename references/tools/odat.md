---
tool_id: odat
title: odat
categories: ["information-gathering", "vulnerability-analysis", "exploitation-tools", "post-exploitation", "password-attacks", "sniffing-spoofing"]
category_slugs: ["information-gathering", "vulnerability-analysis", "exploitation-tools", "post-exploitation", "password-attacks", "sniffing-spoofing"]
homepage: https://github.com/quentinhardy/odat
repository: 
version: 5.1.1-0kali4
architectures: i386 amd64
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\odat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.022898
---

# Tool: odat (odat)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)
- [password-attacks](../password-attacks.md)
- [sniffing-spoofing](../sniffing-spoofing.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/quentinhardy/odat](https://github.com/quentinhardy/odat) |
| Repository |  |
| Version | 5.1.1-0kali4 |
| Architectures | i386 amd64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/odat
- **PackagesInfo**: |
- **Usage examples of ODAT**: []
- ****Installed size**: ** `511 KB`
- ****How to install**: ** `sudo apt install odat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# odat -h
- **usage**: odat.py [-h] [--version]


## Documentation (Upstream)
----------------------------------------
   _        __           _           ___ 
  / \      |  \         / \         |_ _|
 ( o )       o )         o |         | | 
  \_/racle |__/atabase |_n_|ttacking |_|ool 
 -------------------------------------------
 
 By Quentin Hardy (quentin.hardy@protonmail.com or quentin.hardy@bt.com)
 
 positional arguments:
   {all,tnscmd,tnspoison,sidguesser,snguesser,passwordguesser,utlhttp,httpuritype,utltcp,ctxsys,externaltable,dbmsxslprocessor,dbmsadvisor,utlfile,dbmsscheduler,java,passwordstealer,oradbg,dbmslob,stealremotepwds,userlikepwd,smb,privesc,cve,search,unwrapper,clean}
                       
                       Choose a main command
     all               to run all modules in order to know what it is possible to do
     tnscmd            to communicate with the TNS listener
     tnspoison         to exploit TNS poisoning attack (SID required)
     sidguesser        to know valid SIDs
     snguesser         to know valid Service Name(s)
     passwordguesser   to know valid credentials
     utlhttp           to send HTTP requests or to scan ports
     httpuritype       to send HTTP requests or to scan ports
     utltcp            to scan ports
     ctxsys            to read files
     externaltable     to read files or to execute system commands/scripts
     dbmsxslprocessor  to upload files
     dbmsadvisor       to upload files
     utlfile           to download/upload/delete files
     dbmsscheduler     to execute system commands without a standard output
     java              to execute system commands
     passwordstealer   to get hashed Oracle passwords
     oradbg            to execute a bin or script
     dbmslob           to download files
     stealremotepwds   to steal hashed passwords thanks an authentication sniffing (CVE-2012-3137)
     userlikepwd       to try each Oracle username stored in the DB like the corresponding pwd
     smb               to capture the SMB authentication
     privesc           to gain elevated access
     cve               to exploit a CVE
     search            to search in databases, tables and columns
     unwrapper         to unwrap PL/SQL source code (no for 9i version)
     clean             clean traces and logs
 
 options:
   -h, --help          show this help message and exit
   --version           show program's version number and exit
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\odat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.022898
