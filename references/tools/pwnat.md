---
tool_id: pwnat
title: pwnat
categories: ["tunneling-exfiltration", "utilities"]
category_slugs: ["tunneling-exfiltration", "utilities"]
homepage: https://samy.pl/pwnat/
repository: 
version: 0.3.0-0kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation"]
icon: images/pwnat-logo.svg
source_path: kali-tools\pwnat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.060746
---

# Tool: pwnat (pwnat)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://samy.pl/pwnat/](https://samy.pl/pwnat/) |
| Repository |  |
| Version | 0.3.0-0kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation |
| Icon | images/pwnat-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/pwnat
- **PackagesInfo**: |
- ****Installed size**: ** `65 KB`
- ****How to install**: ** `sudo apt install pwnat`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pwnat -h
- **usage**: pwnat <-s | -c> <args>
- **<args>**: ['local ip] [proxy port (def:2222)] [[allowed host]:[allowed port] ...']


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## pwnat Usage Example

On the server, run in server mode (`-s`) on port 8080 (`8080`.

On the client, run in client mode (`-c`) on local port 8000 (`8000`), connect to the server IP (`192.168.1.202`) on port 8080 (`8080`) and use it to connect to google.com on port 80 (`google.com 80`).

```console
root@kali:~# pwnat -s 8080
Listening on UDP 0.0.0.0:8080
```

```console
root@kali:~# pwnat -c 8000 192.168.1.202 8080 google.com 80
Listening on TCP 0.0.0.0:8000
New connection(1): tcp://127.0.0.1:41318 -> udp://192.168.1.202:8080
```


## Source
- Path: kali-tools\pwnat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.060746
