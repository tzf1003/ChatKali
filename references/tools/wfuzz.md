---
tool_id: wfuzz
title: wfuzz
categories: ["web-application-analysis", "information-gathering", "vulnerability-analysis"]
category_slugs: ["web-application-analysis", "information-gathering", "vulnerability-analysis"]
homepage: http://www.edge-security.com/wfuzz.php
repository: 
version: 3.1.0-6
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-fuzzing kali-tools-web"]
icon: images/wfuzz-logo.svg
source_path: kali-tools\wfuzz\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.167956
---

# Tool: wfuzz (wfuzz)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.edge-security.com/wfuzz.php](http://www.edge-security.com/wfuzz.php) |
| Repository |  |
| Version | 3.1.0-6 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-fuzzing kali-tools-web |
| Icon | images/wfuzz-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/wfuzz
- **PackagesInfo**: |
- ****Installed size**: ** `1.54 MB`
- ****How to install**: ** `sudo apt install wfuzz`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# wfuzz --help
- *** Version up to 1.4c coded by**: *
- *** Version 1.4d to 3.1.0 coded by**: *
- **Usage**: wfuzz [options] -z payload,params <url>
- **Options**: []
- **-h/--help**: This help
- **--help**: Advanced help
- **--filter-help**: Filter language specification
- **--version**: Wfuzz version details
- **-e <type>**: List of available encoders/payloads/iterators/printers/scripts
- **--recipe <filename>**: Reads options from a recipe. Repeat for various recipes.
- **--dump-recipe <filename>**: Prints current options as a recipe
- **--oF <filename>**: Saves fuzz results to a file. These can be consumed later using the wfuzz payload.
- **-c**: Output with colors
- **-v**: Verbose information.
- **-f filename,printer**: Store results in the output file using the specified printer (raw printer if omitted).
- **-o printer**: Show results using the specified printer.
- **--interact**: (beta) If selected,all key presses are captured. This allows you to interact with the program.
- **--dry-run**: Print the results of applying the requests without actually making any HTTP request.
- **--prev**: Print the previous HTTP requests (only when using payloads generating fuzzresults)
- **--efield <expr>**: Show the specified language expression together with the current payload. Repeat for various fields.
- **--field <expr>**: Do not show the payload but only the specified language expression. Repeat for various fields.
- **-p addr**: Use Proxy in format ip:port:type. Repeat option for using various proxies.
- **-t N**: Specify the number of concurrent connections (10 default)
- **-s N**: Specify time delay between requests (0 default)
- **-R depth**: Recursive path discovery being depth the maximum recursion level.
- **-D depth**: Maximum link depth level.
- **-L,--follow**: Follow HTTP redirections
- **--ip host**: port            : Specify an IP to connect to instead of the URL's host in the format ip:port
- **-Z**: Scan mode (Connection errors will be ignored).
- **--req-delay N**: Sets the maximum time in seconds the request is allowed to take (CURLOPT_TIMEOUT). Default 90.
- **--conn-delay N**: Sets the maximum time in seconds the connection phase to the server to take (CURLOPT_CONNECTTIMEOUT). Default 90.
- **-A, --AA, --AAA**: Alias for -v -c and --script=default,verbose,discover respectively
- **--no-cache**: Disable plugins cache. Every request will be scanned.
- **--script=**: Equivalent to --script=default
- **--script=<plugins>**: Runs script's scan. <plugins> is a comma separated list of plugin-files or plugin-categories
- **--script-help=<plugins>**: Show help about scripts.
- **--script-args n1=v1,...**: Provide arguments to scripts. ie. --script-args grep.regex="<A href=\"(.*?)\">"
- **-u url**: Specify a URL for the request.
- **-m iterator**: Specify an iterator for combining payloads (product by default)
- **-z payload**: Specify a payload for each FUZZ keyword used in the form of name[,parameter][,encoder].
- **--zP <params>**: Arguments for the specified payload (it must be preceded by -z or -w).
- **--zD <default>**: Default parameter for the specified payload (it must be preceded by -z or -w).
- **--zE <encoder>**: Encoder for the specified payload (it must be preceded by -z or -w).
- **--slice <filter>**: Filter payload's elements using the specified expression. It must be preceded by -z.
- **-w wordlist**: Specify a wordlist file (alias for -z file,wordlist).
- **-V alltype**: All parameters bruteforcing (allvars and allpost). No need for FUZZ keyword.
- **-X method**: Specify an HTTP method for the request, ie. HEAD or FUZZ
- **-b cookie**: Specify a cookie for the requests. Repeat option for various cookies.
- **-d postdata**: Use post data (ex: "id=FUZZ&catalogue=1")
- **-H header**: Use header (ex:"Cookie:id=1312321&user=FUZZ"). Repeat option for various headers.
- **--basic/ntlm/digest auth**: in format "user:pass" or "FUZZ:FUZZ" or "domain\FUZ2Z:FUZZ"
- **--hc/hl/hw/hh N[,N]+**: Hide responses with the specified code/lines/words/chars (Use BBB for taking values from baseline)
- **--sc/sl/sw/sh N[,N]+**: Show responses with the specified code/lines/words/chars (Use BBB for taking values from baseline)
- **--ss/hs regex**: Show/hide responses with the specified regex within the content
- **--filter <filter>**: Show/hide responses using the specified filter expression (Use BBB for taking values from baseline)
- **--prefilter <filter>**: Filter items before fuzzing using the specified expression. Repeat for concatenating filters.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## wfuzz Usage Example

Use colour output (`-c`), a wordlist as a payload (`-z file,/usr/share/wfuzz/wordlist/general/common.txt`), and hide 404 messages (`–hc 404`) to fuzz the given URL (`http://192.168.1.202/FUZZ`):

```console
root@kali:~# wfuzz -c -z file,/usr/share/wfuzz/wordlist/general/common.txt --hc 404 http://192.168.1.202/FUZZ

********************************************************
* Wfuzz 2.2.11 - The Web Fuzzer                        *
********************************************************

Target: http://192.168.1.202/FUZZ
Payload type: file,/usr/share/wfuzz/wordlist/general/common.txt

Total requests: 950
==================================================================
ID  Response   Lines      Word         Chars          Request
==================================================================

00429:  C=200      4 L        25 W      177 Ch    " - index"
00466:  C=301      9 L        28 W      319 Ch    " - javascript"
```


## Source
- Path: kali-tools\wfuzz\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.167956
