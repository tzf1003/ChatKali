---
tool_id: kismet
title: kismet
categories: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
category_slugs: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
homepage: https://www.kismetwireless.net/
repository: 
version: 2025.09.R1-0kali3
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless"]
icon: images/kismet-logo.svg
source_path: kali-tools\kismet\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.960518
---

# Tool: kismet (kismet)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.kismetwireless.net/](https://www.kismetwireless.net/) |
| Repository |  |
| Version | 2025.09.R1-0kali3 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-wireless |
| Icon | images/kismet-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/kismet
- **PackagesInfo**: |
- ****Installed size**: ** `18 KB`
- ****How to install**: ** `sudo apt install python3-kismetcapturertladsb`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# kismet_proxytest -h
- **usage**: kismet_proxytest [-h] [--in-fd INFD] [--out-fd OUTFD]
- **--connect [host]**: [port]      Connect to remote Kismet server on [host] and [port]; by
- **example**: []
- **--autodetect [uuid**: optional] Look for a Kismet server in announcement mode, optionally
- **This package provides the following extra plugins for Kismet**: []
- *** autowep**: detects the WEP key from BSSID and SSID;
- *** btscan**: basic scan support for the 802.15.1 (Bluetooth) protocol;
- *** ptw**: performs the Aircrack-NG PTW attack against captured data;
- *** spectools**: imports data from the spectools spectrum analyzer;
- *** syslog**: provides supports for alerts using standard unix syslog services.
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

```console
kismet
```

![kismet](images/kismet.png)

## kismet_client

```console
root@kali:~# kismet_client -h
Usage: kismet_client [OPTION]
 *** Generic Options ***
 -h, --help                   The obvious
```

## kismet_drone

```console
root@kali:~# kismet_drone -h
Usage: kismet_drone [OPTION]
Nearly all of these options are run-time overrides for values in the
kismet.conf configuration file.  Permanent changes should be made to
the configuration file.
 *** Generic Options ***
 -f, --config-file            Use alternate configuration file
     --no-line-wrap           Turn of linewrapping of output
                              (for grep, speed, etc)
 -s, --silent                 Turn off stdout output after setup phase
     --daemonize              Spawn detatched in the background

 *** Kismet Remote Drone Options ***
     --drone-listen           Override Kismet drone listen options

 *** Packet Capture Source Options ***
 -c, --capture-source         Specify a new packet capture source
                              (Identical syntax to the config file)
 -C, --enable-capture-sources Enable capture sources (comma-separated
                              list of names or interfaces)
```

## kismet_server Usage Example

Start the Kismet server, using the wireless interface as the capture source (`-c wlan0`) and use the external GPSD option (`–use-gpsd-gps`):

```console
root@kali:~# kismet_server -c wlan0 --use-gpsd-gps
ERROR: Kismet was started as root, NOT launching external control binary.
       This is NOT the preferred method of starting Kismet as Kismet will
       continue to run as root the entire time.  Please read the README
       file section about Installation & Security and be sure this is what
       you want to do.
INFO: Reading from config file /etc/kismet/kismet.conf
INFO: No 'dronelisten' config line and no command line drone-listen
      argument given, Kismet drone server will not be enabled.
INFO: Created alert tracker...
INFO: Creating device tracker...
INFO: Registered 80211 PHY as id
```



## Source
- Path: kali-tools\kismet\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.960518
