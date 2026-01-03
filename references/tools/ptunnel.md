---
tool_id: ptunnel
title: ptunnel
categories: ["tunneling-exfiltration", "utilities"]
category_slugs: ["tunneling-exfiltration", "utilities"]
homepage: http://www.mit.edu/afs.new/sipb/user/golem/tmp/ptunnel-0.61.orig/web/
repository: 
version: 0.72-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-post-exploitation"]
icon: images/ptunnel-logo.svg
source_path: kali-tools\ptunnel\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.060252
---

# Tool: ptunnel (ptunnel)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.mit.edu/afs.new/sipb/user/golem/tmp/ptunnel-0.61.orig/web/](http://www.mit.edu/afs.new/sipb/user/golem/tmp/ptunnel-0.61.orig/web/) |
| Repository |  |
| Version | 0.72-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-post-exploitation |
| Icon | images/ptunnel-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/alteholz/ptunnel
- **PackagesInfo**: |
- ****Installed size**: ** `133 KB`
- ****How to install**: ** `sudo apt install ptunnel`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ptunnel -h
- **Usage**: ptunnel -p <addr> -lp <port> -da <dest_addr> -dp <dest_port> [-m max_tunnels] [-v verbosity] [-f logfile]
- **-p**: Set address of peer running packet forwarder. This causes
- **-lp**: Set TCP listening port (only used when operating in forward mode)
- **-da**: Set remote proxy destination address if client
- **-dp**: Set remote proxy destionation port if client
- **-m**: Set maximum number of concurrent tunnels
- **-v**: Verbosity level (-1 to 4, where -1 is no output, and 4 is all output)
- **-c**: Enable libpcap on the given device.
- **-f**: Specify a file to log to, rather than printing to standard out.
- **-s**: Client only. Enables continuous output of statistics (packet loss, etc.)
- **-daemon**: Run in background, the PID will be written in the file supplied as argument
- **-syslog**: Output debug to syslog instead of standard out.
- **-udp**: Toggle use of UDP instead of ICMP. Proxy will listen on port 53 (must be root).
- **Security features**: ['-x password] [-u] [-setuid user] [-setgid group] [-chroot dir']
- **-x**: Set password (must be same on client and proxy)
- **-u**: Run proxy in unprivileged mode. This causes the proxy to forward
- **Please consider combining the following three options instead**: []
- **-setuid**: When started in privileged mode, drop down to user's rights as soon as possible
- **-setgid**: When started in privileged mode, drop down to group's rights as soon as possible
- **-chroot**: When started in privileged mode, restrict file access to the specified directory
- **-setcon**: Set SELinux context when all there is left to do are network I/O operations
- **Starting the proxy (needs to run as root)**: []
- **Starting a client (also needs root)**: []
- **And then using the tunnel to ssh to login.domain.com**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\ptunnel\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.060252
