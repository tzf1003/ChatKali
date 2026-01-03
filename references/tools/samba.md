---
tool_id: samba
title: samba
categories: ["system-services"]
category_slugs: ["system-services"]
homepage: https://www.samba.org
repository: 
version: 2:4.23.3+dfsg-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-detect kali-tools-forensics kali-tools-information-gathering kali-tools-passwords kali-tools-respond kali-tools-top10 kali-tools-vulnerability kali-tools-web kali-tools-wireless"]
icon: images/samba-logo.svg
source_path: kali-tools\samba\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.095024
---

# Tool: samba (samba)

## Categories
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.samba.org](https://www.samba.org) |
| Repository |  |
| Version | 2:4.23.3+dfsg-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-detect kali-tools-forensics kali-tools-information-gathering kali-tools-passwords kali-tools-respond kali-tools-top10 kali-tools-vulnerability kali-tools-web kali-tools-wireless |
| Icon | images/samba-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/samba-team/samba
- **PackagesInfo**: |
- **Features include**: []
- ****Installed size**: ** `4.89 MB`
- ****How to install**: ** `sudo apt install samba`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# eventlogadm -h
- **Usage**: eventlogadm [OPTION]
- **Help options**: []
- **options**: []
- **Options**: []
- **for the input database**: []
- **0**: no ctdb header
- **32**: ctdb header size of a 32 bit system (20 bytes)
- **64**: ctdb header size of a 64 bit system (24 bytes)
- **default**: 32 or 64 depending on the system architecture
- **Commands**: []
- **/usr/bin/onnode**: illegal option -- -
- **ctdb(7), https**: //wiki.samba.org/index.php/Ping_pong
- **with this program; if not, see http**: //www.gnu.org/licenses.
- **Common Samba options**: []
- **Connection options**: []
- **Credential options**: []
- **Deprecated legacy options**: []
- **-k, --kerberos=STRING                        DEPRECATED**: Migrate to
- **Version options**: []
- **application. It supports three kinds of events**: timed events, file
- **Samba Common Options**: []
- **Version Options**: []
- **Credentials Options**: []
- **DEPRECATED**: Migrate to --use-kerberos
- **use colour if available (default**: auto)
- **Available subcommands**: []
- **For more help on a specific subcommand, please type**: samba-tool <subcommand> (-h|--help)
- **Miscellaneous options**: []
- **Active eventlog names**: []


## Documentation (Upstream)
-----------------------------------
 	<None specified>
 ```
 
 - - -
 
 ##### mvxattr
 
 Recursively rename extended attributes
 
 ```
 root@kali:~# mvxattr --help
 Usage: mvxattr -s STRING -d STRING PATH [PATH ...]
   -s, --from=STRING         xattr source name
   -d, --to=STRING           xattr destination name
   -l, --follow-symlinks     follow symlinks, the default is to ignore them
   -p, --print               print files where the xattr got renamed
   -v, --verbose             print files as they are checked
   -f, --force               force overwriting of destination xattr
 
 Help options:
   -?, --help                Show this help message
       --usage               Display brief usage message
 ```
 
 - - -
 
 ##### nmbd
 
 NetBIOS name server to provide NetBIOS over IP naming services to clients
 
 ```
 root@kali:~# nmbd --help
 Usage: nmbd [OPTION...]
   -H, --hosts=STRING                 Load a netbios hosts file
   -p, --port=INT                     Listen on the specified port
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Daemon options:
   -D, --daemon                       Become a daemon (default)
   -i, --interactive                  Run interactive (not a daemon) and log to
                                      stdout
   -F, --foreground                   Run daemon in foreground (for
                                      daemontools, etc.)
       --no-process-group             Don't create a new process group
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ##### oLschema2ldif
 
 Converts LDAP schema's to LDB-compatible LDIF
 
 ```
 root@kali:~# oLschema2ldif --help
 Usage: [OPTION...]
   -b, --basedn=DN             base DN
   -I, --input=inputfile       inputfile of OpenLDAP style schema otherwise
                               STDIN
   -O, --output=outputfile     outputfile otherwise STDOUT
 
 Help options:
   -?, --help                  Show this help message
       --usage                 Display brief usage message
 
 Version options:
   -V, --version               Print version
 ```
 
 - - -
 
 ##### pdbedit
 
 Manage the SAM database (Database of Samba Users)
 
 ```
 root@kali:~# pdbedit --help
 Usage: [OPTION...]
   -L, --list                            list all users
   -v, --verbose                         be verbose
   -w, --smbpasswd-style                 give output in smbpasswd style
   -u, --user=USER                       use username
   -N, --account-desc=STRING             set account description
   -f, --fullname=STRING                 set full name
   -h, --homedir=STRING                  set home directory
   -D, --drive=STRING                    set home drive
   -S, --script=STRING                   set logon script
   -p, --profile=STRING                  set profile path
   -I, --domain=STRING                   set a users' domain
   -U, --user SID=STRING                 set user SID or RID
   -M, --machine SID=STRING              set machine SID or RID
   -a, --create                          create user
   -r, --modify                          modify user
   -m, --machine                         account is a machine account
   -x, --delete                          delete user
   -b, --backend=STRING                  use different passdb backend as
                                         default backend
   -i, --import=STRING                   import user accounts from this backend
   -e, --export=STRING                   export user accounts to this backend
   -g, --group                           use -i and -e for groups
   -y, --policies                        use -i and -e to move account policies
                                         between backends
       --policies-reset                  restore default policies
   -P, --account-policy=STRING           value of an account policy (like
                                         maximum password age)
   -C, --value=LONG                      set the account policy to this value
   -c, --account-control=STRING          Values of account control
       --force-initialized-passwords     Force initialization of corrupt
                                         password strings in a passdb backend
   -z, --bad-password-count-reset        reset bad password count
   -Z, --logon-hours-reset               reset logon hours
       --time-format=STRING              The time format for time parameters
   -t, --password-from-stdin             get password from standard in
   -K, --kickoff-time=STRING             set the kickoff time
       --set-nt-hash=STRING              set password from nt-hash
 
 Help options:
   -?, --help                            Show this help message
       --usage                           Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL           Set debug level
       --debug-stdout                    Send debug output to standard output
   -s, --configfile=CONFIGFILE           Use alternative configuration file
       --option=name=value               Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE        Basename for log/debug files
       --leak-report                     enable talloc leak reporting on exit
       --leak-report-full                enable full talloc leak reporting on
                                         exit
 
 Version options:
   -V, --version                         Print version
 ```
 
 - - -
 
 ##### profiles
 
 A utility to report and change SIDs in registry files
 
 ```
 root@kali:~# profiles --help
 Usage: <profilefile>
   -c, --change-sid=STRING            Provides SID to change
   -n, --new-sid=STRING               Provides SID to change to
   -v, --verbose                      Verbose output
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ##### sharesec
 
 Set or get share ACLs
 
 ```
 root@kali:~# sharesec --help
 Usage: sharesec sharename
 
   -r, --remove=ACL                   Remove ACEs
   -m, --modify=ACL                   Modify existing ACEs
   -a, --add=ACL                      Add ACEs
   -R, --replace=ACLS                 Overwrite share permission ACL
   -D, --delete                       Delete the entire security descriptor
   -S, --setsddl=STRING               Set the SD in sddl format
       --viewsddl                     View the SD in sddl format
   -v, --view                         View current share permissions
       --view-all                     View all current share permissions
   -M, --machine-sid                  Initialize the machine SID
   -F, --force                        Force storing the ACL
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ##### smbd
 
 Server to provide SMB/CIFS services to clients
 
 ```
 root@kali:~# smbd --help
 Usage: smbd [OPTION...]
   -b, --build-options                     Print build options
   -p, --port=STRING                       Listen on the specified transports
   -P, --profiling-level=PROFILE_LEVEL     Set profiling level
 
 Help options:
   -?, --help                              Show this help message
       --usage                             Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL             Set debug level
       --debug-stdout                      Send debug output to standard output
   -s, --configfile=CONFIGFILE             Use alternative configuration file
       --option=name=value                 Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE          Basename for log/debug files
       --leak-report                       enable talloc leak reporting on exit
       --leak-report-full                  enable full talloc leak reporting on
                                           exit
 
 Daemon options:
   -D, --daemon                            Become a daemon (default)
   -i, --interactive                       Run interactive (not a daemon) and
                                           log to stdout
   -F, --foreground                        Run daemon in foreground (for
                                           daemontools, etc.)
       --no-process-group                  Don't create a new process group
 
 Version options:
   -V, --version                           Print version
 ```
 
 - - -
 
 ##### smbstatus
 
 Report on current Samba connections
 
 ```
 root@kali:~# smbstatus --help
 Usage: [OPTION...]
   -p, --processes                    Show processes only
   -v, --verbose                      Be verbose
   -L, --locks                        Show locks only
   -S, --shares                       Show shares only
   -N, --notify                       Show notifies
   -u, --user=STRING                  Switch to user
   -b, --brief                        Be brief
   -P, --profile                      Do profiling
   -R, --profile-rates                Show call rates
   -B, --byterange                    Include byte range locks
   -n, --numeric                      Numeric uid/gid
   -j, --json                         JSON output
   -f, --fast                         Skip checks if processes still exist
       --resolve-uids                 Try to resolve UIDs to usernames
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ### samba-ad-dc
 
 **Samba control files to run AD Domain Controller**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file and printer sharing with
  Microsoft Windows, OS X, and other Unix systems.
   
  This package contains control files to run an Active Directory Domain
  Controller (AD DC).  For now, this is just a metapackage pulling in
  all the required dependencies.
 
 **Installed size:** `204 KB`  
 **How to install:** `sudo apt install samba-ad-dc`  
 
 {{< spoiler "Dependencies:" >}}
 * init-system-helpers 
 * libbsd0 
 * libc6 
 * libldb2 
 * libpopt0 
 * libtalloc2 
 * libtevent0t64 
 * python3
 * python3-dnspython
 * python3-samba 
 * samba 
 * samba-dsdb-modules 
 * samba-libs 
 * winbind 
 {{< /spoiler >}}
 
 ##### samba
 
 A Windows AD and SMB/CIFS fileserver for UNIX
 Server to provide AD and SMB/CIFS services to clients
 
 ```
 root@kali:~# samba --help
 Usage: samba: root process [OPTION...]
   -M, --model=MODEL                  Select process model
       --maximum-runtime=seconds      set maximum runtime of the server
                                      process, till autotermination
   -b, --show-build                   show build info
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Daemon options:
   -D, --daemon                       Become a daemon (default)
   -i, --interactive                  Run interactive (not a daemon) and log to
                                      stdout
   -F, --foreground                   Run daemon in foreground (for
                                      daemontools, etc.)
       --no-process-group             Don't create a new process group
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ##### samba_dnsupdate
 
 
 ```
 root@kali:~# samba_dnsupdate -h
 Usage: samba_dnsupdate [options]
 
 Options:
   -h, --help            show this help message and exit
   --verbose             
   --use-samba-tool      Use samba-tool to make updates over RPC, rather than
                         over DNS
   --use-nsupdate        Use nsupdate command to make updates over DNS
                         (default, if kinit successful)
   --all-names           
   --all-interfaces      
   --current-ip=CURRENT_IP
                         IP address to update DNS to match (helpful if behind
                         NAT, valid multiple times, defaults to values from
                         interfaces=)
   --rpc-server-ip=RPC_SERVER_IP
                         IP address of server to use with samba-tool (defaults
                         to first --current-ip)
   --use-file=USE_FILE   Use a file, rather than real DNS calls
   --update-list=UPDATE_LIST
                         Add DNS names from the given file
   --update-cache=UPDATE_CACHE
                         Cache database of already registered records
   --fail-immediately    Exit on first failure
   --no-credentials      don't try and get credentials
   --no-substitutions    don't try and expands variables in file specified by
                         --update-list
 
   Samba Common Options:
     -s FILE, --configfile=FILE
                         Configuration file
     -d DEBUGLEVEL, --debuglevel=DEBUGLEVEL
                         debug level
     --option=OPTION     set smb.conf option from command line
     --realm=REALM       set the realm name
 
   Version Options:
     -V, --version       Display version number
                         (4.23.3-Debian-4.23.3+dfsg-1+b1)
 ```
 
 - - -
 
 ##### samba_kcc
 
 
 ```
 root@kali:~# samba_kcc -h
 Usage: samba_kcc [options]
 
 Options:
   -h, --help            show this help message and exit
   --readonly            compute topology but do not update database
   --debug               debug output
   --verify              verify that assorted invariants are kept
   --list-verify-tests   list what verification actions are available and do
                         nothing else
   --dot-file-dir=DOT_FILE_DIR
                         Write Graphviz .dot files to this directory
   --seed=SEED           random number seed
   --importldif=<file>   import topology ldif file
   --exportldif=<file>   export topology ldif file
   -H <URL>, --URL=<URL>
                         LDB URL for database or target server
   --tmpdb=<file>        schemaless database file to create for ldif import
   --now=<date>          assume current time is this ('YYYYmmddHHMMSS[tz]',
                         default: system time)
   --forced-local-dsa=<DSA>
                         run calculations assuming the DSA is this DN
   --attempt-live-connections
                         Attempt to connect to other DSAs to test links
   --list-valid-dsas     Print a list of DSA dnstrs that could be used in
                         --forced-local-dsa
   --test-all-reps-from  Create and verify a graph of reps-from for every DSA
   --forget-local-links  pretend not to know the existing local topology
   --forget-intersite-links
                         pretend not to know the existing intersite topology
 
   Samba Common Options:
     -s FILE, --configfile=FILE
                         Configuration file
     -d DEBUGLEVEL, --debuglevel=DEBUGLEVEL
                         debug level
     --option=OPTION     set smb.conf option from command line
     --realm=REALM       set the realm name
 
   Credentials Options:
     --simple-bind-dn=DN
                         DN to use for a simple bind
     --password=PASSWORD
                         Password
     -U USERNAME, --username=USERNAME
                         Username
     -W WORKGROUP, --workgroup=WORKGROUP
                         Workgroup
     -N, --no-pass       Don't ask for a password
     --ipaddress=IPADDRESS
                         IP address of server
     -P, --machine-pass  Use stored machine account password
     --use-kerberos=desired|required|off
                         Use Kerberos authentication
     --use-krb5-ccache=KRB5CCNAME
                         Kerberos Credentials cache
     -A AUTHFILE, --authentication-file=AUTHFILE
                         Authentication file
     -k KERBEROS, --kerberos=KERBEROS
                         DEPRECATED: Migrate to --use-kerberos
 
   Version Options:
     -V, --version       Display version number
                         (4.23.3-Debian-4.23.3+dfsg-1+b1)
 ```
 
 - - -
 
 ##### samba_spnupdate
 
 
 ```
 root@kali:~# samba_spnupdate -h
 Usage: samba_spnupdate
 
 Options:
   -h, --help            show this help message and exit
   --verbose             
 
   Samba Common Options:
     -s FILE, --configfile=FILE
                         Configuration file
     -d DEBUGLEVEL, --debuglevel=DEBUGLEVEL
                         debug level
     --option=OPTION     set smb.conf option from command line
     --realm=REALM       set the realm name
 
   Version Options:
     -V, --version       Display version number
                         (4.23.3-Debian-4.23.3+dfsg-1+b1)
 
   Credentials Options:
     --simple-bind-dn=DN
                         DN to use for a simple bind
     --password=PASSWORD
                         Password
     -U USERNAME, --username=USERNAME
                         Username
     -W WORKGROUP, --workgroup=WORKGROUP
                         Workgroup
     -N, --no-pass       Don't ask for a password
     --ipaddress=IPADDRESS
                         IP address of server
     -P, --machine-pass  Use stored machine account password
     --use-kerberos=desired|required|off
                         Use Kerberos authentication
     --use-krb5-ccache=KRB5CCNAME
                         Kerberos Credentials cache
     -A AUTHFILE, --authentication-file=AUTHFILE
                         Authentication file
     -k KERBEROS, --kerberos=KERBEROS
                         DEPRECATED: Migrate to --use-kerberos
 ```
 
 - - -
 
 ##### samba_upgradedns
 
 
 ```
 root@kali:~# samba_upgradedns -h
 Usage: samba_upgradedns [options]
 
 Options:
   -h, --help            show this help message and exit
   --dns-backend=<BIND9_DLZ|SAMBA_INTERNAL>
                         The DNS server backend, default SAMBA_INTERNAL
   --migrate=<yes|no>    Migrate existing zone data, default yes
   --verbose             Be verbose
 
   Version Options:
     -V, --version       Display version number
                         (4.23.3-Debian-4.23.3+dfsg-1+b1)
 
   Samba Common Options:
     -s FILE, --configfile=FILE
                         Configuration file
     -d DEBUGLEVEL, --debuglevel=DEBUGLEVEL
                         debug level
     --option=OPTION     set smb.conf option from command line
     --realm=REALM       set the realm name
 
   Credentials Options:
     --simple-bind-dn=DN
                         DN to use for a simple bind
     --password=PASSWORD
                         Password
     -U USERNAME, --username=USERNAME
                         Username
     -W WORKGROUP, --workgroup=WORKGROUP
                         Workgroup
     -N, --no-pass       Don't ask for a password
     --ipaddress=IPADDRESS
                         IP address of server
     -P, --machine-pass  Use stored machine account password
     --use-kerberos=desired|required|off
                         Use Kerberos authentication
     --use-krb5-ccache=KRB5CCNAME
                         Kerberos Credentials cache
     -A AUTHFILE, --authentication-file=AUTHFILE
                         Authentication file
     -k KERBEROS, --kerberos=KERBEROS
                         DEPRECATED: Migrate to --use-kerberos
 ```
 
 - - -
 
 ### samba-ad-provision
 
 **Samba files needed for AD domain provision**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file and printer sharing with
  Microsoft Windows, OS X, and other Unix systems.
   
  This package contains files to setup an Active Directory Domain
  Controller (AD DC).
 
 **Installed size:** `16.98 MB`  
 **How to install:** `sudo apt install samba-ad-provision`  
 
 {{< spoiler "Dependencies:" >}}
 * python3-markdown
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-common
 
 **Common files used by both the Samba server and client**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file and printer sharing with
  Microsoft Windows, OS X, and other Unix systems.
   
  This package contains common files used by all parts of Samba.
 
 **Installed size:** `118 KB`  
 **How to install:** `sudo apt install samba-common`  
 
 {{< spoiler "Dependencies:" >}}
 * ucf
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-common-bin
 
 **Samba common files used by both the server and the client**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package contains the common files that are used by both the server
  (provided in the samba package) and the client (provided in the smbclient
  package).
 
 **Installed size:** `4.89 MB`  
 **How to install:** `sudo apt install samba-common-bin`  
 
 {{< spoiler "Dependencies:" >}}
 * libbsd0 
 * libc6 
 * libcups2t64 
 * libgnutls30t64 
 * libjansson4 
 * libldap2 
 * libncurses6 
 * libndr6 
 * libpopt0 
 * libreadline8t64 
 * libsmbldap2 
 * libtalloc2 
 * libtdb1 
 * libtevent0t64 
 * libtinfo6 
 * libwbclient0 
 * samba-common
 * samba-libs 
 {{< /spoiler >}}
 
 ##### dbwrap_tool
 
 Low level TDB/CTDB manipulation tool using the dbwrap interface
 
 ```
 root@kali:~# dbwrap_tool --help
 Usage: [OPTION...]
       --non-persistent               treat the database as non-persistent
                                      (CAVEAT: This mode might wipe your
                                      database!)
       --persistent                   treat the database as persistent
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
 ##### net
 
 Tool for administration of Samba and remote CIFS servers.
 
 ```
 root@kali:~# net -h
 Usage:
   Use 'net help rpc' to get more extensive information about 'net rpc' commands.
   Use 'net help rap' to get more extensive information about 'net rap' commands.
   Use 'net help ads' to get more extensive information about 'net ads' commands.
   Use 'net help file' to get more information about 'net file' commands.
   Use 'net help share' to get more information about 'net share' commands.
   Use 'net help session' to get more information about 'net session' commands.
   Use 'net help server' to get more information about 'net server' commands.
   Use 'net help domain' to get more information about 'net domain' commands.
   Use 'net help printq' to get more information about 'net printq' commands.
   Use 'net help user' to get more information about 'net user' commands.
   Use 'net help group' to get more information about 'net group' commands.
   Use 'net help groupmap' to get more information about 'net groupmap' commands.
   Use 'net help sam' to get more information about 'net sam' commands.
   Use 'net help validate' to get more information about 'net validate' commands.
   Use 'net help groupmember' to get more information about 'net groupmember' commands.
   Use 'net help admin' to get more information about 'net admin' commands.
   Use 'net help service' to get more information about 'net service' commands.
   Use 'net help password' to get more information about 'net password' commands.
   Use 'net help primarytrust' to get more extensive information about 'net primarytrust' commands.
   Use 'net help changetrustpw' to get more information about 'net changetrustpw'.
   net [options] changesecretpw
     Change the ADS domain member machine account password in secrets.tdb.
     Do NOT use this function unless you know what it does.
     Requires the -f flag to work.
   net -U user[%%password] [-W domain] setauthuser
     Set the auth user, password (and optionally domain
     Will prompt for password if not given.
   net setauthuser delete
     Delete the existing auth user settings.
   net getauthuser
     Get the current winbind auth user settings.
   Use 'net help time' to get more information about 'net time' commands.
   Use 'net help lookup' to get more information about 'net lookup' commands.
   Use 'net help g_lock' to get more information about 'net g_lock' commands.
   Use 'net help join' to get more information about 'net join'.
   Use 'net help offlinejoin' to get more information about 'net offlinejoin'.
   Use 'net help dom' to get more information about 'net dom' commands.
   Use 'net help cache' to get more information about 'net cache' commands.
   net getlocalsid
   net setlocalsid S-1-5-21-x-y-z
   net setdomainsid S-1-5-21-x-y-z
   net getdomainsid
   net maxrid
   Use 'net help idmap to get more information about 'net idmap' commands.
   Use 'net help status' to get more information about 'net status' commands.
   Use 'net help usershare to get more information about 'net usershare' commands.
   Use 'net help usersidlist' to get more information about 'net usersidlist'.
   Use 'net help conf' to get more information about 'net conf' commands.
   Use 'net help registry' to get more information about 'net registry' commands.
   Use 'net help eventlog' to get more information about 'net eventlog' commands.
   Use 'net help printing' to get more information about 'net printing' commands.
   Use 'net help serverid' to get more information about 'net serverid' commands.
   Use 'net help notify' to get more information about 'net notify' commands.
   Use 'net help tdb' to get more information about 'net tdb' commands.
   Use 'net help vfs' to get more information about 'net vfs' commands.
   Use 'net help witness' to get more information about 'net witness' commands.
   Use 'net help help' to list usage information for 'net' commands.
 ```
 
 - - -
 
 ##### nmblookup
 
 NetBIOS over TCP/IP client used to lookup NetBIOS names
 
 ```
 root@kali:~# nmblookup --help
 Usage: <NODE> ...
   -B, --broadcast=BROADCAST-ADDRESS         Specify address to use for
                                             broadcasts
   -f, --flags                               List the NMB flags returned
   -U, --unicast=STRING                      Specify address to use for unicast
   -M, --master-browser                      Search for a master browser
       --recursion                           Set recursion desired in package
   -S, --status                              Lookup node status as well
   -T, --translate                           Translate IP addresses into names
   -r, --root-port                           Use root port 137 (Win95 only
                                             replies to this)
   -A, --lookup-by-ip                        Do a node status on <name> as an
                                             IP Address
 
 Help options:
   -?, --help                                Show this help message
       --usage                               Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL               Set debug level
       --debug-stdout                        Send debug output to standard
                                             output
   -s, --configfile=CONFIGFILE               Use alternative configuration file
       --option=name=value                   Set smb.conf option from command
                                             line
   -l, --log-basename=LOGFILEBASE            Basename for log/debug files
       --leak-report                         enable talloc leak reporting on
                                             exit
       --leak-report-full                    enable full talloc leak reporting
                                             on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER     Use these name resolution services
                                             only
   -O, --socket-options=SOCKETOPTIONS        socket options to use
   -m, --max-protocol=MAXPROTOCOL            Set max protocol level
   -n, --netbiosname=NETBIOSNAME             Primary netbios name
       --netbios-scope=SCOPE                 Use this Netbios scope
   -W, --workgroup=WORKGROUP                 Set the workgroup name
       --realm=REALM                         Set the realm name
 
 Version options:
   -V, --version                             Print version
 ```
 
 - - -
 
 ##### samba-log-parser
 
 Samba (winbind) trace parser.
 
 ```
 root@kali:~# samba-log-parser -h
 usage: samba-log-parser [-h] [--traceid ID] [--pid PID] [--breakdown]
                         [--merge-by-timestamp] [--flow] [--flow-compact]
                         path
 
 positional arguments:
   path                  logfile or directory
 
 options:
   -h, --help            show this help message and exit
   --traceid ID          specify the traceid of the trace records
   --pid PID             specify the pid of winbind client
   --breakdown           breakdown the traces into per traceid files
   --merge-by-timestamp  merge logs by timestamp
   --flow                show the request/sub-request flow traces
   --flow-compact        show the request/sub-request flow traces without
                         dcerpc details
 ```
 
 - - -
 
 ##### samba-regedit
 
 Ncurses based tool to manage the Samba registry
 
 ```
 root@kali:~# samba-regedit --help
 Usage: samba-regedit [OPTION...]
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbcontrol
 
 Send messages to smbd, nmbd or winbindd processes
 
 ```
 root@kali:~# smbcontrol -h
 Invalid option
 Usage: smbcontrol [OPTION...] <destination> <message-type> <parameters>
   -t, --timeout=TIMEOUT              Set timeout value in seconds
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 Usage: smbcontrol [OPTION...] <destination> <message-type> <parameters>
   -t, --timeout=TIMEOUT              Set timeout value in seconds
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                      Print version
 
 <destination> is one of "nmbd", "smbd", "winbindd", "ldap_server" or a process ID
 
 <message-type> is one of:
 	debug                         Set debuglevel
 	idmap                         Manipulate idmap cache
 	force-election                Force a browse election
 	ping                          Elicit a response
 	profile                       
 	inject                        Inject a fatal signal into a running smbd
 	stacktrace                    Display a stack trace of a daemon
 	profilelevel                  
 	debuglevel                    Display current debuglevels
 	printnotify                   Send a print notify message
 	close-share                   Forcibly disconnect a share
 	close-denied-share            Forcibly disconnect users from shares disallowed now
 	kill-client-ip                Forcibly disconnect a client with a specific IP address
 	ip-dropped                    Tell winbind that an IP got dropped
 	pool-usage                    Display talloc memory usage
 	rpc-dump-status               Display rpc status
 	ringbuf-log                   Display ringbuf log
 	dmalloc-mark                  
 	dmalloc-log-changed           
 	shutdown                      Shut down daemon
 	drvupgrade                    Notify a printer driver has changed
 	reload-certs                  Reload TLS certificates
 	reload-config                 Force smbd or winbindd to reload config file
 	reload-printers               Force smbd to reload printers
 	nodestatus                    Ask nmbd to do a node status request
 	online                        Ask winbind to go into online state
 	offline                       Ask winbind to go into offline state
 	onlinestatus                  Request winbind online status
 	validate-cache                Validate winbind's credential cache
 	dump-domain-list              Dump winbind domain list
 	disconnect-dc                 
 	notify-cleanup                
 	num-children                  Print number of smbd child processes
 	msg-cleanup                   
 	noop                          Do nothing
 	sleep                         Cause the target process to sleep
 
 ```
 
 - - -
 
 ##### smbpasswd
 
 The Samba encrypted password file
 Change a user's SMB password
 
 ```
 root@kali:~# smbpasswd -h
 When run by root:
     smbpasswd [options] [username]
 otherwise:
     smbpasswd [options]
 
 options:
   -L                   local mode (must be first option)
   -h                   print this usage message
   -s                   use stdin for password prompt
   -c smb.conf file     Use the given path to the smb.conf file
   -D LEVEL             debug level
   -r MACHINE           remote machine
   -U USER              remote username (e.g. SAM/user)
 extra options when run by root or in local mode:
   -a                   add user
   -d                   disable user
   -e                   enable user
   -i                   interdomain trust account
   -m                   machine trust account
   -n                   set no password
   -W                   use stdin ldap admin password
   -w PASSWORD          ldap admin password
   -x                   delete user
   -R ORDER             name resolve order
 ```
 
 - - -
 
 ##### testparm
 
 Check an smb.conf configuration file for internal correctness
 
 ```
 root@kali:~# testparm --help
 Usage: testparm [OPTION...] <config-file> [host-name] [host-ip]
   -s, --suppress-prompt           Suppress prompt for enter
   -v, --verbose                   Show default options too
   -l, --skip-logic-checks         Skip the global checks
       --show-all-parameters       Show the parameters, type, possible values
       --parameter-name=STRING     Limit testparm to a named parameter
       --section-name=STRING       Limit testparm to a named section
 
 Help options:
   -?, --help                      Show this help message
       --usage                     Display brief usage message
 
 Common debug options:
   -d, --debuglevel=DEBUGLEVEL     Set debug level
       --debug-stdout              Send debug output to standard output
 
 Options:
       --option=name=value         Set smb.conf option from command line
 
 Version options:
   -V, --version                   Print version
 ```
 
 - - -
 
 ##### winexe
 
 Winexe is a Remote Windows-command executor
 
 ```
 root@kali:~# winexe --help
 Usage: winexe [OPTION]... //HOST[:PORT] COMMAND
 Options:
       --uninstall                              Uninstall winexe service after
                                                remote execution
       --reinstall                              Reinstall winexe service before
                                                remote execution
       --runas=[DOMAIN\]USERNAME%PASSWORD       Run as the given user (BEWARE:
                                                this password is sent in
                                                cleartext over the network!)
       --runas-file=FILE                        Run as user options defined in
                                                a file
       --interactive=0|1                        Desktop interaction: 0 -
                                                disallow, 1 - allow. If allow,
                                                also use the --system switch
                                                (Windows requirement). Vista
                                                does not support this option.
       --ostype=0|1|2                           OS type: 0 - 32-bit, 1 -
                                                64-bit, 2 - winexe will decide.
                                                Determines which version
                                                (32-bit or 64-bit) of service
                                                will be installed.
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ### samba-dev
 
 **Tools for extending Samba**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package contains include files shared by the various Samba-based
  libraries.
 
 **Installed size:** `1.41 MB`  
 **How to install:** `sudo apt install samba-dev`  
 
 {{< spoiler "Dependencies:" >}}
 * libc6-dev
 * libldb-dev
 * libpopt-dev
 * libtalloc-dev
 * libtdb-dev
 * libtevent-dev
 * libwbclient-dev
 * samba-libs 
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-dsdb-modules
 
 **Samba Directory Services Database**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package contains LDB plugins which add support for various Active
  Directory features to the LDB library.
 
 **Installed size:** `1.60 MB`  
 **How to install:** `sudo apt install samba-dsdb-modules`  
 
 {{< spoiler "Dependencies:" >}}
 * libbsd0 
 * libc6 
 * libgnutls30t64 
 * libgpgme45 
 * libldb2 
 * libndr6 
 * libtalloc2 
 * libtdb1 
 * libtevent0t64 
 * samba-libs 
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-libs
 
 **Samba core libraries**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package contains the shared libraries.
 
 **Installed size:** `25.48 MB`  
 **How to install:** `sudo apt install samba-libs`  
 
 {{< spoiler "Dependencies:" >}}
 * libacl1 
 * libavahi-client3 
 * libavahi-common3 
 * libbsd0 
 * libc6 
 * libcap2 
 * libcrypt1 
 * libgnutls30t64 
 * libicu76 
 * libjansson4 
 * libldap2 
 * libldb2 
 * libngtcp2-16 
 * libngtcp2-crypto-gnutls8 
 * libpam0g 
 * libpopt0 
 * libsystemd0
 * libtalloc2 
 * libtdb1 
 * libtevent0t64 
 * libtirpc3t64 
 * libwbclient0 
 * zlib1g 
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-testsuite
 
 **Test suite from Samba**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package contains programs for testing the reliability and speed
  of SMB servers, Samba in particular.
 
 **Installed size:** `10.43 MB`  
 **How to install:** `sudo apt install samba-testsuite`  
 
 {{< spoiler "Dependencies:" >}}
 * ctdb 
 * libbsd0 
 * libc6 
 * libgnutls30t64 
 * libldb2 
 * libndr6 
 * libpopt0 
 * libreadline8t64 
 * libsmbclient0 
 * libtalloc2 
 * libtdb1 
 * libtevent0t64 
 * libwbclient0 
 * python3-samba 
 * samba-common-bin
 * samba-libs 
 * winbind 
 {{< /spoiler >}}
 
 ##### gentest
 
 Run random generic SMB operations against two SMB servers and show the differences in behavior
 
 ```
 root@kali:~# gentest --help
 Usage: <unc1> <unc2>
       --smb2                                   use SMB2 protocol
       --seed=INT                               Seed to use for randomizer
       --num-ops=INT                            num ops
       --oplocks                                use oplocks
       --showall                                display all operations
       --analyse                                do backtrack analysis
       --analysealways                          analysis always
       --analysecontinuous                      analysis continuous
       --ignore=STRING                          ignore from file
       --preset                                 use preset seeds
       --fast                                   use fast reconnect
       --unclist=STRING                         unclist
       --seedsfile=STRING                       seed file
       --user1=[DOMAIN/]USERNAME[%PASSWORD]     Set first network username
       --user2=[DOMAIN/]USERNAME[%PASSWORD]     Set second network username
       --maskindexing                           mask out the indexed file attrib
       --noeas                                  don't use extended attributes
       --noacls                                 don't use ACLs
       --skip-cleanup                           don't delete files at start
       --valid                                  generate only valid fields
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 
 Deprecated legacy options:
   -k, --kerberos=STRING                        DEPRECATED: Migrate to
                                                --use-kerberos
 ```
 
 - - -
 
 ##### locktest
 
 Find differences in locking between two SMB servers
 
 ```
 root@kali:~# locktest --help
 Usage: <unc1> <unc2>
       --seed=INT                               Seed to use for randomizer
       --num-ops=INT                            num ops
       --lockrange=INT                          locking range
       --lockbase=INT                           locking base
       --minlength=INT                          min lock length
       --hidefails                              hide unlock fails
       --oplocks                                use oplocks
       --showall                                display all operations
       --analyse                                do backtrack analysis
       --zerozero                               do zero/zero lock
       --exacterrors                            use exact error codes
       --unclist=STRING                         unclist
       --user1=[DOMAIN/]USERNAME[%PASSWORD]     Set first network username
       --user2=[DOMAIN/]USERNAME[%PASSWORD]     Set second network username
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 
 Deprecated legacy options:
   -k, --kerberos=STRING                        DEPRECATED: Migrate to
                                                --use-kerberos
 ```
 
 - - -
 
 ##### masktest
 
 Find differences in wildcard matching between Samba's implementation and that of a remote server.
 
 ```
 root@kali:~# masktest --help
 Usage: <unc>
       --seed=INT                               Seed to use for randomizer
       --num-ops=INT                            num ops
       --maxlength=INT                          maximum length
       --dieonerror                             die on errors
       --showall                                display all operations
       --oldlist                                use old list call
       --maskchars=STRING                       mask characters
       --filechars=STRING                       file characters
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 
 Deprecated legacy options:
   -k, --kerberos=STRING                        DEPRECATED: Migrate to
                                                --use-kerberos
 ```
 
 - - -
 
 ##### ndrdump
 
 DCE/RPC Packet Parser and Dumper
 
 ```
 root@kali:~# ndrdump --help
 Usage: ndrdump <pipe|uuid> <format> <in|out|struct> [<filename>]
   -c, --context-file=CTX-FILE         In-filename to parse first
       --validate                      try to validate the data
       --dump-data                     dump the hex data
       --load-dso=STRING               load from shared object file
       --ndr64                         Assume NDR64 data
       --quiet                         Don't actually dump anything
       --base64-input                  Read the input file in as a base64 string
       --hex-input                     Read the input file in as a hex dump
       --input=INPUT                   Provide the input on the command line
                                       (use with --base64-input)
       --print-after-parse-failure     Try to print structures that fail to
                                       parse (used to develop parsers,
                                       segfaults are likely).
 
 Help options:
   -?, --help                          Show this help message
       --usage                         Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL         Set debug level
       --debug-stdout                  Send debug output to standard output
   -s, --configfile=CONFIGFILE         Use alternative configuration file
       --option=name=value             Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE      Basename for log/debug files
       --leak-report                   enable talloc leak reporting on exit
       --leak-report-full              enable full talloc leak reporting on exit
 
 Version options:
   -V, --version                       Print version
 ```
 
 - - -
 
 ##### smbtorture
 
 Run a series of tests against a SMB server
 
 ```
 root@kali:~# smbtorture --help
 smbtorture 4.23.3-Debian-4.23.3+dfsg-1+b1
 Usage: <binding>|<unc> TEST1 TEST2 ...
       --fullname                               use full name for the test
       --format=STRING                          Output format (one of: simple,
                                                subunit)
   -p, --smb-ports=STRING                       SMB ports
       --basedir=BASEDIR                        base directory
       --seed=INT                               Seed to use for randomizer
       --num-progs=INT                          num progs
       --num-ops=INT                            num ops
       --entries=INT                            entries
       --loadfile=STRING                        NBench load file to use
       --list-suites                            List available testsuites and
                                                exit
       --list                                   List available tests in
                                                specified suites and exit
       --unclist=STRING                         unclist
   -t, --timelimit=INT                          Set time limit (in seconds)
   -f, --failures=INT                           failures
   -D, --parse-dns=STRING                       parse-dns
   -X, --dangerous                              run dangerous tests (eg. wiping
                                                out password database)
       --load-module=SOFILE                     load tests from DSO file
       --shell                                  Run shell
   -T, --target=STRING                          samba3|samba4|other
   -a, --async                                  run async tests
       --num-async=INT                          number of simultaneous async
                                                requests
       --maximum-runtime=seconds                set maximum time for smbtorture
                                                to live
       --extra-user=STRING                      extra user credentials
       --load-list=STRING                       load a test id list from a text
                                                file
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 
 Deprecated legacy options:
   -k, --kerberos=STRING                        DEPRECATED: Migrate to
                                                --use-kerberos
 ```
 
 - - -
 
 ### samba-vfs-ceph
 
 **Samba Virtual FileSystem ceph modules**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  Virtual FileSystem modules are stacked shared libraries extending the
  functionality of Samba. This package provides vfs_ceph and vfs_ceph_snapshots
  modules.
 
 **Installed size:** `302 KB`  
 **How to install:** `sudo apt install samba-vfs-ceph`  
 
 {{< spoiler "Dependencies:" >}}
 * libbsd0 
 * libc6 
 * libcephfs2 
 * libtalloc2 
 * libtevent0t64 
 * samba 
 * samba-libs 
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-vfs-glusterfs
 
 **Samba Virtual FileSystem glusterfs modules**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  Virtual FileSystem modules are stacked shared libraries extending the
  functionality of Samba. This package provides vfs_glusterfs and
  vfs_glusterfs_fuse modules.
 
 **Installed size:** `165 KB`  
 **How to install:** `sudo apt install samba-vfs-glusterfs`  
 
 {{< spoiler "Dependencies:" >}}
 * libc6 
 * libgfapi0 
 * libtalloc2 
 * libtevent0t64 
 * samba 
 * samba-libs 
 {{< /spoiler >}}
 
 
 - - -
 
 ### samba-vfs-modules
 
 **Samba Virtual FileSystem plugins (transitional package)**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  Virtual FileSystem modules are stacked shared libraries extending the
  functionality of Samba.  This package used to provide VFS modules for
  samba, but since version 4.20.2+dfsg-3, most of the modules were merged
  into main samba package, or into their own separate packages -
  samba-vfs-ceph and samba-vfs-glusterfs.
   
  This package can safely be removed.
 
 **Installed size:** `66 KB`  
 **How to install:** `sudo apt install samba-vfs-modules`  
 
 
 - - -
 
 ### smbclient
 
 **Command-line SMB/CIFS clients for Unix**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file and printer sharing with
  Microsoft Windows, OS X, and other Unix systems.
   
  This package contains command-line utilities for accessing Microsoft
  Windows and Samba servers, including smbclient, smbtar, and smbspool.
  Utilities for mounting shares locally are found in the package
  cifs-utils.
 
 **Installed size:** `2.05 MB`  
 **How to install:** `sudo apt install smbclient`  
 
 {{< spoiler "Dependencies:" >}}
 * libarchive13t64 
 * libbsd0 
 * libc6 
 * libgnutls30t64 
 * libndr6 
 * libpopt0 
 * libreadline8t64 
 * libsmbclient0 
 * libtalloc2 
 * libtevent0t64 
 * samba-common
 * samba-libs 
 {{< /spoiler >}}
 
 ##### cifsdd
 
 Convert and copy a file over SMB
 
 ```
 root@kali:~# cifsdd --help
 Usage: cifsdd [OPTION...]
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos=STRING                        DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 
 CIFS dd options:
   bs=SIZE                force ibs and obs to SIZE bytes
   ibs=SIZE               read SIZE bytes at a time
   obs=SIZE               write SIZE bytes at a time
   count=COUNT            copy COUNT input blocks
   seek=COUNT             skip COUNT blocks at start of output
   skip=COUNT             skip COUNT blocks at start of input
   if=FILE                read input from FILE
   of=FILE                write output to FILE
   direct=BOOLEAN         use direct I/O if non-zero
   sync=BOOLEAN           use synchronous writes if non-zero
   oplock=BOOLEAN         take oplocks on the input and output files
 
 FILE can be a local filename or a UNC path of the form //server/share/path.
 
 ```
 
 - - -
 
 ##### mdsearch
 
 Run Spotlight searches against an SMB server
 
 ```
 root@kali:~# mdsearch --help
 Usage: mdsearch [OPTIONS] <server> <share> <query>
 
   -p, --path=STRING                            Server-relative search path
   -L, --live                                   live query
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### rpcclient
 
 Tool for executing client side MS-RPC functions
 
 ```
 root@kali:~# rpcclient --help
 Usage: rpcclient [OPTION...] BINDING-STRING|HOST
 Options:
   -c, --command=COMMANDS                       Execute semicolon separated cmds
   -I, --dest-ip=IP                             Specify destination IP address
   -p, --port=PORT                              Specify port number
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbcacls
 
 Set or get ACLs on an NT file or directory names
 
 ```
 root@kali:~# smbcacls --help
 Usage: smbcacls //server1/share1 filename
 ACLs look like: 'ACL:user:[ALLOWED|DENIED]/flags/permissions'
   -D, --delete=ACL                             Delete an acl
   -M, --modify=ACL                             Modify an acl
   -a, --add=ACL                                Add an acl
   -S, --set=ACLS                               Set acls
   -C, --chown=USERNAME                         Change ownership of a file
   -G, --chgrp=GROUPNAME                        Change group ownership of a file
   -I, --inherit=STRING                         Inherit allow|remove|copy
       --propagate-inheritance                  Supports propagation of
                                                inheritable ACE(s) when used in
                                                conjunction with add, delete,
                                                set or modify
       --save=STRING                            stores the DACLs in sddl format
                                                of the specified file or folder
                                                for later use with restore.
                                                SACLS, owner or integrity
                                                labels are not stored
       --restore=STRING                         applies the stored DACLS to
                                                files in directory.
       --recurse                                indicates the operation is
                                                performed on directory and all
                                                files/directories below. (only
                                                applies to save option)
       --numeric                                Don't resolve sids or masks to
                                                names
       --sddl                                   Output and input acls in sddl
                                                format
       --query-security-info=INT                The security-info flags for
                                                queries
       --set-security-info=INT                  The security-info flags for
                                                modifications
   -t, --test-args                              Test arguments
       --domain-sid=SID                         Domain SID for sddl
   -x, --maximum-access                         Query maximum permissions
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbclient
 
 Ftp-like client to access SMB/CIFS resources on servers
 
 ```
 root@kali:~# smbclient --help
 Usage: smbclient [OPTIONS] service <password>
   -M, --message=HOST                           Send message
   -I, --ip-address=IP                          Use this IP to connect to
   -E, --stderr                                 Write messages to stderr
                                                instead of stdout
   -L, --list=HOST                              Get a list of shares available
                                                on a host
   -T, --tar=<c|x>IXFvgbNan                     Command line tar
   -D, --directory=DIR                          Start from directory
   -c, --command=STRING                         Execute semicolon separated
                                                commands
   -b, --send-buffer=BYTES                      Changes the transmit/send buffer
   -t, --timeout=SECONDS                        Changes the per-operation
                                                timeout
   -p, --port=PORT                              Port to connect to
   -g, --grepable                               Produce grepable output
   -q, --quiet                                  Suppress help message
   -B, --browse                                 Browse SMB servers using DNS
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbcquotas
 
 Set or get QUOTAs of NTFS 5 shares
 
 ```
 root@kali:~# smbcquotas --help
 Usage: smbcquotas //server1/share1
   -u, --quota-user=USER                        Show quotas for user
   -L, --list                                   List user quotas
   -F, --fs                                     Show filesystem quotas
   -S, --set=SETSTRING                          Set acls
 SETSTRING:
                                                UQLIM:<username>/<softlimit>/<hardlimit> for user quotas
 FSQLIM:<softlimit>/<hardlimit> for filesystem defaults
 FSQFLAGS:QUOTA_ENABLED/DENY_DISK/LOG_SOFTLIMIT/LOG_HARD_LIMIT
   -n, --numeric                                Don't resolve sids or limits to
                                                names
   -v, --verbose                                be verbose
   -t, --test-args                              Test arguments
   -m, --max-protocol=LEVEL                     Set the max protocol level
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbget
 
 Wget-like utility for download files over SMB
 
 ```
 root@kali:~# smbget --help
 Usage: smbget [OPTION...]
   -a, --guest                                  Work as user guest
   -e, --encrypt                                Encrypt SMB transport
   -r, --resume                                 Automatically resume aborted
                                                files
   -u, --update                                 Download only when remote file
                                                is newer than local file or
                                                local file is missing
       --recursive                              Recursively download files
   -b, --blocksize=INT                          Change number of bytes in a
                                                block
   -o, --outputfile=STRING                      Write downloaded data to
                                                specified file
       --stdout                                 Write data to stdout
   -D, --dots                                   Show dots as progress indication
   -q, --quiet                                  Be quiet
   -v, --verbose                                Be verbose
       --limit-rate=INT                         Limit download speed to this
                                                many KB/s
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Connection options:
   -R, --name-resolve=NAME-RESOLVE-ORDER        Use these name resolution
                                                services only
   -O, --socket-options=SOCKETOPTIONS           socket options to use
   -m, --max-protocol=MAXPROTOCOL               Set max protocol level
   -n, --netbiosname=NETBIOSNAME                Primary netbios name
       --netbios-scope=SCOPE                    Use this Netbios scope
   -W, --workgroup=WORKGROUP                    Set the workgroup name
       --realm=REALM                            Set the realm name
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Deprecated legacy options:
   -k, --kerberos                               DEPRECATED: Migrate to
                                                --use-kerberos
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ##### smbspool
 
 Send a print file to an SMB printer
 
 ```
 root@kali:~# smbspool -h
 Usage: smbspool [DEVICE_URI] job-id user title copies options [file]
        The DEVICE_URI environment variable can also contain the
        destination printer:
 
            smb://[username:password@][workgroup/]server[:port]/printer
 ```
 
 - - -
 
 ##### smbtar
 
 Shell script for backing up SMB/CIFS shares directly to UNIX tape drives
 
 ```
 root@kali:~# smbtar -h
 Illegal option -h
 Usage: smbtar [<options>] [<include/exclude files>]
 Function: backup/restore a Windows PC directories to a local tape file
 Options:         (Description)                 (Default)
   -r             Restore from tape file to PC  Save from PC to tapefile
   -i             Incremental mode              Full backup mode
   -a             Reset archive bit mode        Don't reset archive bit
   -v             Verbose mode: echo command    Don't echo anything
   -s <server>    Specify PC Server             
   -p <password>  Specify PC Password           
   -x <share>     Specify PC Share              backup
   -X             Exclude mode                  Include
   -N <newer>     File for date comparison      
   -b <blocksize> Specify tape's blocksize      
   -d <dir>       Specify a directory in share  \
   -l <log>       Specify a Samba Log Level     2
   -u <user>      Specify User Name             root
   -t <tape>      Specify Tape device           tar.out
 
 Invalid switch specified - abort.
 ```
 
 - - -
 
 ##### smbtree
 
 A text based smb network browser
 
 ```
 root@kali:~# smbtree --help
 Usage: [OPTION...]
   -D, --domains                                List only domains (workgroups)
                                                of tree
   -S, --servers                                List domains(workgroups) and
                                                servers of tree
 
 Help options:
   -?, --help                                   Show this help message
       --usage                                  Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL                  Set debug level
       --debug-stdout                           Send debug output to standard
                                                output
   -s, --configfile=CONFIGFILE                  Use alternative configuration
                                                file
       --option=name=value                      Set smb.conf option from
                                                command line
   -l, --log-basename=LOGFILEBASE               Basename for log/debug files
       --leak-report                            enable talloc leak reporting on
                                                exit
       --leak-report-full                       enable full talloc leak
                                                reporting on exit
 
 Credential options:
   -U, --user=[DOMAIN/]USERNAME[%PASSWORD]      Set the network username
   -N, --no-pass                                Don't ask for a password
       --password=STRING                        Password
       --pw-nt-hash                             The supplied password is the NT
                                                hash
   -A, --authentication-file=FILE               Get the credentials from a file
   -P, --machine-pass                           Use stored machine account
                                                password
       --simple-bind-dn=DN                      DN to use for a simple bind
       --use-kerberos=desired|required|off      Use Kerberos authentication
       --use-krb5-ccache=CCACHE                 Credentials cache location for
                                                Kerberos
       --use-winbind-ccache                     Use the winbind ccache for
                                                authentication
       --client-protection=sign|encrypt|off     Configure used protection for
                                                client connections
 
 Version options:
   -V, --version                                Print version
 ```
 
 - - -
 
 ### tdb-tools
 
 **Trivial Database - bundled binaries**  
  This is a simple database API. It is modelled after the structure
  of GDBM. TDB features, unlike GDBM, multiple writers support with
  appropriate locking and transactions.
   
  This package contains bundled test and utility binaries
 
 **Installed size:** `149 KB`  
 **How to install:** `sudo apt install tdb-tools`  
 
 {{< spoiler "Dependencies:" >}}
 * libc6 
 * libtdb1 
 {{< /spoiler >}}
 
 ##### tdbbackup.tdbtools
 
 Tool for backing up and for validating the integrity of samba .tdb files
 
 ```
 root@kali:~# tdbbackup.tdbtools -h
 Usage: tdbbackup [options] <fname...>
 
    -h            this help message
    -s suffix     set the backup suffix
    -v            verify mode (restore if corrupt)
    -n hashsize   set the new hash size for the backup
    -l            open without locking to back up mutex dbs
    -r            open with read only locking
 ```
 
 - - -
 
 ##### tdbdump
 
 Tool for printing the contents of a TDB file
 
 ```
 root@kali:~# tdbdump -h
 Usage: tdbdump [options] <filename>
 
    -h          this help message
    -k keyname  dumps value of keyname
    -e          emergency dump, for corrupt databases
 ```
 
 - - -
 
 ##### tdbrestore
 
 Tool for creating a TDB file out of a tdbdump output
 
 ```
 root@kali:~# man tdbrestore
 TDBRESTORE(8)             System Administration tools             TDBRESTORE(8)
 
 NAME
        tdbrestore - tool for creating a TDB file out of a tdbdump output
 
 SYNOPSIS
 
        tdbrestore {tdbfilename}
 
 DESCRIPTION
        This tool is part of the samba(1) suite.
 
        tdbrestore is a very simple utility that 'restores' the contents of dump
        file into TDB (Trivial DataBase) file. The dump file is obtained from
        the tdbdump command.
 
        This tool wait on the standard input for the content of the dump and
        will write the tdb in the tdbfilename parameter.
 
        This tool can be used for unpacking the content of tdb as backup mean.
 
 VERSION
        This man page is correct for version 3 of the Samba suite.
 
 AUTHOR
        The original Samba software and related utilities were created by Andrew
        Tridgell. Samba is now developed by the Samba Team as an Open Source
        project similar to the way the Linux kernel is developed. This tool was
        initially written by Volker Lendecke based on an idea by Simon McVittie.
 
        The tdbrestore man page was written by Matthieu Patou.
 
 Samba 3.6                          2015-04-25                     TDBRESTORE(8)
 ```
 
 - - -
 
 ##### tdbtool
 
 Manipulate the contents TDB files
 
 ```
 root@kali:~# man tdbtool
 TDBTOOL(8)                System Administration tools                TDBTOOL(8)
 
 NAME
        tdbtool - manipulate the contents TDB files
 
 SYNOPSIS
 
        tdbtool
 
        tdbtool [-l] TDBFILE [COMMANDS...]
 
 DESCRIPTION
        This tool is part of the samba(1) suite.
 
        tdbtool a tool for displaying and altering the contents of Samba TDB
        (Trivial DataBase) files. Each of the commands listed below can be
        entered interactively or provided on the command line.
 
 OPTIONS
        -l
            This options disables any locking, by passing TDB_NOLOCK to
            tdb_open_ex(). Only use this for database files which are not used
            by any other process! And also only if it is otherwise not possible
            to open the database, e.g. databases which were created with mutex
            locking.
 
 COMMANDS
        create TDBFILE
            Create a new database named TDBFILE.
 
        open TDBFILE
            Open an existing database named TDBFILE.
 
        erase
            Erase the current database.
 
        dump
            Dump the current database as strings.
 
        cdump
            Dump the current database as connection records.
 
        keys
            Dump the current database keys as strings.
 
        hexkeys
            Dump the current database keys as hex values.
 
        info
            Print summary information about the current database.
 
        insert KEY DATA
            Insert a record into the current database.
 
        move KEY TDBFILE
            Move a record from the current database into TDBFILE.
 
        store KEY DATA
            Store (replace) a record in the current database.
 
        storehex KEY DATA
            Store (replace) a record in the current database where key and data
            are in hex format.
 
        show KEY
            Show a record by key.
 
        delete KEY
            Delete a record by key.
 
        list
            Print the current database hash table and free list.
 
        free
            Print the current database and free list.
 
        ! COMMAND
            Execute the given system command.
 
        first
            Print the first record in the current database.
 
        next
            Print the next record in the current database.
 
        check
            Check the integrity of the current database.
 
        repack
            Repack a database using a temporary file to remove fragmentation.
 
        quit
            Exit tdbtool.
 
 CAVEATS
        The contents of the Samba TDB files are private to the implementation
        and should not be altered with tdbtool.
 
 VERSION
        This man page is correct for version 3.6 of the Samba suite.
 
 EXIT STATUS
        The tdbtool program returns 0 if the operation succeeded, or 1 if the
        operation failed.
 
 AUTHOR
        The original Samba software and related utilities were created by Andrew
        Tridgell. Samba is now developed by the Samba Team as an Open Source
        project similar to the way the Linux kernel is developed.
 
 Samba 4.0                          2015-04-25                        TDBTOOL(8)
 ```
 
 - - -
 
 ### winbind
 
 **Service to resolve user and group information from Windows NT servers**  
  Samba is an implementation of the SMB/CIFS protocol for Unix systems,
  providing support for cross-platform file sharing with Microsoft Windows, OS X,
  and other Unix systems.  Samba can also function as a domain controller
  or member server in Active Directory or NT4-style domains.
   
  This package provides winbindd, a daemon which integrates authentication
  and directory service (user/group lookup) mechanisms from a Windows
  domain on a Linux system.
   
  Winbind based user/group lookups via /etc/nsswitch.conf can be enabled via
  the libnss-winbind package. Winbind based Windows domain authentication can
  be enabled via the libpam-winbind package.
 
 **Installed size:** `1.58 MB`  
 **How to install:** `sudo apt install winbind`  
 
 {{< spoiler "Dependencies:" >}}
 * init-system-helpers 
 * libbsd0 
 * libc6 
 * libgnutls30t64 
 * libldap2 
 * libldb2 
 * libndr6 
 * libpopt0 
 * libsmbldap2 
 * libtalloc2 
 * libtdb1 
 * libtevent0t64 
 * libwbclient0 
 * passwd
 * samba-common
 * samba-common-bin 
 * samba-libs 
 {{< /spoiler >}}
 
 ##### ntlm_auth
 
 Tool to allow external access to Winbind's NTLM authentication function
 
 ```
 root@kali:~# ntlm_auth --help
 Usage: [OPTION...]
       --helper-protocol=helper protocol to use     operate as a stdio-based
                                                    helper
       --username=STRING                            username
       --domain=STRING                              domain name
       --workstation=STRING                         workstation
       --challenge=STRING                           challenge (HEX encoded)
       --lm-response=STRING                         LM Response to the
                                                    challenge (HEX encoded)
       --nt-response=STRING                         NT or NTLMv2 Response to
                                                    the challenge (HEX encoded)
       --password=STRING                            User's plaintext password
       --request-lm-key                             Retrieve LM session key
                                                    (or, with --diagnostics,
                                                    expect LM support)
       --request-nt-key                             Retrieve User (NT) session
                                                    key
       --use-cached-creds                           Use cached credentials if
                                                    no password is given
       --allow-mschapv2                             Explicitly allow MSCHAPv2
       --offline-logon                              Use cached passwords when
                                                    DC is offline
       --diagnostics                                Perform diagnostics on the
                                                    authentication chain
       --require-membership-of=STRING               Require that a user be a
                                                    member of this group
                                                    (either name or SID) for
                                                    authentication to succeed
       --pam-winbind-conf=STRING                    Require that request must
                                                    set
                                                    WBFLAG_PAM_CONTACT_TRUSTDOM
                                                    when krb5 auth is required
       --target-service=STRING                      Target service (eg http)
       --target-hostname=STRING                     Target hostname
 
 Help options:
   -?, --help                                       Show this help message
       --usage                                      Display brief usage message
 
 Common debug options:
   -d, --debuglevel=DEBUGLEVEL                      Set debug level
       --debug-stdout                               Send debug output to
                                                    standard output
 
 Config file:
       --configfile=CONFIGFILE                      Use alternative
                                                    configuration file
 
 Options:
       --option=name=value                          Set smb.conf option from
                                                    command line
 
 Version options:
   -V, --version                                    Print version
 ```
 
 - - -
 
 ##### wbinfo
 
 Query information from winbind daemon
 
 ```
 root@kali:~# wbinfo --help
 Usage: wbinfo [OPTION...]
   -u, --domain-users                                 Lists all domain users
   -g, --domain-groups                                Lists all domain groups
   -N, --WINS-by-name=NETBIOS-NAME                    Converts NetBIOS name to
                                                      IP
   -I, --WINS-by-ip=IP                                Converts IP address to
                                                      NetBIOS name
   -n, --name-to-sid=NAME                             Converts name to sid
   -s, --sid-to-name=SID                              Converts sid to name
       --sid-to-fullname=SID                          Converts sid to fullname
   -R, --lookup-rids=RIDs                             Converts RIDs to names
       --lookup-sids=Sid-List                         Converts SIDs to types
                                                      and names
   -U, --uid-to-sid=UID                               Converts uid to sid
   -G, --gid-to-sid=GID                               Converts gid to sid
   -S, --sid-to-uid=SID                               Converts sid to uid
   -Y, --sid-to-gid=SID                               Converts sid to gid
       --allocate-uid                                 Get a new UID out of idmap
       --allocate-gid                                 Get a new GID out of idmap
       --set-uid-mapping=UID,SID                      Create or modify uid to
                                                      sid mapping in idmap
       --set-gid-mapping=GID,SID                      Create or modify gid to
                                                      sid mapping in idmap
       --remove-uid-mapping=UID,SID                   Remove uid to sid mapping
                                                      in idmap
       --remove-gid-mapping=GID,SID                   Remove gid to sid mapping
                                                      in idmap
       --sids-to-unix-ids=Sid-List                    Translate SIDs to Unix IDs
       --unix-ids-to-sids=ID-List (u<num> g<num>)     Translate Unix IDs to SIDs
   -t, --check-secret                                 Check shared secret
   -c, --change-secret                                Change shared secret
       --change-secret-at=STRING                      Change shared secret at
                                                      Domain Controller
   -P, --ping-dc                                      Check the NETLOGON
                                                      connection
   -m, --trusted-domains                              List trusted domains
       --all-domains                                  List all domains (trusted
                                                      and own domain)
       --own-domain                                   List own domain
       --online-status                                Show whether domains
                                                      maintain an active
                                                      connection
   -D, --domain-info=STRING                           Show most of the info we
                                                      have about the domain
   -i, --user-info=USER                               Get user info
       --uid-info=UID                                 Get user info from uid
       --group-info=GROUP                             Get group info
       --user-sidinfo=SID                             Get user info from sid
       --gid-info=GID                                 Get group info from gid
   -r, --user-groups=USER                             Get user groups
       --user-domgroups=SID                           Get user domain groups
       --sid-aliases=SID                              Get sid aliases
       --user-sids=SID                                Get user group sids for
                                                      user SID
   -a, --authenticate=user%password                   authenticate user
       --pam-logon=user%password                      do a pam logon equivalent
       --logoff                                       log off user
       --logoff-user=STRING                           username to log off
       --logoff-uid=INT                               uid to log off
       --set-auth-user=user%password                  Store user and password
                                                      used by winbindd (root
                                                      only)
       --ccache-save=user%password                    Store user and password
                                                      for ccache operation
       --getdcname=domainname                         Get a DC name for a
                                                      foreign domain
       --dsgetdcname=domainname                       Find a DC for a domain
       --dc-info=domainname                           Find the currently known
                                                      DCs
       --get-auth-user                                Retrieve user and
                                                      password used by winbindd
                                                      (root only)
   -p, --ping                                         Ping winbindd to see if
                                                      it is alive
       --domain=domain                                Define to the domain to
                                                      restrict operation
   -K, --krb5auth=user%password                       authenticate user using
                                                      Kerberos
       --krb5ccname=krb5ccname                        authenticate user using
                                                      Kerberos and specific
                                                      credential cache type
       --separator                                    Get the active winbind
                                                      separator
       --verbose                                      Print additional
                                                      information per command
       --change-user-password=STRING                  Change the password for a
                                                      user
       --ntlmv1                                       Use NTLMv1 cryptography
                                                      for user authentication
       --ntlmv2                                       Use NTLMv2 cryptography
                                                      for user authentication
       --lanman                                       Use lanman cryptography
                                                      for user authentication
 
 Help options:
   -?, --help                                         Show this help message
       --usage                                        Display brief usage
                                                      message
 
 Version options:
   -V, --version                                      Print version
 ```
 
 - - -
 
 ##### winbindd
 
 Name Service Switch daemon for resolving names from NT servers
 
 ```
 root@kali:~# winbindd --help
 Usage: winbindd [OPTION...]
   -n, --no-caching                   Disable caching
 
 Help options:
   -?, --help                         Show this help message
       --usage                        Display brief usage message
 
 Common Samba options:
   -d, --debuglevel=DEBUGLEVEL        Set debug level
       --debug-stdout                 Send debug output to standard output
   -s, --configfile=CONFIGFILE        Use alternative configuration file
       --option=name=value            Set smb.conf option from command line
   -l, --log-basename=LOGFILEBASE     Basename for log/debug files
       --leak-report                  enable talloc leak reporting on exit
       --leak-report-full             enable full talloc leak reporting on exit
 
 Daemon options:
   -D, --daemon                       Become a daemon (default)
   -i, --interactive                  Run interactive (not a daemon) and log to
                                      stdout
   -F, --foreground                   Run daemon in foreground (for
                                      daemontools, etc.)
       --no-process-group             Don't create a new process group
 
 Version options:
   -V, --version                      Print version
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\samba\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.095024
