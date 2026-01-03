---
tool_id: freerdp2
title: freerdp2
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.freerdp.com/
repository: 
version: 2.11.7+dfsg1-4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-passwords"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\freerdp2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.905306
---

# Tool: freerdp2 (freerdp2)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.freerdp.com/](https://www.freerdp.com/) |
| Repository |  |
| Version | 2.11.7+dfsg1-4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-passwords |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://salsa.debian.org/debian-remote-team/freerdp2
- **PackagesInfo**: |
- ****Installed size**: ** `172 KB`
- ****How to install**: ** `sudo apt install winpr-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# winpr-makecert -h
- **[04**: 14:41:636] [270310:270310] [INFO][com.freerdp.server.shadow] - 	Print help
- **Currently, the FreeRDP clients supports the following Windows Versions**: []
- **wlfreerdp  [file]  [default_client_options]  [/v**: <server>[:port]] [/ver-
- **/v**: server[:port]
- **Currently, the FreeRDP client supports the following Windows Versions**: []
- **xfreerdp [file] [options] [/v**: server[:port]]
- **/a**: addin[,options], /addin:addin[,options]
- **/action-script**: file-name
- **Action script (default**: ~/.config/freerdp/action.sh)
- **desktop composition (default**: off)
- **/app**: path or ||alias
- **/app-cmd**: parameters
- **/app-file**: file-name
- **/app-guid**: app-guid
- **/app-icon**: icon-path
- **/app-name**: app-name
- **/app-workdir**: workspace path
- **/assistance**: password
- **/auto-request-control**: []
- **Asynchronous channels (experimental) (default**: off)
- **Asynchronous input (default**: off)
- **Asynchronous update (default**: off)
- **/audio-mode**: mode
- **Authenticate only (default**: off)
- **Authentication (experimental) (default**: on)
- **Automatic reconnection (default**: off)
- **/auto-reconnect-max-retries**: retries
- **bitmap cache (default**: off)
- **/bpp**: depth
- **Session bpp (color depth) (default**: 16)
- **/cert**: [deny,ignore,name:name,tofu,fingerprint:hash:hash as
- **hex[,fingerprint**: hash:another hash]]
- **[deprecated, use /cert**: tofu] Automatically accept certificate on
- **/cert-name**: name
- **/client-build-number**: number
- **/client-hostname**: name
- **/clipboard**: ['use-selection:atom']
- **Redirect clipboard. * use-selection**: <atom> ... (X11) Specify which X
- **middle-click selection. (default**: on)
- **/codec-cache**: ['rfx|nsc|jpeg']
- **compression (default**: on)
- **/compression-level**: level
- **credentials delegation (default**: off)
- **/d**: domain
- **Window decorations (default**: on)
- **/drive**: home,/home/user
- **enabled with /drive**: hotplug,*. This argument provides the same
- **Redirect all mount points as shares (default**: off)
- **/dvc**: channel[,options]
- **Encryption (experimental) (default**: on)
- **/encryption-methods**: ['40', '][56', '][128', '][FIPS']
- **fast-path input/output (default**: on)
- **FIPS mode (default**: off)
- **/floatbar[**: sticky:[on|off],default:[visible|hidden],show:[always|fullscreen||window]]
- **smooth fonts (ClearType) (default**: on)
- **/frame-ack**: number
- **/from-stdin[**: force]
- **/g**: gateway[:port]
- **/gateway-usage-method**: ['direct|detect]', '/gum:[direct|detect']
- **/gd**: domain
- **/gdi**: sw|hw
- **Consume multitouch input locally (default**: off)
- **/gfx[**: RFX]
- **RDP8 graphics pipeline using progressive codec (default**: off)
- **RDP8 graphics pipeline using small cache mode (default**: off)
- **RDP8 graphics pipeline using thin client mode (default**: off)
- **Glyph cache (experimental) (default**: off)
- **/gp**: password
- **Grab keyboard (default**: on)
- **Grab mouse (default**: on)
- **/gt**: ['rpc|http[', 'no-websockets]|auto[', 'no-websockets]']
- **/gu**: ['[domain\\]user|user[@domain]']
- **/gat**: access token
- **/h**: height
- **Height (default**: 768)
- **Support heartbeat PDUs (default**: on)
- **Redirect user home as share (default**: off)
- **/kbd**: 0xid or name
- **/kbd-lang**: 0xid
- **/kbd-fn-key**: value
- **/kbd-remap**: List of key=value,... pairs to remap scancodes
- **/kbd-subtype**: id
- **/kbd-type**: id
- **/load-balance-info**: info-string
- **/log-filters**: tag:level[,tag:level[,...]]
- **/log-level**: ['OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE']
- **/max-fast-path-size**: size
- **/max-loop-time**: time
- **menu animations (default**: off)
- **/microphone[**: [sys:sys,][dev:dev,][format:format,][rate:rate,][channel:channel]],
- **/mic[**: ['sys:sys', '][dev:dev', '][format:format', '][rate:rate', '][channel:channel]']
- **/monitors**: id[,id[,...]]
- **Send mouse motion (default**: on)
- **/multimon[**: force]
- **Redirect multitouch input (default**: off)
- **Support multitransport protocol (default**: off)
- **protocol security negotiation (default**: on)
- **/network**: ['modem|broadband|broadband-low|broadband-high|wan|lan|auto']
- **offscreen bitmap cache (default**: off)
- **/orientation**: ['0|90|180|270']
- **(default**: 9000)
- **/p**: password
- **/parallel[**: name[,path]]
- **/parent-window**: window-id
- **/pcb**: blob
- **/pcid**: id
- **/pheight**: height
- **/play-rfx**: pcap-file
- **/port**: number
- **suppress output when minimized (default**: on)
- **Print base64 reconnect cookie after connecting (default**: off)
- **/printer[**: name[,driver]]
- **/proxy**: [proto://][user:password@]host:port
- **Proxy settings**: override env. var (see also environment variable
- **/pth**: password-hash, /pass-the-hash:password-hash
- **/pwidth**: width
- **/rdp2tcp**: executable path[:arg...]
- **/reconnect-cookie**: base64-cookie
- **/redirect-prefer**: FQDN|IP|NETBIOS,[...]
- **/rfx-mode**: ['image|video']
- **/scale**: ['100|140|180']
- **Scaling factor of the display (default**: 100)
- **/scale-desktop**: percentage
- **/scale-device**: 100|140|180
- **Scaling factor for app store applications (default**: 100)
- **/sec**: ['rdp|tls|nla|ext']
- **NLA extended protocol security (default**: off)
- **NLA protocol security (default**: on)
- **RDP protocol security (default**: on)
- **TLS protocol security (default**: on)
- **/serial[**: name[,path[,driver[,permissive]]]],
- **/tty[**: name[,path[,driver[,permissive]]]]
- **/shell**: shell
- **/shell-dir**: dir
- **/size**: widthxheight or percent%[wh]
- **Screen size (default**: 1024x768)
- **/smart-sizing[**: widthxheight]
- **/smartcard[**: str[,str...]]
- **Activates Smartcard Logon authentication. (EXPERIMENTAL**: NLA not
- **/sound[**: [sys:sys,][dev:dev,][format:format,][rate:rate,][channel:channel,][latency:latency,][quality:quality]],
- **/audio[**: ['sys:sys', '][dev:dev', '][format:format', '][rate:rate', '][channel:channel', '][latency:latency', '][quality:quality]']
- **/spn-class**: service-class
- **/t**: title, /title:title
- **themes (default**: on)
- **/timeout**: time in ms, /timeout:time in ms
- **Advanced setting for high latency links**: Adjust connection timeout,
- **/tls-ciphers**: ['netmon|ma|ciphers']
- **/tls-seclevel**: level
- **TLS security level - defaults to 1 (default**: 1)
- **version negotiation and might fail without this (default**: off)
- **Alt+Ctrl+Enter to toggle fullscreen (default**: on)
- **/tune**: setting:value,setting:value
- **extreme caution! (default**: )
- **/u**: ['[domain\\]user|user[@domain]']
- **Let server see real physical pointer button (default**: off)
- **/vc**: channel[,options]
- **/vmconnect[**: vmid]
- **/w**: width
- **Width (default**: 1024)
- **wallpaper (default**: on)
- **full window drag (default**: off)
- **/window-position**: xposxypos
- **/wm-class**: class-name
- **xfreerdp connection.rdp /p**: Pwd123! /f
- **xfreerdp /u**: JohnDoe /p:Pwd123!
- **like /size**: 50%w. 50 percent of the width is used.
- **/vmconnect**: C824F53E-95D2-46C6-9A18-23A5BB403532 /v:192.168.1.100
- **/smartcard**: <device>
- **/printer**: <device>,<driver>
- **/serial**: <device>
- **/parallel**: <device>
- **/sound**: sys:alsa
- **Activate audio output redirection using device sys**: alsa
- **/microphone**: sys:alsa
- **Activate audio input redirection using device sys**: alsa
- **/multimedia**: sys:alsa
- **Activate multimedia redirection using device sys**: alsa
- **/usb**: id,dev:054c:0268
- **054c**: 0268
- **http**: //www.freerdp.com/
- **winpr-hash**: NTLM hashing tool
- **Usage**: winpr-makecert [options] [output file]
- **-e <mm/dd/yyyy>      	Unsupported - Specifies the end of the validity period. Defaults to 12/31/2039 11**: 59:59 GMT.
- **-iky <keyType>       	Unsupported - Specifies the issuer's key type, which must be one of the following**: signature (which indicates that the key is used for a digital signature), exchange (which indicates that the key is used for key encryption and key exchange), or an integer that represents a provider type. By default, you can pass 1 for an exchange key or 2 for a signature key.
- **-sky <keyType>       	Unsupported - Specifies the subject's key type, which must be one of the following**: signature (which indicates that the key is used for a digital signature), exchange (which indicates that the key is used for key encryption and key exchange), or an integer that represents a provider type. By default, you can pass 1 for an exchange key or 2 for a signature key.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\freerdp2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.905306
