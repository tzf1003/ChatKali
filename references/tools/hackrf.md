---
tool_id: hackrf
title: hackrf
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: http://greatscottgadgets.com/hackrf/
repository: 
version: 2024.02.1-4
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-sdr kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\hackrf\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.925377
---

# Tool: hackrf (hackrf)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://greatscottgadgets.com/hackrf/](http://greatscottgadgets.com/hackrf/) |
| Repository |  |
| Version | 2024.02.1-4 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-sdr kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/bottoms/pkg-hackrf
- **PackagesInfo**: |
- **This package contains a set of command line utilities**: []
- *** hackrf_clock**: HackRF clock configuration utility
- *** hackrf_cpldjtag**: program CLPD
- *** hackrf_debug**: chip register read/write/config tool
- *** hackrf_info**: probe device and show configuration
- *** hackrf_operacake**: control of operacake board via hackrf
- *** hackrf_spiflash**: read and write flash data from file.
- *** hackrf_sweep**: control frequency sweep of hackrf
- *** hackrf_transfer**: file based transmit and receive sdr
- ****Installed size**: ** `75 KB`
- ****How to install**: ** `sudo apt install libhackrf0`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hackrf_transfer -h
- **hackrf_biast**: invalid option -- '-'
- **Usage**: []
- **The -r/-t/-o options support the following mode settings**: []
- **-h, --help**: this help
- **-r, --read <clock_num>**: read settings for clock_num
- **-a, --all**: read settings for all clocks
- **-i, --clkin**: get CLKIN status
- **-o, --clkout <clkout_enable>**: enable/disable CLKOUT
- **-d, --device <serial_number>**: Serial number of desired HackRF.
- **Examples**: []
- **hackrf_clock -r 3**: prints settings for CLKOUT
- **-x, --xsvf <filename>**: XSVF file to be written to CPLD.
- **-d, --device <serialnumber>**: Serial number of device, if multiple devices
- **-n, --register <n>**: set register number for read/write operations
- **-r, --read**: read register specified by last -n argument, or all registers
- **-w, --write <v>**: write register specified by last -n argument with value <v>
- **-c, --config**: print SI5351C multisynth configuration information
- **-d, --device <s>**: specify a particular device by serial number
- **-m, --max2837**: target MAX2837
- **-s, --si5351c**: target SI5351C
- **-f, --rffc5072**: target RFFC5072
- **-S, --state**: display M0 state
- **-T, --tx-underrun-limit <n>**: set TX underrun limit in bytes (0 for no limit)
- **-R, --rx-overrun-limit <n>**: set RX overrun limit in bytes (0 for no limit)
- **-u, --ui <1/0>**: enable/disable UI
- **-l, --leds <state>**: configure LED state (0 for all off, 1 for default)
- **Great    Scott    Gadgets   HackRF   web   page**: http://greatscottgad-
- **Other hackrf programs**: []
- **This  program is free software**: you can redistribute it and/or modify it
- **-d, --device <n>**: specify a particular device by serial number
- **-o, --address <n>**: specify a particular Opera Cake by address [default: 0]
- **-m, --mode <mode>**: specify switching mode [options: manual, frequency, time]
- **-a <port>**: set port connected to port A0
- **-b <port>**: set port connected to port B0
- **-f <port**: min:max>: automatically assign <port> for range <min:max> in MHz. This argument can be repeated to specify a list of ports.
- **-t <port**: dwell>: in time mode, dwell on <port> for <dwell> samples. Specify only <port> to use the default dwell time (with -w). This argument can be repeated to specify a list of ports.
- **-w <n>**: set default dwell time in samples for time mode
- **-l, --list**: list available Opera Cake boards
- **-g, --gpio_test**: test GPIO functionality of an Opera Cake
- **-a, --address <n>**: starting address (default: 0)
- **-l, --length <n>**: number of bytes to read (default: 1048576)
- **-r, --read <filename>**: Read data into file.
- **-w, --write <filename>**: Write data from file.
- **-i, --no-check**: Skip check for firmware compatibility with target device.
- **-s, --status**: Read SPI flash status registers before other operations.
- **-c, --clear**: Clear SPI flash status registers before other operations.
- **-R, --reset**: Reset HackRF after other operations.
- **-v, --verbose**: Verbose output.
- **hackrf_sweep**: invalid option -- '-'
- **[-f freq_min**: freq_max] # minimum and maximum frequencies in MHz
- **Output fields**: []
- **Possible values**: 1.75/2.5/3.5/5/5.5/6/7/8/9/10/12/14/15/20/24/28MHz, default <= 0.75 * sample_rate_hz.
- **The following hardware is supported**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\hackrf\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.925377
