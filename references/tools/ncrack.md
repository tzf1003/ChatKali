---
tool_id: ncrack
title: ncrack
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://nmap.org/ncrack/
repository: 
version: 0.7+debian-6
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-web"]
icon: images/ncrack-logo.svg
source_path: kali-tools\ncrack\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.003636
---

# Tool: ncrack (ncrack)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://nmap.org/ncrack/](https://nmap.org/ncrack/) |
| Repository |  |
| Version | 0.7+debian-6 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords kali-tools-web |
| Icon | images/ncrack-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/ncrack
- **PackagesInfo**: |
- **Be sure to read the Ncrack man page (https**: //nmap.org/ncrack/man.html)
- ****Installed size**: ** `1.66 MB`
- ****How to install**: ** `sudo apt install ncrack`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ncrack -h
- **Ncrack 0.7 ( http**: //ncrack.org )
- **Usage**: ncrack [Options] {target and service specification}
- **TARGET SPECIFICATION**: []
- **Ex**: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
- **-iX <inputfilename>**: Input from Nmap's -oX XML output format
- **-iN <inputfilename>**: Input from Nmap's -oN Normal output format
- **-iL <inputfilename>**: Input from list of hosts/networks
- **--exclude <host1[,host2][,host3],...>**: Exclude hosts/networks
- **--excludefile <exclude_file>**: Exclude list from file
- **SERVICE SPECIFICATION**: []
- **Can pass target specific services in <service>**: //target (standard) notation or
- **(-m) or global (-g). Ex**: ssh://10.0.0.10,at=10,cl=30 -m ssh:at=50 -g cd=3000
- **Ex2**: ncrack -p ssh,ftp:3500,25 10.0.0.10 scanme.nmap.org google.com:80,ssl
- **-p <service-list>**: services will be applied to all non-standard notation hosts
- **-m <service>**: <options>: options will be applied to all services of this type
- **-g <options>**: options will be applied to every service globally
- **Misc options**: []
- **ssl**: enable SSL over this service
- **path <name>**: used in modules like HTTP ('=' needs escaping if used)
- **db <name>**: used in modules like MongoDB to specify the database
- **domain <name>**: used in modules like WinRM to specify the domain
- **TIMING AND PERFORMANCE**: []
- **Service-specific options**: []
- **cl (min connection limit)**: minimum number of concurrent parallel connections
- **CL (max connection limit)**: maximum number of concurrent parallel connections
- **at (authentication tries)**: authentication attempts per connection
- **cd (connection delay)**: delay <time> between each connection initiation
- **cr (connection retries)**: caps number of service connection attempts
- **to (time-out)**: maximum cracking <time> for service, regardless of success so far
- **-T<0-5>**: Set timing template (higher is faster)
- **--connection-limit <number>**: threshold for total concurrent connections
- **--stealthy-linear**: try credentials using only one connection against each specified host
- **AUTHENTICATION**: []
- **-U <filename>**: username file
- **-P <filename>**: password file
- **--user <username_list>**: comma-separated username list
- **--pass <password_list>**: comma-separated password list
- **--passwords-first**: Iterate password list for each username. Default is opposite.
- **--pairwise**: Choose usernames and passwords in pairs.
- **OUTPUT**: []
- **-oN/-oX <file>**: Output scan in normal and XML format, respectively, to the given filename.
- **-oA <basename>**: Output in the two major formats at once
- **-v**: Increase verbosity level (use twice or more for greater effect)
- **-d[level]**: Set or increase debugging level (Up to 10 is meaningful)
- **--nsock-trace <level>**: Set nsock trace level (Valid range: 0 - 10)
- **--log-errors**: Log errors/warnings to the normal-format output file
- **--append-output**: Append to rather than clobber specified output files
- **MISC**: []
- **--resume <file>**: Continue previously saved session
- **--save <file>**: Save restoration file with specific filename
- **-f**: quit cracking service after one found credential
- **-6**: Enable IPv6 cracking
- **-sL or --list**: only list hosts and services
- **--datadir <dirname>**: Specify custom Ncrack data file location
- **--proxy <type**: //proxy:port>: Make connections via socks4, 4a, http.
- **-V**: Print version number
- **-h**: Print this help summary page.
- **MODULES**: []
- **EXAMPLES**: []
- **ncrack -v --user root localhost**: 22
- **ncrack -v -T5 https**: //192.168.0.1
- **SEE THE MAN PAGE (http**: //nmap.org/ncrack/man.html) FOR MORE OPTIONS AND EXAMPLES


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## ncrack Usage Example

Use verbose mode (`-v`), read a list of IP addresses (`-iL win.txt`), and attempt to login with the username victim (`–user victim`) along with the passwords in a dictionary (`-P passes.txt`) using the RDP protocol (`-p rdp`) with a one connection at a time (`CL=1`):

```console
root@kali:~# ncrack -v -iL win.txt --user victim -P passes.txt -p rdp CL=1

Starting Ncrack 0.6 ( http://ncrack.org ) at 2018-12-01 09:54 EDT

rdp://192.168.1.220:3389 finished.
Discovered credentials on rdp://192.168.1.200:3389 'victim' 's3cr3t'
```


## Source
- Path: kali-tools\ncrack\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.003636
