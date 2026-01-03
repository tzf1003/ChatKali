---
tool_id: apache2
title: apache2
categories: ["system-services"]
category_slugs: ["system-services"]
homepage: https://httpd.apache.org/
repository: 
version: 2.4.65-3
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-forensics kali-tools-respond kali-tools-social-engineering kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\apache2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.783572
---

# Tool: apache2 (apache2)

## Categories
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://httpd.apache.org/](https://httpd.apache.org/) |
| Repository |  |
| Version | 2.4.65-3 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-forensics kali-tools-respond kali-tools-social-engineering kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/apache-team/apache2
- **PackagesInfo**: |
- ****Installed size**: ** `445 KB`
- ****How to install**: ** `sudo apt install apache2-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man split-logfile
- **/usr/sbin/a2query version [unknown] calling Getopt**: :Std::getopts (version 1.14 [paranoid]),
- **Usage**: rotatelogs [-vlfDtTec] [-L linkname] [-p prog] [-n number] <logfile> {<rotation time in seconds>|<rotation size>(B|K|M|G)} [offset minutes from UTC]
- **The following single-character options are accepted**: []
- **With arguments**: -m -s -c
- **Boolean (without arguments)**: -h -a -v -M -d -q
- **See 'perldoc Getopt**: :Std' about $Getopt::Std::STANDARD_HELP_VERSION.]
- **Options**: []
- **-D name**: define a name for use in <IfDefine name> directives
- **-d directory**: specify an alternate initial ServerRoot
- **-f file**: specify an alternate ServerConfigFile
- **-C "directive"**: process directive before reading config files
- **-c "directive"**: process directive after reading config files
- **-e level**: show startup errors of level (see LogLevel)
- **-E file**: log startup errors to file
- **-v**: show version number
- **-V**: show compile settings
- **-h**: list available command line options (this page)
- **-l**: list compiled in modules
- **-L**: list available configuration directives
- **-t -D DUMP_VHOSTS**: show parsed vhost settings
- **-t -D DUMP_RUN_CFG**: show parsed run settings
- **-S**: a synonym for -t -D DUMP_VHOSTS -D DUMP_RUN_CFG
- **-t -D DUMP_MODULES**: show all loaded modules
- **-M**: a synonym for -t -D DUMP_MODULES
- **-t -D DUMP_INCLUDES**: show all included configuration files
- **-t**: run syntax check for config files
- **-T**: start without DocumentRoot(s) check
- **-X**: debug mode (only one worker, do not detach)
- **apxs**: Error: Unknown option: h.
- **Provides some add-on programs useful for any web server.  These include**: ['ab (Apache benchmark tool)', 'fcgistarter (Start a FastCGI program)', 'logresolve (Resolve IP addresses to hostnames in logfiles)', 'htpasswd (Manipulate basic authentication files)', 'htdigest (Manipulate digest authentication files)', 'htdbm (Manipulate basic authentication files in DBM format, using APR)', 'htcacheclean (Clean up the disk cache)', 'rotatelogs (Periodically stop writing to a logfile and open a new one)', 'split-logfile (Split a single log including multiple vhosts)', 'checkgid (Checks whether the caller can setgid to the specified group)', 'check_forensic (Extract mod_log_forensic output from Apache log files)', 'httxt2dbm (Generate dbm files for use with RewriteMap)']
- **ab**: wrong number of arguments
- **Options are**: []
- **-H attribute    Add Arbitrary header line, eg. 'Accept-Encoding**: gzip'
- **-X proxy**: port   Proxyserver and port number to use
- **fcgistarter**: illegal option -- h
- **usage**: fcgistarter -c <command> -p <port> [-i <interface> -N <num>]
- **htcacheclean error**: Option -p must be specified
- **attributes in the following order**: url, header size, body size,
- **deleted from the cache. A reverse proxied URL is made up as follows**: []
- **http**: //<hostname>:<port><path>?[query]. So, for the path "/" on the
- **"http**: //localhost:80/?". Note the '?' in the URL must always be
- **htdbm**: illegal option -- h
- **(higher is more secure but slower, default**: 5000).
- **htpasswd**: illegal option -- h
- **httxt2dbm**: illegal option -- h
- **Error**: Parsing Arguments Failed
- **logresolve**: illegal option -- h
- **rotatelogs**: illegal option -- h
- **Add this**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\apache2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.783572
