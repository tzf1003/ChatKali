---
tool_id: socat
title: socat
categories: ["utilities", "tunneling-exfiltration"]
category_slugs: ["utilities", "tunneling-exfiltration"]
homepage: https://www.dest-unreach.org/socat/
repository: 
version: 1.8.0.3-1
architectures: linux-any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-tools-web"]
icon: images/socat-logo.svg
source_path: kali-tools\socat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.116680
---

# Tool: socat (socat)

## Categories
- [utilities](../utilities.md)
- [tunneling-exfiltration](../tunneling-exfiltration.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.dest-unreach.org/socat/](https://www.dest-unreach.org/socat/) |
| Repository |  |
| Version | 1.8.0.3-1 |
| Architectures | linux-any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-tools-web |
| Icon | images/socat-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `1.75 MB`
- ****How to install**: ** `sudo apt install socat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# socat1 -h
- **filan by Gerhard Rieger and contributors - see http**: //www.dest-unreach.org/socat/
- **Usage**: []
- **options**: []
- **-n<fdnum>      analyze all fds from 0 up to fdnum-1 (default**: 1024)
- **-o<filename>   output goes to filename, that can be**: []
- **options (general command line options)**: []
- **-d0|1|2|3|4    set verbosity level (0**: Errors; 4 all including Debug)
- **bi-address**: /* is an address that may act both as data sync and source */
- **single-address**: []
- **address-head**: []
- **ABSTRACT-CLIENT**: <filename>		groups=FD,SOCKET,RETRY,UNIX
- **ABSTRACT-CONNECT**: <filename>		groups=FD,SOCKET,RETRY,UNIX
- **ABSTRACT-LISTEN**: <filename>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,UNIX
- **ABSTRACT-RECV**: <filename>			groups=FD,SOCKET,RETRY,UNIX
- **ABSTRACT-RECVFROM**: <filename>		groups=FD,SOCKET,CHILD,RETRY,UNIX
- **ABSTRACT-SENDTO**: <filename>		groups=FD,SOCKET,RETRY,UNIX
- **ACCEPT-FD**: <fdnum>				groups=FD,SOCKET,CHILD,RETRY,RANGE,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
- **CREATE**: <filename>				groups=FD,REG,NAMED
- **DCCP-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,DCCP
- **DCCP-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,DCCP
- **DCCP4-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,DCCP
- **DCCP4-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,DCCP
- **DCCP6-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,DCCP
- **DCCP6-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,DCCP
- **EXEC**: <command-line>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
- **FD**: <fdnum>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,TERMIOS,UNIX,IP4,IP6,UDP,TCP,SCTP,DCCP,UDPLITE
- **GOPEN**: <filename>				groups=FD,FIFO,CHR,BLK,REG,SOCKET,NAMED,OPEN,TERMIOS,UNIX
- **INTERFACE**: <interface>			groups=FD,SOCKET,INTERFACE
- **IP-DATAGRAM**: <host>:<protocol>		groups=FD,SOCKET,RANGE,IP4,IP6
- **IP-RECV**: <protocol>			groups=FD,SOCKET,RANGE,IP4,IP6
- **IP-RECVFROM**: <protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6
- **IP-SENDTO**: <host>:<protocol>		groups=FD,SOCKET,IP4,IP6
- **IP4-DATAGRAM**: <host>:<protocol>		groups=FD,SOCKET,RANGE,IP4
- **IP4-RECV**: <protocol>			groups=FD,SOCKET,RANGE,IP4
- **IP4-RECVFROM**: <protocol>			groups=FD,SOCKET,CHILD,RANGE,IP4
- **IP4-SENDTO**: <host>:<protocol>		groups=FD,SOCKET,IP4
- **IP6-DATAGRAM**: <host>:<protocol>		groups=FD,SOCKET,RANGE,IP6
- **IP6-RECV**: <protocol>			groups=FD,SOCKET,RANGE,IP6
- **IP6-RECVFROM**: <protocol>			groups=FD,SOCKET,CHILD,RANGE,IP6
- **IP6-SENDTO**: <host>:<protocol>		groups=FD,SOCKET,IP6
- **OPEN**: <filename>				groups=FD,FIFO,CHR,BLK,REG,NAMED,OPEN,TERMIOS
- **OPENSSL**: <host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,OPENSSL
- **OPENSSL-DTLS-CLIENT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,UDP,OPENSSL
- **OPENSSL-DTLS-SERVER**: <port>		groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,UDP,OPENSSL
- **OPENSSL-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP,OPENSSL
- **PIPE[**: <filename>]				groups=FD,FIFO,NAMED,OPEN
- **POSIXMQ-BIDIRECTIONAL**: <mqname>		groups=FD,NAMED,OPEN,RETRY,POSIXMQ
- **POSIXMQ-READ**: <mqname>			groups=FD,NAMED,OPEN,RETRY,POSIXMQ
- **POSIXMQ-RECEIVE**: <mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
- **POSIXMQ-SEND**: <mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
- **POSIXMQ-WRITE**: <mqname>			groups=FD,NAMED,OPEN,CHILD,RETRY,POSIXMQ
- **PROXY**: <proxy-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,HTTP
- **SCTP-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,SCTP
- **SCTP-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,SCTP
- **SCTP4-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,SCTP
- **SCTP4-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,SCTP
- **SCTP6-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,SCTP
- **SCTP6-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,SCTP
- **SHELL**: <shell-command>			groups=FD,FIFO,SOCKET,EXEC,FORK,SHELL,TERMIOS,PTY,PARENT,UNIX
- **SOCKET-CONNECT**: <domain>:<protocol>:<remote-address>	groups=FD,SOCKET,CHILD,RETRY
- **SOCKET-DATAGRAM**: <domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET,RANGE
- **SOCKET-LISTEN**: <domain>:<protocol>:<local-address>	groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE
- **SOCKET-RECV**: <domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,RANGE
- **SOCKET-RECVFROM**: <domain>:<type>:<protocol>:<local-address>	groups=FD,SOCKET,CHILD,RANGE
- **SOCKET-SENDTO**: <domain>:<type>:<protocol>:<remote-address>	groups=FD,SOCKET
- **SOCKETPAIR**: <filename>			groups=FD,SOCKET
- **SOCKS4**: <socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
- **SOCKS4A**: <socks-server>:<host>:<port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
- **SOCKS5-CONNECT**: <socks-server>[:<socks-port>]:<target-host>:<target-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
- **SOCKS5-LISTEN**: <socks-server>[:<socks-port>]:<listen-host>:<listen-port>	groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP,SOCKS
- **SYSTEM**: <shell-command>			groups=FD,FIFO,SOCKET,EXEC,FORK,TERMIOS,PTY,PARENT,UNIX
- **TCP-CONNECT**: <host>:<port>			groups=FD,SOCKET,CHILD,RETRY,IP4,IP6,TCP
- **TCP-LISTEN**: <port>				groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,IP6,TCP
- **TCP4-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP4,TCP
- **TCP4-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP4,TCP
- **TCP6-CONNECT**: <host>:<port>		groups=FD,SOCKET,CHILD,RETRY,IP6,TCP
- **TCP6-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY,RANGE,IP6,TCP
- **TUN[**: <ip-addr>/<bits>]			groups=FD,CHR,OPEN,INTERFACE
- **UDP-CONNECT**: <host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
- **UDP-DATAGRAM**: <host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP
- **UDP-LISTEN**: <port>				groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP
- **UDP-RECV**: <port>				groups=FD,SOCKET,RANGE,IP4,IP6,UDP
- **UDP-RECVFROM**: <port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP
- **UDP-SENDTO**: <host>:<port>			groups=FD,SOCKET,IP4,IP6,UDP
- **UDP4-CONNECT**: <host>:<port>		groups=FD,SOCKET,IP4,UDP
- **UDP4-DATAGRAM**: <host>:<port>		groups=FD,SOCKET,RANGE,IP4,UDP
- **UDP4-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP
- **UDP4-RECV**: <port>				groups=FD,SOCKET,RANGE,IP4,UDP
- **UDP4-RECVFROM**: <port>			groups=FD,SOCKET,CHILD,RANGE,IP4,UDP
- **UDP4-SENDTO**: <host>:<port>			groups=FD,SOCKET,IP4,UDP
- **UDP6-CONNECT**: <host>:<port>		groups=FD,SOCKET,IP6,UDP
- **UDP6-DATAGRAM**: <host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP
- **UDP6-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP
- **UDP6-RECV**: <port>				groups=FD,SOCKET,RANGE,IP6,UDP
- **UDP6-RECVFROM**: <port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP
- **UDP6-SENDTO**: <host>:<port>			groups=FD,SOCKET,IP6,UDP
- **UDPLITE-CONNECT**: <host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
- **UDPLITE-DATAGRAM**: <host>:<port>		groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
- **UDPLITE-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
- **UDPLITE-RECV**: <port>			groups=FD,SOCKET,RANGE,IP4,IP6,UDP,UDPLITE
- **UDPLITE-RECVFROM**: <port>			groups=FD,SOCKET,CHILD,RANGE,IP4,IP6,UDP,UDPLITE
- **UDPLITE-SENDTO**: <host>:<port>		groups=FD,SOCKET,IP4,IP6,UDP,UDPLITE
- **UDPLITE4-CONNECT**: <host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
- **UDPLITE4-DATAGRAM**: <remote-address>:<port>	groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
- **UDPLITE4-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP4,UDP,UDPLITE
- **UDPLITE4-RECV**: <port>			groups=FD,SOCKET,RANGE,IP4,UDP,UDPLITE
- **UDPLITE4-RECVFROM**: <host>:<port>		groups=FD,SOCKET,CHILD,RANGE,IP4,UDP,UDPLITE
- **UDPLITE4-SENDTO**: <host>:<port>		groups=FD,SOCKET,IP4,UDP,UDPLITE
- **UDPLITE6-CONNECT**: <host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
- **UDPLITE6-DATAGRAM**: <host>:<port>		groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
- **UDPLITE6-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RANGE,IP6,UDP,UDPLITE
- **UDPLITE6-RECV**: <port>			groups=FD,SOCKET,RANGE,IP6,UDP,UDPLITE
- **UDPLITE6-RECVFROM**: <port>			groups=FD,SOCKET,CHILD,RANGE,IP6,UDP,UDPLITE
- **UDPLITE6-SENDTO**: <host>:<port>		groups=FD,SOCKET,IP6,UDP,UDPLITE
- **UNIX-CLIENT**: <filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
- **UNIX-CONNECT**: <filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
- **UNIX-LISTEN**: <filename>			groups=FD,SOCKET,NAMED,LISTEN,CHILD,RETRY,UNIX
- **UNIX-RECV**: <filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
- **UNIX-RECVFROM**: <filename>			groups=FD,SOCKET,NAMED,CHILD,RETRY,UNIX
- **UNIX-SENDTO**: <filename>			groups=FD,SOCKET,NAMED,RETRY,UNIX
- **VSOCK-CONNECT**: <cid>:<port>		groups=FD,SOCKET,CHILD,RETRY
- **VSOCK-LISTEN**: <port>			groups=FD,SOCKET,LISTEN,CHILD,RETRY
- **<options>**: []
- **For example**: []
- **TCP4-L**: 1234,reuseaddr,fork \
- **TCP-L**: 1234
- **Example to drive SOCKS over TLS**: []
- **SOCKS**: :<server>:<port> \
- **Clients that connect to port 1234 will be forwarded to <server>**: <port> using socks
- **Example**: []
- **/usr/bin/socat-mux.sh TCP4-L**: 1234,reuseaddr,fork TCP:10.2.3.4:12345


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\socat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.116680
