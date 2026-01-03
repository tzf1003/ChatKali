---
tool_id: whatweb
title: whatweb
categories: ["information-gathering", "web-application-analysis"]
category_slugs: ["information-gathering", "web-application-analysis"]
homepage: https://morningstarsecurity.com/research/whatweb
repository: 
version: 0.6.3-1kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web"]
icon: images/whatweb-logo.svg
source_path: kali-tools\whatweb\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.170657
---

# Tool: whatweb (whatweb)

## Categories
- [information-gathering](../information-gathering.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://morningstarsecurity.com/research/whatweb](https://morningstarsecurity.com/research/whatweb) |
| Repository |  |
| Version | 0.6.3-1kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering kali-tools-vulnerability kali-tools-web |
| Icon | images/whatweb-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `18.75 MB`
- ****How to install**: ** `sudo apt install whatweb`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# whatweb -h
- **$. $     $$$ $. $$$$$$ $. $$$$$$ `$  $. $**: ' $. $     $$$ $. $$$$   $. $$$$$.
- **$**: :$  .  $$$ $::$  $$$ $::$  $$$     $::$     $::$  .  $$$ $::$      $::$  $$$$
- **Usage**: whatweb [options] <URLs>
- **TARGET SELECTION**: []
- **TARGET MODIFICATION**: []
- **AGGRESSION**: []
- **--aggression, -a=LEVEL	Set the aggression level. Default**: 1.
- **HTTP OPTIONS**: []
- **--header, -H			Add an HTTP header. eg "Foo**: Bar". Specifying a
- **empty value, e.g. "User-Agent**: " will remove it.
- **or `always'. Default**: always.
- **--max-redirects=NUM		Maximum number of redirects. Default**: 10.
- **AUTHENTICATION**: []
- **--user, -u=<user**: password>	HTTP basic authentication.
- **PROXY**: []
- **--proxy			<hostname[**: port]> Set proxy hostname and port.
- **Default**: 0.0.0.0.
- **--proxy-user			<username**: password> Set proxy user and password.
- **PLUGINS**: []
- **Examples**: :text=>'powered by abc'
- **"**: md5=>'8666257030b94d3bdb46e05945f60b42'"
- **"{**: text=>'powered by abc'}"
- **OUTPUT**: []
- **LOGGING**: []
- **--log-mongo-username		MongoDB username. Default**: nil.
- **--log-mongo-password		MongoDB password. Default**: nil.
- **--log-elastic-index		Name of the index to store results. Default**: whatweb
- **--log-elastic-host		Host**: port of the elastic http interface. Default: 127.0.0.1:9200
- **PERFORMANCE & STABILITY**: []
- **--max-threads, -t		Number of simultaneous threads. Default**: 25.
- **--open-timeout		Time in seconds. Default**: 15.
- **--read-timeout		Time in seconds. Default**: 30.
- **HELP & MISCELLANEOUS**: []
- **EXAMPLE USAGE**: []
- **whatweb --no-errors --url-prefix https**: // 192.168.0.0/24


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## WhatWeb Usage Example

```console
root@kali:~# whatweb -v -a 3 192.168.0.102
WhatWeb report for http://192.168.0.102
Status    : 200 OK
Title     : Toolz TestBed
IP        : 192.168.0.102
Country   : RESERVED, ZZ

Summary   : JQuery, Script, X-UA-Compatible[IE=edge], HTML5, Apache[2.2,2.2.22], HTTPServer[Ubuntu Linux][Apache/2.2.22 (Ubuntu)]

Detected Plugins:
[ Apache ]
  The Apache HTTP Server Project is an effort to develop and
  maintain an open-source HTTP server for modern operating
  systems including UNIX and Windows NT. The goal of this
  project is to provide a secure, efficient and extensible
  server that provides HTTP services in sync with the current
  HTTP standards.

  Version      : 2.2.22 (from HTTP Server Header)
  Version      : 2.2
  Version      : 2.2
  Google Dorks: (3)
  Website     : http://httpd.apache.org/

[ HTML5 ]
  HTML version 5, detected by the doctype declaration


[ HTTPServer ]
  HTTP server header string. This plugin also attempts to
  identify the operating system from the server header.

  OS           : Ubuntu Linux
  String       : Apache/2.2.22 (Ubuntu) (from server string)

[ JQuery ]
  A fast, concise, JavaScript that simplifies how to traverse
  HTML documents, handle events, perform animations, and add
  AJAX.

  Website     : http://jquery.com/

[ Script ]
  This plugin detects instances of script HTML elements and
  returns the script language/type.


[ X-UA-Compatible ]
  This plugin retrieves the X-UA-Compatible value from the
  HTTP header and meta http-equiv tag. - More Info:
  http://msdn.microsoft.com/en-us/library/cc817574.aspx

  String       : IE=edge

HTTP Headers:
  HTTP/1.1 200 OK
  Date: Mon, 26 Mar 2018 07:58:48 GMT
  Server: Apache/2.2.22 (Ubuntu)
  Last-Modified: Fri, 02 Feb 2018 15:27:56 GMT
  ETag: "11f-2e38-5643c5b56a8d3"
  Accept-Ranges: bytes
  Vary: Accept-Encoding
  Content-Encoding: gzip
  Content-Length: 3541
  Connection: close
  Content-Type: text/html

root@kali:~#
```


## Source
- Path: kali-tools\whatweb\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.170657
