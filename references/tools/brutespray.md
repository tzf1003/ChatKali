---
tool_id: brutespray
title: brutespray
categories: ["password-attacks", "system-services"]
category_slugs: ["password-attacks", "system-services"]
homepage: https://github.com/x90skysn3k/brutespray
repository: 
version: 2.2.2-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\brutespray\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.816936
---

# Tool: brutespray (brutespray)

## Categories
- [password-attacks](../password-attacks.md)
- [system-services](../system-services.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/x90skysn3k/brutespray](https://github.com/x90skysn3k/brutespray) |
| Repository |  |
| Version | 2.2.2-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/brutespray
- **PackagesInfo**: |
- ****Installed size**: ** `24.46 MB`
- ****How to install**: ** `sudo apt install brutespray`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# brutespray -h
- **Usage of brutespray**: []
- **Specify a combo wordlist deiminated by '**: ', example: user1:password
- **Target in the format service**: //host:port, CIDR ranges supported,
- **File to parse; Supported**: Nmap, Nessus, Nexpose, Lists, etc
- **Service type**: ssh, ftp, smtp, etc; Default all (default "all")


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## brutespray Usage Examples

Attack all services in `nas.gnmap` with a specific user list (`unix_users.txt`) and password list (`password.lst`):

```console
root@kali:~# brutespray --file nas.gnmap -U /usr/share/wordlists/metasploit/unix_users.txt -P /usr/share/wordlists/metasploit/password.lst --threads 3 --hosts 1

                              #@                           @/
                           @@@                               @@@
                        %@@@                                   @@@.
                      @@@@@                                     @@@@%
                     @@@@@                                       @@@@@
                    @@@@@@@                  @                  @@@@@@@
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@
                                  @@@   @@@@@@@@@@@   @@@
                                 @@@@*  ,@@@@@@@@@(  ,@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@.@@@@@@@@@@@@@@@ @@@
                                    @@@@@@ @@@@@ @@@@@@
                                       @@@@@@@@@@@@@
                                       @@   @@@   @@
                                       @@ @@@@@@@ @@
                                         @@% @  @@



        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝███████║ ╚████╔╝
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗███████║██║     ██║  ██║██║  ██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝



 brutespray.py v1.5.2
 Created by: Shane Young/@x90skysn3k && Jacob Robles/@shellfail
 Inspired by: Leon Johnson/@sho-luv
 Credit to Medusa: JoMo-Kun / Foofus Networks <jmk@foofus.net>

Starting to brute, please make sure to use the right amount of threads(-t) and parallel hosts(-T)...  \

Brute-Forcing...
Medusa v2.2 [http://www.foofus.net] (C) JoMo-Kun / Foofus Networks <jmk@foofus.net>

ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^& (1 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$% (2 of 88396 complete)
ACCOUNT CHECK: [mysql] Host: 192.168.86.4 (1 of 1, 0 complete) User: 4Dgifts (1 of 111, 0 complete) Password: !@#$%^ (3 of 88396 complete)
[...]
```

Interactive mode, brute forcing the FTP service only.

```console
root@kali:~# brutespray -i -f nas.gnmap

                              #@                           @/
                           @@@                               @@@
                        %@@@                                   @@@.
                      @@@@@                                     @@@@%
                     @@@@@                                       @@@@@
                    @@@@@@@                  @                  @@@@@@@
                    @(@@@@@@@%            @@@@@@@            &@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                     @@*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@
                       @@@( @@@@@#@@@@@@@@@*@@@,@@@@@@@@@@@@@@@  @@@
                           @@@@@@ .@@@/@@@@@@@@@@@@@/@@@@ @@@@@@
                                  @@@   @@@@@@@@@@@   @@@
                                 @@@@*  ,@@@@@@@@@(  ,@@@@
                                 @@@@@@@@@@@@@@@@@@@@@@@@@
                                  @@@.@@@@@@@@@@@@@@@ @@@
                                    @@@@@@ @@@@@ @@@@@@
                                       @@@@@@@@@@@@@
                                       @@   @@@   @@
                                       @@ @@@@@@@ @@
                                         @@% @  @@



        ██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗██████╗ ██████╗  █████╗ ██╗   ██╗
        ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
        ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ███████╗██████╔╝██████╔╝███████║ ╚████╔╝
        ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ╚════██║██╔═══╝ ██╔══██╗██╔══██║  ╚██╔╝
        ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗███████║██║     ██║  ██║██║  ██║   ██║
        ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝



 brutespray.py v1.5.2
 Created by: Shane Young/@x90skysn3k && Jacob Robles/@shellfail
 Inspired by: Leon Johnson/@sho-luv
 Credit to Medusa: JoMo-Kun / Foofus Networks <jmk@foofus.net>

Loading File: /

Welcome to interactive mode!


WARNING: Leaving an option blank will leave it empty and refer to default


Available services to brute-force:
Service: ftp on port 21 with 1 hosts
Service: ssh on port 22 with 1 hosts
Service: mysql on port 3306 with 1 hosts

Enter services you want to brute - default all (ssh,ftp,etc): ftp
Enter the number of parallel threads (default is 2): 4
Enter the number of parallel hosts to scan per service (default is 1): 1
Would you like to specify a wordlist? (y/n): y
Enter a userlist you would like to use: /usr/share/wordlists/metasploit/unix_users.txt
Enter a passlist you would like to use: /usr/share/wordlists/metasploit/password.lst
Would to specify a single username or password (y/n): n

Starting to brute, please make sure to use the right amount of threads(-t) and parallel hosts(-T)...  \

Brute-Forcing...
```


## Source
- Path: kali-tools\brutespray\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.816936
