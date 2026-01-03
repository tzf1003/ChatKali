---
tool_id: armitage
title: armitage
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://github.com/r00t0v3rr1d3/armitage
repository: 
version: 20221206-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-exploitation"]
icon: images/armitage-logo.svg
source_path: kali-tools\armitage\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.788798
---

# Tool: armitage (armitage)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/r00t0v3rr1d3/armitage](https://github.com/r00t0v3rr1d3/armitage) |
| Repository |  |
| Version | 20221206-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-exploitation |
| Icon | images/armitage-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/armitage
- **PackagesInfo**: |
- ****Installed size**: ** `10.95 MB`
- ****How to install**: ** `sudo apt install armitage`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# teamserver -h
- **[*] You must provide**: <external IP address> <team password>


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![armitage](images/armitage.png)

## armitage Usage Example

```console
root@kali:~# armitage
[*] Starting msfrpcd for you.
```

## teamserver Usage Example

Start teamserver on the external IP (`192.168.1.202`) and set the server password (`s3cr3t`):

```console
root@kali:~# teamserver 192.168.1.202 s3cr3t
[*] Generating X509 certificate and keystore (for SSL)
[*] Starting RPC daemon
[*] MSGRPC starting on 127.0.0.1:55554 (NO SSL):Msg...
[*] MSGRPC backgrounding at 2014-05-14 15:05:46 -0400...
[*] sleeping for 20s (to let msfrpcd initialize)
[*] Starting Armitage team server
[-] Java 1.6 is not supported with this tool. Please upgrade to Java 1.7
[*] Use the following connection details to connect your clients:
    Host: 192.168.1.202
    Port: 55553
    User: msf
    Pass: s3cr3t

[*] Fingerprint (check for this string when you connect):
    a3b60bef430037a6b628d9011924341b8c09081
[+] multi-player metasploit... ready to go
```


## Source
- Path: kali-tools\armitage\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.788798
