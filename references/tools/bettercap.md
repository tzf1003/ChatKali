---
tool_id: bettercap
title: bettercap
categories: ["sniffing-spoofing", "information-gathering"]
category_slugs: ["sniffing-spoofing", "information-gathering"]
homepage: https://www.bettercap.org
repository: 
version: 2.33.0-1kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-nethunter kali-tools-sniffing-spoofing"]
icon: images/bettercap-logo.svg
source_path: kali-tools\bettercap\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.800737
---

# Tool: bettercap (bettercap)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.bettercap.org](https://www.bettercap.org) |
| Repository |  |
| Version | 2.33.0-1kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-nethunter kali-tools-sniffing-spoofing |
| Icon | images/bettercap-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bettercap
- **PackagesInfo**: |
- **Main Features**: []
- *** More! (https**: //www.bettercap.org/modules/)
- ****Installed size**: ** `27.72 MB`
- ****How to install**: ** `sudo apt install bettercap`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bettercap -h
- **Usage of bettercap**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## bettercap Usage Example

Scan the system in quiet mode (`-Q`) and output in cronjob format (`–cronjob`):

```console
root@kali:~# bettercap
bettercap v2.11 (type 'help' for a list of commands)

172.16.10.0/24 > 172.16.10.212  » [12:34:15] [endpoint.new] endpoint 172.16.10.254 detected as 00:50:56:01:33:70 (VMware, Inc.).
172.16.10.0/24 > 172.16.10.212  » help

           help MODULE : List available commands or show module specific help if no module name is provided.
                active : Show information about active modules.
                  quit : Close the session and exit.
         sleep SECONDS : Sleep for the given amount of seconds.
              get NAME : Get the value of variable NAME, use * alone for all, or NAME* as a wildcard.
        set NAME VALUE : Set the VALUE of variable NAME.
  read VARIABLE PROMPT : Show a PROMPT to ask the user for input that will be saved inside VARIABLE.
                 clear : Clear the screen.
        include CAPLET : Load and run this caplet in the current session.
             ! COMMAND : Execute a shell command and print its output.
        alias MAC NAME : Assign an alias to a given endpoint given its MAC address.

Modules

      any.proxy > not running
       api.rest > not running
      arp.spoof > not running
      ble.recon > not running
        caplets > not running
    dhcp6.spoof > not running
      dns.spoof > not running
  events.stream > running
            gps > not running
     http.proxy > not running
    http.server > not running
    https.proxy > not running
    mac.changer > not running
   mysql.server > not running
      net.probe > not running
      net.recon > running
      net.sniff > not running
   packet.proxy > not running
       syn.scan > not running
      tcp.proxy > not running
         ticker > not running
         update > not running
           wifi > not running
            wol > not running

172.16.10.0/24 > 172.16.10.212  » net.show

+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
|       IP        |        MAC         |  Name    |         Vendor          | Sent    | Recvd  | Last Seen  |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+
| 172.16.10.212   | 00:b0:52:af:4a:50  | eth0     | Atheros Communications  | 0 B     | 0 B     | 12:34:15   |
| 172.16.10.2     | 00:50:56:13:37:0a  | gateway  | VMware, Inc.            | 49 kB   | 20 kB   | 12:34:15   |
|                 |                    |          |                         |         |         |            |
| 172.16.10.254   | 00:50:56:01:33:70  |          | VMware, Inc.            | 2.4 kB  | 2.4 kB  | 12:35:15   |
+-----------------+--------------------+----------+-------------------------+---------+---------+------------+

↑ 0 B / ↓ 3.2 MB / 11354 pkts / 0 errs
```


## Source
- Path: kali-tools\bettercap\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.800737
