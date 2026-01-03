---
tool_id: hashcat
title: hashcat
categories: ["password-attacks"]
category_slugs: ["password-attacks"]
homepage: https://hashcat.net/hashcat/
repository: 
version: 7.1.2+ds1-3
architectures: kfreebsd-any amd64 arm64 armhf i386 all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-passwords kali-tools-wireless"]
icon: images/hashcat-logo.svg
source_path: kali-tools\hashcat\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.927719
---

# Tool: hashcat (hashcat)

## Categories
- [password-attacks](../password-attacks.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://hashcat.net/hashcat/](https://hashcat.net/hashcat/) |
| Repository |  |
| Version | 7.1.2+ds1-3 |
| Architectures | kfreebsd-any amd64 arm64 armhf i386 all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-802-11 kali-tools-passwords kali-tools-wireless |
| Icon | images/hashcat-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/hashcat
- **PackagesInfo**: |
- **Examples of hashcat supported hashing algorithms are**: []
- **osCommerce, xt**: Commerce, Skype, nsldap, Netscape, LDAP, nsldaps,
- **SSHA-1(Base64), Oracle S**: Type (Oracle 11+), SMF > v1.1, OS X v10.4,
- **complex coverage over a hash's keyspace. These modes are**: []
- ****Installed size**: ** `31.54 MB`
- ****How to install**: ** `sudo apt install hashcat-data`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# hashcat -h
- **Usage**: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...
- **-p, --separator                | Char | Separator char for hashlists and outfile             | -p**: []
- **--keyspace                 |      | Show keyspace base**: mod values and quit               |
- **--brain-server-timer       | Num  | Update the brain server dump each X seconds (min**: 60) | --brain-server-timer=300
- **1 | hash[**: salt]
- **3 | Original-Word**: Finding-Rule
- **4 | Original-Word**: Finding-Rule:Processed-Word
- **5 | Original-Word**: Finding-Rule:Processed-Word:Wordlist
- **s |  !"#$%&'()*+,-./**: ;<=>?@[\]^_`{|}~
- **If you still have no idea what just happened, try the following pages**: []
- *** https**: //hashcat.net/discord
- **If you think you need help by a real human come to the hashcat Discord**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## hashcat Usage Examples

Run a benchmark test on all supported hash types to determine cracking speed:

```console
root@kali:~# hashcat -b
hashcat (v5.0.0) starting in benchmark mode...

Benchmarking uses hand-optimized kernel code by default.
You can use it in your cracking session by setting the -O option.
Note: Using optimized kernel code limits the maximum supported password length.
To disable the optimized kernel code in benchmark mode, use the -w option.

* Device #1: Not a native Intel OpenCL runtime. Expect massive speed loss.
             You can use --force to override, but do not report related errors.
OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz, skipped.

OpenCL Platform #2: Intel(R) Corporation
========================================
* Device #2: Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz, 986/3946 MB allocatable, 2MCU

Benchmark relevant options:
===========================
* --optimized-kernel-enable

Hashmode: 0 - MD5

Speed.#2.........:   134.9 MH/s (15.41ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Hashmode: 100 - SHA1

Speed.#2.........: 98899.4 kH/s (21.04ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8

Hashmode: 1400 - SHA2-256

Speed.#2.........: 42768.3 kH/s (48.86ms) @ Accel:1024 Loops:1024 Thr:1 Vec:8
[...]
```

Use md5crypt mode (`-m 500`) to cracking the sample hash (`example500.hash`) with the provided wordlist (`/usr/share/wordlists/sqlmap.txt`):

```console
root@kali:~# hashcat -m 500 example500.hash /usr/share/wordlists/sqlmap.txt
hashcat (v5.0.0) starting...

* Device #1: Not a native Intel OpenCL runtime. Expect massive speed loss.
             You can use --force to override, but do not report related errors.
OpenCL Platform #1: The pocl project
====================================
* Device #1: pthread-Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz, skipped.

OpenCL Platform #2: Intel(R) Corporation
========================================
* Device #2: Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz, 986/3946 MB allocatable, 2MCU

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Applicable optimizers:
* Zero-Byte
* Single-Hash
* Single-Salt

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

ATTENTION! Pure (unoptimized) OpenCL kernels selected.
This enables cracking passwords and salts > length 32 but for the price of drastically reduced performance.
If you want to switch to optimized OpenCL kernels, append -O to your commandline.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

* Device #2: build_opts '-cl-std=CL1.2 -I OpenCL -I /usr/share/hashcat/OpenCL -D VENDOR_ID=8 -D CUDA_ARCH=0 -D AMD_ROCM=0 -D VECT_SIZE=8 -D DEVICE_TYPE=2 -D DGST_R0=0 -D DGST_R1=1 -D DGST_R2=2 -D DGST_R3=3 -D DGST_ELEM=4 -D KERN_TYPE=500 -D _unroll'
Dictionary cache hit:
* Filename..: /usr/share/wordlists/sqlmap.txt
* Passwords.: 1406529
* Bytes.....: 12790573
* Keyspace..: 1406529

[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit => s

Session..........: hashcat
Status...........: Running
Hash.Type........: md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)
Hash.Target......: $1$uOM6WNc4$r3ZGeSB11q6UUSILqek3J1
Time.Started.....: Sat Nov 24 22:37:25 2018 (26 secs)
Time.Estimated...: Sat Nov 24 22:40:46 2018 (2 mins, 55 secs)
Guess.Base.......: File (/usr/share/wordlists/sqlmap.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#2.........:     6969 H/s (9.09ms) @ Accel:256 Loops:125 Thr:1 Vec:8
Recovered........: 0/1 (0.00%) Digests, 0/1 (0.00%) Salts
Progress.........: 183808/1406529 (13.07%)
Rejected.........: 0/183808 (0.00%)
Restore.Point....: 183808/1406529 (13.07%)
Restore.Sub.#2...: Salt:0 Amplifier:0-1 Iteration:375-500
Candidates.#2....: 6104484 -> 61758102mt

[s]tatus [p]ause [b]ypass [c]heckpoint [q]uit =>
```


## Source
- Path: kali-tools\hashcat\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.927719
