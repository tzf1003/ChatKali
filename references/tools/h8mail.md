---
tool_id: h8mail
title: h8mail
categories: ["information-gathering", "password-attacks"]
category_slugs: ["information-gathering", "password-attacks"]
homepage: https://github.com/khast3x/h8mail
repository: 
version: 2.5.6-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\h8mail\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.924697
---

# Tool: h8mail (h8mail)

## Categories
- [information-gathering](../information-gathering.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/khast3x/h8mail](https://github.com/khast3x/h8mail) |
| Repository |  |
| Version | 2.5.6-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/h8mail
- **PackagesInfo**: |
- ****Installed size**: ** `142 KB`
- ****How to install**: ** `sudo apt install h8mail`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# h8mail -h
- **Official h8mail posts**: []
- **https**: //khast3x.club/tags/h8mail/


## Documentation (Upstream)
---------;
  	!___| |_______!  Heartfelt Email OSINT
  	.___|_|_| |___.    Use responsibly
  	| ._____| |_. | ;____________________;
  	| !_! | | !_! | ; github.com/khast3x ;
  	!_____! !_____! ;--------------------;
  	
 [>] h8mail is up to date
 usage: h8mail [-h] [-t USER_TARGETS [USER_TARGETS ...]]
               [-u USER_URLS [USER_URLS ...]] [-q USER_QUERY] [--loose]
               [-c CONFIG_FILE [CONFIG_FILE ...]] [-o OUTPUT_FILE]
               [-j OUTPUT_JSON] [-bc BC_PATH] [-sk]
               [-k CLI_APIKEYS [CLI_APIKEYS ...]]
               [-lb LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]]
               [-gz LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]] [-sf]
               [-ch [CHASE_LIMIT]] [--power-chase] [--hide] [--debug]
               [--gen-config]
 
 Email information and password lookup tool
 
 options:
   -h, --help            show this help message and exit
   -t, --targets USER_TARGETS [USER_TARGETS ...]
                         Either string inputs or files. Supports email pattern
                         matching from input or file, filepath globing and
                         multiple arguments
   -u, --url USER_URLS [USER_URLS ...]
                         Either string inputs or files. Supports URL pattern
                         matching from input or file, filepath globing and
                         multiple arguments. Parse URLs page for emails.
                         Requires http:// or https:// in URL.
   -q, --custom-query USER_QUERY
                         Perform a custom query. Supports username, password,
                         ip, hash, domain. Performs an implicit "loose" search
                         when searching locally
   --loose               Allow loose search by disabling email pattern
                         recognition. Use spaces as pattern seperators
   -c, --config CONFIG_FILE [CONFIG_FILE ...]
                         Configuration file for API keys. Accepts keys from
                         Snusbase, WeLeakInfo, Leak-Lookup, HaveIBeenPwned,
                         Emailrep, Dehashed and hunterio
   -o, --output OUTPUT_FILE
                         File to write CSV output
   -j, --json OUTPUT_JSON
                         File to write JSON output
   -bc, --breachcomp BC_PATH
                         Path to the breachcompilation torrent folder. Uses the
                         query.sh script included in the torrent
   -sk, --skip-defaults  Skips Scylla and HunterIO check. Ideal for local scans
   -k, --apikey CLI_APIKEYS [CLI_APIKEYS ...]
                         Pass config options. Supported format: "K=V,K=V"
   -lb, --local-breach LOCAL_BREACH_SRC [LOCAL_BREACH_SRC ...]
                         Local cleartext breaches to scan for targets. Uses
                         multiprocesses, one separate process per file, on
                         separate worker pool by arguments. Supports file or
                         folder as input, and filepath globing
   -gz, --gzip LOCAL_GZIP_SRC [LOCAL_GZIP_SRC ...]
                         Local tar.gz (gzip) compressed breaches to scans for
                         targets. Uses multiprocesses, one separate process per
                         file. Supports file or folder as input, and filepath
                         globing. Looks for 'gz' in filename
   -sf, --single-file    If breach contains big cleartext or tar.gz files, set
                         this flag to view the progress bar. Disables
                         concurrent file searching for stability
   -ch, --chase [CHASE_LIMIT]
                         Add related emails from hunter.io to ongoing target
                         list. Define number of emails per target to chase.
                         Requires hunter.io private API key if used without
                         power-chase
   --power-chase         Add related emails from ALL API services to ongoing
                         target list. Use with --chase
   --hide                Only shows the first 4 characters of found passwords
                         to output. Ideal for demonstrations
   --debug               Print request debug information
   --gen-config, -g      Generates a configuration file template in the current
                         working directory & exits. Will overwrite existing
                         h8mail_config.ini file
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\h8mail\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.924697
