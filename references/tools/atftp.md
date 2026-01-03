---
tool_id: atftp
title: atftp
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://sourceforge.net/projects/atftp
repository: 
version: 0.8.0-8
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\atftp\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.792520
---

# Tool: atftp (atftp)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sourceforge.net/projects/atftp](https://sourceforge.net/projects/atftp) |
| Repository |  |
| Version | 0.8.0-8 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/atftp
- **PackagesInfo**: |
- ****Installed size**: ** `183 KB`
- ****How to install**: ** `sudo apt install atftpd`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# in.tftpd -h
- **Usage**: tftpd [options] [directory]
- **[options] may be**: []
- **-g, --get**: get file
- **--mget**: get file using mtftp
- **-p, --put**: put file
- **-l, --local-file <file>**: local file name
- **-r, --remote-file <file>**: remote file name
- **-P, --password <password>**: specify password (Linksys extension)
- **--tftp-timeout <value>**: delay before retransmission, client side
- **--option <"name value">**: set option name to value
- **--mtftp <"name value">**: set mtftp variable to value
- **--no-source-port-checking**: violate RFC, see man page
- **--prevent-sas**: prevent Sorcerer's Apprentice Syndrome
- **--verbose**: set verbose mode on
- **--trace**: log all sent and received packets
- **-V, --version**: print version information
- **-h, --help**: print this help
- **-t, --tftpd-timeout <value>**: number of second of inactivity before exiting
- **-r, --retry-timeout <value>**: time to wait a reply before retransmition
- **-m, --maxthread <value>**: number of concurrent thread allowed
- **-v, --verbose [value]**: increase or set the level of output messages
- **--no-timeout**: disable 'timeout' from RFC2349
- **--no-tsize**: disable 'tsize' from RFC2349
- **--no-blksize**: disable 'blksize' from RFC2348
- **--no-windowsize**: disable 'windowsize' from RFC7440
- **--no-multicast**: disable 'multicast' from RFC2090
- **--logfile <file>**: logfile to log logs to ;-) (use - for stdout)
- **--pidfile <file>**: write PID to this file
- **--listen-local**: force listen on local network address
- **--daemon**: run atftpd standalone (no inetd)
- **--no-fork**: run as a daemon, don't fork
- **--user <user[.group]>**: default is nobody
- **--group <group>**: default is nogroup
- **--port <port>**: port on which atftp listen
- **--bind-address <IP>**: local address atftpd listen to
- **--mcast-ttl**: ttl to used for multicast
- **--mcast-addr <address list>**: list/range of IP address to use
- **--mcast-port <port range>**: ports to use for multicast transfer
- **--pcre <file>**: use this file for pattern replacement
- **--pcre-test <file>**: just test pattern file, not starting server
- **--mtftp <file>**: mtftp configuration file
- **--mtftp-port <port>**: port mtftp will listen
- **--mcast-switch-client**: switch client on first timeout, see man page


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\atftp\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.792520
