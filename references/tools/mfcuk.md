---
tool_id: mfcuk
title: mfcuk
categories: ["password-attacks", "utilities"]
category_slugs: ["password-attacks", "utilities"]
homepage: https://github.com/nfc-tools/mfcuk
repository: 
version: 0.3.8+git20180720-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-rfid kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\mfcuk\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.990621
---

# Tool: mfcuk (mfcuk)

## Categories
- [password-attacks](../password-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/nfc-tools/mfcuk](https://github.com/nfc-tools/mfcuk) |
| Repository |  |
| Version | 0.3.8+git20180720-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-rfid kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/mfcuk
- **PackagesInfo**: |
- **Special emphasis of the toolkit is on the following**: []
- ****Installed size**: ** `87 KB`
- ****How to install**: ** `sudo apt install mfcuk`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# mfcuk -h
- **by Andrei Costin, zveriu@gmail.com, http**: //andreicostin.com
- **Usage**: []
- **-V sector[**: A/B/any_other_alphanum[:fullkey]] - verify key for specified sector, -1 means all sectors
- **After first semicolon key-type can specified**: A recovers only keyA, B recovers only keyB, anything else recovers both keys
- **-R sector[**: A/B/any_other_alphanum] - recover key for sector, -1 means all sectors.
- **-s - milliseconds to sleep for SLEEP_AT_FIELD_OFF (Default**: 10 ms)
- **-S - milliseconds to sleep for SLEEP_AFTER_FIELD_ON (Default**: 50 ms)
- **-P hex_literals_separated - try to recover the key from a conversation sniffed with Proxmark3 (mifarecrack.c based). Accepts several options**: []
- **Concatenated string in hex literal format of form uid**: tag_chal:nr_enc:reader_resp:tag_resp
- **Example -P 0x5c72325e**: 0x50829cd6:0xb8671f76:0xe00eefc9:0x4888964f would find key FFFFFFFFFFFF
- **Usage examples**: []
- **Recover all keys from all sectors**: []
- **Recover the sector #0 key with 250 ms for all delays (delays could give more results)**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\mfcuk\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.990621
