---
tool_id: uhd
title: uhd
categories: ["wireless-attacks", "utilities"]
category_slugs: ["wireless-attacks", "utilities"]
homepage: https://www.ettus.com/sdr-software/uhd-usrp-hardware-driver/
repository: 
version: 4.9.0.0+ds1-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-rfid kali-tools-sdr kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\uhd\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.150325
---

# Tool: uhd (uhd)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.ettus.com/sdr-software/uhd-usrp-hardware-driver/](https://www.ettus.com/sdr-software/uhd-usrp-hardware-driver/) |
| Repository |  |
| Version | 4.9.0.0+ds1-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-rfid kali-tools-sdr kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/bottoms/pkg-uhd
- **PackagesInfo**: |
- ****Installed size**: ** `77.42 MB`
- ****How to install**: ** `sudo apt install uhd-rfnoc-dev`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# usrpctl -h
- **usage**: usrpctl [-h] [-v] [id] {find,probe,reset} ...
- **options**: []
- **RFNoC Modtool**: The tool to create and manipulate RFNoC OOT modules.
- **positional arguments**: []
- **descriptor file. Note**: Must be called from within a
- **add-gr-oot          Add GNU Radio OOT Module. Note**: Must be called from
- **descriptor file based on user input. Note**: Must be
- **add GRC bindings for a given block. Note**: Must be
- **block implementation for an RFNoC block. Note**: Must be
- **Note**: Not all daughterboards support this feature. Refer to the UHD manual for details.
- **Set the log level (default**: INFO)
- **UHD ADC self calibration Allowed options**: []
- **USRP Generate RX IQ Balance Calibration Table Allowed options**: []
- **--subdev arg                          Subdevice specification (default**: first
- **USRP Generate TX DC Offset Calibration Table Allowed options**: []
- **USRP Generate TX IQ Balance Calibration Table Allowed options**: []
- **UHD Config Info - Allowed Options**: []
- **UHD Find Devices Allowed options**: []
- **Allowed options**: []
- **Download image files required for USRPs. Usage**: The `uhd_images_downloader`
- **(default**: False)
- **Set custom install location for images (default**: None)
- **Set custom location for the manifest file (default**: []
- **Set custom location for the inventory file (default**: []
- **base URL (-b ''). (default**: False)
- **--url-only            With -l, only print the URLs, nothing else. (default**: []
- **Set download buffer size (default**: 8192)
- **or by providing --yes. (default**: 1073741824)
- **http[s]**: //user:pass@1.2.3.4:port If this this option
- **proxy. (default**: None)
- **https**: //files.ettus.com/binaries/cache/ otherwise.
- **directory (default**: False)
- **purposes). (default**: False)
- **them. (default**: False)
- **-q, --quiet           Decrease verbosity level (default**: 0)
- **-v, --verbose         Increase verbosity level (default**: 0)
- **UHD USRP Probe Allowed options**: []
- **std**: :vector
- **--interactive-reg-iface arg RFNoC devices only**: Spawn a shell to
- **Usage**: usrp2_card_burner [options]
- **Options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\uhd\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.150325
