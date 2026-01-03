---
tool_id: rdesktop
title: rdesktop
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.rdesktop.org/
repository: 
version: 1.9.0-2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\rdesktop\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.073174
---

# Tool: rdesktop (rdesktop)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.rdesktop.org/](https://www.rdesktop.org/) |
| Repository |  |
| Version | 1.9.0-2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `680 KB`
- ****How to install**: ** `sudo apt install rdesktop`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rdesktop --help
- **rdesktop**: A Remote Desktop Protocol client.
- **See http**: //www.rdesktop.org/ for more information.
- **Usage**: rdesktop [options] server[:port]
- **-u**: user name
- **-d**: domain
- **-s**: shell / seamless application to start remotely
- **-c**: working directory
- **-p**: password (- to prompt)
- **-n**: client hostname
- **-k**: keyboard layout on server (en-us, de, sv, etc.)
- **-g**: desktop geometry (WxH[@DPI][+X[+Y]])
- **-i**: enables smartcard authentication, password is used as pin
- **-f**: full-screen mode
- **-b**: force bitmap updates
- **-L**: local codepage
- **-A**: path to SeamlessRDP shell, this enables SeamlessRDP mode
- **-V**: tls version (1.0, 1.1, 1.2, defaults to negotiation)
- **-B**: use BackingStore of X-server (if available)
- **-e**: disable encryption (French TS)
- **-E**: disable encryption from client to server
- **-m**: do not send motion events
- **-M**: use local mouse cursor
- **-C**: use private colour map
- **-D**: hide window manager decorations
- **-K**: keep window manager key bindings
- **-S**: caption button size (single application mode)
- **-T**: window title
- **-t**: disable use of remote ctrl
- **-N**: enable numlock synchronization
- **-X**: embed into another window with a given id.
- **-a**: connection colour depth
- **-z**: enable rdp compression
- **-x**: RDP5 experience (m[odem 28.8], b[roadband], l[an] or hex nr.)
- **-P**: use persistent bitmap caching
- **-r**: enable specified device redirection (this flag can be repeated)
- **'-r comport**: COM1=/dev/ttyS0': enable serial redirection of /dev/ttyS0 to COM1
- **'-r disk**: floppy=/mnt/floppy': enable redirection of /mnt/floppy to 'floppy' share
- **'-r clientname=<client name>'**: Set the client name displayed
- **'-r lptport**: LPT1=/dev/lp0': enable parallel redirection of /dev/lp0 to LPT1
- **'-r printer**: mydeskjet': enable printer redirection
- **'-r sound**: [local[:driver[:device]]|off|remote]': enable sound redirection
- **available drivers for 'local'**: []
- **alsa**: ALSA output driver, default device: default
- **'-r clipboard**: [off|PRIMARYCLIPBOARD|CLIPBOARD]': enable clipboard
- **'-r scard[**: "Scard Name"="Alias Name[;Vendor Name]"[,...]]
- **example**: -r scard:"eToken PRO 00 00"="AKS ifdh 0;AKS"
- **-0**: attach to console
- **-4**: use RDP version 4
- **-5**: use RDP version 5 (default)
- **-o**: name=value: Adds an additional option to rdesktop.
- **-v**: enable verbose logging


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\rdesktop\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.073174
