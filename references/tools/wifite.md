---
tool_id: wifite
title: wifite
categories: ["wireless-attacks", "information-gathering"]
category_slugs: ["wireless-attacks", "information-gathering"]
homepage: https://github.com/kimocoder/wifite2
repository: 
version: 2.7.0-3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless"]
icon: images/wifite-logo.svg
source_path: kali-tools\wifite\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.172923
---

# Tool: wifite (wifite)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/kimocoder/wifite2](https://github.com/kimocoder/wifite2) |
| Repository |  |
| Version | 2.7.0-3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless |
| Icon | images/wifite-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/wifite
- **PackagesInfo**: |
- ****Installed size**: ** `2.35 MB`
- ****How to install**: ** `sudo apt install wifite`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wifite -h
- ****: :  :  (¯)  :  :  :  a wireless auditor by derv82
- **`     /¯¯¯\     ´    https**: //github.com/kimocoder/wifite2
- **options**: []
- **SETTINGS**: []
- **-v, --verbose                 Shows more options (-h -v). Prints commands and outputs. (default**: quiet)
- **-i [interface]                Wireless interface to use, e.g. wlan0mon (default**: ask)
- **-c [channel]                  Wireless channel to scan e.g. 1,3-6 (default**: all 2Ghz channels)
- **-inf, --infinite              Enable infinite attack mode. Modify scanning time with -p (default**: off)
- **-mac, --random-mac            Randomize wireless card MAC address (default**: off)
- **-p [scan_time]                Pillage**: Attack all targets after scan_time (seconds)
- **--kill                        Kill processes that conflict with Airmon/Airodump (default**: off)
- **--skip-crack                  Skip cracking captured handshakes/pmkid (default**: off)
- **-ic, --ignore-cracked         Hides previously-cracked targets. (default**: off)
- **--clients-only                Only show targets that have associated clients (default**: off)
- **--nodeauths                   Passive mode**: Never deauthenticates clients (default: deauth targets)
- **--daemon                      Puts device back in managed mode after quitting (default**: off)
- **WEP**: []
- **--require-fakeauth            Fails attacks if fake-auth fails (default**: off)
- **--keep-ivs                    Retain .IVS files and reuse when cracking (default**: off)
- **WPA**: []
- **--new-hs                      Captures new handshakes, ignores existing handshakes in hs (default**: off)
- **--dict [file]                 File containing passwords for cracking (default**: /usr/share/dict/wordlist-probable.txt)
- **WPS**: []
- **--wps-only                    Only use WPS PIN & Pixie-Dust attacks (default**: off)
- **--bully                       Use bully program for WPS PIN & Pixie-Dust attacks (default**: reaver)
- **--reaver                      Use reaver program for WPS PIN & Pixie-Dust attacks (default**: reaver)
- **--ignore-locks                Do not stop WPS PIN attack if AP becomes locked (default**: stop)
- **PMKID**: []
- **--pmkid                       Only use PMKID capture, avoids other WPS & WPA attacks (default**: off)
- **--no-pmkid                    Don't use PMKID capture (default**: off)
- **--pmkid-timeout [sec]         Time to wait for PMKID capture (default**: 300 seconds)
- **COMMANDS**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## wifite Usage Example

Attack access points with over 50 dB of power (`-pow 50`) using the WPS attack (`-wps`):

```console
root@kali:~# wifite -pow 50 -wps

  .;'                     `;,
 .;'  ,;'             `;,  `;,   WiFite v2 (r85)
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   ( )   :   ::   ::  automated wireless auditor
':.  ':.  ':. /_\ ,:'  ,:'  ,:'
 ':.  ':.    /___\    ,:'  ,:'   designed for Linux
  ':.       /_____\      ,:'
           /       \

 [+] targeting WPS-enabled networks

 [+] scanning for wireless devices...
 [+] enabling monitor mode on wlan0... done
 [+] initializing scan (mon0), updates at 5 sec intervals, CTRL+C when ready.
```


## Source
- Path: kali-tools\wifite\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.172923
