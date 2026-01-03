---
tool_id: impacket-scripts
title: impacket-scripts
categories: ["information-gathering", "post-exploitation", "password-attacks"]
category_slugs: ["information-gathering", "post-exploitation", "password-attacks"]
homepage: []
repository: 
version: 1.10
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-respond kali-tools-vulnerability"]
icon: images/impacket-scripts-logo.svg
source_path: kali-tools\impacket-scripts\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.944979
---

# Tool: impacket-scripts (impacket-scripts)

## Categories
- [information-gathering](../information-gathering.md)
- [post-exploitation](../post-exploitation.md)
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage |  |
| Repository |  |
| Version | 1.10 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-respond kali-tools-vulnerability |
| Icon | images/impacket-scripts-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/impacket-scripts
- **PackagesInfo**: |
- ****Installed size**: ** `65 KB`
- ****How to install**: ** `sudo apt install impacket-scripts`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# impacket-wmiquery -h
- **usage**: wmiquery.py [-h] [-namespace NAMESPACE] [-file FILE] [-debug] [-ts]
- **positional arguments**: []
- **options**: []
- **[-hashes LMHASH**: NTHASH] [-no-pass] [-k] [-aesKey hex key]
- **target                [[domain/]username[**: password]@]<targetName or address>
- **-base-dir BASE_DIR    Directory to search in (Default**: /)
- **authentication**: []
- **-hashes LMHASH**: NTHASH
- **NTLM hashes, format is LMHASH**: NTHASH
- **connection**: []
- **target                domain[/username[**: password]]
- **[-outputfile OUTPUTFILE] [-hashes LMHASH**: NTHASH]
- **[-debug] [-hashes LMHASH**: NTHASH] [-no-pass] [-k]
- **specified. Example**: `workstation01$`
- **[domain/]username[**: password]
- **LDAP**: []
- **[-codec CODEC] [-hashes LMHASH**: NTHASH] [-no-pass] [-k]
- **chcp.com at the target, map the result with https**: //do
- **-newhashes LMHASH**: NTHASH
- **New credentials for target**: []
- **new NTLM hashes, format is NTHASH or LMHASH**: NTHASH
- **Authentication (target user whose password is changed)**: []
- **NTLM hashes, format is NTHASH or LMHASH**: NTHASH
- **Authentication (optional, privileged user performing the change)**: []
- **Alternative NT hash, format is NTHASH or LMHASH**: NTHASH
- **Method of operations**: []
- **Kerberos authentication**: []
- **identity              domain.local/username[**: password]
- **authentication & connection**: []
- **principal**: []
- **target**: []
- **dacl editor**: []
- **added or removed (default**: allowed)
- **Rights to write/remove in the target DACL (default**: []
- **-mask [MASK]          Force access mask, possible values**: readwrite, write,
- **[-com-version MAJOR_VERSION**: MINOR_VERSION]
- **-com-version MAJOR_VERSION**: MINOR_VERSION
- **DCOM version, format is MAJOR_VERSION**: MINOR_VERSION
- **Ticket decryption credentials (optional)**: []
- **account's Kerberos keys.(example**: if the ticket is for user:"john" for
- **service**: "cifs/service.domain.local", you need to supply credentials or
- **PAC Credentials decryption material**: []
- **(https**: //www.thehacker.recipes/ad/movement/kerberos/unpac-the-hash)
- **[-user USER] [-disabled] [-hashes LMHASH**: NTHASH]
- **credentials           domain/username[**: password]. Valid domain credentials
- **identity              [domain/]username[**: password]
- **[-tf TF] [-hashes LMHASH**: NTHASH] [-no-pass] [-k]
- **LIST option**: []
- **volume            NTFS volume to open (e.g. \\.\C**: or /dev/disk1s1)
- **[-auth-smb [domain/]username[**: password]]
- **[-hashes-smb LMHASH**: NTHASH] [-rpc-smb-port {139,445}]
- **[-machine-hashes LMHASH**: NTHASH] [-domain DOMAIN]
- **Main options**: []
- **hostname or URL like domain\username@host**: port
- **("0.0.0.0" or "**: :" if omitted)
- **`-`. Ex**: `80,8000-8010`
- **-r SMBSERVER          Redirect HTTP requests to a file**: // path on SMBSERVER
- **dumps will be stored (default**: current directory).
- **Server (16 hex bytes long. eg**: 1122334455667788)
- **SMB client options**: []
- **RPC client options**: []
- **-auth-smb [domain/]username[**: password]
- **-hashes-smb LMHASH**: NTHASH
- **MSSQL client options**: []
- **HTTP options**: []
- **-machine-hashes LMHASH**: NTHASH
- **Domain machine hashes, format is LMHASH**: NTHASH
- **LDAP client options**: []
- **Common options for SMB and LDAP**: []
- **IMAP client options**: []
- **Mailbox name to dump. Default**: INBOX
- **Max number of emails to dump (0 = unlimited, default**: []
- **AD CS attack options**: []
- **Shadow Credentials attack options**: []
- **SCCM Policies attack options**: []
- **'http**: //<MP>/ccm_system_windowsauth/request'
- **SCCM Distribution Point attack options**: []
- **target 'http**: //<DP>/sms_dp_smspkg$/Datalib'
- **owner**: []
- **Use**: /usr/share/doc/python3-impacket/examples/ping6.py <src ip> <dst ip>
- **target (w/o path) - (default**: cmd.exe)
- **target                domain/username[**: password]
- **[-hashes-rpc LMHASH**: NTHASH] [-hashes-transport LMHASH:NTHASH]
- **stringbinding         String binding to connect to MSRPC interface, for example**: []
- **ncacn_ip_tcp**: 192.168.0.1[135]
- **ncacn_np**: 192.168.0.1[\pipe\spoolss]
- **ncacn_http**: localhost[3388,RpcProxy=rds.contoso:443]
- **ncacn-np-details**: []
- **-auth-rpc AUTH_RPC    [domain/]username[**: password]
- **-hashes-rpc LMHASH**: NTHASH
- **-hashes-transport LMHASH**: NTHASH
- **[-debug] [-ts] [-hashes LMHASH**: NTHASH] [-no-pass] [-k]
- **[-password PASSWORD] [-hashes LMHASH**: NTHASH]
- **hash. Example**: smbserver.py -comment 'My share' TMP /tmp
- **NTLM hashes for the Username, format is LMHASH**: NTHASH
- **ip address of listening interface ("0.0.0.0" or "**: :"
- **Warning**: This functionality will be deprecated in the next Impacket version
- **Please select an interface**: []
- **Ignoring unknown protocol**: -h
- **Traceback (most recent call last)**: []
- **pcapy.PcapError**: -h: No such file or directory
- **target                [domain/][username[**: password]@]<address>


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\impacket-scripts\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.944979
