---
tool_id: bind9
title: bind9
categories: ["system-services"]
category_slugs: ["system-services"]
homepage: https://www.isc.org/downloads/bind/
repository: 
version: 9.20.15-2-Debian
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\bind9\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.803241
---

# Tool: bind9 (bind9)

## Categories
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.isc.org/downloads/bind/](https://www.isc.org/downloads/bind/) |
| Repository |  |
| Version | 9.20.15-2-Debian |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/dns-team/bind9
- **PackagesInfo**: |
- ****Installed size**: ** `719 KB`
- ****How to install**: ** `sudo apt install bind9-utils`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rndc-confgen -h
- **Usage**: []
- **-a alg**: algorithm (default hmac-sha256)
- **-k keyname**: the name as it will be used  in named.conf and rndc.conf
- **-s name**: domain name to be updated using the created key
- **-z zone**: name of the zone as it will be used in named.conf
- **-q**: suppress printing written key path
- **dnssec-importkey**: invalid argument --
- **Options**: (default value in parenthesis)
- **-f file**: read key from zone file
- **-K <directory>**: key directory
- **-L ttl**: set default key TTL
- **-V**: print version information
- **-h**: help
- **Timing options**: []
- **-P date/[+-]offset/none**: set/unset key publication date
- **-P sync date/[+-]offset/none**: set/unset CDS and CDNSKEY publication date
- **-D date/[+-]offset/none**: set/unset key deletion date
- **-D sync date/[+-]offset/none**: set/unset CDS and CDNSKEY deletion date
- **usage**: named-compilezone [-djqvD] [-c class] [-f inputformat] [-F outputformat] [-J filename] [-s (full|relative)] [-t directory] [-w directory] [-k (ignore|warn|fail)] [-m (ignore|warn|fail)] [-n (ignore|warn|fail)] [-r (ignore|warn|fail)] [-i (full|full-sibling|local|local-sibling|none)] [-M (ignore|warn|fail)] [-S (ignore|warn|fail)] [-W (ignore|warn)] -o filename zonename [ (filename|-) ]
- **named**: unknown option '-h'
- **named-journalprint**: illegal option -- h
- **named-rrchecker**: illegal option -- -
- **-o origin**: []
- **-p**: print the record in canonical format
- **-C**: generate a keyset file, for compatibility
- **-P**: disable post-sign verification
- **-T**: TTL of output records (omitted by default)
- **-u**: update or replace an existing NSEC/NSEC3 chain
- **nsec3hash**: illegal option -- h
- **Invalid option**: --help
- **Where**: []
- **q-class  is one of (in,hs,ch,...) [default**: in]
- **q-type   is one of (a,any,mx,ns,soa,hinfo,axfr,txt,...) [default**: a]
- **q-opt    is one of**: []
- **d-opt    is of the form +keyword[=value], where keyword is**: []
- **+[no]qmin[=mode]    (QNAME minimization**: relaxed or strict)
- **-y [hmac**: ]name:key  (specify named base64 tsig key)
- **+ednsopt=###[**: value] (Send specified EDNS option)
- **dnstap-read**: illegal option -- h
- **anywhere opt    is one of**: []
- **global opt      is one of**: []
- **local opt       is one of**: []
- **has two modes**: interactive and non-interactive. Interactive mode  allows
- **Interactive mode is entered in the following cases**: []
- **onds, type**: []
- **lookups. Valid keywords are**: []
- **This keyword changes the query class to one of**: []
- **nsupdate**: invalid argument --
- **host**: illegal option -- h
- **dnssec-dsfromkey**: invalid argument --
- **-1**: digest algorithm SHA-1 (deprecated)
- **-2**: digest algorithm SHA-256
- **-a algorithm**: []
- **-A**: include all keys in DS set, not just KSKs (-f only)
- **-c class**: rdata class for DS set (default IN) (-f or -s only)
- **-f zonefile**: read keys from a zone file
- **-K directory**: []
- **-s**: update key state file (default no)
- **-v level**: set level of verbosity
- **Output**: []
- **dnssec-keyfromlabel**: invalid argument --
- **Required options**: []
- **-l label**: label of the key pair
- **name**: owner of the key
- **Other options**: []
- **-3**: use NSEC3-capable algorithm
- **-c class (default**: IN)
- **-E <engine>**: name of an OpenSSL engine to use
- **-f keyflag**: KSK | REVOKE
- **-k**: generate a TYPE=KEY key
- **-M <min>**: <max>: allowed Key ID range
- **-n nametype**: ZONE | HOST | ENTITY | USER | OTHER
- **-p protocol**: default: 3 [dnssec]
- **-t type**: AUTHCONF | NOAUTHCONF | NOAUTH | NOCONF (default: AUTHCONF)
- **-y**: permit keys that might collide
- **Date options**: []
- **-P date/[+-]offset**: set key publication date
- **-P sync date/[+-]offset**: set CDS and CDNSKEY publication date
- **-A date/[+-]offset**: set key activation date
- **-R date/[+-]offset**: set key revocation date
- **-I date/[+-]offset**: set key inactivation date
- **-D date/[+-]offset**: set key deletion date
- **-D sync date/[+-]offset**: set CDS and CDNSKEY deletion date
- **-G**: generate key only; do not set -P or -A
- **-S <key>**: generate a successor to an existing key
- **-i <interval>**: prepublication interval for successor key (default: 30 days)
- **dnssec-keygen**: invalid argument --
- **-k <policy>**: name of a DNSSEC policy
- **-l <file>**: file with dnssec-policy config
- **-a <algorithm>**: []
- **-b <key size in bits>**: []
- **RSASHA1 (deprecated)**: ['1024..4096']
- **NSEC3RSASHA1 (deprecated)**: ['1024..4096']
- **RSASHA256**: ['1024..4096']
- **RSASHA512**: ['1024..4096']
- **ECDSAP256SHA256**: ignored
- **ECDSAP384SHA384**: ignored
- **ED25519**: ignored
- **ED448**: ignored
- **-n <nametype>**: ZONE | HOST | ENTITY | USER | OTHER
- **-c <class>**: (default: IN)
- **-f <keyflag>**: ZSK | KSK | REVOKE
- **-F**: FIPS mode
- **-L <ttl>**: default key TTL
- **-p <protocol>**: (default: 3 [dnssec])
- **-s <strength>**: strength value this key signs DNS records with (default: 0)
- **-T <rrtype>**: DNSKEY | KEY (default: DNSKEY; use KEY for SIG(0))
- **-t <type>**: AUTHCONF | NOAUTHCONF | NOAUTH | NOCONF (default: AUTHCONF)
- **-m <memory debugging mode>**: []
- **-v <level>**: set verbosity level
- **-A date/[+-]offset/none**: set/unset key activation date
- **-R date/[+-]offset/none**: set/unset key revocation date
- **-I date/[+-]offset/none**: set/unset key inactivation date
- **-e <date/offset>**: end date
- **-f**: force update of old-style keys
- **-i <date/offset>**: start date
- **Commands**: []
- **keygen**: pregenerate ZSKs
- **request**: create a Key Signing Request (KSR)
- **sign**: sign a KSR, creating a Signed Key Response (SKR)
- **dnssec-revoke**: invalid argument --
- **-E engine**: []
- **-r**: remove old keyfiles after creating revoked version
- **dnssec-settime**: invalid argument --
- **General options**: []
- **-P ds date/[+-]offset/none**: set/unset DS publication date
- **-D ds date/[+-]offset/none**: set/unset DS deletion date
- **Key state options**: []
- **-g state**: set the goal state for this key
- **-d state date/[+-]offset**: set the DS state
- **-k state date/[+-]offset**: set the DNSKEY state
- **-r state date/[+-]offset**: set the RRSIG (KSK) state
- **-z state date/[+-]offset**: set the RRSIG (ZSK) state
- **Printing options**: []
- **-p C/P/Psync/A/R/I/D/Dsync/all**: print a particular time value or values
- **dnssec-signzone**: invalid argument --
- **-S**: smart signing: automatically finds key files
- **-d directory**: []
- **-g**: update DS records based on child zones' dsset-* files
- **-G sync-records**: what CDNSKEY and CDS to publish
- **-s [YYYYMMDDHHMMSS|+offset]**: []
- **-e [YYYYMMDDHHMMSS|+offset|"now"+offset]**: []
- **-X [YYYYMMDDHHMMSS|+offset|"now"+offset]**: []
- **-i interval**: []
- **-j jitter**: []
- **-f outfile**: []
- **-I format**: []
- **-O format**: []
- **-N format**: []
- **-D**: []
- **-a**: generate just the key clause and write it to keyfile (/etc/bind/rndc.key)
- **-Q**: remove signatures from keys that are no longer active
- **-R**: remove signatures from keys that no longer exist
- **-T TTL**: TTL for newly added DNSKEYs
- **-t**: print statistics
- **-x**: DNSKEY record signed with KSKs only, not ZSKs
- **-z**: All records signed with KSKs
- **Signing Keys**: (default: all zone keys that have private keys)
- **dnssec-verify**: invalid argument --
- **named-checkconf**: invalid argument --
- **named-checkzone**: invalid argument --
- **named-compilezone**: invalid argument --
- **command is one of the following**: []
- **-A alg**: algorithm (default hmac-sha256)
- **-b bits**: from 1 through 512, default 256; total length of the secret
- **-c keyfile**: specify an alternate key file (requires -a)
- **-p port**: the port named will listen on and rndc will connect to
- **-s addr**: the address to which rndc should connect
- **-t chrootdir**: write a keyfile in chrootdir as well (requires -a)
- **-u user**: set the keyfile owner to "user" (requires -a)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\bind9\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.803241
