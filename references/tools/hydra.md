---
tool_id: hydra
title: hydra
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://github.com/vanhauser-thc/thc-hydra
repository: 
version: 9.6-3
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web"]
icon: images/hydra-logo.svg
source_path: kali-tools\hydra\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.940909
---

# Tool: hydra (hydra)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/vanhauser-thc/thc-hydra](https://github.com/vanhauser-thc/thc-hydra) |
| Repository |  |
| Version | 9.6-3 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-passwords kali-tools-top10 kali-tools-vulnerability kali-tools-web |
| Icon | images/hydra-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/hydra
- **PackagesInfo**: |
- **It supports**: Cisco AAA, Cisco auth, Cisco enable, CVS, FTP, HTTP(S)-FORM-GET,
- ****Installed size**: ** `964 KB`
- ****How to install**: ** `sudo apt install hydra`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pw-inspector -h
- **Syntax**: pw-inspector [-i FILE] [-o FILE] [-m MINLEN] [-M MAXLEN] [-c MINSETS] -l -u -n -p -s
- **http**: //open-sez.me
- **Options**: []
- **help        Help**: Show this message
- **refresh     Refresh list**: Download the full (d)efault (p)assword (l)ist
- **the format username**: password (as required by THC hydra).
- **Example**: []
- **-x MIN**: MAX:CHARSET  password bruteforce generation, type "-x -h" to get help
- **-C FILE   colon separated "login**: pass" format, instead of -L/-P options
- **-M FILE   list of servers to attack, one entry per line, '**: ' to specify port
- **-b FORMAT specify the format for the -o FILE**: text(default), json, jsonv1
- **-f / -F   exit when a login/pass pair is found (-M**: -f per host, -F global)
- **-t TASKS  run TASKS number of connects in parallel per target (default**: 16)
- **-T TASKS  run TASKS connects in parallel overall (for -M, default**: 64)
- **server    the target**: DNS, IP or 192.168.0.0/24 (this OR the -M option)
- **Supported services**: adam6500 asterisk cisco cisco-enable cobaltstrike cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smb2 smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp
- **https**: //github.com/vanhauser-thc/thc-hydra
- **These services were not compiled in**: afp ncp oracle sapr3.
- **E.g. % export HYDRA_PROXY=socks5**: //l:p@127.0.0.1:9150 (or: socks4:// connect://)
- **% export HYDRA_PROXY_HTTP=http**: //login:pass@proxy:8080
- **Examples**: []
- **hydra -l user -P passlist.txt ftp**: //192.168.0.1
- **hydra -L userlist.txt -p defaultpw imap**: //192.168.0.1/PLAIN
- **hydra -C defaults.txt -6 pop3s**: //[2001:db8::1]:143/TLS:DIGEST-MD5
- **hydra -l admin -p password ftp**: //[192.168.0.0/24]/
- **PW-Inspector v0.2 (c) 2005 by van Hauser / THC vh@thc.org [https**: //github.com/vanhauser-thc/thc-hydra]
- **-i FILE    file to read passwords from (default**: stdin)
- **-o FILE    file to write valid passwords to (default**: stdout)
- **-c MINSETS the minimum number of sets required (default**: all given)
- **Sets**: []
- **Use for security**: check passwords, if 0 is returned, reject password choice.
- **Use for hacking**: trim your dictionary file to the pw requirements of the target.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hydra Usage Example

Attempt to login as the root user (`-l root`) using a password list (`-P /usr/share/wordlists/metasploit/unix_passwords.txt`) with 6 threads (`-t 6`) on the given SSH server (`ssh://192.168.1.123`):

```console
root@kali:~# hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt -t 6 ssh://192.168.1.123
Hydra v7.6 (c)2013 by van Hauser/THC & David Maciejak - for legal purposes only

Hydra (http://www.thc.org/thc-hydra) starting at 2014-05-19 07:53:33
[DATA] 6 tasks, 1 server, 1003 login tries (l:1/p:1003), ~167 tries per task
[DATA] attacking service ssh on port 22
```

## pw-inspector Usage Example

Read in a list of passwords (`-i /usr/share/wordlists/nmap.lst`) and save to a file (`-o /root/passes.txt`), selecting passwords of a minimum length of 6 (`-m 6`) and a maximum length of 10 (`-M 10`):

```console
root@kali:~# pw-inspector -i /usr/share/wordlists/nmap.lst -o /root/passes.txt -m 6 -M 10
root@kali:~# wc -l /usr/share/wordlists/nmap.lst
5086 /usr/share/wordlists/nmap.lst
root@kali:~# wc -l /root/passes.txt
4490 /root/passes.txt
```



## Source
- Path: kali-tools\hydra\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.940909
