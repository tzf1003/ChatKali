---
tool_id: dotdotpwn
title: dotdotpwn
categories: ["vulnerability-analysis", "web-application-analysis", "information-gathering"]
category_slugs: ["vulnerability-analysis", "web-application-analysis", "information-gathering"]
homepage: https://dotdotpwn.blogspot.ca
repository: 
version: 3.0.2-0kali4
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\dotdotpwn\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.876145
---

# Tool: dotdotpwn (dotdotpwn)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://dotdotpwn.blogspot.ca](https://dotdotpwn.blogspot.ca) |
| Repository |  |
| Version | 3.0.2-0kali4 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dotdotpwn
- **PackagesInfo**: |
- ****Installed size**: ** `236 KB`
- ****How to install**: ** `sudo apt install dotdotpwn`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# dotdotpwn -h
- **Usage**: ./dotdotpwn.pl -m <module> -h <host> [OPTIONS]
- **Available options**: []
- **-d	Depth of traversals (e.g. deepness 3 equals to ../../../; default**: 6)
- **-f	Specific filename (e.g. /etc/motd; default**: according to OS detected, defaults in TraversalEngine.pm)
- **-S	Use SSL for HTTP and Payload module (not needed for http-url, use a https**: // url instead)
- **-u	URL with the part to be fuzzed marked as TRAVERSAL (e.g. http**: //foo:8080/id.php?x=TRAVERSAL&y=31337)
- **-k	Text pattern to match in the response (http-url & payload modules - e.g. "root**: " if trying /etc/passwd)
- **-x	Port to connect (default**: HTTP=80; FTP=21; TFTP=69)
- **-t	Time in milliseconds between each test (default**: 300 (.3 second))
- **-U	Username (default**: 'anonymous')
- **-P	Password (default**: 'dot@dot.pwn')
- **-M	HTTP Method to use when using the 'http' module [GET | POST | HEAD | COPY | MOVE] (default**: GET)
- **-r	Report filename (default**: 'HOST_MM-DD-YYYY_HOUR-MIN.txt')


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## dotdotpwn Usage Example

Use the HTTP scan module (`-m http`) against a host (`-h 192.168.1.1`) , using the GET method (`-M GET`):

```console
root@kali:~# dotdotpwn.pl -m http -h 192.168.1.1 -M GET
#################################################################################
#                                                                               #
#  CubilFelino                                                       Chatsubo   #
#  Security Research Lab              and            [(in)Security Dark] Labs   #
#  chr1x.sectester.net                             chatsubo-labs.blogspot.com   #
#                                                                               #
#                               pr0udly present:                                #
#                                                                               #
#  ________            __  ________            __  __________                   #
#  \______ \    ____ _/  |_\______ \    ____ _/  |_\______   \__  _  __ ____    #
#   |    |  \  /  _ \\   __\|    |  \  /  _ \\   __\|     ___/\ \/ \/ //    \   #
#   |    `   \(  <_> )|  |  |    `   \(  <_> )|  |  |    |     \     /|   |  \  #
#  /_______  / \____/ |__| /_______  / \____/ |__|  |____|      \/\_/ |___|  /  #
#          \/                      \/                                      \/   #
#                               - DotDotPwn v3.0 -                              #
#                         The Directory Traversal Fuzzer                        #
#                         http://dotdotpwn.sectester.net                        #
#                            dotdotpwn@sectester.net                            #
#                                                                               #
#                               by chr1x & nitr0us                              #
#################################################################################

[+] Report name: Reports/192.168.1.1_05-20-2014_08-41.txt

[========== TARGET INFORMATION ==========]
[+] Hostname: 192.168.1.1
[+] Protocol: http
[+] Port: 80

[=========== TRAVERSAL ENGINE ===========]
[+] Creating Traversal patterns (mix of dots and slashes)
[+] Multiplying 6 times the traversal patterns (-d switch)
[+] Creating the Special Traversal patterns
[+] Translating (back)slashes in the filenames
[+] Adapting the filenames according to the OS type detected (generic)
[+] Including Special sufixes
[+] Traversal Engine DONE ! - Total traversal tests created: 19680

[=========== TESTING RESULTS ============]
[+] Ready to launch 3.33 traversals per second
[+] Press Enter to start the testing (You can stop it pressing Ctrl + C)
```


## Source
- Path: kali-tools\dotdotpwn\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.876145
