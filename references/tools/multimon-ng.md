---
tool_id: multimon-ng
title: multimon-ng
categories: ["wireless-attacks"]
category_slugs: ["wireless-attacks"]
homepage: https://github.com/EliasOenal/multimon-ng/
repository: 
version: 1.3.1+dfsg-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-sdr kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\multimon-ng\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.996661
---

# Tool: multimon-ng (multimon-ng)

## Categories
- [wireless-attacks](../wireless-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/EliasOenal/multimon-ng/](https://github.com/EliasOenal/multimon-ng/) |
| Repository |  |
| Version | 1.3.1+dfsg-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-sdr kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian-hamradio-team/multimon-ng
- **PackagesInfo**: |
- **transmission modes commonly found on VHF/UHF bands**: []
- **provided via a file or a pipe. Common setups are**: a radio connected
- ****Installed size**: ** `138 KB`
- ****How to install**: ** `sudo apt install multimon-ng`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# multimon-ng --help
- **multimon-ng**: unrecognized option '--help'
- **Available demodulators**: POCSAG512 POCSAG1200 POCSAG2400 FLEX FLEX_NEXT EAS UFSK1200 CLIPFSK FMSFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR MORSE_CW DUMPCSV X10 SCOPE
- **Usage**: multimon-ng [file] [file] [file] ...
- **-t <type>**: Input file type (any other type than raw requires sox)
- **-a <demod>**: Add demodulator
- **-s <demod>**: Subtract demodulator
- **-c**: Remove all demodulators (must be added with -a <demod>)
- **-q**: Quiet
- **-v <level>**: Level of verbosity (e.g. '-v 3')
- **-h**: This help
- **-A**: APRS mode (TNC2 text output)
- **-m**: Mute SoX warnings
- **-r**: Call SoX in repeatable mode (e.g. fixed random seed for dithering)
- **-n**: Don't flush stdout, increases performance.
- **-j**: FMS: Just output hex data and CRC, no parsing.
- **-e**: POCSAG: Hide empty messages.
- **-u**: POCSAG: Heuristically prune unlikely decodes.
- **-i**: POCSAG: Inverts the input samples. Try this if decoding fails.
- **-p**: POCSAG: Show partially received messages.
- **-f <mode>**: POCSAG: Overrides standards and forces decoding of data as <mode>
- **-b <level>**: POCSAG: BCH bit error correction level. Set 0 to disable, default is 2.
- **-C <cs>**: POCSAG: Set Charset.
- **-o**: CW: Set threshold for dit detection (default: 500)
- **-d**: CW: Dit length in ms (default: 50)
- **-g**: CW: Gap length in ms (default: 50)
- **-x**: CW: Disable auto threshold detection
- **-y**: CW: Disable auto timing detection
- **--timestamp**: Add a time stamp in front of every printed line
- **--label**: Add a label to the front of every printed line


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## multimon-ng Usage Example

Take raw input from rtl_fm (`-t raw`), add the POCSAG512, POCSAG1200, POCSAG2400, and SCOPE modules (`-a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE`), decode in alpha mode (`-f alpha`), reading from stdin (`/dev/stdin`):

```console
root@kali:~# rtl_fm -f 149.614M -s 22050 -p -19 | multimon-ng -t raw -a POCSAG512 -a POCSAG1200 -a POCSAG2400 -a SCOPE -f alpha /dev/stdin
multimon-ng  (C) 1996/1997 by Tom Sailer HB9JNX/AE4WA
             (C) 2012/2013 by Elias Oenal
available demodulators: POCSAG512 POCSAG1200 POCSAG2400 EAS UFSK1200 CLIPFSK AFSK1200 AFSK2400 AFSK2400_2 AFSK2400_3 HAPN4800 FSK9600 DTMF ZVEI1 ZVEI2 ZVEI3 DZVEI PZVEI EEA EIA CCIR SCOPE
Enabled demodulators: POCSAG512 POCSAG1200 POCSAG2400 SCOPE
Found 1 device(s):
  0:  Realtek, RTL2838UHIDIR, SN: 00000001

Using device 0: ezcap USB 2.0 DVB-T/DAB/FM dongle
Found Rafael Micro R820T tuner
Oversampling input by: 46x.
Oversampling output by: 1x.
Buffer size: 8.08ms
Tuned to 149867575 Hz.
Sampling at 1014300 Hz.
Output at 22050 Hz.
Exact sample rate is: 1014300.020041 Hz
Tuner gain set to automatic.
```


## Source
- Path: kali-tools\multimon-ng\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.996661
