---
tool_id: tlssled
title: tlssled
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: http://www.taddong.com/en/lab.html
repository: 
version: 1.3-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\tlssled\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.144634
---

# Tool: tlssled (tlssled)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://www.taddong.com/en/lab.html](http://www.taddong.com/en/lab.html) |
| Repository |  |
| Version | 1.3-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/tlssled
- **PackagesInfo**: |
- ****Installed size**: ** `38 KB`
- ****How to install**: ** `sudo apt install tlssled`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# tlssled -h


## Documentation (Upstream)
---------------------------------------------------
  TLSSLed - (1.3) based on sslscan and openssl
                  by Raul Siles (www.taddong.com)
 ------------------------------------------------------
     openssl version: OpenSSL 3.5.4 30 Sep 2025 (Library: OpenSSL 3.5.4 30 Sep 2025)
     
 ------------------------------------------------------
     Date: 20251127-114634
 ------------------------------------------------------
 
 [!] Usage: /usr/bin/tlssled <hostname or IP_address> <port>
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## TLSSLed Usage Example

Check SSL/TLS on the host (`192.168.1.1`) and port (`443`):

```console
root@kali:~# tlssled 192.168.1.1 443
------------------------------------------------------
 TLSSLed - (1.3) based on sslscan and openssl
                 by Raul Siles (www.taddong.com)
------------------------------------------------------
    openssl version: OpenSSL 1.0.1e 11 Feb 2013
    sslscan version 1.8.2
------------------------------------------------------
    Date: 20140513-165131
------------------------------------------------------

[*] Analyzing SSL/TLS on 192.168.1.1:443 ...
    [.] Output directory: TLSSLed_1.3_192.168.1.1_443_20140513-165131 ...

[*] Checking if the target service speaks SSL/TLS...
    [.] The target service 192.168.1.1:443 seems to speak SSL/TLS...

    [.] Using SSL/TLS protocol version:
        (empty means I'm using the default openssl protocol version(s))

[*] Running sslscan on 192.168.1.1:443 ...

    [-] Testing for SSLv2 ...

    [-] Testing for the NULL cipher ...
```


## Source
- Path: kali-tools\tlssled\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.144634
