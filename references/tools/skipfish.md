---
tool_id: skipfish
title: skipfish
categories: ["web-application-analysis", "vulnerability-analysis"]
category_slugs: ["web-application-analysis", "vulnerability-analysis"]
homepage: []
repository: 
version: 2.10b-2kali7
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web"]
icon: images/skipfish-logo.svg
source_path: kali-tools\skipfish\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.110276
---

# Tool: skipfish (skipfish)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage |  |
| Repository |  |
| Version | 2.10b-2kali7 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web |
| Icon | images/skipfish-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/skipfish
- **PackagesInfo**: |
- ****Installed size**: ** `559 KB`
- ****How to install**: ** `sudo apt install skipfish`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# skipfish -h
- **Usage**: skipfish [ options ... ] -W wordlist -o output_dir start_url [ start_url2 ... ]
- **Authentication and access options**: []
- **-A user**: pass      - use specified HTTP authentication credentials
- **Crawl scope options**: []
- **Reporting options**: []
- **Dictionary management options**: []
- **Performance settings**: []
- **Other settings**: []
- **-k duration     - stop scanning after the given duration h**: m:s


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## skipfish Usage Example

Using the given directory for output (`-o 202`), scan the web application URL (`http://192.168.1.202/wordpress`):

```console
root@kali:~# skipfish -o 202 http://192.168.1.202/wordpress

skipfish version 2.10b by lcamtuf@google.com

  - 192.168.1.202 -

Scan statistics:

      Scan time : 0:00:05.849
  HTTP requests : 2841 (485.6/s), 1601 kB in, 563 kB out (370.2 kB/s)
    Compression : 802 kB in, 1255 kB out (22.0% gain)
    HTTP faults : 0 net errors, 0 proto errors, 0 retried, 0 drops
 TCP handshakes : 46 total (61.8 req/conn)
     TCP faults : 0 failures, 0 timeouts, 16 purged
 External links : 512 skipped
   Reqs pending : 0

Database statistics:

         Pivots : 13 total, 12 done (92.31%)
    In progress : 0 pending, 0 init, 0 attacks, 1 dict
  Missing nodes : 0 spotted
     Node types : 1 serv, 4 dir, 6 file, 0 pinfo, 0 unkn, 2 par, 0 val
   Issues found : 10 info, 0 warn, 0 low, 8 medium, 0 high impact
      Dict size : 20 words (20 new), 1 extensions, 202 candidates
     Signatures : 77 total

[+] Copying static resources...
[+] Sorting and annotating crawl nodes: 13
[+] Looking for duplicate entries: 13
[+] Counting unique nodes: 11
[+] Saving pivot data for third-party tools...
[+] Writing scan description...
[+] Writing crawl tree: 13
[+] Generating summary views...
[+] Report saved to '202/index.html' [0x7054c49d].
[+] This was a great day for science!
```


## Source
- Path: kali-tools\skipfish\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.110276
