---
tool_id: gr-osmosdr
title: gr-osmosdr
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://osmocom.org/projects/gr-osmosdr/wiki
repository: 
version: 0.2.6-4
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-sdr kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\gr-osmosdr\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.921364
---

# Tool: gr-osmosdr (gr-osmosdr)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://osmocom.org/projects/gr-osmosdr/wiki](https://osmocom.org/projects/gr-osmosdr/wiki) |
| Repository |  |
| Version | 0.2.6-4 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-sdr kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/bottoms/pkg-gr-osmosdr
- **PackagesInfo**: |
- **as well supports**: ['FUNcube Dongle through gr-funcube', 'FUNcube Dongle Pro+ through gr-funcube', 'RTL2832U based DVB-T dongles through librtlsdr', 'RTL-TCP spectrum server (see librtlsdr project)', 'gnuradio .cfile input through libgnuradio-blocks', 'RFSPACE SDR-IQ, SDR-IP, NetSDR (incl. X2 option)', 'Great Scott Gadgets HackRF through libhackrf', 'Nuand LLC bladeRF through libbladeRF library', 'Ettus USRP Devices through Ettus UHD library', "Fairwaves UmTRX through Fairwaves' fork of UHD", 'AIRSPY Receiver', 'AIRSPY HF+ Receiver', 'SoapySDR support', 'Red Pitaya SDR transceiver (http://bazaar.redpitaya.com)', 'FreeSRP through libfreesrp']
- ****Installed size**: ** `1.26 MB`
- ****How to install**: ** `sudo apt install libgnuradio-osmosdr0.2.0t64`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# osmocom_siggen_nogui -h
- **device=hw**: 2
- **Enable direct sampling mode on the RTL chip. 0**: Disable, 1: use I
- **channel, 2**: use Q channel
- **NOTE**: if you don't specify rtl_xtal/tuner_xtal,  the  underlying  driver
- **rtl_tcp=<hostname>**: <port>
- **Examples**: "A:0",  "B:0",  "A:0 B:0" when nchan=2. Refer original
- **Usage**: osmocom_siggen_nogui: [options]
- **Options**: []
- **Set named gain in dB, name**: gain,name:gain,...


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\gr-osmosdr\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.921364
