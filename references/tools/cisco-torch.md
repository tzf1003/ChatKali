---
tool_id: cisco-torch
title: cisco-torch
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: []
repository: 
version: 0.4b-1kali6
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\cisco-torch\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.845785
---

# Tool: cisco-torch (cisco-torch)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage |  |
| Repository |  |
| Version | 0.4b-1kali6 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/cisco-torch
- **PackagesInfo**: |
- **community.txt list**: -) and TFTP servers (configuration
- ****Installed size**: ** `117 KB`
- ****How to install**: ** `sudo apt install cisco-torch`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# cisco-torch -h
- **usage**: cisco-torch <options> <IP,hostname,network>
- **or**: cisco-torch <options> -F <hostlist>
- **Available options**: []
- **examples**: cisco-torch -A 10.10.0.0/16


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## cisco-torch Usage Example

Run all available scan types (`-A`) against the target IP address (`192.168.99.202`):

```console
root@kali:~# cisco-torch -A 192.168.99.202
Using config file torch.conf...
Loading include and plugin ...

###############################################################
#   Cisco Torch Mass Scanner                   #
#   Becase we need it...                                      #
#   http://www.arhont.com/cisco-torch.pl                      #
###############################################################

List of targets contains 1 host(s)
8853:   Checking 192.168.99.202 ...
HUH db not found, it should be in fingerprint.db
Skipping Telnet fingerprint
* Cisco by SNMP found ***
*System Description: Cisco Internetwork Operating System Software
IOS (tm) 3600 Software (C3640-IK9O3S-M), Version 12.3(22), RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2007 by cisco Systems, Inc.
Compiled Wed 24-Jan-07 1

Cisco-IOS Webserver found
 HTTP/1.1 401 Unauthorized
Date: Tue, 13 Apr 1993 00:57:07 GMT
Server: cisco-IOS
Accept-Ranges: none
WWW-Authenticate: Basic realm="level_15_access"

401 Unauthorized


 Cisco WWW-Authenticate webserver found
 HTTP/1.1 401 Unauthorized
Date: Tue, 13 Apr 1993 00:57:07 GMT
Server: cisco-IOS
Accept-Ranges: none
WWW-Authenticate: Basic realm="level_15_access"

401 Unauthorized


--->
- All scans done. Cisco Torch Mass Scanner  -
---> Exiting.
```


## Source
- Path: kali-tools\cisco-torch\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.845785
