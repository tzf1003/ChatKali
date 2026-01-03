---
tool_id: responder
title: responder
categories: ["sniffing-spoofing", "information-gathering"]
category_slugs: ["sniffing-spoofing", "information-gathering"]
homepage: https://github.com/lgandx/Responder
repository: 
version: 3.1.7.0-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing kali-tools-top10"]
icon: images/responder-logo.svg
source_path: kali-tools\responder\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.080682
---

# Tool: responder (responder)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/lgandx/Responder](https://github.com/lgandx/Responder) |
| Repository |  |
| Version | 3.1.7.0-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-sniffing-spoofing kali-tools-top10 |
| Icon | images/responder-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/responder
- **PackagesInfo**: |
- **based on their name suffix (see**: http://support.microsoft.com/kb/163409). By
- ****Installed size**: ** `4.08 MB`
- ****How to install**: ** `sudo apt install responder`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# responder -h


## Documentation (Upstream)
-.-----.-----.-----.-----.-----.--|  |.-----.----.
   |   _|  -__|__ --|  _  |  _  |     |  _  ||  -__|   _|
   |__| |_____|_____|   __|_____|__|__|_____||_____|__|
                    |__|
 
 Usage: responder -I eth0 -w -d
 or:
 responder -I eth0 -wd
 
 Options:
   --version             show program's version number and exit
   -h, --help            show this help message and exit
   -A, --analyze         Analyze mode. This option allows you to see NBT-NS,
                         BROWSER, LLMNR requests without responding.
   -I eth0, --interface=eth0
                         Network interface to use, you can use 'ALL' as a
                         wildcard for all interfaces
   -i 10.0.0.21, --ip=10.0.0.21
                         Local IP to use (only for OSX)
   -6 2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed, --externalip6=2002:c0a8:f7:1:3ba8:aceb:b1a9:81ed
                         Poison all requests with another IPv6 address than
                         Responder's one.
   -e 10.0.0.22, --externalip=10.0.0.22
                         Poison all requests with another IP address than
                         Responder's one.
   -b, --basic           Return a Basic HTTP authentication. Default: NTLM
   -d, --DHCP            Enable answers for DHCP broadcast requests. This
                         option will inject a WPAD server in the DHCP response.
                         Default: False
   -D, --DHCP-DNS        This option will inject a DNS server in the DHCP
                         response, otherwise a WPAD server will be added.
                         Default: False
   -w, --wpad            Start the WPAD rogue proxy server. Default value is
                         False
   -u UPSTREAM_PROXY, --upstream-proxy=UPSTREAM_PROXY
                         Upstream HTTP proxy used by the rogue WPAD Proxy for
                         outgoing requests (format: host:port)
   -F, --ForceWpadAuth   Force NTLM/Basic authentication on wpad.dat file
                         retrieval. This may cause a login prompt. Default:
                         False
   -P, --ProxyAuth       Force NTLM (transparently)/Basic (prompt)
                         authentication for the proxy. WPAD doesn't need to be
                         ON. This option is highly effective. Default: False
   -Q, --quiet           Tell Responder to be quiet, disables a bunch of
                         printing from the poisoners. Default: False
   --lm                  Force LM hashing downgrade for Windows XP/2003 and
                         earlier. Default: False
   --disable-ess         Force ESS downgrade. Default: False
   -v, --verbose         Increase verbosity.
   -t 1e, --ttl=1e       Change the default Windows TTL for poisoned answers.
                         Value in hex (30 seconds = 1e). use '-t random' for
                         random TTL
   -N ANSWERNAME, --AnswerName=ANSWERNAME
                         Specifies the canonical name returned by the LLMNR
                         poisoner in its Answer section. By default, the
                         answer's canonical name is the same as the query.
                         Changing this value is mainly useful when attempting
                         to perform Kerberos relaying over HTTP.
   -E, --ErrorCode       Changes the error code returned by the SMB server to
                         STATUS_LOGON_FAILURE. By default, the status is
                         STATUS_ACCESS_DENIED. Changing this value permits to
                         obtain WebDAV authentications from the poisoned
                         machines where the WebClient service is running.
 ```
 
 - - -
 
 ##### responder-BrowserListener
 
 
 
 - - -
 
 ##### responder-DHCP_Auto
 
 
 
 - - -
 
 ##### responder-FindSQLSrv
 
 
 
 - - -
 
 ##### responder-Icmp-Redirect
 
 
 ```
 root@kali:~# responder-Icmp-Redirect -h
 Usage: responder-Icmp-Redirect -I eth0 -i 10.20.30.40 -g 10.20.30.254 -t 10.20.30.48 -r 10.20.40.1
 
 Options:
   -h, --help            show this help message and exit
   -i 10.20.30.40, --ip=10.20.30.40
                         The ip address to redirect the traffic to. (usually
                         yours)
   -g 10.20.30.254, --gateway=10.20.30.254
                         The ip address of the original gateway (issue the
                         command 'route -n' to know where is the gateway
   -t 10.20.30.48, --target=10.20.30.48
                         The ip address of the target
   -r 10.20.40.1, --route=10.20.40.1
                         The ip address of the destination target, example: DNS
                         server. Must be on another subnet.
   -s 10.20.40.1, --secondaryroute=10.20.40.1
                         The ip address of the destination target, example:
                         Secondary DNS server. Must be on another subnet.
   -I eth0, --interface=eth0
                         Interface name to use, example: eth0
   -a 10.20.30.40, --alternate=10.20.30.40
                         The alternate gateway, set this option if you wish to
                         redirect the victim traffic to another host than yours
 ```
 
 - - -
 
 ##### responder-MultiRelay
 
 
 ```
 root@kali:~# responder-MultiRelay -h
 [!]MultiRelay/bin/ folder is empty. You need to run these commands:
 
 apt-get install gcc-mingw-w64-x86-64
 x86_64-w64-mingw32-gcc ./MultiRelay/bin/Runas.c -o ./MultiRelay/bin/Runas.exe -municode -lwtsapi32 -luserenv
 x86_64-w64-mingw32-gcc ./MultiRelay/bin/Syssvc.c -o ./MultiRelay/bin/Syssvc.exe -municode
 
 Additionally, you can add your custom mimikatz executables (mimikatz.exe and mimikatz_x86.exe)
 in the MultiRelay/bin/ folder for the mimi32/mimi command.
 ```
 
 - - -
 
 ##### responder-RunFinger
 
 
 ```
 root@kali:~# responder-RunFinger -h
 Usage: responder-RunFinger -i 10.10.10.224
 or:
 responder-RunFinger -i 10.10.10.0/24
 
 Options:
   --version             show program's version number and exit
   -h, --help            show this help message and exit
   -i 10.10.10.224, --ip=10.10.10.224
                         Target IP address or class C
   -f ips.txt, --filename=ips.txt
                         Target file
   -t 0.9, --timeout=0.9
                         Timeout for all connections. Use this option to fine
                         tune Runfinger.
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## responder Usage Example

Specify the IP address to redirect to (`-i 192.168.1.202`), enabling the WPAD rogue proxy (`-w On`), answers for netbios wredir (`-r On`), and fingerprinting (`-f On`):

```console
root@kali:~# responder -i 192.168.1.202 -w On -r On -f On
NBT Name Service/LLMNR Responder 2.0.
Please send bugs/comments to: lgaffie@trustwave.com
To kill this script hit CRTL-C

[+]NBT-NS &amp; LLMNR responder started
[+]Loading Responder.conf File..
Global Parameters set:
Responder is bound to this interface:ALL
Challenge set is:1122334455667788
WPAD Proxy Server is:ON
WPAD script loaded:function FindProxyForURL(url, host){if ((host == "localhost") || shExpMatch(host, "localhost.*") ||(host == "127.0.0.1") || isPlainHostName(host)) return "DIRECT"; if (dnsDomainIs(host, "RespProxySrv")||shExpMatch(host, "(*.RespProxySrv|RespProxySrv)")) return "DIRECT"; return 'PROXY ISAProxySrv:3141; DIRECT';}
HTTP Server is:ON
HTTPS Server is:ON
SMB Server is:ON
SMB LM support is set to:OFF
SQL Server is:ON
FTP Server is:ON
IMAP Server is:ON
POP3 Server is:ON
SMTP Server is:ON
DNS Server is:ON
LDAP Server is:ON
FingerPrint Module is:ON
Serving Executable via HTTP&amp;WPAD is:OFF
Always Serving a Specific File via HTTP&amp;WPAD is:OFF
```


## Source
- Path: kali-tools\responder\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.080682
