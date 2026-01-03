---
tool_id: hcxtools
title: hcxtools
categories: ["wireless-attacks", "password-attacks"]
category_slugs: ["wireless-attacks", "password-attacks"]
homepage: https://github.com/ZerBea/hcxtools
repository: 
version: 6.3.5-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\hcxtools\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.930850
---

# Tool: hcxtools (hcxtools)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ZerBea/hcxtools](https://github.com/ZerBea/hcxtools) |
| Repository |  |
| Version | 6.3.5-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/hcxtools
- **PackagesInfo**: |
- **hcx stands for**: ['h = hash', 'c = capture, convert and calculate candidates', 'x = different hashtypes']
- ****Installed size**: ** `580 KB`
- ****How to install**: ** `sudo apt install hcxtools`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wlancap2wpasec -h
- **usage**: wlancap2wpasec <options>  [input.pcapng] [input.pcap] [input.cap] [input.pcapng.gz]...
- **options**: []
- **-i <file>**: input wordlist
- **-d <file>**: output digit wordlist
- **-x <file>**: output xdigit wordlist
- **-c <file>**: input PMKID/EAPOL hash file (hashcat -m 22000/22001)
- **-s <file>**: output character wordlist (A-Za-z - other characters replaced by 0x0a)
- **-h**: show version
- **-v**: show version
- **--help**: show this help
- **--version**: show version
- **example**: []
- **format**: 112233445566
- **--pmkid-eapol=<file>**: input PMKID EAPOL (22000) combi hash file
- **--pmkid=<file>**: output deprecated PMKID file (delimiter *)
- **--hccapx=<file>**: output deprecated hccapx v4 file
- **--hccap=<file>**: output deprecated hccap file
- **--john=<file>**: output deprecated PMKID/EAPOL (JtR wpapsk-opencl/wpapsk-pmk-opencl)
- **Important notice**: []
- **-o <file>**: output wordlist to file
- **-E <file>**: output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
- **-E stdout**: output ESSID list to stdout (autohex enabled)
- **-L <file>**: output ESSID list (unfiltered and unsorted)
- **-d**: download https://standards-oui.ieee.org/oui/oui.txt
- **--essid-group**: convert to ESSID groups in working directory
- **--oui-group**: convert to OUI groups in working directory
- **--mac-group-ap**: convert APs to MAC groups in working directory
- **--mac-group-client**: convert CLIENTs to MAC groups in working directory
- **--type=<digit>**: filter by hash type
- **bitmask**: []
- **--hcx-min=<digit>**: disregard hashes with occurrence lower than hcx-min/ESSID
- **--hcx-max=<digit>**: disregard hashes with occurrence higher than hcx-max/ESSID
- **--essid-len**: filter by ESSID length
- **default ESSID length**: 0...32
- **--essid-min**: filter by ESSID minimum length
- **default ESSID minimum length**: 0
- **--essid-max**: filter by ESSID maximum length
- **default ESSID maximum length**: 32
- **--essid=<ESSID>**: filter by ESSID
- **--essid-part=<part of ESSID>**: filter by part of ESSID (case sensitive)
- **--essid-partx=<part of ESSID>**: filter by part of ESSID (case insensitive)
- **--essid-list=<file>**: filter by ESSID file
- **--essid-regex=<regex>**: filter ESSID by regular expression
- **--mac-ap=<MAC>**: filter AP by MAC
- **--mac-client=<MAC>**: filter CLIENT by MAC
- **--mac-list=<file>**: filter by MAC file
- **--mac-skiplist=<file>**: exclude MAC from file
- **--oui-ap=<OUI>**: filter AP by OUI
- **--oui-client=<OUI>**: filter CLIENT by OUI
- **--vendor=<VENDOR>**: filter AP or CLIENT by (part of) VENDOR name
- **--vendor-ap=<VENDOR>**: filter AP by (part of) VENDOR name
- **--vendor-client=<VENDOR>**: filter CLIENT by (part of) VENDOR name
- **--authorized**: filter EAPOL pairs by status authorized (M2M3, M3M4, M1M4)
- **--challenge**: filter EAPOL pairs by status CHALLENGE (M1M2, M1M2ROGUE)
- **--rc**: filter EAPOL pairs by replaycount status checked
- **--rc-not**: filter EAPOL pairs by replaycount status not checked
- **--apless**: filter EAPOL pairs by status M1M2ROGUE (M2 requested from CLIENT)
- **--info=<file>**: output detailed information about content of hash file
- **--info=stdout**: stdout output detailed information about content of hash file
- **--info-vendor=<file>**: output detailed information about ACCESS POINT and CLIENT VENDORs
- **--info-vendor-ap=<file>**: output detailed information about ACCESS POINT VENDORs
- **--info-vendor-client=<file>**: output detailed information about CLIENT VENDORs
- **--info-vendor=stdout**: stdout output detailed information about ACCESS POINT and CLIENT VENDORs
- **--info-vendor-ap=stdout**: stdout output detailed information about ACCESS POINT VENDORs
- **--info-vendor-client=stdout**: stdout output detailed information about CLIENT VENDORs
- **--psk=<PSK>**: pre-shared key to test
- **--pmk=<PMK>**: plain master key to test
- **--hccapx-in=<file>**: input deprecated hccapx file
- **--hccapx-out=<file>**: output to deprecated hccapx file
- **--hccap-in=<file>**: input ancient hccap file
- **--hccap-out=<file>**: output to ancient hccap file
- **--hccap-single**: output to ancient hccap single files (MAC + count)
- **--vendorlist**: stdout output complete OUI list sorted by OUI
- **short options**: []
- **-R <file>**: output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
- **-I <file>**: output unsorted identity list to use as input wordlist for cracker
- **-U <file>**: output unsorted username list to use as input wordlist for cracker
- **-D <file>**: output device information list
- **long options**: []
- **--all**: convert all possible hashes instead of only the best one
- **--eapoltimeout=<digit>**: set EAPOL TIMEOUT (milliseconds)
- ****: oui (fist three bytes of mac addr)
- **--nonce-error-corrections=<digit>**: set nonce error correction
- **warning**: values > 0 can lead to uncrackable handshakes
- **--ignore-ie**: do not use CIPHER and AKM information
- **--max-essids=<digit>**: maximum allowed ESSIDs
- **default**: stdout
- **--eapmd5=<file>**: output EAP MD5 CHALLENGE (hashcat -m 4800)
- **--eapmd5-john=<file>**: output EAP MD5 CHALLENGE (john chap)
- **--eapleap=<file>**: output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
- **--tacacs-plus=<file>**: output TACACS PLUS v1 (hashcat -m 16100, john tacacs-plus)
- **--nmea=<file>**: output GPS data in NMEA 0183 format
- **to convert it to gpx, use GPSBabel**: []
- **--csv=<file>**: output ACCESS POINT information in CSV format
- **delimiter**: tabulator (0x08)
- **columns**: []
- **YYYY-MM-DD HH**: MM:SS MAC_AP ESSID ENC_TYPE CIPHER AKM COUNTRY_INFO CHANNEL RSSI GPS(DM.m) GPS(D.d) GPSFIX SATCOUNT HDOP ALTITUDE UNIT
- **GPS FIX**: []
- **--log=<file>**: output logfile
- **--raw-out=<file>**: output frames in HEX ASCII
- **--raw-in=<file>**: input frames in HEX ASCII
- **--lts=<file>**: output BSSID list to sync with external GPS data
- **--pmkid-client=<file>**: output WPA-(MESH/REPEATER)-PMKID hash file (hashcat -m 22000)
- **--prefix=<file>**: convert everything to lists using this prefix (overrides single options):
- **-o <file.22000>**: output PMKID/EAPOL hash file
- **-E <file.essid>**: output wordlist (autohex enabled on non ASCII characters) to use as input wordlist for cracker
- **-I <file.identity>**: output unsorted identity list to use as input wordlist for cracker
- **-U <file.username>**: output unsorted username list to use as input wordlist for cracker
- **--eapmd5=<file.4800>**: output EAP MD5 CHALLENGE (hashcat -m 4800)
- **--eapleap=<file.5500>**: output EAP LEAP and MSCHAPV2 CHALLENGE (hashcat -m 5500, john netntlm)
- **--tacacs-plus=<file.16100>**: output TACACS+ (hashcat -m 16100, john tacacs-plus)
- **--nmea=<file.nmea>**: output GPS data in NMEA 0183 format
- **--add-timestamp**: add date/time and EAPOL TIME gap (time between two EAPOL MESSAGEs in nsec) to hash line
- **this must be filtered out before feeding hashcat with the hash, e.g. by awk**: []
- **bitmask of PMKID hash line (WPA*01) message pair field**: []
- **0**: reserved
- **1**: PMKID taken from AP
- **2**: PMKID taken from AP possible PSKSHA256 FT using PSK
- **3**: reserved
- **4**: NC (set to 1) - nonce-error-corrections deactivated on M1M2ROGUE, M2M3E3 and M3M4E3
- **5**: LE router detected (set to 1) - nonce-error-corrections required only on LE
- **6**: BE router detected (set to 1) - nonce-error-corrections required only on BE
- **7**: NC (set to 1) - nonce-error-corrections activated
- **bitmask of EAPOL hash line (WPA*02) message pair field**: []
- **2,1,0**: []
- **Do not use hcxpcapngtool in combination with third party cap/pcap/pcapng cleaning tools (except**: tshark and/or Wireshark)!
- **Recommended tools to show additional 802.11 fields or to decrypt WiFi traffic**: Wireshark and/or tshark
- **Recommended tool to filter converted hash by several options**: hcxhashtool
- **Recommended tool to get default or standard PSKs**: hcxpsktool
- **Recommended tool to calculate wordlists based on ESSID**: hcxeiutool
- **Recommended tools to retrieve PSK from hash**: hashcat, JtR
- **-l <hash line>**: input hashcat hash line (-m 22000)
- **-e <ESSID>**: input ESSID
- **-p <PSK>**: input Pre Shared Key (PSK) or Plain Master Key (PMK)
- **-p -**: read Pre Shared Key (PSK) from stdin
- **exit codes**: []
- **-j <file>**: input EAPOL hash file (john)
- **-z <file>**: input PMKID hash file (hashcat -m 16800/16801 and john)
- **-e <char>**: input ESSID
- **-b <xdigit>**: input MAC access point
- **--maconly**: print only candidates based on ACCESS POINT MAC
- **--noessidcombination**: exclude ESSID combinations
- **--netgear**: include weak NETGEAR / ORBI / NTGR_VMB / ARLO_VMB / FoxtelHub candidates
- **--spectrum**: include weak MySpectrumWiFi / SpectrumSetup / MyCharterWiFi candidates
- **--digit10**: include weak 10 digit candidates (INFINITUM, ALHN, INEA, VodafoneNet, VIVACOM)
- **--phome**: include weak PEGATRON / Vantiva candidates (CBCI, HOME, [SP/XF]SETUP)
- **--tenda**: include weak Tenda / NOVA / NOVE / BrosTrend candidates
- **--ee**: include weak 5GHz-EE / BrightBox / EE / EE-BrightBox candidates
- **--eeupper**: include weak EE-Hub candidates
- **--alticeoptimum**: include weak Altice/Optimum candidates (MyAltice, MyOptimum)
- **--asus**: include weak ASUS RT-AC candidates (ASUS_XX, RT-AC)
- **--weakpass**: include weak password candidates
- **--eudate**: include complete european dates
- **--usdate**: include complete american dates
- **--wpskeys**: include complete WPS keys
- **--egn**: include Bulgarian EGN
- **--simple**: include simple pattern
- **--straight**: output format untouched
- **--digit**: output format only digits
- **--xdigit**: output format only xdigits
- **--lower**: output format only lower
- **--upper**: output format only upper
- **--capital**: output format only capital
- **--length=<digit>**: password length (8...32)
- **examples**: []
- **-m <mac>**: mac (six bytes of mac addr) or
- **-p <hashline>**: input PMKID and/or EAPOL hashline (hashmode 22000 or 16800)
- **-P <hashline>**: input EAPOL hashline from potfile (hashcat <= 5.1.0)
- **-x <xdigit>**: input ESSID in hex
- **-v <vendor>**: vendor name
- **-k <key>**: wpa-sec user key
- **-u <url>**: set user defined URL
- **default = https**: //wpa-sec.stanev.org
- **-t <seconds>**: set connection timeout
- **-e <email address>**: set email address, if required
- **-R**: remove cap if upload was successful
- **To ‎remove unnecessary packets, run tshark**: []
- **To reduce the size of the cap file, compress it with gzip**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\hcxtools\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.930850
