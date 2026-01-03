---
tool_id: rsmangler
title: rsmangler
categories: ["password-attacks", "utilities"]
category_slugs: ["password-attacks", "utilities"]
homepage: https://digi.ninja/projects/rsmangler.php
repository: 
version: 1.5-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords"]
icon: images/rsmangler-logo.svg
source_path: kali-tools\rsmangler\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.087600
---

# Tool: rsmangler (rsmangler)

## Categories
- [password-attacks](../password-attacks.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://digi.ninja/projects/rsmangler.php](https://digi.ninja/projects/rsmangler.php) |
| Repository |  |
| Version | 1.5-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-passwords |
| Icon | images/rsmangler-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/rsmangler
- **PackagesInfo**: |
- ****Installed size**: ** `24 KB`
- ****How to install**: ** `sudo apt install rsmangler`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rsmangler -h
- **rsmangler v 1.5 Robin Wood (robin@digi.ninja) <https**: //digi.ninja>
- **Basic usage**: []
- **To pass the initial words in on standard in do**: []
- **To send the output to a file**: []
- **Usage**: rsmangler [OPTION]
- **--help, -h**: show help
- **--file, -f**: the input file, use - for STDIN
- **--output, -o**: the output file, use - for STDOUT
- **--max, -x**: maximum word length
- **--min, -m**: minimum word length
- **--perms, -p**: permutate all the words
- **--double, -d**: double each word
- **--reverse, -r**: reverser the word
- **--leet, -t**: l33t speak the word
- **--full-leet, -T**: all posibilities l33t
- **--capital, -c**: capitalise the word
- **--upper, -u**: uppercase the word
- **--lower, -l**: lowercase the word
- **--swap, -s**: swap the case of the word
- **--ed, -e**: add ed to the end of the word
- **--ing, -i**: add ing to the end of the word
- **--punctuation**: add common punctuation to the end of the word
- **--years, -y**: add all years from 1990 to current year to start and end
- **--acronym, -a**: create an acronym based on all the words entered in order and add to word list
- **--common, -C**: add the following words to start and end: admin, sys, pw, pwd
- **--pna**: add 01 - 09 to the end of the word
- **--pnb**: add 01 - 09 to the beginning of the word
- **--na**: add 1 - 123 to the end of the word
- **--nb**: add 1 - 123 to the beginning of the word
- **--force**: don't check output size
- **--space**: add spaces between words
- **--allow-duplicates**: allow duplicates in the output list


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## rsmangler Usage Example

Use the original wordlist (`cat words.txt |`) and mangle words with a minimum length of 6 (`-m 6`) and maximum length of 8 (`-x 8`), using stdin as input (`–file -`) and redirecting the results to a new wordlist (`> mangled.txt`):

```console
root@kali:~# cat words.txt | rsmangler -m 6 -x 8 --file - > mangled.txt
root@kali:~# wc -l mangled.txt
367 mangled.txt
root@kali:~# wc -l words.txt
3 words.txt
```


## Source
- Path: kali-tools\rsmangler\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.087600
