---
tool_id: bully
title: bully
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/kimocoder/bully
repository: 
version: 1.4.00-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-wireless"]
icon: images/bully-logo.svg
source_path: kali-tools\bully\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.820165
---

# Tool: bully (bully)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/kimocoder/bully](https://github.com/kimocoder/bully) |
| Repository |  |
| Version | 1.4.00-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-wireless |
| Icon | images/bully-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/bully
- **PackagesInfo**: |
- ****Installed size**: ** `175 KB`
- ****How to install**: ** `sudo apt install bully`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bully -h
- **maintained by kimocoder - https**: //twitter.com/kimocoder
- **usage**: bully <options> interface
- **Required arguments**: []
- **interface**: Wireless interface in monitor mode (root required)
- **-b, --bssid macaddr**: MAC address of the target access point
- **-e, --essid string**: Extended SSID for the access point
- **Optional arguments**: []
- **-c, --channel N[,N...]**: Channel number of AP, or list to hop [b/g]
- **-i, --index N**: Starting pin index (7 or 8 digits)  [Auto]
- **-l, --lockwait N**: Seconds to wait if the AP locks WPS   [43]
- **-o, --outfile file**: Output file for messages          [stdout]
- **-p, --pin N**: Starting pin number (7 or 8 digits) [Auto]
- **-s, --source macaddr**: Source (hardware) MAC address      [Probe]
- **-u, --lua**: Lua script file
- **-v, --verbosity N**: Verbosity level 1-4, 1 is quietest     [3]
- **-w, --workdir path**: Location of pin/session files  [~/.bully/]
- **-5, --5ghz**: Hop on 5GHz a/n default channel list  [No]
- **-B, --bruteforce**: Bruteforce the WPS pin checksum digit [No]
- **-F, --force**: Force continue in spite of warnings   [No]
- **-S, --sequential**: Sequential pins (do not randomize)    [No]
- **-T, --test**: Test mode (do not inject any packets) [No]
- **Advanced arguments**: []
- **-d, --pixiewps**: Attempt to use pixiewps               [No]
- **-a, --acktime N**: Deprecated/ignored                  [Auto]
- **-r, --retries N**: Resend packets N times when not acked  [2]
- **-m, --m13time N**: Deprecated/ignored                  [Auto]
- **-t, --timeout N**: Deprecated/ignored                  [Auto]
- **-1, --pin1delay M,N**: Delay M seconds every Nth nack at M5 [0,1]
- **-2, --pin2delay M,N**: Delay M seconds every Nth nack at M7 [5,1]
- **-A, --noacks**: Disable ACK check for sent packets    [No]
- **-C, --nocheck**: Skip CRC/FCS validation (performance) [No]
- **-D, --detectlock**: Detect WPS lockouts unreported by AP  [No]
- **-E, --eapfail**: EAP Failure terminate every exchange  [No]
- **-L, --lockignore**: Ignore WPS locks reported by the AP   [No]
- **-M, --m57nack**: M5/M7 timeouts treated as WSC_NACK's  [No]
- **-N, --nofcs**: Packets don't contain the FCS field [Auto]
- **-P, --probe**: Use probe request for nonbeaconing AP [No]
- **-Q, --wpsinfo**: Use probe request to gather WPS info  [No]
- **-R, --radiotap**: Assume radiotap headers are present [Auto]
- **-W, --windows7**: Masquerade as a Windows 7 registrar   [No]
- **-Z, --suppress**: Suppress packet throttling algorithm  [No]
- **-V, --version**: Print version info and exit
- **-h, --help**: Display this help information


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## bully Usage Example

Attack the wireless ESSID (`-e 6F36E6`) through the monitor mode interface (`wlan0mon`):

```console
root@kali:~# bully -e 6F36E6 wlan0mon
[!] Bully v1.0-22 - WPS vulnerability assessment utility
[X] Unknown frequency '-113135872' reported by interface 'mon0'
[!] Using '00:1f:33:f3:51:13' for the source MAC address
[+] Datalink type set to '127', radiotap headers present
[+] Scanning for beacon from '6F36E6' on channel 'unknown'
[+] Got beacon for '6F36E6' (9c:d3:6d:b8:ff:56)
[+] Switching interface 'mon0' to channel '8'
[!] Beacon information element indicates WPS is locked
[!] Creating new randomized pin file '/root/.bully/pins'
[+] Index of starting pin number is '0000000'
[+] Last State = 'NoAssoc'   Next pin '54744431'
```


## Source
- Path: kali-tools\bully\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.820165
