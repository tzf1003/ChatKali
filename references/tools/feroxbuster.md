---
tool_id: feroxbuster
title: feroxbuster
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://github.com/epi052/feroxbuster
repository: 
version: 2.13.0-0kali1
architectures: amd64 arm64
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/feroxbuster-logo.svg
source_path: kali-tools\feroxbuster\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.896783
---

# Tool: feroxbuster (feroxbuster)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/epi052/feroxbuster](https://github.com/epi052/feroxbuster) |
| Repository |  |
| Version | 2.13.0-0kali1 |
| Architectures | amd64 arm64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/feroxbuster-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/feroxbuster
- **PackagesInfo**: |
- ****Installed size**: ** `12.28 MB`
- ****How to install**: ** `sudo apt install feroxbuster`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# feroxbuster --help
- **Usage**: feroxbuster [OPTIONS]
- **Options**: []
- **Target selection**: []
- **Composite settings**: []
- **Set --proxy to http**: //127.0.0.1:8080 and set --insecure to true
- **Set --replay-proxy to http**: //127.0.0.1:8080 and set --insecure to true
- **Set -H 'Content-Type**: application/json', --data to <data-json>
- **Proxy settings**: []
- **Proxy to use for requests (ex**: http(s)://host:port,
- **socks5(h)**: //host:port)
- **Status Codes to send through a Replay Proxy when found (default**: []
- **Request settings**: []
- **Sets the User-Agent (default**: feroxbuster/2.13.0)
- **File extension(s) to search for (ex**: -x php -x pdf js); reads values
- **(newline-separated) from file if input starts with an @ (ex**: @ext.txt)
- **Which HTTP request method(s) should be sent (default**: GET)
- **(ex**: @post.bin)
- **Specify HTTP headers to be used in each request (ex**: -H Header:val -H
- **'stuff**: things')
- **Specify HTTP cookies to be used in each request (ex**: -b stuff=things)
- **Request's URL query parameters (ex**: -Q token=stuff -Q secret=key)
- **with domain only (default**: https)
- **Request filters**: []
- **Response filters**: []
- **Filter out messages of a particular size (ex**: -S 5120 -S 4927,1970)
- **body/headers (ex**: -X '^ignore me$')
- **Filter out messages of a particular word count (ex**: -W 312 -W 91,82)
- **Filter out messages of a particular line count (ex**: -N 20 -N 31,30)
- **Filter out status codes (deny list) (ex**: -C 200 -C 401)
- **--filter-similar-to http**: //site.xyz/soft404)
- **Status Codes to include (allow list) (default**: All Status Codes)
- **Client settings**: []
- **Number of seconds before a client's request times out (default**: 7)
- **Scan settings**: []
- **Number of concurrent threads (default**: 50)
- **Maximum recursion depth, a depth of 0 is infinite recursion (default**: []
- **Limit total number of concurrent scans (default**: 0, i.e. no limit)
- **Limit number of requests per second (per directory) (default**: 0, i.e.
- **Limit size of response body to read in bytes (default**: 4MB)
- **Limit total run time of all scans (ex**: --time-limit 10m)
- **Dynamic collection settings**: []
- **(default**: ~, .bak, .bak2, .old, .1)
- **Output settings**: []
- **Number of directory scan bars to show at any given time (default**: no
- **Update settings**: []
- **NOTE**: []
- **extensions**: []
- **feroxbuster -u http**: //127.1 --auto-tune
- **EXAMPLES**: []
- **Multiple headers**: []
- **IPv6, non-recursive scan with INFO-level logging enabled**: []
- **https**: //epi052.github.io/feroxbuster-docs/docs/examples/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\feroxbuster\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.896783
