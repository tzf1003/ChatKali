---
tool_id: autorecon
title: autorecon
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://github.com/Tib3rius/AutoRecon
repository: 
version: 0.0~git20251116.e7e98f6-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\autorecon\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.794268
---

# Tool: autorecon (autorecon)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/Tib3rius/AutoRecon](https://github.com/Tib3rius/AutoRecon) |
| Repository |  |
| Version | 0.0~git20251116.e7e98f6-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/autorecon
- **PackagesInfo**: |
- ****Installed size**: ** `1.24 MB`
- ****How to install**: ** `sudo apt install autorecon`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# autorecon -h
- **usage**: autorecon [-t TARGET_FILE] [-p PORTS] [-m MAX_SCANS]
- **[-mpti PLUGIN**: NUMBER [PLUGIN:NUMBER ...]]
- **[-mpgi PLUGIN**: NUMBER [PLUGIN:NUMBER ...]] [--accessible] [-v]
- **positional arguments**: []
- **options**: []
- **Specify TCP/UDP ports by prepending list with T**: /U: To
- **scan both TCP/UDP, put port(s) at start or specify B**: []
- **e.g. 53,T**: 21-25,80,U:123,B:123. Default: None
- **Default**: []
- **Location of AutoRecon's config file. Default**: []
- **Location of AutoRecon's global file. Default**: []
- **PortScan plugins (comma separated). Default**: None
- **ServiceScan plugins (comma separated). Default**: None
- **plugins (comma separated). Default**: None
- **The location of the plugins directory. Default**: []
- **to the main one. Default**: None
- **-o, --output OUTPUT   The output directory for results. Default**: results
- **created. Default**: False
- **directory itself. Default**: False
- **status messages. Default**: 60
- **AutoRecon should run for. Default**: None
- **moving on. Default**: None
- **--nmap NMAP           Override the {nmap_extra} variable in scans. Default**: []
- **scans from running. Default**: False
- **otherwise prevent AutoRecon from running. Default**: []
- **style**: nmap-http:2 dirbuster:1. Default: None
- **-mpti, --max-plugin-target-instances PLUGIN**: NUMBER [PLUGIN:NUMBER ...]
- **-mpgi, --max-plugin-global-instances PLUGIN**: NUMBER [PLUGIN:NUMBER ...]
- **number of global instances in the following style**: []
- **nmap-http**: 2 dirbuster:1. Default: None
- **screenreaders. Default**: False
- **plugin arguments**: []
- **--curl.path VALUE     The path on the web server to curl. Default**: /
- **The tool to use for directory busting. Default**: []
- **Separate multiple wordlists with spaces. Default**: []
- **separated). Default**: txt,html,php,asp,aspx,jsp
- **Warning**: This may cause significant increases to scan
- **times. Default**: False
- **enumeration. Default**: enum4linux-ng
- **try. Default**: []
- **example.com) for subdomain enumeration. Default**: None
- **subdomains. Default**: 10
- **example.com) for virtual host enumeration. Default**: []
- **hosts. Default**: 10
- **global plugin arguments**: []
- **Active Directory. Default**: None


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\autorecon\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.794268
