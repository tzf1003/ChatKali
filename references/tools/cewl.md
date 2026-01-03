---
tool_id: cewl
title: cewl
categories: ["information-gathering", "password-attacks"]
category_slugs: ["information-gathering", "password-attacks"]
homepage: https://github.com/digininja/CeWL
repository: 
version: 6.2.1-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: images/cewl-logo.svg
source_path: kali-tools\cewl\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.831280
---

# Tool: cewl (cewl)

## Categories
- [information-gathering](../information-gathering.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/digininja/CeWL](https://github.com/digininja/CeWL) |
| Repository |  |
| Version | 6.2.1-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | images/cewl-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/cewl
- **PackagesInfo**: |
- ****Installed size**: ** `81 KB`
- ****How to install**: ** `sudo apt install cewl`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fab-cewl -h
- **CeWL 6.2.1 (More Fixes) Robin Wood (robin@digi.ninja) (https**: //digi.ninja/)
- **Usage**: fab-cewl [OPTION] ... filename/list
- **OPTIONS**: []
- **-h, --help**: show help
- **-k, --keep**: Keep the downloaded file.
- **-d <x>,--depth <x>**: Depth to spider to, default 2.
- **-m, --min_word_length**: Minimum word length, default 3.
- **-x, --max_word_length**: Maximum word length, default unset.
- **-o, --offsite**: Let the spider visit other sites.
- **--exclude**: A file containing a list of paths to exclude
- **--allowed**: A regex pattern that path must match to be followed
- **-w, --write**: Write the output to the file.
- **-u, --ua <agent>**: User agent to send.
- **-n, --no-words**: Don't output the wordlist.
- **-g <x>, --groups <x>**: Return groups of words as well
- **--lowercase**: Lowercase all parsed words
- **--with-numbers**: Accept words with numbers in as well as just letters
- **--convert-umlauts**: Convert common ISO-8859-1 (Latin-1) umlauts (ä-ae, ö-oe, ü-ue, ß-ss)
- **-a, --meta**: include meta data.
- **--meta_file file**: Output file for meta data.
- **-e, --email**: Include email addresses.
- **--email_file <file>**: Output file for email addresses.
- **--meta-temp-dir <dir>**: The temporary directory used by exiftool when parsing files, default /tmp.
- **-c, --count**: Show the count for each word found.
- **-v, --verbose**: Verbose.
- **--debug**: Extra debug information.
- **--auth_type**: Digest or basic.
- **--auth_user**: Authentication username.
- **--auth_pass**: Authentication password.
- **--proxy_host**: Proxy host.
- **--proxy_port**: Proxy port, default 8080.
- **--proxy_username**: Username for proxy, if required.
- **--proxy_password**: Password for proxy, if required.
- **--header, -H**: In format name:value - can pass multiple.
- **<url>**: The site to spider.
- **-v**: verbose
- **filename/list**: the file or list of files to check


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## cewl Usage Example

Scan to a depth of 2 (`-d 2`) and use a minimum word length of 5 (`-m 5`), save the words to a file (`-w docswords.txt`), targeting the given URL (`https://example.com`):

```console
root@kali:~# cewl -d 2 -m 5 -w docswords.txt https://example.com
CeWL 5.4.3 (Arkanoid) Robin Wood (robin@digi.ninja) (https://digi.ninja/)
root@kali:~# wc -l docswords.txt
13 docswords.txt
```


## Source
- Path: kali-tools\cewl\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.831280
