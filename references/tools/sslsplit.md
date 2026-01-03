---
tool_id: sslsplit
title: sslsplit
categories: ["sniffing-spoofing", "information-gathering"]
category_slugs: ["sniffing-spoofing", "information-gathering"]
homepage: http://www.roe.ch/SSLsplit
repository: 
version: 0.5.5-2.1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-sniffing-spoofing kali-tools-web"]
icon: images/sslsplit-logo.svg
source_path: kali-tools\sslsplit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.127197
---

# Tool: sslsplit (sslsplit)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.roe.ch/SSLsplit](http://www.roe.ch/SSLsplit) |
| Repository |  |
| Version | 0.5.5-2.1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-sniffing-spoofing kali-tools-web |
| Icon | images/sslsplit-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/sslsplit
- **PackagesInfo**: |
- ****Installed size**: ** `255 KB`
- ****How to install**: ** `sudo apt install sslsplit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sslsplit -h
- **Usage**: sslsplit [-D] [-f conffile] [-o opt=val] [options...] [proxyspecs...]
- **-K pemfile  use key from pemfile for leaf certs (default**: generate)
- **matching the common names (non-matching**: -T or generate if CA)
- **client cert auth or no matching cert and no CA (default**: drop)
- **-g pemfile  use DH group params from pemfile (default**: keyfiles or auto)
- **-G curve    use ECDH named curve (default**: prime256v1)
- **-r proto    only support one of tls10 tls11 tls12 (default**: all)
- **-R proto    disable one of tls10 tls11 tls12 (default**: none)
- **-s ciphers  use the given OpenSSL cipher suite spec (default**: ALL:-aNULL)
- **-e engine   specify default NAT engine to use (default**: netfilter)
- **-u user     drop privileges to user (default if run as root**: nobody)
- **-m group    when using -u, override group (default**: primary group of user)
- **-p pidfile  write pid to pidfile (default**: no pid file)
- **-l logfile  connect log**: log one line summary per connection to logfile
- **-L logfile  content log**: full data to file or named pipe (excludes -S/-F)
- **-S logdir   content log**: full data to separate files in dir (excludes -L/-F)
- **-F pathspec content log**: full data to sep files with % subst (excl. -L/-S):
- **-X pcapfile pcap log**: packets to pcapfile (excludes -Y/-y)
- **-Y pcapdir  pcap log**: packets to separate files in dir (excludes -X/-y)
- **-y pathspec pcap log**: packets to sep files with % subst (excl. -X/-Y):
- **-d          daemon mode**: run in background, log error messages to syslog
- **-D          debug mode**: run in foreground, log debug messages on stderr
- **https**: :1 8443 2001:db8::1 443   # https/6; static address dst
- **ssl 2001**: db8::2 9999 pf          # ssl/6; NAT engine 'pf'
- **autossl**: :1 10025                # autossl/6; STARTTLS et al
- **Example**: []
- **sslsplit -k ca.key -c ca.pem -P  https 127.0.0.1 8443  https**: :1 8443


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sslsplit Usage Example

Run in debug mode (`-D`), log the connections (`-l connections.log`), set the chroot jail (`-j /tmp/sslsplit/`), save files to disk (`-S /tmp/`), specify the key (`-k ca.key`), specify the cert (`-c ca.crt`), specify ssl (`ssl`), and configure the proxy (`0.0.0.0 8443 tcp 0.0.0.0 8080`):

```console
root@kali:~# sslsplit -D -l connections.log -j /tmp/sslsplit/ -S /tmp/ -k ca.key -c ca.crt ssl 0.0.0.0 8443 tcp 0.0.0.0 8080
Generated RSA key for leaf certs.
SSLsplit 0.4.6 (built 2013-06-06)
Copyright (c) 2009-2013, Daniel Roethlisberger <daniel@roe.ch>
http://www.roe.ch/SSLsplit
Features: -DDISABLE_SSLV2_SESSION_CACHE -DHAVE_NETFILTER
NAT engines: netfilter* tproxy
netfilter:  IP_TRANSPARENT SOL_IPV6 !IPV6_ORIGINAL_DST
compiled against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
rtlinked against OpenSSL 1.0.1e 11 Feb 2013 (1000105f)
TLS Server Name Indication (SNI) supported
OpenSSL is thread-safe with THREADID
```


## Source
- Path: kali-tools\sslsplit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.127197
