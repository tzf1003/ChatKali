---
tool_id: s3scanner
title: s3scanner
categories: ["information-gathering", "vulnerability-analysis"]
category_slugs: ["information-gathering", "vulnerability-analysis"]
homepage: https://github.com/sa7mon/s3scanner
repository: 
version: 3.0.0-0kali2
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\s3scanner\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.091466
---

# Tool: s3scanner (s3scanner)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sa7mon/s3scanner](https://github.com/sa7mon/s3scanner) |
| Repository |  |
| Version | 3.0.0-0kali2 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/s3scanner
- **PackagesInfo**: |
- **The features are**: []
- ****Installed size**: ** `17.85 MB`
- ****How to install**: ** `sudo apt install s3scanner`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# s3scanner -h
- **INPUT**: (1 required)
- **-mq                    Connect to RabbitMQ to get buckets. Requires config file key "mq". Default**: false
- **OUTPUT**: []
- **-db       Save results to a Postgres database. Requires config file key "db.uri". Default**: false
- **-json     Print logs to stdout in JSON format instead of human-readable. Default**: false
- **OPTIONS**: []
- **-enumerate           Enumerate bucket objects (can be time-consuming). Default**: false
- **-provider    string  Object storage provider**: aws, custom, digitalocean, dreamhost, gcp, linode - custom requires config file. Default: "aws"
- **-threads     int     Number of threads to scan with. Default**: 4
- **DEBUG**: []
- **-verbose     Enable verbose logging. Default**: false
- **-version     Print version Default**: false
- **If config file is required these locations will be searched for config.yml**: ." "/etc/s3scanner/" "$HOME/.s3scanner/


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\s3scanner\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.091466
