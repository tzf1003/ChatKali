---
tool_id: snmpcheck
title: snmpcheck
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://www.nothink.org/codes/snmpcheck/index.php
repository: 
version: 1.9-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\snmpcheck\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.115141
---

# Tool: snmpcheck (snmpcheck)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.nothink.org/codes/snmpcheck/index.php](http://www.nothink.org/codes/snmpcheck/index.php) |
| Repository |  |
| Version | 1.9-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/snmpcheck
- **PackagesInfo**: |
- ****Installed size**: ** `46 KB`
- ****How to install**: ** `sudo apt install snmpcheck`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# snmp-check -h
- **Usage**: snmp-check [OPTIONS] <target IP address>
- **-p --port**: SNMP port. Default port is 161;
- **-c --community**: SNMP community. Default is public;
- **-v --version**: SNMP version (1,2c). Default is 1;
- **-w --write**: detect write access (separate action by enumeration);
- **-d --disable_tcp**: disable TCP connections enumeration!
- **-t --timeout**: timeout in seconds. Default is 5;
- **-r --retries**: request retries. Default is 1;
- **-i --info**: show script version;
- **-h --help**: show help menu;


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## snmp-check Usage Example

Scan the target host (`192.168.1.2`) using the public SNMP community string (`-c public`):

```console
root@kali:~# snmp-check 192.168.1.2 -c public
snmp-check v1.9 - SNMP enumerator
Copyright (c) 2005-2015 by Matteo Cantoni (www.nothink.org)

[+] Try to connect to 192.168.1.2:161 using SNMPv1 and community 'public'

[*] System information:

  Host IP address               : 192.168.1.2
  Hostname                      : ...retracted...
  Description                   : ...retracted...
  Contact                       : ...retracted...
  Location                      : ...retracted...
  Uptime snmp                   : -
  Uptime system                 : 3 days, 00:13:51.05
  System date                   : -

[*] Network information:

[...]

[*] Network interfaces:

[...]

[*] Network IP:

[...]

[*] Routing information:

[...]

[*] TCP connections and listening ports:

[...]

[*] Listening UDP ports:

[...]

root@kali:~#
```


## Source
- Path: kali-tools\snmpcheck\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.115141
