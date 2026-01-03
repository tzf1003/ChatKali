---
tool_id: firewalk
title: firewalk
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: http://packetfactory.openwall.net/projects/firewalk/
repository: 
version: 5.0-6
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-information-gathering"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\firewalk\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.900432
---

# Tool: firewalk (firewalk)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://packetfactory.openwall.net/projects/firewalk/](http://packetfactory.openwall.net/projects/firewalk/) |
| Repository |  |
| Version | 5.0-6 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-information-gathering |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/firewalk
- **PackagesInfo**: |
- ****Installed size**: ** `51 KB`
- ****How to install**: ** `sudo apt install firewalk`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# firewalk --help
- **firewalk**: invalid option -- '-'
- **Usage**: firewalk [options] target_gateway metric


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## firewalk Usage Example

Scan ports 8079-8081 (`-S8079-8081`) through the eth0 interface (`-i eth0`), do not resolve hostnames (`-n`), use TCP (`-pTCP`) via the gateway (`192.168.1.1`) against the target IP (`192.168.0.1`):

```console
root@kali:~# firewalk -S8079-8081  -i eth0 -n -pTCP 192.168.1.1 192.168.0.1
Firewalk 5.0 [gateway ACL scanner]
Firewalk state initialization completed successfully.
TCP-based scan.
Ramping phase source port: 53, destination port: 33434
Hotfoot through 192.168.1.1 using 192.168.0.1 as a metric.
Ramping Phase:
 1 (TTL  1): expired [192.168.1.1]
Binding host reached.
Scan bound at 2 hops.
Scanning Phase:
port 8079: *no response*
port 8080: A! open (port not listen) [192.168.0.1]
port 8081: *no response*

Scan completed successfully.

Total packets sent:                4
Total packet errors:               0
Total packets caught               2
Total packets caught of interest   2
Total ports scanned                3
Total ports open:                  1
Total ports unknown:               0
```


## Source
- Path: kali-tools\firewalk\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.900432
