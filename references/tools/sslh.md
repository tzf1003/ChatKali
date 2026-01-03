---
tool_id: sslh
title: sslh
categories: ["utilities", "tunneling-exfiltration"]
category_slugs: ["utilities", "tunneling-exfiltration"]
homepage: http://www.rutschle.net/tech/sslh/README.html
repository: 
version: 2.1.4-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-post-exploitation kali-tools-web"]
icon: images/sslh-logo.svg
source_path: kali-tools\sslh\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.125698
---

# Tool: sslh (sslh)

## Categories
- [utilities](../utilities.md)
- [tunneling-exfiltration](../tunneling-exfiltration.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.rutschle.net/tech/sslh/README.html](http://www.rutschle.net/tech/sslh/README.html) |
| Repository |  |
| Version | 2.1.4-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-post-exploitation kali-tools-web |
| Icon | images/sslh-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/sslh.git
- **PackagesInfo**: |
- ****Installed size**: ** `513 KB`
- ****How to install**: ** `sudo apt install sslh`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sslh-select -h
- **sslhcfg**: invalid option "-h"
- **[-Vfin] [-F <file>] [--verbose-config=<n>] [--verbose-config-error=<n>] [--verbose-connections=<n>] [--verbose-connections-try=<n>] [--verbose-connections-error=<n>] [--verbose-fd=<n>] [--verbose-packets=<n>] [--verbose-probe-info=<n>] [--verbose-probe-error=<n>] [--verbose-system-error=<n>] [--verbose-int-error=<n>] [--transparent] [-t <n>] [--udp-max-connections=<n>] [-u <str>] [-P <file>] [-C <path>] [--syslog-facility=<str>] [--logfile=<str>] [--on-timeout=<str>] [--prefix=<str>] [-p <host**: port>]... [--ssh=<host:port>]... [--tls=<host:port>]... [--ssl=<host:port>]... [--openvpn=<host:port>]... [--tinc=<host:port>]... [--wireguard=<host:port>]... [--xmpp=<host:port>]... [--http=<host:port>]... [--adb=<host:port>]... [--socks5=<host:port>]... [--syslog=<host:port>]... [--msrdp=<host:port>]... [--anyprot=<host:port>]...
- **-i, --inetd              	Run in inetd mode**: use stdin/stdout instead of network listen
- **-p, --listen=<host**: port> 	Listen on host:port
- **--ssh=<host**: port>        	Set up ssh target
- **--tls=<host**: port>        	Set up TLS/SSL target
- **--ssl=<host**: port>        	Set up TLS/SSL target
- **--openvpn=<host**: port>    	Set up OpenVPN target
- **--tinc=<host**: port>       	Set up tinc target
- **--wireguard=<host**: port>  	Set up WireGuard target
- **--xmpp=<host**: port>       	Set up XMPP target
- **--http=<host**: port>       	Set up HTTP (plain) target
- **--adb=<host**: port>        	Set up ADB (Android Debug) target
- **--socks5=<host**: port>     	Set up socks5 target
- **--syslog=<host**: port>     	Set up syslog target
- **--msrdp=<host**: port>      	Set up msrdp target
- **--anyprot=<host**: port>    	Set up default target


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sslh\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.125698
