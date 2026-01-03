---
tool_id: minicom
title: minicom
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://salsa.debian.org/minicom-team/minicom
repository: 
version: 2.10-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-hardware"]
icon: images/minicom-logo.svg
source_path: kali-tools\minicom\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.992143
---

# Tool: minicom (minicom)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://salsa.debian.org/minicom-team/minicom](https://salsa.debian.org/minicom-team/minicom) |
| Repository |  |
| Version | 2.10-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-hardware |
| Icon | images/minicom-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `1.09 MB`
- ****How to install**: ** `sudo apt install minicom`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man xminicom
- **ascii-xfr**: invalid option -- 'h'
- **Usage**: minicom [OPTION]... [configuration]
- **-s**: send
- **-r**: receive
- **-e**: send the End Of File character (default is not to)
- **-d**: set End Of File character to Control-D (instead of Control-Z)
- **-v**: verbose (statistics on stderr output)
- **-n**: do not translate CRLF <--> LF
- **-b, --baudrate**: set baudrate (ignore the value from config)
- **-D, --device**: set device name (ignore the value from config)
- **-s, --setup**: enter setup mode
- **-o, --noinit**: do not initialize modem & lockfiles at startup
- **-m, --metakey**: use meta or alt key for commands
- **-M, --metakey8**: use 8bit meta key for commands
- **-l, --ansi**: literal; assume screen uses non IBM-PC character set
- **-L, --iso**: don't assume screen uses ISO8859
- **-w, --wrap**: Linewrap on
- **-H, --displayhex**: display output in hex
- **-z, --statline**: try to use terminal's status line
- **-7, --7bit**: force 7bit mode
- **-8, --8bit**: force 8bit mode
- **-c, --color=on/off**: ANSI style color usage on or off
- **-a, --attrib=on/off**: use reverse or highlight attributes on or off
- **-t, --term=TERM**: override TERM environment variable
- **-S, --script=SCRIPT**: run SCRIPT at startup
- **-d, --dial=ENTRY**: dial ENTRY from the dialing directory
- **-p, --ptty=TTYP**: connect to pseudo terminal
- **-C, --capturefile=FILE**: start capturing to FILE
- **--capturefile-buffer-mode=MODE**: set buffering mode of capture file
- **-F, --statlinefmt**: format of status line
- **-R, --remotecharset**: character set of communication partner
- **-v, --version**: output version information and exit
- **-h, --help**: show help
- **configuration**: configuration file to use
- **Runscript recognizes the following commands**: []
- **can be**: ["regular text, e.g. 'send hello'", 'text enclosed in quotes, e.g. \'send "hello world"\'']
- **Within <string> the following sequences are recognized**: []
- **Minicom passes three special environment variables**: $(LOGIN), which
- **label**: []
- **120 seconds. This can be changed with this command.  Warning**: this
- **User's Manual             $Date**: 2007-10-07 18:13:51 $             RUNSCRIPT(1)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\minicom\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.992143
