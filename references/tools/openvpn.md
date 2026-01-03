---
tool_id: openvpn
title: openvpn
categories: ["tunneling-exfiltration", "utilities"]
category_slugs: ["tunneling-exfiltration", "utilities"]
homepage: https://openvpn.net/community/
repository: 
version: 2.7.0~rc2-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\openvpn\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.030584
---

# Tool: openvpn (openvpn)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://openvpn.net/community/](https://openvpn.net/community/) |
| Repository |  |
| Version | 2.7.0~rc2-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/openvpn
- **PackagesInfo**: |
- ****Installed size**: ** `1.78 MB`
- ****How to install**: ** `sudo apt install openvpn`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# openvpn --help
- **General Options**: []
- **--config file**: Read configuration options from file.
- **--help**: Show options.
- **--version**: Show copyright and version information.
- **Tunnel Options**: []
- **--local host|* [port]**: Local host name or IP address and port for bind.
- **'all IPv4 addresses' use '0.0.0.0', for 'all IPv6 addresses' use '**: :'.
- **--remote host [port]**: Remote host name or ip address.
- **--remote-random**: If multiple --remote options specified, choose one randomly.
- **--remote-random-hostname**: Add a random string to remote DNS name.
- **--mode m**: Major mode, m = 'p2p' (default, point-to-point) or 'server'.
- **--proto p**: Use protocol p for communicating with peer.
- **--proto-force p**: only consider protocol p in list of connection profiles.
- **--connect-retry n [m]**: For client, number of seconds to wait between
- **--connect-retry-max n**: Maximum connection attempt retries, default infinite.
- **--http-proxy s p [up] [auth]**: Connect to remote host
- **--http-proxy s p 'auto[-nct]'**: Like the above directive, but automatically
- **--http-proxy-option type [parm]**: Set extended HTTP proxy options.
- **--socks-proxy s [p] [up]**: Connect to remote host through a Socks5 proxy at
- **--socks-proxy-retry**: Retry indefinitely on Socks proxy errors.
- **--resolv-retry n**: If hostname resolve fails for --remote, retry
- **--float**: Allow remote to change its IP address/port, such as through
- **--ipchange cmd**: Run command cmd on remote ip address initial
- **setting or change -- execute as**: cmd ip-address port#
- **--port port**: TCP/UDP port # for both local and remote.
- **--lport port**: TCP/UDP port # for local (default=1194). Implies --bind.
- **--rport port**: TCP/UDP port # for remote (default=1194).
- **--bind**: Bind to local address and port. (This is the default unless
- **--nobind**: Do not bind to local address and port.
- **--dev tunX|tapX**: tun/tap device
- **--dev-type dt**: Device type.  See tunnel options above for details.
- **--dev-node node**: Explicitly set the device node rather than using
- **--disable-dco**: Do not attempt using Data Channel Offload.
- **--lladdr hw**: Set the link layer address of the tap device.
- **--topology t**: Set --dev tun topology: 'net30', 'p2p', or 'subnet'.
- **--ifconfig l rn**: TUN: configure device to use IP address l as a local
- **TAP**: configure device to use IP address l as a local
- **--ifconfig-ipv6 l r**: configure device to use IPv6 address l as local
- **--ifconfig-noexec**: Don't actually execute ifconfig/netsh command, instead
- **--ifconfig-nowarn**: Don't warn if the --ifconfig option on this side of the
- **--route-table table_id**: Specify a custom routing table for use with --route(-ipv6).
- **--route network [netmask] [gateway] [metric]**: []
- **netmask default**: 255.255.255.255
- **gateway default**: taken from --route-ipv6-gateway or 'remote'
- **--route-ipv6 network/bits [gateway] [metric]**: []
- **--route-gateway gw|'dhcp'**: Specify a default gateway for use with --route.
- **--route-ipv6-gateway gw**: Specify a default gateway for use with --route-ipv6.
- **--route-metric m**: Specify a default metric for use with --route.
- **--route-delay n [w]**: Delay n seconds after connection initiation before
- **--route-up cmd**: Run command cmd after routes are added.
- **--route-pre-down cmd**: Run command cmd before routes are removed.
- **--route-noexec**: Don't add routes automatically.  Instead pass routes to
- **--route-nopull**: When used with --client or --pull, accept options pushed
- **--allow-pull-fqdn**: Allow client to pull DNS names from server for
- **--redirect-gateway [flags]**: Automatically execute routing
- **--redirect-private [flags]**: Like --redirect-gateway, but omit actually changing
- **--block-ipv6**: (Client) Instead sending IPv6 to the server generate
- **--client-nat snat|dnat network netmask alias**: on client add 1-to-1 NAT rule.
- **--push-peer-info**: (client only) push client info to server.
- **--setenv name value**: Set a custom environmental variable to pass to script.
- **--setenv FORWARD_COMPATIBLE 1**: Relax config file syntax checking to allow
- **--ignore-unknown-option opt1 opt2 ...**: Relax config file syntax. Allow
- **--script-security level**: Where level can be:
- **--shaper n**: Restrict output to peer to n bytes per second.
- **--keepalive n m**: Helper option for setting timeouts in server mode.  Send
- **--inactive n [bytes]**: Exit after n seconds of activity on tun/tap device
- **--session-timeout n**: Limit connection time to n seconds.
- **--ping-exit n**: Exit if n seconds pass without reception of remote ping.
- **--ping-restart n**: Restart if n seconds pass without reception of remote ping.
- **--ping-timer-rem**: Run the --ping-exit/--ping-restart timer only if we have a
- **--ping n**: Ping remote once every n seconds over TCP/UDP port.
- **--multihome**: Configure a multi-homed UDP server.
- **--fast-io**: Optimize TUN/TAP/UDP writes.
- **--remap-usr1 s**: On SIGUSR1 signals, remap signal (s='SIGHUP' or 'SIGTERM').
- **--persist-tun**: Keep tun/tap device open across SIGUSR1 or --ping-restart.
- **--persist-remote-ip**: Keep remote IP address across SIGUSR1 or --ping-restart.
- **--persist-local-ip**: Keep local IP address across SIGUSR1 or --ping-restart.
- **--passtos**: TOS passthrough (applies to IPv4 only).
- **--tun-mtu n**: Take the tun/tap device MTU to be n and derive the
- **--tun-mtu-extra n**: Assume that tun/tap device might return as many
- **--tun-mtu-max n**: Maximum pushable MTU (default and minimum=1600).
- **--link-mtu n**: Take the TCP/UDP device MTU to be n and derive the tun MTU
- **--mtu-disc type**: Should we do Path MTU discovery on TCP/UDP channel?
- **--mtu-test**: Empirically measure and report MTU.
- **--fragment max**: Enable internal datagram fragmentation so that no UDP
- **--mssfix [n]**: Set upper bound on TCP MSS, default = tun-mtu size
- **--sndbuf size**: Set the TCP/UDP send buffer size.
- **--rcvbuf size**: Set the TCP/UDP receive buffer size.
- **--mark value**: Mark encrypted packets being sent with value. The mark value
- **--bind-dev dev**: Bind to the given device when making connection to a peer or
- **--txqueuelen n**: Set the tun/tap TX queue length to n (Linux only).
- **--mlock**: Disable Paging -- ensures key material and tunnel
- **--up cmd**: Run command cmd after successful tun device open.
- **Execute as**: cmd tun/tap-dev tun-mtu link-mtu \
- **--up-delay**: Delay tun/tap open and possible --up script execution
- **--down cmd**: Run command cmd after tun device close.
- **--down-pre**: Run --down command before TUN/TAP close.
- **--up-restart**: Run up/down commands for all restarts including those
- **--user user**: User to set privilege to.
- **--group group**: Group to set privilege to.
- **--chroot dir**: Chroot to this directory after initialization.
- **--cd dir**: Change to this directory before initialization.
- **--daemon [name]**: Become a daemon after initialization.
- **--syslog [name]**: Output to syslog, but do not become a daemon.
- **--log file**: Output log to file which is created/truncated on open.
- **--log-append file**: Append log to file, or create file if nonexistent.
- **--suppress-timestamps**: Don't log timestamps to stdout/stderr.
- **--machine-readable-output**: Always log timestamp, message flags to stdout/stderr.
- **--writepid file**: Write main process ID to file.
- **--nice n**: Change process priority (>0 = lower, <0 = higher).
- **--echo [parms ...]**: Echo parameters to log output.
- **--verb n**: Set output verbosity to n (default=1):
- ****: Use --show-tls to see a list of supported TLS ciphers (suites).
- **--mute n**: Log at most n consecutive messages in the same category.
- **--status file [n]**: Write operational status to file every n seconds.
- **--status-version [n]**: Choose the status file format version number.
- **--disable-occ**: (DEPRECATED) Disable options consistency check between peers.
- **--gremlin mask**: Special stress testing mode (for debugging only).
- **--compress alg**: Use compression algorithm alg
- **--allow-compression**: Specify whether compression should be allowed
- **--comp-lzo**: Use LZO compression -- may add up to 1 byte per
- **--comp-noadapt**: Don't use adaptive compression when --comp-lzo
- **--management ip port [pass]**: Enable a TCP server on ip:port to handle
- **--management-client**: Management interface will connect as a TCP client to
- **--management-query-passwords**: Query management channel for private key
- **--management-query-proxy**: Query management channel for proxy information.
- **--management-query-remote**: Query management channel for --remote directive.
- **--management-hold**: Start OpenVPN in a hibernating state, until a client
- **--management-signal**: Issue SIGUSR1 when management disconnect event occurs.
- **--management-forget-disconnect**: Forget passwords when management disconnect
- **--management-up-down**: Report tunnel up/down events to management interface.
- **--management-log-cache n**: Cache n lines of log file history for usage
- **--management-client-user u**: When management interface is a unix socket, only
- **--management-client-group g**: When management interface is a unix socket, only
- **--management-client-auth**: gives management interface client the responsibility
- **--plugin m [str]**: Load plug-in module m passing str as an argument
- **--vlan-tagging**: Enable 802.1Q-based VLAN tagging.
- **--vlan-accept tagged|untagged|all**: Set VLAN tagging mode. Default is 'all'.
- **--vlan-pvid v**: Sets the Port VLAN Identifier. Defaults to 1.
- **Multi-Client Server options (when --mode server is used)**: []
- **--server network netmask**: Helper option to easily configure server mode.
- **--server-ipv6 network/bits**: Configure IPv6 server mode.
- **--server-bridge [IP netmask pool-start-IP pool-end-IP]**: Helper option to
- **--push "option"**: Push a config file option back to the peer for remote
- **--push-reset**: Don't inherit global push list for specific
- **--push-remove opt**: Remove options matching 'opt' from the push list for
- **--ifconfig-pool start-IP end-IP [netmask]**: Set aside a pool of subnets
- **--ifconfig-pool-persist file [seconds]**: Persist/unpersist ifconfig-pool
- **--ifconfig-ipv6-pool base-IP/bits**: set aside an IPv6 network block
- **--ifconfig-push local remote-netmask**: Push an ifconfig option to remote,
- **--ifconfig-ipv6-push local/bits remote**: Push an ifconfig-ipv6 option to
- **--iroute network [netmask]**: Route subnet to client.
- **--iroute-ipv6 network/bits**: Route IPv6 subnet to client.
- **--disable**: Client is disabled.
- **--override-username**: Overrides the client-specific username to be used.
- **--verify-client-cert [none|optional|require]**: perform no, optional or
- **--username-as-common-name**: For auth-user-pass authentication, use
- **--auth-user-pass-verify cmd method**: Query client for username/password and
- **--auth-user-pass-optional**: Allow connections by clients that don't
- **--no-name-remapping**: (DEPRECATED) Allow Common Name and X509 Subject to include
- **--client-to-client**: Internally route client-to-client traffic.
- **--duplicate-cn**: Allow multiple clients with the same common name to
- **--client-connect cmd**: Run command cmd on client connection.
- **--client-disconnect cmd**: Run command cmd on client disconnection.
- **--client-config-dir dir**: Directory for custom client config files.
- **--ccd-exclusive**: Refuse connection unless custom client config is found.
- **--tmp-dir dir**: Temporary directory, used for --client-connect return file and plugin communication.
- **--hash-size r v**: Set the size of the real address hash table to r and the
- **--bcast-buffers n**: Allocate n broadcast buffers.
- **--tcp-queue-limit n**: Maximum number of queued TCP output packets.
- **--tcp-nodelay**: Macro that sets TCP_NODELAY socket flag on the server
- **--learn-address cmd**: Run command cmd to validate client virtual addresses.
- **--connect-freq n s**: Allow a maximum of n new connections per s seconds.
- **--connect-freq-initial n s**: Allow a maximum of n replies for initial connections attempts per s seconds.
- **--max-clients n**: Allow a maximum of n simultaneously connected clients.
- **--max-routes-per-client n**: Allow a maximum of n internal routes per client.
- **--stale-routes-check n [t]**: Remove routes with a last activity timestamp
- **--explicit-exit-notify [n]**: On exit/restart, send exit signal to
- **--port-share host port [dir]**: When run in TCP mode, proxy incoming HTTPS
- **sessions to a web server at host**: port.  dir specifies an
- **optional directory to write origin IP**: port data.
- **Client options (when connecting to a multi-client server)**: []
- **--client**: Helper option to easily configure client mode.
- **--auth-user-pass [up]**: Authenticate with server using username/password.
- **--pull**: Accept certain config file options from the peer as if they
- **--pull-filter accept|ignore|reject t**: Filter each option received from the
- **--dns server <n> <option> <value> [value ...]**: Configure option for DNS server #n
- **Valid options are**: []
- **address <addr[**: port]> [addr[:port] ...] : server addresses 4/6
- **resolve-domains <domain> [domain ...]**: split domains
- **dnssec <yes|no|optional>**: option to use DNSSEC
- **transport <DoH|DoT>**: query server over HTTPS / TLS
- **sni <domain>**: DNS server name indication
- **--dns search-domains <domain> [domain ...]**: []
- **--dns-updown cmd|force|disable**: Run cmd as user defined dns config command,
- **--auth-retry t**: How to handle auth failures.  Set t to
- **--static-challenge t e [<scrv1|concat>]**: Enable static challenge/response protocol using
- **--connect-timeout n**: when polling possible remote servers to connect to
- **--allow-recursive-routing**: When this option is set, OpenVPN will not drop
- **Data Channel Encryption Options (must be compatible between peers)**: []
- **--auth alg**: Authenticate packets with HMAC using message
- **--cipher alg**: Encrypt packets with cipher algorithm alg.
- **--data-ciphers list**: List of ciphers that are allowed to be negotiated.
- **--engine [name]**: Enable OpenSSL hardware crypto engine functionality.
- **--mute-replay-warnings**: Silence the output of replay warnings to log file.
- **--replay-window n [t]**: Use a replay protection sliding window of size n
- **--replay-persist file**: Persist replay-protection state across sessions
- **--test-crypto**: Run a self-test of crypto features enabled.
- **TLS Key Negotiation Options**: []
- **--tls-server**: Enable TLS and assume server role during TLS handshake.
- **--tls-client**: Enable TLS and assume client role during TLS handshake.
- **--ca file**: Certificate authority file in .pem format containing
- **--capath dir**: A directory of trusted certificates (CAs and CRLs).
- **--dh file**: File containing Diffie Hellman parameters
- **--cert file**: Local certificate in .pem format or a URI -- must be signed
- **--extra-certs file**: one or more PEM certs that complete the cert chain.
- **--key file**: Local private key in .pem format or a URI.
- **--tls-version-min <version> ['or-highest']**: sets the minimum TLS version we
- **--tls-version-max <version>**: sets the maximum TLS version we will use.
- **--pkcs12 file**: PKCS#12 file containing local private key, local certificate
- **--x509-username-field**: Field in x509 certificate containing the username.
- **--verify-hash hash [algo]**: Specify fingerprint for level-1 certificate.
- **--tls-cipher l**: A list l of allowable TLS ciphers separated by : (optional).
- **--tls-ciphersuites l**: A list of allowed TLS 1.3 cipher suites separated by : (optional)
- **--tls-cert-profile p**: Set the allowed certificate crypto algorithm profile
- **--providers l**: A list l of OpenSSL providers to load.
- **--tls-timeout n**: Packet retransmit timeout on TLS control channel
- **--reneg-bytes n**: Renegotiate data chan. key after n bytes sent and recvd.
- **--reneg-pkts n**: Renegotiate data chan. key after n packets sent and recvd.
- **--reneg-sec max [min]**: Renegotiate data chan. key after at most max (default=3600)
- **--hand-window n**: Data channel key exchange must finalize within n seconds
- **--tran-window n**: Transition window -- old key can live this many seconds
- **--single-session**: Allow only one session (reset state on restart).
- **--tls-exit**: Exit on TLS negotiation failure.
- **--tls-auth f [d]**: Add an additional layer of authentication on top of the TLS
- **--tls-crypt key**: Add an additional layer of authenticated encryption on top
- **--tls-crypt-v2 key**: For clients: use key as a client-specific tls-crypt key.
- **For servers**: use key to decrypt client-specific keys.  For
- **key generation (--genkey tls-crypt-v2-client)**: use key to
- **--genkey tls-crypt-v2-client [keyfile] [base64 metadata]**: Generate a
- **--genkey tls-crypt-v2-server [keyfile] [base64 metadata]**: Generate a
- **--tls-crypt-v2-verify cmd**: Run command cmd to verify the metadata of the
- **--askpass [file]**: Get PEM password from controlling tty before we daemonize.
- **--auth-nocache**: Don't cache --askpass or --auth-user-pass passwords.
- **--crl-verify crl ['dir']**: Check peer certificate against a CRL.
- **--tls-verify cmd**: Run command cmd to verify the X509 name of a
- **--verify-x509-name name**: Accept connections only from a host with X509 subject
- **--ns-cert-type t**: (DEPRECATED) Require that peer certificate was signed with
- **--x509-track x**: Save peer X509 attribute x in environment for use by
- **--keying-material-exporter label len**: Save Exported Keying Material (RFC5705)
- **--remote-cert-ku v ...**: Require that the peer certificate was signed with
- **--remote-cert-eku oid**: Require that the peer certificate was signed with
- **--remote-cert-tls t**: Require that peer certificate was signed with explicit
- **PKCS#11 Options**: []
- **--pkcs11-providers provider ...**: PKCS#11 provider to load.
- **--pkcs11-protected-authentication [0|1] ...**: Use PKCS#11 protected authentication
- **--pkcs11-private-mode hex ...**: PKCS#11 private key mode mask.
- **0**: Try  to determine automatically (default).
- **1**: Use Sign.
- **2**: Use SignRecover.
- **4**: Use Decrypt.
- **8**: Use Unwrap.
- **--pkcs11-cert-private [0|1] ...**: Set if login should be performed before
- **--pkcs11-pin-cache seconds**: Number of seconds to cache PIN. The default is -1
- **--pkcs11-id-management**: Acquire identity from management interface.
- **--pkcs11-id serialized-id 'id'**: Identity to use, get using standalone --show-pkcs11-ids
- **SSL Library information**: []
- **--show-ciphers**: Show cipher algorithms to use with --cipher option.
- **--show-digests**: Show message digest algorithms to use with --auth option.
- **--show-engines**: Show hardware crypto accelerator engines (if available).
- **--show-tls**: Show all TLS ciphers (TLS used only as a control channel).
- **Generate a new key**: []
- **--genkey tls-auth file**: Generate a new random key of type and write to file
- **Tun/tap config mode (available with linux 2.4+)**: []
- **--mktun**: Create a persistent tunnel.
- **--rmtun**: Remove a persistent tunnel.
- **PKCS#11 standalone options**: []
- **--show-pkcs11-ids [provider] [cert_private]**: Show PKCS#11 available ids.
- **General Standalone Options**: []
- **--show-gateway [address]**: Show info about gateway [to v4/v6 address].


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\openvpn\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.030584
