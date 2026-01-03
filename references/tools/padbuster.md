---
tool_id: padbuster
title: padbuster
categories: ["web-application-analysis", "vulnerability-analysis", "exploitation-tools"]
category_slugs: ["web-application-analysis", "vulnerability-analysis", "exploitation-tools"]
homepage: https://github.com/GDSSecurity/PadBuster
repository: 
version: 0.3.3+git20210818.50e4a3e-1kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\padbuster\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.037312
---

# Tool: padbuster (padbuster)

## Categories
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/GDSSecurity/PadBuster](https://github.com/GDSSecurity/PadBuster) |
| Repository |  |
| Version | 0.3.3+git20210818.50e4a3e-1kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/padbuster
- **PackagesInfo**: |
- ****Installed size**: ** `40 KB`
- ****How to install**: ** `sudo apt install padbuster`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# padbuster -h
- **Use**: padbuster URL EncryptedSample BlockSize [options]
- **Where**: URL = The target URL (and query string if applicable)
- **Options**: []
- **-auth [username**: password]: HTTP Basic Authentication
- **-bruteforce**: Perform brute force against the first block
- **-ciphertext [Bytes]**: CipherText for Intermediate Bytes (Hex-Encoded)
- **-cookies [HTTP Cookies]**: Cookies (name1=value1; name2=value2)
- **-encoding [0-4]**: Encoding Format of Sample (Default 0)
- **-encodedtext [Encoded String]**: Data to Encrypt (Encoded)
- **-error [Error String]**: Padding Error Message
- **-headers [HTTP Headers]**: Custom Headers (name1::value1;name2::value2)
- **-interactive**: Prompt for confirmation on decrypted bytes
- **-intermediate [Bytes]**: Intermediate Bytes for CipherText (Hex-Encoded)
- **-log**: Generate log files (creates folder PadBuster.DDMMYY)
- **-noencode**: Do not URL-encode the payload (encoded by default)
- **-noiv**: Sample does not include IV (decrypt first block)
- **-plaintext [String]**: Plain-Text to Encrypt
- **-post [Post Data]**: HTTP Post Data String
- **-prefix [Prefix]**: Prefix bytes to append to each sample (Encoded)
- **-proxy [address**: port]: Use HTTP/S Proxy
- **-proxyauth [username**: password]: Proxy Authentication
- **-resume [Block Number]**: Resume at this block number
- **-usebody**: Use response body content for response analysis phase
- **-verbose**: Be Verbose
- **-veryverbose**: Be Very Verbose (Debug Only)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\padbuster\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.037312
