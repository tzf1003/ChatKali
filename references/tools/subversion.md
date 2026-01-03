---
tool_id: subversion
title: subversion
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: http://subversion.apache.org/
repository: 
version: 1.14.5-4
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\subversion\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.132933
---

# Tool: subversion (subversion)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [http://subversion.apache.org/](http://subversion.apache.org/) |
| Repository |  |
| Version | 1.14.5-4 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/jamessan/subversion
- **PackagesInfo**: |
- ****Installed size**: ** `1.02 MB`
- ****How to install**: ** `sudo apt install subversion-tools`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# svnwrap -h
- **usage**: svnraisetreeconflict [OPTIONS] WC_PATH NODE_KIND OPERATION ACTION REASON REPOS_URL1 PATH_IN_REPOS1 PEG_REV1 NODE_KIND1 REPOS_URL2 PATH_IN_REPOS2 PEG_REV2 NODE_KIND2
- **Available subcommands**: []
- **For additional information, see http**: //subversion.apache.org/
- **general usage**: svnsync SUBCOMMAND DEST_URL  [ARGS & OPTIONS ...]
- **pre-1.8 compatibility mode**: run the 'validate' subcommand on TARGET.
- **Note**: any subcommand which takes the '--revision' and '--transaction'
- **Actions**: []
- **cp REV SRC-URL DST-URL**: copy SRC-URL@REV to DST-URL
- **mkdir URL**: create new directory URL
- **mv SRC-URL DST-URL**: move SRC-URL to DST-URL
- **rm URL**: delete URL
- **put SRC-FILE URL**: add or modify file URL with contents copied from
- **propset NAME VALUE URL**: set property NAME on URL to VALUE
- **propsetf NAME FILE URL**: set property NAME on URL to value read from FILE
- **propdel NAME URL**: delete property NAME from URL
- **Valid options**: []
- **-h, -? [--help]**: display this text
- **-m [--message] ARG**: use ARG as a log message
- **-F [--file] ARG**: read log message from file ARG
- **-u [--username] ARG**: commit the changes as username ARG
- **-p [--password] ARG**: use ARG as the password
- **--password-from-stdin**: read password from stdin
- **-U [--root-url] ARG**: interpret all action URLs relative to ARG
- **-r [--revision] ARG**: use revision ARG as baseline for changes
- **--with-revprop ARG**: set revision property in the following format:
- **--non-interactive**: do no interactive prompting (default is to
- **--force-interactive**: do interactive prompting even if standard
- **--trust-server-cert**: deprecated;
- **-X [--extra-args] ARG**: append arguments from file ARG (one per line;
- **--config-dir ARG**: use ARG to override the config directory
- **--config-option ARG**: use ARG to override a configuration option
- **--no-auth-cache**: do not cache authentication tokens
- **--version**: show program version information
- **-d [--daemon]**: daemon mode
- **-i [--inetd]**: inetd mode
- **-t [--tunnel]**: tunnel mode
- **-X [--listen-once]**: listen-once mode (useful for debugging)
- **-r [--root] ARG**: root of directory to serve
- **-R [--read-only]**: force read only, overriding repository config file
- **--config-file ARG**: read configuration from file ARG
- **--listen-port ARG**: listen port. The default port is 3690.
- **[mode**: tunnel]
- **--listen-host ARG**: listen hostname or IP address
- **-6 [--prefer-ipv6]**: prefer IPv6 when resolving the listen hostname
- **-c [--compression] ARG**: compression level to use for network transmissions
- **-M [--memory-cache-size] ARG**: size of the extra in-memory cache in MB used to
- **--cache-txdeltas ARG**: enable or disable caching of deltas between older
- **--cache-fulltexts ARG**: enable or disable caching of file contents
- **--cache-revprops ARG**: enable or disable caching of revision properties.
- **--cache-nodeprops ARG**: enable or disable caching of node properties
- **--client-speed ARG**: Optimize network handling based on the assumption
- **--block-read ARG**: Parse and cache all data found in block instead
- **-T [--threads]**: use threads instead of fork [mode: daemon]
- **--min-threads ARG**: Minimum number of server threads, even if idle.
- **--max-threads ARG**: Maximum number of server threads, even if there
- **--max-request-size ARG**: Maximum acceptable size of a client request in MB.
- **--max-response-size ARG**: Maximum acceptable server response size in MB.
- **--foreground**: run in foreground (useful for debugging)
- **--single-thread**: handle one connection at a time in the parent
- **--log-file ARG**: svnserve log file
- **--pid-file ARG**: write server process ID to file ARG
- **--tunnel-user ARG**: tunnel username (default is current uid's name)
- **-h [--help]**: display this help
- **--virtual-host**: virtual host mode (look for repo in directory
- **-q [--quiet]**: no progress (only errors) to stderr
- **is written to standard output.  For example**: []
- **copy is unusual the version identifier will be more complex**: []
- **4123**: 4168MS   mixed revision, modified, switched working copy
- **-n [--no-newline]**: do not output the trailing newline
- **-c [--committed]**: last changed rather than current revisions
- **clients and servers**: []
- *** svn-backup-dumps**: Incremental dumpfile-based backup script
- *** svn-bisect**: Bisect revisions to find a regression
- *** svn-clean**: Remove unversioned files from a working copy
- *** svn-hot-backup**: Backup script, primarily for BDB repositories
- *** svn_apply_autoprops**: Apply property settings from
- *** svn_load_dirs**: Sophisticated replacement for 'svn import'
- *** svnwrap**: Set umask to 002 before calling svn or svnserve
- *** fsfs-access-map**: Convert strace output into FSFS access map
- *** several example hook scripts**: commit-access-control, commit-email,
- **A typical strace invocation looks like this**: []
- **stats**: usage: svnfsfs stats REPOS_PATH
- **minimize redundant operations. Default**: 16.
- **Usage**: svnwrap {program} [args...]
- **Options**: []
- **the following command will skip files ending in ".zip"**: []
- **command will skip files ending in ".jpg" or ".png"**: []
- **The following command will skip the entire "build" subdirectory**: []
- **USAGE**: svn-hot-backup [OPTIONS] REPOS_PATH BACKUP_PATH
- **--archive-type=FMT Create an archive of the backup. FMT can be one of**: []
- **bz2**: Creates a bzip2 compressed tar file.
- **gz**: Creates a gzip compressed tar file.
- **zip**: Creates a compressed zip file.
- **zip64**: Creates a zip64 file (can be > 2GB).
- **positional arguments**: []
- **options**: []
- **--auto              Automatic mode**: detect moves, apply them and copy
- **--detect FILE       Semi-automatic mode**: detect moves and save them to FILE
- **--apply FILE        Semi-automatic mode**: apply the moves from FILE and copy
- **--save FILE         Automatic mode**: save moves to FILE after detection, then
- **Valid options are**: []
- **--help, -h**: Print this help text.
- **--config ARG**: Read the Subversion config file at path ARG
- **Unknown option**: h
- **svn_url        is the file**: // or http:// URL of the svn repository
- **-no_auto_exe   don't set svn**: executable for executable files
- **Valid enum argument values**: []
- **NODE_KIND, NODE_KIND1, NODE_KIND2**: []
- **OPERATION**: []
- **ACTION (what svn tried to do)**: []
- **REASON (what local change made svn fail)**: []
- **REPOS_URL1, REPOS_URL2**: []
- **The URL of the repository itself, e.g.**: file://usr/repos
- **PATH_IN_REPOS1, PATH_IN_REPOS2**: []
- **The complete path of the node in the repository, e.g.**: sub/dir/foo
- **PEG_REV1, PEG_REV2**: []
- **Example**: []
- **svnraisetreeconflict ./foo file update delete deleted file**: //usr/repos sub/dir/foo 1 file file://usr/repos sub/dir/foo 3 none
- **Valid programs**: svn svnlook svnserve svnadmin svnversion


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\subversion\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.132933
