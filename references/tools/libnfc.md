---
tool_id: libnfc
title: libnfc
categories: ["wireless-attacks", "utilities"]
category_slugs: ["wireless-attacks", "utilities"]
homepage: http://www.nfc-tools.org/
repository: 
version: 1.8.0-3.1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-rfid kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\libnfc\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.966797
---

# Tool: libnfc (libnfc)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.nfc-tools.org/](http://www.nfc-tools.org/) |
| Repository |  |
| Version | 1.8.0-3.1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-rfid kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/libnfc
- **PackagesInfo**: |
- ****Installed size**: ** `206 KB`
- ****How to install**: ** `sudo apt install libnfc6`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man pn53x-tamashell
- **Usage**: pn53x-diagnose
- **Options**: []
- **usage**: nfc-poll [-v]
- **-1**: force Tag Type 4 v1.0 (default is v2.0)
- **Please report any bugs on the libnfc issue tracker at**: []
- **https**: //github.com/nfc-tools/libnfc/issues
- **-t X	 poll only for types according to bitfield X**: []
- **1**: ISO14443A
- **2**: Felica (212 kbps)
- **4**: Felica (424 kbps)
- **8**: ISO14443B
- **16**: ISO14443B'
- **32**: ISO14443B-2 ST SRx
- **64**: ISO14443B-2 ASK CTx
- **128**: ISO14443B iClass
- **256**: ISO14443A-3 Jewel
- **512**: ISO14443A-2 NFC Barcode
- **Examples**: []
- **Read card to file, using key A**: []
- **Write file to blank card, using key A**: []
- **Write new data and/or keys to previously written card, using key A**: []
- **Format/wipe card (note two passes required to ensure writes for all ACL cases)**: []
- **Read card to file, using key A and uid 0x01 0xab 0x23 0xcd**: []
- **Arguments**: []
- **several NFC Forum compliant devices due to the following reasons**: ['The emulated target has only a 4-byte UID while most devices assume a']
- **Please   report   any   bugs   on   the   libnfc   issue   tracker   at**: []
- **Currently, this tool partially emulates a Mifare Mini**: it is detected as
- **To be able to emulate a target, there are two main parts**: ['communication: handle modulation, anticollision, etc.', 'computation: process commands (input) and produce results (output).']
- **commands in a single function**: target_io()
- **ment  an  ISO14443-4  tag this way**: RATS request expects a quick ATS an-
- **-q	Quiet mode. Silent output**: received and sent frames will not be shown (improves timing).
- ***** Note**: this utility only works with special Mifare 1K cards (Chinese clones).
- **Warning**: the SAM inside a Touchatag/ACR122U  is not hooked to the PN532
- **Shebang is supported, simply start your script with**: []
- **GetFirmware command is D4 02, so one has just to send the command "02"**: []
- **Connected to NFC reader**: SCM Micro/SCL3711-NFC&RW - PN533 v2.7 (0x07)
- **Tx**: 40
- **Rx**: Command Not Acceptable
- **Same thing, with a script**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\libnfc\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.966797
