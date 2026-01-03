---
tool_id: termineter
title: termineter
categories: ["exploitation-tools", "information-gathering", "password-attacks"]
category_slugs: ["exploitation-tools", "information-gathering", "password-attacks"]
homepage: https://github.com/rsmusllp/termineter
repository: 
version: 1.0.6-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-exploitation"]
icon: images/termineter-logo.svg
source_path: kali-tools\termineter\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.137989
---

# Tool: termineter (termineter)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [information-gathering](../information-gathering.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/rsmusllp/termineter](https://github.com/rsmusllp/termineter) |
| Repository |  |
| Version | 1.0.6-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-exploitation |
| Icon | images/termineter-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/termineter
- **PackagesInfo**: |
- ****Installed size**: ** `343 KB`
- ****How to install**: ** `sudo apt install termineter`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# termineter -h
- **usage**: termineter [-h] [-v] [-L {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
- **Termineter**: Python Smart Meter Testing Framework
- **options**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/154407.js" id="asciicast-154407" async></script>

## termineter Usage Example

```console
root@kali:~# termineter

   ______              _          __
  /_  __/__ ______ _  (_)__  ___ / /____ ____
   / / / -_) __/  ' \/ / _ \/ -_) __/ -_) __/
  /_/  \__/_/ /_/_/_/_/_//_/\__/\__/\__/_/

  <[ termineter                     v1.0.4
  <[ model:                         T-1000
  <[ loaded modules:                    17

termineter > show modules

Modules
=======

  Name                    Description
  ----------------------  ------------------------------------------------
  brute_force_login       Brute Force Credentials
  diff_tables             Check C12.19 Tables For Differences
  dump_tables             Write Readable C12.19 Tables To A CSV File
  enum_tables             Enumerate Readable C12.19 Tables From The Device
  enum_user_ids           Enumerate Valid User IDs From The Device
  get_identification      Read And Parse The Identification Information
  get_info                Get Basic Meter Information By Reading Tables
  get_local_display_info  Get Information From The Local Display Tables
  get_log_info            Get Information About The Meter's Logs
  get_modem_info          Get Information About The Integrated Modem
  get_security_info       Get Information About The Meter's Access Control
  read_table              Read Data From A C12.19 Table
  remote_reset            Initiate A Reset Procedure
  run_procedure           Initiate A Custom Procedure
  set_meter_id            Set The Meter's I.D.
  set_meter_mode          Change the Meter's Operating Mode
  write_table             Write Data To A C12.19 Table

termineter >
```


## Source
- Path: kali-tools\termineter\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.137989
