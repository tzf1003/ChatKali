---
tool_id: python-faraday
title: python-faraday
categories: ["information-gathering", "vulnerability-analysis", "reporting-tools"]
category_slugs: ["information-gathering", "vulnerability-analysis", "reporting-tools"]
homepage: https://faradaysec.com
repository: 
version: 5.17.0-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-reporting"]
icon: images/python-faraday-logo.svg
source_path: kali-tools\python-faraday\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.062932
---

# Tool: python-faraday (python-faraday)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [reporting-tools](../reporting-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://faradaysec.com](https://faradaysec.com) |
| Repository |  |
| Version | 5.17.0-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-reporting |
| Icon | images/python-faraday-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/python-faraday
- **PackagesInfo**: |
- ****Installed size**: ** `35 KB`
- ****How to install**: ** `sudo apt install python-faraday`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# python-faraday -h
- **Usage**: faraday-manage [OPTIONS] COMMAND [ARGS]...
- **Options**: []
- **Commands**: []
- **usage**: faraday-worker-gevent [-h] [--queue QUEUE] [--concurrency CONCURRENCY]
- **options**: []
- **Could not start faraday-server. b'Failed to start faraday-server.service**: Unit faraday-server.service not found.\n'


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![python-faraday](images/faraday-01-main.png)

## Faraday Usage Examples

Faraday is a GUI application that consists of a ZSH terminal and a sidebar with details about your workspaces and hosts.

When Faraday supports the command you are running, it will automatically detect it and import the results. In the example below, the original nmap command that was entered was `nmap -A 192.168.0.7`, which Faraday converted on the fly.

```console
>>> WELCOME TO FARADAY
[+] Current Workspace: dev1
[+] API: OK
[faraday](dev1) kali#  nmap -oX /root/.faraday/data/devel1_Nmap_output-3.46164772371.xml -A 192.168.0.7 2>&1 | tee -a tmp.tu0ldZUG2JgzuHvLOjBYEzBx3Bu7O

Starting Nmap 7.40 ( https://nmap.org ) at 2017-03-07 13:46 MST
Nmap scan report for pi-hole (192.168.0.7)
Host is up (0.0011s latency).
Not shown: 995 closed ports
PORT    STATE SERVICE    VERSION
22/tcp  open  ssh        OpenSSH 6.7p1 Raspbian 5+deb8u3 (protocol 2.0)
| ssh-hostkey:
|   1024 f7:5d:7c:e2:c5:46:32:19:08:e9:4b:79:5e:80:1c:83 (DSA)
|   2048 3c:f9:1d:ce:03:0f:2e:d2:17:05:77:af:81:54:32:fc (RSA)
|_  256 ea:20:d1:e0:e1:89:2c:65:9e:0d:d0:d0:e9:8b:9b:28 (ECDSA)
53/tcp  open  domain     dnsmasq 2.72
| dns-nsid:
|_  bind.version: dnsmasq-2.72
80/tcp  open  http       lighttpd 1.4.35
|_http-server-header: lighttpd/1.4.35
|_http-title: Welcome page
110/tcp open  tcpwrapped
143/tcp open  tcpwrapped
Device type: general purpose
Running: Linux 2.4.X|3.X
OS CPE: cpe:/o:linux:linux_kernel:2.4.37 cpe:/o:linux:linux_kernel:3.2
OS details: DD-WRT v24-sp2 (Linux 2.4.37), Linux 3.2
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT     ADDRESS
1   0.27 ms 172.16.206.2
2   0.21 ms pi-hole (192.168.0.7)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.41 seconds
[faraday](devel1) kali#
```

Once the nmap scan is finished, double-clicking on the host under the `Hosts` tab will bring up details about the host, its services, and any vulnerabilities that were detected.

![python-faraday](images/faraday-02-host.png)

The excellent dirb utility is also supported by Faraday by default:

```console
[faraday](devel1) kali#  dirb http://192.168.0.23/commix-testbed -w 2>&1 | tee -a tmp.qNejUxvvrPpbGPVEfwf8OZOuM1F1E

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Tue Mar  7 13:58:52 2017
URL_BASE: http://192.168.0.23/commix-testbed/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt
OPTION: Not Stoping on warning messages

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://192.168.0.23/commix-testbed/ ----
==> DIRECTORY: http://192.168.0.23/commix-testbed/css/
==> DIRECTORY: http://192.168.0.23/commix-testbed/fonts/
==> DIRECTORY: http://192.168.0.23/commix-testbed/img/
+ http://192.168.0.23/commix-testbed/index.php (CODE:200|SIZE:14346)
==> DIRECTORY: http://192.168.0.23/commix-testbed/js/
==> DIRECTORY: http://192.168.0.23/commix-testbed/readme/

---- Entering directory: http://192.168.0.23/commix-testbed/css/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.0.23/commix-testbed/fonts/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.0.23/commix-testbed/img/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.0.23/commix-testbed/js/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

---- Entering directory: http://192.168.0.23/commix-testbed/readme/ ----
(!) WARNING: Directory IS LISTABLE. No need to scan it.
    (Use mode '-w' if you want to scan it anyway)

-----------------
END_TIME: Tue Mar  7 14:04:24 2017
DOWNLOADED: 27672 - FOUND: 1
```

When the scan is finished, double-clicking on the host will bring up its details, including the directories that dirb detected.

![python-faraday](images/faraday-03-vuln.png)

Take a look in the `/usr/share/python-faraday/plugins/repo` directory to see what other applications Faraday supports.

```console
root@kali:/usr/share/python-faraday/plugins/repo# ls
acunetix  dnsrecon      listurl       netsparker     retina          wapiti
amap      dnswalk       maltego       nexpose        reverseraider   wcscan
appscan   fierce        masscan       nexpose-full   sentinel        webfuzzer
arachni   fruitywifi    medusa        nikto          skipfish        whois
arp-scan  ftp           metagoofil    nmap           sqlmap          wpscan
beef      goohost       metasploit    openvas        sshdefaultscan  x1
burp      hping3        metasploiton  pasteanalyzer  sslcheck        zap
dig       hydra         ndiff         peepingtom     telnet
dirb      impact        nessus        ping           theharvester
dnsenum   __init__.py   netcat        propecia       traceroute
dnsmap    __init__.pyc  netdiscover   qualysguard    w3af
```

Faraday also includes a full-featured web interface that provides you, your team, and any other interested parties with an immense amount of information.

![python-faraday](images/faraday-04-web.png)


## Source
- Path: kali-tools\python-faraday\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.062932
