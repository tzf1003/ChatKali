---
tool_id: testssl.sh
title: testssl.sh
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://testssl.sh/
repository: 
version: 3.2.2+dfsg-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\testssl.sh\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.139257
---

# Tool: testssl.sh (testssl.sh)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://testssl.sh/](https://testssl.sh/) |
| Repository |  |
| Version | 3.2.2+dfsg-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/testssl.sh
- **PackagesInfo**: |
- *** Clear output**: you can tell easily whether anything is good or bad
- *** Ease of installation**: It works for Linux, Darwin, FreeBSD and
- **MSYS2/Cygwin out of the box**: no need to install or configure
- *** Flexibility**: You can test any SSL/TLS enabled and STARTTLS service,
- *** Toolbox**: Several command line options help you to run YOUR test and
- *** Reliability**: features are tested thoroughly
- *** Verbosity**: If a particular check cannot be performed because of a
- *** Privacy**: It's only you who sees the result, not a third party
- *** Freedom**: It's 100% open source. You can look at the code, see what's
- ****Installed size**: ** `3.52 MB`
- ****How to install**: ** `sudo apt install testssl.sh`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# testssl --help
- **"testssl <option>", where <option> is mostly standalone and one of**: []
- **-V, --local [pattern]         pretty print all local ciphers (of openssl only). If search pattern supplied**: it is an
- **"testssl [options] <URI>", where <URI> is**: []
- **<URI>                         host|host**: port|URL|URL:port   port 443 is default, URL can only contain HTTPS as a protocol
- **and [options] is/are**: []
- **--file/-iL <fname>            Mass testing option**: Reads one testssl.sh command line per line from <fname>.
- **Text format 1**: Comments via # allowed, EOF signals end of <fname>
- **Text format 2**: nmap output in greppable format (-oG), 1 port per line allowed
- **single check as <options>  ("testssl URI" does everything except -E and -g)**: []
- **-P, --server-preference       displays the server's picks**: protocol+cipher
- **(if <pattern> not a number**: word match)
- **-W, --sweet32                 tests 64 bit block ciphers (3DES, RC2 and IDEA)**: SWEET32 vulnerability
- **tuning / connect options (most also can be preset via environment variables)**: []
- **--openssl <PATH>              use this openssl binary (default**: look in $PATH, $RUN_DIR of testssl)
- **--proxy <host**: port|auto>      (experimental) proxy connects via <host:port>, auto: values from $env ($http(s)_proxy)
- **b) "one" means**: just test the first DNS returns (useful for multiple IPs)
- **c) "proxy" means**: dns resolution via proxy. Needed when host has no DNS.
- **-n, --nodns <min|none>        if "none"**: do not try any DNS lookups, "min" queries A, AAAA and MX records
- **--sneaky                      leave less traces in target logs**: user agent, referer
- **--basicauth <user**: pass>       provide HTTP basic auth information
- **output options (can also be preset via environment variables)**: []
- **--show-each                   for wide outputs**: display all ciphers tested -- not only succeeded ones
- **--mapping <openssl|           openssl**: use the OpenSSL cipher suite name as the primary name cipher suite name form (default)
- **--color <0|1|2|3>             0**: no escape or other codes,  1: b/w escape codes,  2: color (default), 3: extra color (color all ciphers)
- **--debug <0-6>                 1**: screen output normal but keeps debug output in /tmp/.  2-6: see "grep -A 5 '^DEBUG=' testssl.sh"
- **--out(f,F)ile|-oa/-oA <fname> log to a LOG,JSON,CSV,HTML file (see nmap). -oA/-oa**: pretty/flat JSON.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\testssl.sh\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.139257
