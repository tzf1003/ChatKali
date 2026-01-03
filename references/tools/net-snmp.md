---
tool_id: net-snmp
title: net-snmp
categories: ["information-gathering", "utilities"]
category_slugs: ["information-gathering", "utilities"]
homepage: https://net-snmp.sourceforge.net/
repository: 
version: 5.9.4.pre2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-protect kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\net-snmp\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.005691
---

# Tool: net-snmp (net-snmp)

## Categories
- [information-gathering](../information-gathering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://net-snmp.sourceforge.net/](https://net-snmp.sourceforge.net/) |
| Repository |  |
| Version | 5.9.4.pre2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-protect kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/net-snmp
- **PackagesInfo**: |
- ****Installed size**: ** `1.62 MB`
- ****How to install**: ** `sudo apt install tkmib`
- **{{< spoiler "Dependencies**: " >}}
- **NOTE**: If you want the OIDs (Object Identifiers) to resolve to their text
- **root@kali**: ~# tkmib -h
- **Usage**: snmptrapd [OPTIONS] [LISTENING ADDRESSES]
- **SNMP Setup commands**: []
- **building external SNMP applications**: []
- **Automated subagent building (produces an OUTPUTNAME binary file)**: []
- **Details on how the net-snmp package was compiled**: []
- **USAGE**: snmpwalk [OPTIONS] AGENT [OID]
- **Web**: http://www.net-snmp.org/
- **Email**: net-snmp-coders@lists.sourceforge.net
- **OPTIONS**: []
- **-m MIB[**: ...]		load given list of MIBs (ALL loads everything)
- **-M DIR[**: ...]		look in given list of directories for MIBs
- **-P MIBOPTS		Toggle various defaults controlling mib parsing**: []
- **u**: print OIDs using UCD-style prefix suppression
- **c**: do not check returned OIDs are increasing
- **d**: save the DESCRIPTIONs of the MIB objects
- **e**: log to standard error
- **w**: enable warnings when MIB symbols conflict
- **W**: enable detailed warnings when MIB symbols conflict
- **R**: do random access to OID labels
- **-L LOGOPTS		Toggle various defaults controlling logging**: []
- **o**: log to standard output
- **n**: don't log at all
- **f file**: log to the specified file
- **s facility**: log to syslog (via the specified facility)
- **[EON] pri**: log to standard error, output or /dev/null for level 'pri' and above
- **[EON] p1-p2**: log to standard error, output or /dev/null for levels 'p1' to 'p2'
- **[FS] pri token**: log to file/syslog for level 'pri' and above
- **[FS] p1-p2 token**: log to file/syslog for levels 'p1' to 'p2'
- **TRAP-PARAMETERS**: []
- **Passphrase will be taken from the first successful source as follows**: []
- **MIB search path**: /root/.snmp/mibs:/usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf
- **Cannot find module (SNMPv2-MIB)**: At line 1 in (none)
- **Cannot find module (IF-MIB)**: At line 1 in (none)
- **Cannot find module (IP-MIB)**: At line 1 in (none)
- **Cannot find module (TCP-MIB)**: At line 1 in (none)
- **Cannot find module (UDP-MIB)**: At line 1 in (none)
- **Cannot find module (HOST-RESOURCES-MIB)**: At line 1 in (none)
- **Cannot find module (NOTIFICATION-LOG-MIB)**: At line 1 in (none)
- **Cannot find module (DISMAN-EVENT-MIB)**: At line 1 in (none)
- **Cannot find module (DISMAN-SCHEDULE-MIB)**: At line 1 in (none)
- **Cannot find module (HOST-RESOURCES-TYPES)**: At line 1 in (none)
- **Cannot find module (MTA-MIB)**: At line 1 in (none)
- **Cannot find module (NETWORK-SERVICES-MIB)**: At line 1 in (none)
- **Cannot find module (SNMPv2-TC)**: At line 25 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
- **Cannot find module (SNMPv2-SMI)**: At line 8 in /usr/share/snmp/mibs/NET-SNMP-MIB.txt
- **Cannot find module (HCNUM-TC)**: At line 37 in /usr/share/snmp/mibs/UCD-SNMP-MIB.txt
- **Unlinked OID in UCD-SNMP-MIB**: ucdavis ::= { enterprises 2021 }
- **Undefined identifier**: netSnmpObjects near line 28 of /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
- **Unlinked OID in UCD-DISKIO-MIB**: ucdDiskIOMIB ::= { ucdExperimental 15 }
- **Unlinked OID in UCD-DLMOD-MIB**: ucdDlmodMIB ::= { ucdExperimental 14 }
- **Unlinked OID in LM-SENSORS-MIB**: lmSensors ::= { ucdExperimental 16 }
- **Unlinked OID in UCD-DEMO-MIB**: ucdDemoMIB ::= { ucdavis 14 }
- **Cannot find module (SNMP-TARGET-MIB)**: At line 1 in (none)
- **Cannot find module (SNMP-FRAMEWORK-MIB)**: At line 9 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
- **Unlinked OID in NET-SNMP-MIB**: netSnmp ::= { enterprises 8072 }
- **Unlinked OID in NET-SNMP-AGENT-MIB**: nsNotifyStart ::= { netSnmpNotifications 1 }
- **Cannot find module (SNMP-MPD-MIB)**: At line 1 in (none)
- **Cannot find module (SNMP-USER-BASED-SM-MIB)**: At line 1 in (none)
- **Cannot find module (SNMP-VIEW-BASED-ACM-MIB)**: At line 16 in /usr/share/snmp/mibs/NET-SNMP-VACM-MIB.txt
- **Cannot find module (SNMP-COMMUNITY-MIB)**: At line 1 in (none)
- **Cannot find module (IPV6-ICMP-MIB)**: At line 1 in (none)
- **Cannot find module (IPV6-MIB)**: At line 1 in (none)
- **Cannot find module (IPV6-TCP-MIB)**: At line 1 in (none)
- **Cannot find module (IPV6-UDP-MIB)**: At line 1 in (none)
- **Cannot find module (IP-FORWARD-MIB)**: At line 1 in (none)
- **Cannot find module (INET-ADDRESS-MIB)**: At line 13 in /usr/share/snmp/mibs/NET-SNMP-EXAMPLES-MIB.txt
- **Unlinked OID in NET-SNMP-EXAMPLES-MIB**: netSnmpExamples ::= { netSnmp 2 }
- **Unlinked OID in NET-SNMP-PASS-MIB**: netSnmpPassExamples ::= { netSnmpExamples 255 }
- **Unlinked OID in NET-SNMP-EXTEND-MIB**: netSnmpExtendMIB ::= { nsExtensions 1 }
- **Cannot find module (SNMP-NOTIFICATION-MIB)**: At line 1 in (none)
- **Cannot find module (SNMPv2-TM)**: At line 1 in (none)
- **Unlinked OID in NET-SNMP-VACM-MIB**: netSnmpVacmMIB ::= { netSnmpObjects 9 }
- **Cannot adopt OID in UCD-SNMP-MIB**: laIndex ::= { laEntry 1 }
- **Cannot adopt OID in NET-SNMP-VACM-MIB**: netSnmpVacmMIB ::= { netSnmpObjects 9 }
- **Cannot adopt OID in UCD-DEMO-MIB**: ucdDemoMIB ::= { ucdavis 14 }
- **Cannot adopt OID in UCD-DLMOD-MIB**: ucdDlmodMIB ::= { ucdExperimental 14 }
- **Cannot adopt OID in NET-SNMP-EXAMPLES-MIB**: netSnmpIETFWGTable ::= { netSnmpExampleTables 1 }
- **Cannot adopt OID in NET-SNMP-MIB**: netSnmp ::= { enterprises 8072 }
- **Cannot adopt OID in NET-SNMP-AGENT-MIB**: nsNotifyRestart ::= { netSnmpNotifications 3 }
- **Cannot adopt OID in NET-SNMP-EXTEND-MIB**: nsExtendLineIndex ::= { nsExtendOutput2Entry 1 }
- **Cannot adopt OID in UCD-DISKIO-MIB**: diskIOTable ::= { ucdDiskIOMIB 1 }
- **Cannot adopt OID in LM-SENSORS-MIB**: lmSensorsMIB ::= { lmSensors 1 }
- **Cannot adopt OID in NET-SNMP-PASS-MIB**: netSnmpPassIndex ::= { netSnmpPassEntry 1 }
- **(default**: $HOME/.snmp/mibs:/usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf)
- **-P MIBOPTS		Toggle various defaults controlling MIB parsing**: []
- **-O OUTOPTS		Toggle various defaults controlling output display**: []
- **0**: print leading 0 for single-digit hex characters
- **a**: print all strings in ascii format
- **b**: do not break OID indexes down
- **E**: escape quotes in string indices
- **f**: print full OIDs on output
- **p PRECISION**: display floating point values with specified PRECISION (printf format string)
- **q**: quick print for easier parsing
- **Q**: quick print with equal-signs
- **s**: print only last symbolic element of OID
- **S**: print MIB module-id plus last element
- **t**: print timeticks unparsed as numeric integers
- **T**: print human-readable text along with hex strings
- **U**: don't print units
- **v**: print values only (not OID = value)
- **x**: print all strings in hex format
- **X**: extended index format
- **-I INOPTS		Toggle various defaults controlling input parsing**: []
- **h**: don't apply DISPLAY-HINTs
- **r**: do not check values for range/type legality
- **s SUFFIX**: Append all textual OIDs with SUFFIX before parsing
- **S PREFIX**: Prepend all textual OIDs with PREFIX before parsing
- **-C APPOPTS		Set various application specific behaviours**: []
- **n<NUM>**: set non-repeaters to <NUM>
- **r<NUM>**: for GETBULK: set max-repeaters to <NUM>
- **i**: include given OID in the search range
- **p**: print the number of variables found
- **X Options**: []
- **-V NUM	sets the initial verbosity level of the command log (def**: 1)
- **Ascii Options**: []
- **options**: []
- **snmpdf options**: []
- **-C APPOPTS		Set various application specific behaviour**: []
- **-v 1 TRAP-PARAMETERS**: []
- **-v 2 TRAP-PARAMETERS**: []
- **usage**: snmpnetstat [snmp_opts] [-Canv] [-Cf address_family]
- **snmpping options**: []
- **snmpps options**: []
- **TYPE**: one of i, u, t, a, o, s, x, d, b
- **B**: print all matching objects for a regex search
- **c<NUM>**: print table in columns of <NUM> chars width
- **f<STR>**: print table delimitied with <STR>
- **H**: print no column headers
- **l**: enable labeled OID report
- **for GETNEXT**: retrieve <NUM> entries at a time
- **w<NUM>**: print table in parts of <NUM> chars width
- **snmptranslate**: invalid option -- '-'
- **invalid option**: -?
- **-T TRANSOPTS		Set various options controlling report produced**: []
- **z**: enable MIB child OID report
- **snmpusm commands**: []
- **snmpusm options**: []
- **snmpvacm commands**: []
- **I**: don't include the given OID, even if no results are returned
- **E {OID}**: End the walk at the specified OID
- **unknown suboption to /usr/bin/net-snmp-create-v3-user**: -h
- **(config search path**: /etc/snmp:/usr/share/snmp:/usr/lib/x86_64-linux-gnu/snmp:/root/.snmp)
- **(default $HOME/.snmp/mibs**: /usr/share/snmp/mibs:/usr/share/snmp/mibs/iana:/usr/share/snmp/mibs/ietf)
- **Deprecated options**: []
- **NET-SNMP Version**: 5.9.4.pre2
- **Options**: []
- **-f fromaddress     Sets the email address to be used on the From**: line.
- **-f CONFIG_FILE  load CONFIG_FILE after starting up. (default**: ~/.snmp/tkmibrc)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\net-snmp\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.005691
