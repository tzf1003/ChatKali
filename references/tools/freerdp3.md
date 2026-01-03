---
tool_id: freerdp3
title: freerdp3
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.freerdp.com/
repository: 
version: 3.18.0+dfsg-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\freerdp3\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.905886
---

# Tool: freerdp3 (freerdp3)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.freerdp.com/](https://www.freerdp.com/) |
| Repository |  |
| Version | 3.18.0+dfsg-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian-remote-team/freerdp3
- **PackagesInfo**: |
- ****Installed size**: ** `46 KB`
- ****How to install**: ** `sudo apt install winpr3-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# winpr-makecert3 -h
- **[09**: 18:28:116] [3473311:0034ff9f] [INFO][com.freerdp.proxy.server] - [main]: 	Git commit: 3.18.0
- **Usage**: winpr-makecert3 [options] [output file]
- **Syntax**: []
- **/option**: <value> (specifies option with value)
- **/a**: <addin>[,<options>]           Addin
- **/action-script**: <file-name>       Action script
- **/app**: program:[<path>|<||alias>],cmd:<command>,file:<filename>,guid:<guid>,
- **/args-from**: <file>|stdin|fd:<number>|env:<name>
- **/assistance**: <password>           Remote assistance password
- **/audio-mode**: <mode>               Audio output mode
- **/auth-pkg-list**: [[none],]<!ntlm,kerberos,!u2u>
- **/auto-reconnect-max-retries**: <retries>
- **/azure**: [tenantid:<id>],[use-tenantid[:[on|off]],[ad:<url>][
- **avd-access**: <format string>],[avd-token:<format string>],[
- **avd-scope**: <format string>] AzureAD options
- **/bpp**: <depth>                     Session bpp (color depth)
- **/cache**: [bitmap[:on|off],codec[:rfx|nsc],glyph[:on|off],offscreen[:on|off],
- **persist,persist-file**: <filename>]
- **/cert**: [deny,ignore,name:<name>,tofu,fingerprint:<hash>:<hash as hex>[,
- **fingerprint**: <hash>:<another hash>]]
- **/client-build-number**: <number>    Client Build Number sent to server
- **/client-hostname**: <name>          Client Hostname to send to server
- **[-|/]clipboard[**: [[use-selection:<atom>],[direction-to:[
- **all|local|remote|off]],[files-to[**: all|local|remote|off]]]]
- **Disable Redirect clipboard**: []
- *** use-selection**: <atom>  ... (X11)
- *** direction-to**: ['all|local|remote|off']
- *** files-to**: ['all|local|remote|off']
- **/compression-level**: <level>       Compression level (0,1,2)
- **/d**: <domain>                      Domain
- **/drive**: hotplug,*. This argument provides
- **/dump**: <record|replay>,file:<file>[,nodelay]
- **/dvc**: <channel>[,<options>]       Dynamic virtual channel
- **/encryption-methods**: ['40', '][56', '][128', '][FIPS']
- **/floatbar[**: sticky:[on|off],default:[visible|hidden],show:[
- **/frame-ack**: <number>              Number of frame acknowledgement
- **/from-stdin[**: force]              Read credentials from stdin. With <force>
- **/gateway**: g:<gateway>[:<port>],u:<user>,d:<domain>,p:<password>,
- **usage-method**: [direct|detect],access-token:<token>,type:[rpc|http[,
- **extauth-sspi-ntlm]]|arm,url**: <wss://url>,
- **bearer**: <oauth2-bearer-token>
- **/gdi**: sw|hw                       GDI rendering
- **/gfx[**: [[progressive[:on|off]|RFX[:on|off]|AVC420[:on|off]AVC444[:on|off]],
- **mask**: <value>,small-cache[:on|off],thin-client[:on|off],progressive[
- ****: on|off],frame-ack[:on|off]]]
- **/h**: <height>                      Height
- **/ipv4[**: [:force]]                 Prefer IPv4 A record over IPv6 AAAA
- **/ipv6[**: [:force]]                 Prefer IPv6 AAAA record over IPv4 A
- **/jpeg-quality**: <percentage>       JPEG quality
- **/kbd**: remap:0x1e=0x1f,remap:0x1f=0x1e
- **subtype**: <value>,unicode[:on|off],remap:<key1>=<value1>,
- **remap**: <key2>=<value2>,pipe:<filename>]
- **Keyboard related options**: []
- *** layout**: set the keybouard layout
- *** lang**: set the keyboard language
- *** fn-key**: Function key value
- *** remap**: RDP scancode to another one.
- **Use /list**: kbd-scancode to get the
- **mapping. Example**: To switch 'a' and 's'
- **on a US keyboard**: []
- *** pipe**: Name of a named pipe that can be
- **/kerberos**: [kdc-url:<url>,lifetime:<time>,start-time:<time>,
- **renewable-lifetime**: <time>,cache:<path>,armor:<path>,
- **pkinit-anchors**: <path>][,pkcs11-module:<name>]]
- **/list**: timezones for allowed values
- **/load-balance-info**: <info-string> Load balance info
- **/log-filters**: <tag>:<level>[,<tag>:<level>[,...]]
- **/log-level**: ['OFF|FATAL|ERROR|WARN|INFO|DEBUG|TRACE']
- **/max-fast-path-size**: <size>       Specify maximum fast-path update size
- **/max-loop-time**: <time>            Specify maximum time in milliseconds
- **/microphone[**: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
- **channel**: <channel>,][latency:<latency>,][quality:<quality>]]
- **/monitors**: <id>[,<id>[,...]]      Select monitors to use (only effective in
- **/mouse**: ['relative:[on|off]', 'grab:[on|off]']
- **Mouse related options**: []
- *** relative**: send relative mouse
- *** grab**: grab the mouse if within
- **/multimon[**: force]                Use multiple monitors
- **/network**: ['invalid|modem|broadband|broadband-low|broadband-high|wan|lan|auto']
- **/orientation**: [0|90|180|270]      Orientation of display in degrees
- **/p**: <password>                    Password
- **/parallel[**: <name>[,<path>]]      Redirect parallel device
- **/parent-window**: <window-id>       Parent window id
- **/pcb**: <blob>                      Preconnection Blob
- **/pcid**: <id>                       Preconnection Id
- **/pheight**: <height>                Physical height of display (in
- **/play-rfx**: <pcap-file>            Replay rfx pcap file
- **/port**: <number>                   Server port
- **/prevent-session-lock[**: <time in sec>]
- **the connection is idle (default interval**: []
- **/printer[**: <name>[,<driver>[,default]]]
- **/proxy**: ['<proto>://][<user>:<password>@]<host>[:<port>']
- **Proxy settings**: override env. var (see
- **/pth**: <password-hash>             Pass the hash (restricted admin mode)
- **/pwidth**: <width>                  Physical width of display (in
- **/rdp2tcp**: <executable path[:arg...]>
- **/reconnect-cookie**: <base64-cookie> Pass base64 reconnect cookie to the
- **/redirect-prefer**: <FQDN|IP|NETBIOS>,[...]
- **/rfx-mode**: [image|video]          RemoteFX mode
- **/scale**: [100|140|180]             Scaling factor of the display
- **/scale-desktop**: <percentage>      Scaling factor for desktop applications
- **/scale-device**: 100|140|180        Scaling factor for app store applications
- **/sec**: nla enables NLA and disables all
- **others, while /sec**: nla:[on|off] just
- **/serial[**: <name>[,<path>[,<driver>[,permissive]]]]
- **/server-name**: <name>              User-specified server name to use for
- **/shell**: <shell>                   Alternate shell
- **/shell-dir**: <dir>                 Shell working directory
- **/size**: <width>x<height> or <percent>%[wh]
- **/smart-sizing[**: <width>x<height>] Scale remote desktop to window size
- **/smartcard[**: <str>[,<str>...]]    Redirect the smartcard devices containing
- **/smartcard-logon[**: [cert:<path>,key:<key>,pin:<pin>,csp:<csp name>,
- **reader**: <reader>,card:<card>]]
- **/sound[**: [sys:<sys>,][dev:<dev>,][format:<format>,][rate:<rate>,][
- **/spn-class**: <service-class>       SPN authentication service class
- **/sspi-module**: <SSPI module path>  SSPI shared library module file path
- **/t**: <title>                       Window title
- **/timeout**: <time in ms>            Advanced setting for high latency links:
- **/timezone**: <windows timezone>     Use supplied windows timezone for
- **/tls**: ['ciphers|seclevel|secrets-file|enforce']
- **TLS configuration options**: *
- **ciphers**: ['netmon|ma|<cipher names>']
- *** seclevel**: <level>, default: 1, range:
- *** secrets-file**: <filename>
- *** enforce[**: [ssl3|1.0|1.1|1.2|1.3]] Force
- **/tune**: <setting:value>,<setting:value>
- **/u**: ['[<domain>\\]<user>|<user>[@<domain>]']
- **/usb**: ['dbg', '][id:<vid>:<pid>#...', '][addr:<bus>:<addr>#...', '][auto']
- **/v**: <server>[:port]               Server hostname|URL|IPv4|IPv6 or
- **/some/path/to/pipe or |**: 1234 to pass a
- **/vc**: <channel>[,<options>]        Static virtual channel
- **/vmconnect[**: <vmid>]              Hyper-V console (use port 2179, disable
- **/w**: <width>                       Width
- **/window-position**: <xpos>x<ypos>   window position
- **/winscard-module**: <WinSCard module path>
- **/wm-class**: <class-name>           Set the WM_CLASS hint for the window
- **Examples**: []
- **sdl-freerdp3 connection.rdp /p**: Pwd123! /f
- **sdl-freerdp3 /u**: \AzureAD\user@corp.example /p:pwd /v:host
- **Use a generic pipe as transport**: xfreerdp3 /v:/path/to/pipe
- **Use a external socket**: xfreerdp3 /v:|:1234
- **Clipboard Redirection**: +clipboard
- **Drive Redirection**: /drive:home,/home/user
- **Smartcard Redirection**: /smartcard:<device>
- **Smartcard logon with Kerberos authentication**: /smartcard-logon /sec:nla
- **Serial Port Redirection**: /serial:COM1,/dev/ttyS0
- **Parallel Port Redirection**: /parallel:<name>,<device>
- **Printer Redirection**: /printer:<device>,<driver>,[default]
- **TCP redirection**: /rdp2tcp:/usr/bin/rdp2tcp
- **Audio Output Redirection**: /sound:sys:alsa
- **Audio Input Redirection**: /microphone:sys:alsa
- **Multimedia Redirection**: /video
- **USB Device Redirection**: /usb:id:054c:0268#4669:6e6b,addr:04:0c
- **For Gateways, the https_proxy environment variable is respected**: []
- **export https_proxy=http**: //proxy.contoso.com:3128/
- **sdl-freerdp3 /g**: rdp.contoso.com ...
- **The following configuration options are supported**: []
- **An array of SDL_Keymod strings as defined at https**: //wiki.libsdl.org/SDL3/SDL_Keymod
- **A string as defined at https**: //wiki.libsdl.org/SDL3/SDLScancodeLookup
- **Notes**: By default NLA security is active.
- **Provide one with /sam-file**: <file with path>
- **-auth (default**: on)
- **/bind-address**: <bind-address>[,<another address>, ...]
- **An address to bind to. Use '[<ipv6>]' for IPv6 addresses, e.g. '[**: :1]' for localhost
- **+bitmap-compat (default**: off)
- **/ccache**: <file>
- **-gfx (default**: on)
- **-gfx-avc420 (default**: on)
- **-gfx-avc444 (default**: on)
- **-gfx-planar (default**: on)
- **-gfx-progressive (default**: on)
- **-gfx-rfx (default**: on)
- **/ipc-socket**: <ipc-socket>
- **/keytab**: <file>
- **/max-connections**: <number>
- **-may-interact (default**: on)
- **-may-view (default**: on)
- **+mouse-relative (default**: off)
- **-nsc (default**: on)
- **/rect**: <x,y,w,h>
- **+remote-guard (default**: off)
- **-restricted-admin (default**: on)
- **-rfx (default**: on)
- **/sam-file**: <file>
- **+sec-ext (default**: off)
- **-sec-nla (default**: on)
- **-sec-rdp (default**: on)
- **-sec-tls (default**: on)
- **+server-side-cursor (default**: off)
- **/tls-secrets-file**: <file>
- **Hyper-V console server (bind on vsock**: //1)
- **wlfreerdp  [file]  [default_client_options]  [/v**: <server>[:port]] [/ver-
- **xfreerdp3 connection.rdp /p**: Pwd123! /f
- **xfreerdp3 /u**: \AzureAD\user@corp.example /p:pwd /v:host
- **xfreerdp3 /g**: rdp.contoso.com ...
- **Keyboard Shortcuts**: []
- **Scripts can be provided at the default location ~/.config/freerdp/action.sh or as command line argument /action**: script:<path>
- **winpr-hash**: NTLM hashing tool
- **-e <mm/dd/yyyy>      	Unsupported - Specifies the end of the validity period. Defaults to 12/31/2039 11**: 59:59 GMT.
- **-iky <keyType>       	Unsupported - Specifies the issuer's key type, which must be one of the following**: signature (which indicates that the key is used for a digital signature), exchange (which indicates that the key is used for key encryption and key exchange), or an integer that represents a provider type. By default, you can pass 1 for an exchange key or 2 for a signature key.
- **-sky <keyType>       	Unsupported - Specifies the subject's key type, which must be one of the following**: signature (which indicates that the key is used for a digital signature), exchange (which indicates that the key is used for key encryption and key exchange), or an integer that represents a provider type. By default, you can pass 1 for an exchange key or 2 for a signature key.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\freerdp3\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.905886
