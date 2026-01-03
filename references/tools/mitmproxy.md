---
tool_id: mitmproxy
title: mitmproxy
categories: ["sniffing-spoofing", "web-application-analysis", "information-gathering"]
category_slugs: ["sniffing-spoofing", "web-application-analysis", "information-gathering"]
homepage: https://mitmproxy.org
repository: 
version: 12.2.0-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-identify kali-tools-information-gathering kali-tools-sniffing-spoofing kali-tools-vulnerability kali-tools-web"]
icon: images/mitmproxy-logo.svg
source_path: kali-tools\mitmproxy\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.993678
---

# Tool: mitmproxy (mitmproxy)

## Categories
- [sniffing-spoofing](../sniffing-spoofing.md)
- [web-application-analysis](../web-application-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://mitmproxy.org](https://mitmproxy.org) |
| Repository |  |
| Version | 12.2.0-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-identify kali-tools-information-gathering kali-tools-sniffing-spoofing kali-tools-vulnerability kali-tools-web |
| Icon | images/mitmproxy-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/mitmproxy
- **PackagesInfo**: |
- **Features**: ['intercept and modify HTTP and HTTPS requests and responses and modify them']
- ****Installed size**: ** `4.50 MB`
- ****How to install**: ** `sudo apt install mitmproxy`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# mitmweb -h
- **usage**: mitmweb [options]
- **positional arguments**: []
- **options**: []
- **"transparent", "socks5", "reverse**: SPEC",
- **"upstream**: SPEC", and "wireguard[:PATH]" proxy servers.
- **specification in the form of "http[s]**: //host[:port]".
- **`@listen_port` or `@listen_host**: listen_port` to
- **--flow-detail LEVEL   The display detail level for flows in mitmdump**: 0
- **(quiet) to 4 (very verbose). 0**: no output 1: shortened
- **request URL with response status code 2**: full request
- **URL with response status code and HTTP headers 3**: 2 +
- **TCP messages (content_view_lines_cutoff**: 512) 4: 3 +
- **Proxy Options**: []
- **--upstream-auth USER**: PASS
- **reverse proxy requests. Format**: username:password.
- **--proxyauth SPEC      Require proxy authentication. Format**: "username:pass",
- **use an Apache htpasswd file, or "ldap[s]**: url_server_ld
- **ap[**: port]:dn_auth:password:dn_subtree[?search_filter_k
- **SSL**: []
- **Client Replay**: []
- **Server Replay**: []
- **Map Remote**: []
- **Map Local**: []
- **Modify Body**: []
- **Modify Headers**: []
- **Filters**: []
- **Mitmweb**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## mitmproxy Usage Example

Run mitmproxy listening (p) on port2139.

```console
root@kali:~# mitmproxy -p 2139
```


## Source
- Path: kali-tools\mitmproxy\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.993678
