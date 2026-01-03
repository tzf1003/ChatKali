---
tool_id: wireshark
title: wireshark
categories: ["sniffing-spoofing", "information-gathering"]
category_slugs: ["sniffing-spoofing", "information-gathering"]
homepage: https://www.wireshark.org/
repository: 
version: 4.6.0-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-forensics kali-tools-respond kali-tools-sniffing-spoofing kali-tools-top10 kali-tools-voip kali-tools-web kali-tools-wireless"]
icon: images/wireshark-logo.svg
source_path: kali-tools\wireshark\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.175863
---

# Tool: wireshark (wireshark)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.wireshark.org/](https://www.wireshark.org/) |
| Repository |  |
| Version | 4.6.0-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-forensics kali-tools-respond kali-tools-sniffing-spoofing kali-tools-top10 kali-tools-voip kali-tools-web kali-tools-wireless |
| Icon | images/wireshark-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/wireshark
- **PackagesInfo**: |
- ****Installed size**: ** `13.99 MB`
- ****How to install**: ** `sudo apt install wireshark-doc`
- **{{< spoiler "Dependencies**: " >}}
- **Supported formats are**: []
- **Wiretap's shortcomings are**: no filter capability and no support for packet
- **root@kali**: ~# man idl2wrs
- **See https**: //www.wireshark.org for more information.
- **Usage**: idl2deb [options]
- **Input file**: []
- **Processing**: []
- **-n                       disable all name resolutions (def**: "mNd" enabled, or
- **-N <name resolve flags>  enable specific name resolution(s)**: mnNtdv
- **Example**: idl2deb -e me@foo.net -i bar.idl -n "My Name" -d "-rfakeroot -uc -us"
- **Output**: []
- **format of text output (def**: text)
- **-E<fieldsoption>=<value> set options for output when -Tfields selected**: []
- **output format of time stamps (def**: r: rel. to first)
- **-u s|hms                 output format of seconds (def**: s: seconds)
- **-X <key>**: <value>         eXtension options, see man page for details
- **(default**: /tmp)
- **Diagnostic output**: []
- **Miscellaneous**: []
- **-o <name>**: <value> ...    override preference setting
- **You might want to enable it by executing**: []
- **Capture source**: []
- **name or idx of source (def**: first source listed by -D or --list-sources)
- **link layer type (def**: first appropriate)
- **Capture display**: []
- **-k                       start capturing immediately (def**: do nothing)
- **--update-interval        interval between updates with new items, in milliseconds (def**: 100ms)
- **Capture stop conditions**: []
- **-c <item count>          stop after n items (def**: infinite)
- **duration**: NUM - switch to next file after NUM secs
- **filesize**: NUM - switch to next file after NUM kB
- **files**: NUM - ringbuffer: replace after NUM files
- **events**: NUM - switch to next file after NUM events
- **Capture output**: []
- **interval**: NUM - switch to next file when the time is
- **User interface**: []
- **format of time stamps (def**: r: rel. to first)
- **-P <key>**: <path>          persconf:path - personal configuration files
- **persdata**: path - personal data files
- **Capture interface**: []
- **name or idx of interface (def**: first non-loopback)
- **packet snapshot length (def**: appropriate maximum)
- **size of kernel buffer in MiB (def**: 2MiB)
- **--update-interval        interval between updates with new packets, in milliseconds (def**: 100ms)
- **-c <packet count>        stop after n packets (def**: infinite)
- **packets**: NUM - ringbuffer: replace after NUM packets
- **printname**: FILE - print filename to FILE when written
- **General infos**: []
- **Size infos**: []
- **Time infos**: []
- **Statistic infos**: []
- **Metadata infos**: []
- **Output format**: []
- **Table report options**: []
- **or for remote capturing, use this format**: []
- **TCP@<host>**: <port>
- **Stop conditions**: []
- **Output (files)**: []
- **-w <filename>            name of file to save (def**: tempfile)
- **-F                       output file type (default**: pcapng)
- **Packet selection**: []
- **YYYY-MM-DDThh**: mm:ss[.nnnnnnnnn][Z|+-hh:mm]
- **Duplicate packet removal**: []
- **NOTE**: Do not enable it if the input file does not
- **Packet manipulation**: []
- **-C [offset**: ]<choplen>  chop each packet by <choplen> bytes. Positive values
- **-R <framenum>**: <time>   replace the timestamp for given frame number.
- **-a <framenum>**: <comment> Add or replace packet comment for given frame number.
- **Output File(s)**: []
- **Options**: []
- **-v**: display version info and exit
- **-h**: display this help and exit
- **-f**: path to a MaxMind Database file
- **-b                maximum bytes per packet (default**: 5000)
- **-c                packet count (default**: 1000)
- **-F                output file type (default**: pcapng)
- **Types**: []
- **-d <encap**: linktype>|<proto:protoname>
- **Supported socket types**: []
- **unix**: @sharkd          - listen on abstract Unix socket 'sharkd' (Linux-only)
- **Examples**: []
- **sharkd -a unix**: /tmp/sharkd.sock -C myprofile
- **For full details, see https**: //wiki.wireshark.org/Development/sharkd
- **Input**: []
- **"%H**: %M:%S.%f"
- **Named capturing subgroups are used to identify fields**: []
- **> 0**: 00:00.265620 a130368b000000080060
- **< 0**: 00:00.295459 a2010800000000000000000800000000
- **(def**: 16: hexadecimal) No effect in hexdump mode.
- **https**: //www.wireshark.org.
- **Prepend dummy header**: []
- **These programs are**: []
- **eg**: PYTHONPATH=/usr/lib/python3/
- **http**: //omniorb.sourceforge.net/
- **Some of the more important things to do are**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

```console
wireshark
```

![wireshark](images/wireshark.png)

## tshark Usage Example

```console
root@kali:~# tshark -f "tcp port 80" -i eth0
```


## Source
- Path: kali-tools\wireshark\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.175863
