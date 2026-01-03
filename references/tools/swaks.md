---
tool_id: swaks
title: swaks
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://www.jetmore.org/john/code/swaks/
repository: 
version: 20240103.0-2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering"]
icon: images/swaks-logo.svg
source_path: kali-tools\swaks\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.134540
---

# Tool: swaks (swaks)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.jetmore.org/john/code/swaks/](https://www.jetmore.org/john/code/swaks/) |
| Repository |  |
| Version | 20240103.0-2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-information-gathering |
| Icon | images/swaks-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/swaks
- **PackagesInfo**: |
- **SMTP dialog at any stage, e.g to check RCPT TO**: without actually
- ****Installed size**: ** `312 KB`
- ****How to install**: ** `sudo apt install swaks`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# swaks --help
- **test-server.example.net**: []
- **message DATA part.**: []
- **MX records for example.com**: []
- **test server**: []
- **messages envelope does not have  to  match  its  "To**:   and  "From:
- **"To**: ", "From:", "Subject:", etc.   In  this  document  headers  will
- **Here is an example of the contents of a configuration file**: []
- **h-From**: "Fred Example" <fred@example.com>
- **Options specific to configuration file**: []
- **example**: []
- **"SWAKS_OPT_header="Foo**: bar"" will work.)
- **file and environment variable sections**: []
- **$ swaks --from fred@example.com --h-From**: "Fred Example" <fred@example.com>
- **This  transport requires the IO**: :Socket::IP module for both IPv4 and
- **use the IO**: :Socket library for IPv4 and IO::Socket::INET6  for  IPv6
- **The fall back to IO**: :Socket and IO::Socket::INET6 is deprecated  and
- **-s, --server [<target-server>[**: <port>]]
- **email  address  using  the  Net**: :DNS module.  If Net::DNS is not
- **for   this   include  SERVER**: PORT  (supporting  names  and  IPv4
- **addresses); [SERVER]**: PORT  and  SERVER/PORT  (supporting  names,
- **-li, --local-interface [<local-interface>[**: <port>]]
- **additional  comments  on**: <port>  format.   A port set via this
- **transport  requires the IO**: :Socket::UNIX module which is part of the
- **This  transport  requires the IPC**: :Open2 module which is part of the
- **"%TO_ADDRESS%"  will  be  used  for  the  To**: header  and, if it is
- **populated,  "%CC_HEADER%"  will  be   used   for   a   Cc**: header.
- **Otherwise  the value from Win32**: :LoginName() will be used on Windows
- **Quit after MAIL FROM**: is sent.
- **Quit after RCPT TO**: is sent.
- **(PRDR) (<https**: //tools.ietf.org/html/draft-hall-prdr-00.txt>).  PRDR
- **Net**: :SSLeay  module  is used to perform encryption when it is requested.
- **<https**: //www.openssl.org/docs/manmaster/man1/openssl-ciphers.html#CIPHER-LIST-FORMAT>.
- **A brief example would be "--tls-cipher '3DES**: +RSA'". (Arg-Required)
- **All authentication methods require base64 encoding.  If the MIME**: :Base64
- **encodings.  If MIME**: :Base64 is not available  Swaks  will  use  its  own
- **onboard  base64  routines.   These  are  slower  than  the  MIME**: :Base64
- **Using the MIME**: :Base64 module is encouraged.
- **The  CRAM-MD5 authenticator requires the Digest**: :MD5 module.  It
- **The DIGEST-MD5 authenticator (RFC2831) requires the Authen**: :SASL
- **module.   Version  20100211.0 and earlier used Authen**: :DigestMD5
- **working  with  some servers.  Authen**: :SASL's DIGEST-MD5 handling
- **The  CRAM-SHA1  authenticator  requires  the Digest**: :SHA module.
- **These authenticators require the Authen**: :NTLM module.  This type
- **via .netrc (requires the Net**: :Netrc  module).   If  no  password  is
- **<http**: //twitter.com/SwaksSMTP>
- **argument starts with "base64**: ", that prefix is stripped and the rest
- **value  for  this  option  is  "Date**: %DATE%\nTo: %TO_ADDRESS%\nFrom:
- **%FROM_ADDRESS%\nSubject**: test           %DATE%\nMessage-Id:
- **<%MESSAGEID%>\nX-Mailer**: swaks           v%SWAKS_VERSION%
- **inclusion in the Date**: header.  Note this attempts  to  use  the
- **"--add-header  'Foo**: bar' --add-header 'Baz: foo'" and "--add-header
- **'Foo**: bar\nBaz: foo'" end up adding  the  same  two  headers.  (Arg-
- **the DATA.  "--header  'Subject**: foo'"  and  "--h-Subject  foo"  are
- **transaction.  This table indicates the hints and their meanings**: []
- **useful when Time**: :HiRes is available, in which case the  time  lapse
- **will  be  displayed  in  thousandths of a second.  If Time**: :HiRes is
- **use of IO**: :Socket and IO::Socket::INET6 modules
- **implemented with the IO**: :Socket::IP  module.   For  the  time  being
- **there    is   still   legacy   support   of   the   IO**: :Socket   and
- **IO**: :Socket::IP is installed to ensure future functionality.
- **instance, if a mail server returns a 550 response to  a  MAIL  FROM**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\swaks\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.134540
