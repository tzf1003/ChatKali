---
tool_id: freeradius
title: freeradius
categories: ["system-services"]
category_slugs: ["system-services"]
homepage: http://www.freeradius.org/
repository: 
version: 3.2.8+dfsg-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\freeradius\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.904334
---

# Tool: freeradius (freeradius)

## Categories
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.freeradius.org/](http://www.freeradius.org/) |
| Repository |  |
| Version | 3.2.8+dfsg-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/freeradius
- **PackagesInfo**: |
- **FreeRADIUS is a high-performance RADIUS server with support for**: ['Authentication by local files, SQL, Kerberos, LDAP, PAM, and more.', 'Powerful policy configuration language.', 'Proxying and replicating requests by any criteria.', 'Support for many EAP types; TLS, PEAP, TTLS, etc.', 'Many vendor-specific attributes.', 'Regexp matching in string attributes.']
- ****Installed size**: ** `578 KB`
- ****How to install**: ** `sudo apt install libfreeradius3`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# smbencrypt -h
- **Usage**: rlm_ippool_tool -u <filename> <new-filename>
- **Options**: []
- **Arguments**: []
- **or**: []
- **You can install a custom package which sets "Provides**: freeradius-config" in
- **the FreeRADIUS Server project, including**: ['radclient', 'radcrypt', 'radeapclient', 'radlast', 'radsecret', 'radsniff', 'radsqlrelay', 'radtest', 'radwho', 'radzap', 'rlm_ippool_tool', 'smbencrypt']
- **radclient**: invalid option -- '-'
- **-f <file>[**: <file>]     Read packets from file, not stdin.
- **Unknown option**: h
- **last**: invalid option -- 'h'
- **Commands**: last, boot, boottime, rotate, shutdown, import
- **Options for last**: []
- **--time-format FORMAT  Display timestamps in the specified FORMAT**: []
- **TIME must be in the format "YYYY-MM-DD HH**: MM:SS"
- **Options for boot (writes boot entry to wtmpdb)**: []
- **Options for boottime (print time of last system boot)**: []
- **Options for rotate (exports old entries to wtmpdb_<datetime>))**: []
- **Options for shutdown (writes shutdown time to wtmpdb)**: []
- **Options for import (imports legacy wtmp logs)**: []
- **Generic options**: []
- **options**: []
- **Event may be one of the following**: ['received - a request or response.', 'norsp    - seen for a request.', "rtx      - of a request that we've seen before.", 'noreq    - could be matched with the response.', 'reused   - ID too soon.', 'error    - decoding the packet.']
- **stats options**: []
- **/usr/bin/radsqlrelay version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **The following single-character options are accepted**: []
- **With arguments**: -b -d -f -h -P -p -u
- **Boolean (without arguments)**: -x -1 -?
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
- **usage**: radsqlrelay [options] file_path
- **-1		One-shot mode**: push the file to database and exit.
- **-d sql_driver	Driver to use**: mysql, pg, oracle.
- **radwho**: invalid option -- 'h'
- **-d raddb_directory**: directory where radiusd.conf is located.
- **-D dict_directory**: directory where the dictionaries are located.
- **-N nas_ip_address**: IP address of the NAS to zap.
- **-P nas_port**: NAS port that the user is logged into.
- **-u username**: Name of user to zap (case insensitive).
- **-U username**: like -u, but case-sensitive.
- **-a**: print all active entries
- **-c**: report number of active entries
- **-r**: remove active entries
- **-v**: verbose report of all entries
- **-o**: Assume old database format (nas/port pair, not md5 output)
- **-n**: Mark the entry nasIP/nasPort as having ipaddress
- **-u**: Update old format database to new.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\freeradius\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.904334
