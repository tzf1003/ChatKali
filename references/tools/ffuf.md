---
tool_id: ffuf
title: ffuf
categories: ["information-gathering", "web-application-analysis", "vulnerability-analysis"]
category_slugs: ["information-gathering", "web-application-analysis", "vulnerability-analysis"]
homepage: https://github.com/ffuf/ffuf
repository: 
version: 2.1.0-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: images/ffuf-logo.svg
source_path: kali-tools\ffuf\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.897700
---

# Tool: ffuf (ffuf)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ffuf/ffuf](https://github.com/ffuf/ffuf) |
| Repository |  |
| Version | 2.1.0-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | images/ffuf-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/ffuf/
- **PackagesInfo**: |
- ****Installed size**: ** `9.12 MB`
- ****How to install**: ** `sudo apt install ffuf`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# ffuf -h
- **HTTP OPTIONS**: []
- **-H                  Header `"Name**: Value"`, separated by colon. Multiple -H flags are accepted.
- **-http2              Use HTTP2 protocol (default**: false)
- **-ignore-body        Do not fetch the response content. (default**: false)
- **-r                  Follow redirects (default**: false)
- **-raw                Do not encode URI (default**: false)
- **-recursion          Scan recursively. Only FUZZ keyword is supported, and URL (-u) has to end in it. (default**: false)
- **-recursion-depth    Maximum recursion depth. (default**: 0)
- **-recursion-strategy Recursion strategy**: "default" for a redirect based, and "greedy" to recurse on all matches (default: default)
- **-timeout            HTTP request timeout in seconds. (default**: 10)
- **-x                  Proxy URL (SOCKS5 or HTTP). For example**: http://127.0.0.1:8080 or socks5://127.0.0.1:8080
- **GENERAL OPTIONS**: []
- **-V                  Show version information. (default**: false)
- **-ac                 Automatically calibrate filtering options (default**: false)
- **-ach                Per host autocalibration (default**: false)
- **-ack                Autocalibration keyword (default**: FUZZ)
- **-c                  Colorize output. (default**: false)
- **-json               JSON output, printing newline-delimited JSON records (default**: false)
- **-maxtime            Maximum running time in seconds for entire process. (default**: 0)
- **-maxtime-job        Maximum running time in seconds per job. (default**: 0)
- **-noninteractive     Disable the interactive console functionality (default**: false)
- **-rate               Rate of requests per second (default**: 0)
- **-s                  Do not print additional information (silent mode) (default**: false)
- **-sa                 Stop on all error cases. Implies -sf and -se. (default**: false)
- **-scrapers           Active scraper groups (default**: all)
- **-se                 Stop on spurious errors (default**: false)
- **-sf                 Stop when > 95% of responses return 403 Forbidden (default**: false)
- **-t                  Number of concurrent threads. (default**: 40)
- **-v                  Verbose output, printing full URL and redirect location (if any) with the results. (default**: false)
- **MATCHER OPTIONS**: []
- **-mc                 Match HTTP status codes, or "all" for everything. (default**: 200-299,301,302,307,401,403,405,500)
- **-mmode              Matcher set operator. Either of**: and, or (default: or)
- **-mt                 Match how many milliseconds to the first response byte, either greater or less than. EG**: >100 or <100
- **FILTER OPTIONS**: []
- **-fmode              Filter set operator. Either of**: and, or (default: or)
- **-ft                 Filter by number of milliseconds to the first response byte, either greater or less than. EG**: >100 or <100
- **INPUT OPTIONS**: []
- **-D                  DirSearch wordlist compatibility mode. Used in conjunction with -e flag. (default**: false)
- **-enc                Encoders for keywords, eg. 'FUZZ**: urlencode b64encode'
- **-ic                 Ignore wordlist comments (default**: false)
- **-input-num          Number of inputs to test. Used in conjunction with --input-cmd. (default**: 100)
- **-mode               Multi-wordlist operation mode. Available modes**: clusterbomb, pitchfork, sniper (default: clusterbomb)
- **-request-proto      Protocol to use along with raw request (default**: https)
- **-w                  Wordlist file path and (optional) keyword separated by colon. eg. '/path/to/wordlist**: KEYWORD'
- **OUTPUT OPTIONS**: []
- **-of                 Output file format. Available formats**: json, ejson, html, md, csv, ecsv (or, 'all' for all formats) (default: json)
- **-or                 Don't create the output file if we don't have results (default**: false)
- **EXAMPLE USAGE**: []
- **ffuf -w wordlist.txt -u https**: //example.org/FUZZ -mc all -fs 42 -c -v
- **ffuf -w hosts.txt -u https**: //example.org/ -H "Host: FUZZ" -mc 200
- **ffuf -w entries.txt -u https**: //example.org/ -X POST -H "Content-Type: application/json" \
- **-d '{"name"**: FUZZ", "anotherkey": "anothervalue"}' -fr "error
- **ffuf -w params.txt**: PARAM -w values.txt:VAL -u https://example.org/?PARAM=VAL -mr "VAL" -c
- **More information and examples**: https://github.com/ffuf/ffuf


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\ffuf\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.897700
