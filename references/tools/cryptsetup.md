---
tool_id: cryptsetup
title: cryptsetup
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://gitlab.com/cryptsetup/cryptsetup
repository: 
version: 2:2.8.1-1
architectures: linux-any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-protect"]
icon: images/cryptsetup-logo.svg
source_path: kali-tools\cryptsetup\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.856972
---

# Tool: cryptsetup (cryptsetup)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://gitlab.com/cryptsetup/cryptsetup](https://gitlab.com/cryptsetup/cryptsetup) |
| Repository |  |
| Version | 2:2.8.1-1 |
| Architectures | linux-any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-protect |
| Icon | images/cryptsetup-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/cryptsetup-team/cryptsetup
- **PackagesInfo**: |
- ****Installed size**: ** `665 KB`
- ****How to install**: ** `sudo apt install libcryptsetup12`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# cryptsetup-ssh --help
- **Usage**: cryptsetup-ssh [OPTION...] <action> <device>
- **cryptsetup 2.8.1 flags**: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
- **Help options**: []
- **--keyslot-cipher=STRING             LUKS2 keyslot**: The cipher used for
- **--keyslot-key-size=BITS             LUKS2 keyslot**: The size of the
- **--new-token-id=INT                  Token number (default**: any)
- **--pbkdf=STRING                      PBKDF algorithm (for LUKS2)**: []
- **--priority=STRING                   Keyslot priority**: ignore, normal,
- **--sector-size=INT                   Encryption sector size (default**: 512
- **--token-id=INT                      Token number (default**: any)
- **-M, --type=STRING                       Type of device metadata**: luks,
- **<action> is one of**: []
- **You can also use old <action> syntax aliases**: []
- **open**: create (plainOpen), luksOpen, loopaesOpen, tcryptOpen, bitlkOpen, fvault2Open
- **close**: remove (plainClose), luksClose, loopaesClose, tcryptClose, bitlkClose, fvault2Close
- **LUKS2 external token plugin path**: /usr/lib/x86_64-linux-gnu/cryptsetup.
- **Default compiled-in key and passphrase parameters**: []
- **Maximum keyfile size**: 4kB
- **Default PBKDF for LUKS1**: pbkdf2, iteration time: 2000 (ms)
- **Default PBKDF for LUKS2**: argon2id
- **Iteration time**: 2000, Memory required: 1048576kB, Parallel threads: 4
- **Default compiled-in device cipher parameters**: []
- **loop-AES**: aes, Key 256 bits
- **plain**: aes-xts-plain64, Key: 256 bits, Password hashing: sha256
- **LUKS**: Default keysize with XTS mode (two internal keys) will be doubled.
- **integritysetup 2.8.1 flags**: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
- **Default compiled-in dm-integrity parameters**: []
- **Checksum algorithm**: crc32c
- **veritysetup 2.8.1 flags**: UDEV BLKID KEYRING KERNEL_CAPI HW_OPAL
- **Default compiled-in dm-verity parameters**: []
- **Hash**: sha256, Data block (bytes): 4096, Hash block (bytes): 4096, Salt size: 32, Hash format: 1
- **Options for the 'add' action**: []
- **Generic options**: []
- **Note**: The information provided when adding the token (SSH server address, user


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\cryptsetup\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.856972
