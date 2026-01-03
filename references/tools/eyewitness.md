---
tool_id: eyewitness
title: eyewitness
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://www.christophertruncer.com/eyewitness-triage-tool/
repository: 
version: 20230525.1+git20230720-0kali4
architectures: amd64 arm64 i386
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-reporting kali-tools-vulnerability kali-tools-web"]
icon: images/eyewitness-logo.svg
source_path: kali-tools\eyewitness\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.893321
---

# Tool: eyewitness (eyewitness)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.christophertruncer.com/eyewitness-triage-tool/](https://www.christophertruncer.com/eyewitness-triage-tool/) |
| Repository |  |
| Version | 20230525.1+git20230720-0kali4 |
| Architectures | amd64 arm64 i386 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-large kali-tools-information-gathering kali-tools-reporting kali-tools-vulnerability kali-tools-web |
| Icon | images/eyewitness-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/eyewitness
- **PackagesInfo**: |
- ****Installed size**: ** `5.78 MB`
- ****How to install**: ** `sudo apt install eyewitness`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# geckodriver -h
- **usage**: EyeWitness.py [--web] [-f Filename] [-x Filename.xml]
- **Protocols**: []
- **Input Options**: []
- **Timing Options**: []
- **web page (Default**: 7)
- **Report Output Options**: []
- **Web Options**: []
- **requests are close "enough" (Default**: 50)
- **--prepend-https       Prepend http**: // and https:// to URLs without either
- **Resume Options**: []
- **geckodriver 0.33.0 (a80e5fd61076 2023-04-02 18**: 31 +0000)
- **USAGE**: []
- **OPTIONS**: []
- **List of request origins to allow. These must be formatted as scheme**: //host:port. By
- **Selects storage location to be used for test data (deprecated). [possible values**: auto,
- **Host IP to use for WebDriver server [default**: 127.0.0.1]
- **Set Gecko log level [possible values**: fatal, error, warn, info, config, debug, trace]
- **Host to use to connect to Gecko [default**: 127.0.0.1]
- **Port to use to connect to Gecko [default**: system-allocated port]
- **Port to use for WebDriver server [default**: 4444]
- **Port to use to connect to WebDriver BiDi [default**: 9222]


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## eyewitness Usage Examples

Take a screenshot of each of the websites listed in the provided file using headless mode:

```console
root@kali:~# cat urls.txt
https://www.kali.org
https://www.kali.org/docs
https://www.kali.org/tools
https://www.exploit-db.com
https://www.offsec.com

root@kali:~# eyewitness -f /root/urls.txt -d screens --headless

################################################################################
#                                  EyeWitness                                  #
################################################################################

Starting Web Requests (5 Hosts)
Attempting to screenshot https://www.kali.org
Attempting to screenshot https://www.kali.org/docs
Attempting to screenshot https://www.kali.org/tools
Attempting to screenshot https://www.exploit-db.com
Attempting to screenshot https://www.offsec.com
Finished in 14.1417660713 seconds

[*] Done! Report written in the /usr/share/eyewitness/screens folder!
Would you like to open the report now? [Y/n] Y
```


## Source
- Path: kali-tools\eyewitness\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.893321
