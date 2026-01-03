---
tool_id: john
title: john
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://www.openwall.com/john/
repository: 
version: 1.9.0-Jumbo-1+git20211102-0kali10
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-identify kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-reverse-engineering kali-tools-social-engineering kali-tools-top10 kali-tools-vulnerability kali-tools-web"]
icon: images/john-logo.svg
source_path: kali-tools\john\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.954035
---

# Tool: john (john)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.openwall.com/john/](https://www.openwall.com/john/) |
| Repository |  |
| Version | 1.9.0-Jumbo-1+git20211102-0kali10 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-identify kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-reverse-engineering kali-tools-social-engineering kali-tools-top10 kali-tools-vulnerability kali-tools-web |
| Icon | images/john-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/john
- **PackagesInfo**: |
- ****Installed size**: ** `61.07 MB`
- ****How to install**: ** `sudo apt install john-data`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# truecrypt2john -h
- **SIPcrack is a SIP login sniffer/cracker that contains 2  programs**: sip-
- **base64conv**: invalid option -- 'h'
- **Usage**: truecrypt2john [options]
- **Input/Output types**: []
- **Flags (note more than 1 -f command switch can be given at one time)**: []
- **Options**: []
- **-p**: include non printable and 8-bit characters
- **-p        Only convert stuff after first '**: ' (.pot file).
- **John the Ripper 1.9.0-jumbo-1+bleeding-aec1328d6c 2021-11-02 10**: 45:52 +0100 OMP [linux-gnu 64-bit x86_64 SSE2 AC]
- **--single=**: rule[,..]        Same, using "immediate" rule(s)
- **--single-user-seed=FILE    Wordlist with seeds per username (user**: password[s]
- **--rules=**: rule[;..]]        Same, using "immediate" rule(s)
- **--rules-stack=**: rule[;..]   Same, using "immediate" rule(s)
- **--rules-skip-nop           Skip any NOP "**: " rules (you already ran w/o rules)
- **--salts=[-]COUNT[**: MAX]     Load salts with[out] COUNT [to MAX] hashes, or
- **--costs=[-]C[**: M][,...]     Load salts with[out] cost value Cn [to Mn]. For
- **--field-separator-char=C   Use 'C' instead of the '**: ' in input and pot files
- **keepass2john**: invalid option -- 'h'
- **rar2john**: invalid option -- 'h'
- **tgtsnarf**: invalid option -- '-'
- **Supported encapsulations**: 802.11, Prism, Radiotap, PPI and TZSP over UDP.
- **-e <essid**: mac>	Manually add Name:MAC pair(s) in case the file lacks beacons.
- **eg. -e "Magnum WIFI**: 6d:61:67:6e:75:6d"
- **zip2john**: invalid option -- 'h'
- **Options for 'old' PKZIP encrypted files only**: []
- **NOTE**: By default it is assumed that all files in each archive have the same
- **usage**: tezos2john [-h] [-i] [-I]
- **options**: []
- **/usr/bin/cisco2john/john -format**: md5 -wordlist:seed.txt -rules hashfile
- **positional arguments**: []
- **Traceback (most recent call last)**: []
- **FileNotFoundError**: [Errno 2] No such file or directory: '-h'
- **During handling of the above exception, another exception occurred**: []
- **sys.stderr.write("! %s**: %s\n" % filename, str(e))
- **TypeError**: not enough arguments for format string
- **-h**: [Errno 2] No such file or directory: '-h'
- **Find more Information**: []
- **Syntax**: pdf2john.pl <.pdf file(s)>
- **ERPScan Research Group - https**: //www.erpscan.io
- **[Errno 2] No such file or directory**: -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Mailer

```console
root@kali:~# mailer
Usage: /usr/sbin/mailer PASSWORD-FILE
```

## Unique

```console
root@kali:~# unique
Usage: unique [-v] [-inp=fname] [-cut=len] [-mem=num] OUTPUT-FILE [-ex_file=FNAME2] [-ex_file_only=FNAME2]

       reads from stdin 'normally', but can be overridden by optional -inp=
       If -ex_file=XX is used, then data from file XX is also used to
       unique the data, but nothing is ever written to XX. Thus, any data in
       XX, will NOT output into OUTPUT-FILE (for making iterative dictionaries)
       -ex_file_only=XX assumes the file is 'unique', and only checks against XX
       -cut=len  Will trim each input lines to 'len' bytes long, prior to running
       the unique algorithm. The 'trimming' is done on any -ex_file[_only] file
       -mem=num.  A number that overrides the UNIQUE_HASH_LOG value from within
       params.h.  The default is 21.  This can be raised, up to 25 (memory usage
       doubles each number).  If you go TOO large, unique will swap and thrash and
       work VERY slow

       -v is for 'verbose' mode, outputs line counts during the run
```


## john Usage Example

Using a wordlist (`–wordlist=/usr/share/john/password.lst`), apply mangling rules (`–rules`) and attempt to crack the password hashes in the given file (`unshadowed.txt`):

```console
root@kali:~# john --wordlist=/usr/share/john/password.lst --rules unshadowed.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "crypt"
Use the "--format=crypt" option to force loading these as that type instead
Loaded 1 password hash (sha512crypt [64/64])
toor             (root)
guesses: 1  time: 0:00:00:07 DONE (Mon May 19 08:13:05 2014)  c/s: 482  trying: 1701d - andrew
Use the "--show" option to display all of the cracked passwords reliably
```

- - -

```console
kali@kali:~$ echo -n test2 | md5sum
ad0234829205b9033196ba818f7a872b  -
kali@kali:~$ echo -n test2 | md5sum | awk '{print $1}'
ad0234829205b9033196ba818f7a872b
kali@kali:~$ echo -n test2 | md5sum | awk '{print $1}' > hash
kali@kali:~$ 
kali@kali:~$ for x in $(seq 0 9); do echo test$x >> wordlists; done
kali@kali:~$ grep test2 wordlists 
test2
kali@kali:~$ wc -l wordlists 
10 wordlists
kali@kali:~$ 
kali@kali:~$ john --list=formats | grep -i 'md5'
descrypt, bsdicrypt, md5crypt, md5crypt-long, bcrypt, scrypt, LM, AFS, 
aix-ssha512, andOTP, ansible, argon2, as400-des, as400-ssha1, asa-md5, 
dahua, dashlane, diskcryptor, Django, django-scrypt, dmd5, dmg, dominosec, 
mschapv2-naive, krb5pa-md5, mssql, mssql05, mssql12, multibit, mysqlna, 
mysql-sha1, mysql, net-ah, nethalflm, netlm, netlmv2, net-md5, netntlmv2, 
netntlm, netntlm-naive, net-sha1, nk, notes, md5ns, nsec3, NT, o10glogon, 
PBKDF2-HMAC-MD4, PBKDF2-HMAC-MD5, PBKDF2-HMAC-SHA1, PBKDF2-HMAC-SHA256, 
PHPS2, pix-md5, PKZIP, po, postgres, PST, PuTTY, pwsafe, qnx, RACF, 
Raw-Keccak, Raw-Keccak-256, Raw-MD4, Raw-MD5, Raw-MD5u, Raw-SHA1, 
Stribog-256, Stribog-512, STRIP, SunMD5, SybaseASE, Sybase-PROP, tacacs-plus, 
tcp-md5, telegram, tezos, Tiger, tc_aes_xts, tc_ripemd160, tc_ripemd160boot, 
ZipMonster, plaintext, has-160, HMAC-MD5, HMAC-SHA1, HMAC-SHA224, 
kali@kali:~$ 
kali@kali:~$ john  --format=raw-md5 --wordlist=wordlists hash
Created directory: /home/g0tmi1k/.john
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-MD5 [MD5 128/128 AVX 4x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 10 candidates left, minimum 12 needed for performance.
test2            (?)
1g 0:00:00:00 DONE (2021-11-04 10:30) 100.0g/s 1000p/s 1000c/s 1000C/s test0..test9
Use the "--show --format=Raw-MD5" options to display all of the cracked passwords reliably
Session completed
kali@kali:~$
```

## unique Usage Example

Using verbose mode (`-v`), read a list of passwords (`-inp=allwords.txt`) and save only unique words to a file (`uniques.txt`):

```console
root@kali:~# unique -v -inp=allwords.txt uniques.txt
Total lines read 6089 Unique lines written 5083
```


## Source
- Path: kali-tools\john\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.954035
