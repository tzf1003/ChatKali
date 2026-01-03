---
tool_id: openssh
title: openssh
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.openssh.com/
repository: 
version: 1:10.2p1-2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-linux-wsl"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\openssh\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.027214
---

# Tool: openssh (openssh)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.openssh.com/](https://www.openssh.com/) |
| Repository |  |
| Version | 1:10.2p1-2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-linux-wsl |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/ssh-team/openssh
- **PackagesInfo**: |
- ****Installed size**: ** `214 KB`
- ****How to install**: ** `sudo apt install ssh-askpass-gnome`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sshd -h
- **scp**: unknown option -- h
- **usage**: sshd [-46DdeGiqTtV] [-C connection_spec] [-c host_cert_file]
- **[-c cipher_spec] [-D [bind_address**: ]port] [-E log_file]
- **[-S ctl_path] [-W host**: port] [-w local_tun[:remote_tun]]
- **The options are as follows**: []
- **prints.  Valid options are**: "md5" and "sha256".  The default  is
- **ssh_config(5)    known    hosts    files**: ~/.ssh/known_hosts,
- **port**: host:hostport] [-R port:host:hostport] [-D port] [command]
- **Usage**: /usr/bin/ssh-copy-id [-h|-?|-f|-n|-s|-x] [-i [identity_file]] [-t target_path] [-F ssh_config] [[-o ssh_option] ...] [-p port] [user@]hostname
- **-f**: force mode -- copy keys without trying to check if they are already installed
- **-n**: dry run    -- no keys are actually copied
- **-s**: use sftp   -- use sftp instead of executing remote-commands. Can be useful if the remote only allows sftp
- **-x**: debug      -- enables -x in this shell, for debugging
- **-h|-?**: print this help
- **protocol described in**: []
- **http**: //www.openssh.com/txt/draft-ietf-secsh-filexfer-02.txt


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\openssh\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.027214
