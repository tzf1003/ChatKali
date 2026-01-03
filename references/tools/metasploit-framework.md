---
tool_id: metasploit-framework
title: metasploit-framework
categories: ["exploitation-tools", "information-gathering", "post-exploitation"]
category_slugs: ["exploitation-tools", "information-gathering", "post-exploitation"]
homepage: https://www.metasploit.com/
repository: 
version: 6.4.99-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-identify kali-tools-information-gathering kali-tools-post-exploitation kali-tools-reverse-engineering kali-tools-social-engineering kali-tools-top10 kali-tools-vulnerability kali-tools-web"]
icon: images/metasploit-framework-logo.svg
source_path: kali-tools\metasploit-framework\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.990185
---

# Tool: metasploit-framework (metasploit-framework)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [information-gathering](../information-gathering.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.metasploit.com/](https://www.metasploit.com/) |
| Repository |  |
| Version | 6.4.99-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-identify kali-tools-information-gathering kali-tools-post-exploitation kali-tools-reverse-engineering kali-tools-social-engineering kali-tools-top10 kali-tools-vulnerability kali-tools-web |
| Icon | images/metasploit-framework-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/metasploit-framework
- **PackagesInfo**: |
- ****Installed size**: ** `541.06 MB`
- ****How to install**: ** `sudo apt install metasploit-framework`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# msfvenom -h
- **Usage**: /usr/bin/msfvenom [options] <var=val>
- **Example**: /usr/bin/msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> -f exe -o payload.exe
- **Specific options**: []
- **OPTIONS**: []
- **-b   The list of characters to avoid**: \x00\xff
- **The format of hash file is <identifier>**: <hex-salt>:<hash>
- **-d, --databases <names>          (Optional) Select databases**: all, authsecu, i337, md5_my_addr, md5_net, md5crack, md5cracker, md5decryption, md5online, md5pass, netmd5crack, tmto (Default=all)
- **-E ex[**: in]        Set default external (ex) and internal (in) encodings
- **-W[level=2]       Set warning level**: 0=silence, 1=medium, 2=verbose
- **Set prompt mode. Pre-defined prompt modes are**: []
- **Options**: []
- **Common options**: []
- **Database options**: []
- **Framework options**: []
- **Module options**: []
- **Console options**: []
- **-a   Bind to this IP address (default**: 0.0.0.0)
- **-c   (JSON-RPC) Path to certificate (default**: /root/.msf4/msf-ws-cert.pem)
- **-k   (JSON-RPC) Path to private key (default**: /root/.msf4/msf-ws-key.pem)
- **-p   Bind to this port (default**: 55553)
- **-t   Token Timeout seconds (default**: 300)
- **-l, --list            <type>     List all modules for [type]. Types are**: payloads, encoders, nops, platforms, archs, encrypt, formats, all
- **--sec-name        <value>    The new section name to use when generating large Windows binaries. Default**: random 4-character alpha string
- **-b, --bad-chars       <list>     Characters to avoid example**: \x00\xff


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/118945.js" id="asciicast-118945" async></script>

## msfrpcd

```console
root@kali:~# msfrpcd -h

Usage: msfrpcd <options>

OPTIONS:

    -P <opt>  Specify the password to access msfrpcd
    -S        Disable SSL on the RPC socket
    -U <opt>  Specify the username to access msfrpcd
    -a <opt>  Bind to this IP address
    -f        Run the daemon in the foreground
    -h        Help banner
    -n        Disable database
    -p <opt>  Bind to this port instead of 55553
    -t <opt>  Token Timeout (default 300 seconds
    -u <opt>  URI for Web server
```

## Metasploit-Framework Usage Examples

One of the best sources of information on using the Metasploit Framework is [Metasploit Unleashed](https://www.offsec.com/metasploit-unleashed/?utm_source=kali&utm_medium=web&utm_campaign=tools), a free online course created by OffSec. Metasploit Unleashed guides you from the absolute basics of Metasploit all the way through to advanced topics.


## Source
- Path: kali-tools\metasploit-framework\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.990185
