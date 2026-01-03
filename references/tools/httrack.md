---
tool_id: httrack
title: httrack
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://www.httrack.com
repository: 
version: 3.49.6-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: images/httrack-logo.svg
source_path: kali-tools\httrack\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.939127
---

# Tool: httrack (httrack)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.httrack.com](http://www.httrack.com) |
| Repository |  |
| Version | 3.49.6-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | images/httrack-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://github.com/xroche/httrack.git
- **PackagesInfo**: |
- ****Installed size**: ** `1.27 MB`
- ****How to install**: ** `sudo apt install webhttrack-common`
- **{{< spoiler "Dependencies**: " >}}
- **Offline browser**: copy websites to a local directory
- **root@kali**: ~# webhttrack -h
- **usage**: /usr/bin/htsserver [--port <port>] [--ppid parent-pid] <path-to-html-root-dir> [key value [key value]..]
- **with options listed below**: (* is the default value)
- **General options**: []
- **Action options**: []
- **Proxy options**: []
- **P  proxy use (-P proxy**: port or -P user:pass@proxy:port) (--proxy <param>)
- **Limits options**: []
- **Flow control**: []
- **HN host is abandoned if**: 0=never, 1=timeout, 2=slow, 3=timeout or slow (--host-control[=N])
- **Links options**: []
- **n  get non-html files 'near' an html file (ex**: an image located outside) (--near)
- **Build options**: []
- **NN structure type (0 *original structure, 1+**: see below) (--structure[=N])
- **KN keep original links (e.g. http**: //www.adr/link) (K0 *relative link, K absolute links, K4 original links, K3 absolute URI links, K5 transparent proxy link) (--keep-links[=N])
- **Spider options**: []
- **j *parse Java Classes (j0 don't parse, bitmask**: |1 parse default, |2 don't parse .class |4 don't parse .js |8 don't be aggressive) (--parse-java[=N])
- **%s  update hacks**: various hacks to limit re-transfers when updating (identical size, bogus response..) (--updatehack)
- **%u  url hacks**: various hacks to limit duplicate URLs (strip //, www.foo.com==foo.com..) (--urlhack)
- **shortcut**: '--assume standard' is equivalent to -%A php2 php3 php4 php cgi asp jsp pl cfm nsf=text/html
- **can also be used to force a specific file type**: --assume foo.cgi=text/html
- **Browser ID**: []
- **%X  additional HTTP header line (-%X "X-Magic**: 42" (--headers <param>)
- **Expert options**: []
- **pN priority mode**: (* p3) (--priority[=N])
- **l  stay on the same TLD (eg**: .com) (--stay-on-same-tld)
- **Guru options**: (do NOT use if possible)
- **Dangerous options**: (do NOT use unless you exactly know what you are doing)
- **IMPORTANT NOTE**: DANGEROUS OPTION, ONLY SUITABLE FOR EXPERTS
- **Command-line specific options**: []
- **V execute system command after each files ($0 is the filename**: -V "rm \$0") (--userdef-cmd <param>)
- **Details**: Option %W: External callbacks prototypes
- **'%n' Name of file without file type (ex**: image)
- **'%N' Name of file, including file type (ex**: image.gif)
- **'%t' File type (ex**: gif)
- **'%p' Path [without ending /] (ex**: /someimages)
- **'%h' Host name (ex**: www.someweb.com)
- **'%r' protocol name (ex**: http)
- **'%s?' Short name version (ex**: %sN)
- **'%[param**: before:after:empty:notfound]' advanced variable extraction
- **%[param**: before:after:empty:notfound]
- **param**: parameter name
- **before**: string to prepend if the parameter was found
- **after**: string to append if the parameter was found
- **notfound**: string replacement if the parameter could not be found
- **empty**: string replacement if the parameter was empty
- **K                 ->  http**: //www.foobar.com/folder/foo.cgi?q=45 (absolute URL) (--keep-links[=N])
- **K5                ->  http**: //www.foobar.com/folder/foo4B54.html?q=45 (transparent proxy URL)
- **Shortcuts**: []
- **--spider      <URLs>  spider site(s), to test links**: reports Errors & Warnings (-p0C0I0t)
- **example**: /usr/bin/htsserver /usr/share/httrack/
- **means**: mirror the two sites together (with shared links) and accept any .jpg files on .com sites
- **proxy mode**: []
- **convert mode**: []
- **Snapshots**: http://www.httrack.com/page/21/
- **Offline browser server**: copy websites to a local directory
- **htsserver - offline browser server**: copy websites to a local directory
- **then, browse http**: //localhost:8080/
- **This  program is free software**: you can redistribute it and/or modify it
- **with this program. If not, see <http**: //www.gnu.org/licenses/>.
- **The  most  recent released version of  (web)httrack  can  be  found  at**: []
- **http**: //www.httrack.com
- **The HTML documentation (available online at http**: //www.httrack.com/html/
- **FAQ (available online at http**: //www.httrack.com/html/faq.html )
- **** Warning**: use the webhttrack frontend if available
- **/usr/bin/webhttrack(1336952)**: Could not spawn htsserver


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\httrack\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.939127
