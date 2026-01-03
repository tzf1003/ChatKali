---
tool_id: jsql
title: jsql
categories: ["information-gathering", "vulnerability-analysis", "web-application-analysis", "password-attacks", "exploitation-tools", "post-exploitation"]
category_slugs: ["information-gathering", "vulnerability-analysis", "web-application-analysis", "password-attacks", "exploitation-tools", "post-exploitation"]
homepage: https://github.com/ron190/jsql-injection
repository: 
version: 0.112-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-database kali-tools-web"]
icon: images/jsql-logo.svg
source_path: kali-tools\jsql\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.956172
---

# Tool: jsql (jsql)

## Categories
- [information-gathering](../information-gathering.md)
- [vulnerability-analysis](../vulnerability-analysis.md)
- [web-application-analysis](../web-application-analysis.md)
- [password-attacks](../password-attacks.md)
- [exploitation-tools](../exploitation-tools.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ron190/jsql-injection](https://github.com/ron190/jsql-injection) |
| Repository |  |
| Version | 0.112-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-database kali-tools-web |
| Icon | images/jsql-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/jsql
- **PackagesInfo**: |
- ****Installed size**: ** `11.60 MB`
- ****How to install**: ** `sudo apt install jsql-injection`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# jsql-injection -h
- **2025-11-27 10**: 11:58,429 ERROR [main] jsql.MainApp (MainApp.java:28) - Headless runtime not supported, use default Java runtime instead


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## Description
**jSQL Injection** is a lightweight application used to find database information from a server.

It's **free**, **open source** and **cross-platform** and it works with Java from version 11 to 20.

The source code is available on Github: https://github.com/ron190/jsql-injection

## Features
- Automatic injection of 33 database engines: Access, Altibase, C-treeACE, CockroachDB, CUBRID, DB2, Derby, Exasol, Firebird, FrontBase, H2, Hana, HSQLDB, Informix, Ingres, InterSystems-IRIS, MaxDB, Mckoi, MemSQL, MimerSQL, MonetDB, MySQL, Neo4j, Netezza, NuoDB, Oracle, PostgreSQL, Presto, SQLite, SQL Server, Sybase, Teradata and Vertica
- Multiple injection strategies: Normal, Stacked, Error, Blind and Time
- Parallel bitwise Boolean Blind and Time strategies
- Various injection processes: Default, Zip, Dios
- Database fingerprint: Basic error, Order By error, Boolean single query
- Script sandboxes for SQL and tampering
- Inject multiple targets
- Read and write files using injection
- Create and display Web shell and SQL shell
- Bruteforce password hash
- Search for admin pages
- Hash, encode and decode text
- Authenticate using Basic, Digest, NTLM and Kerberos  
- Proxy connection on HTTP, SOCKS4 and SOCKS5

## Continuous integration
This software is developed using open source libraries like [Spring](https://spring.io), [Spock](http://spockframework.org) and [Hibernate](https://hibernate.org) and is tested using continuous integration platform Github Actions.<br> 
Non regression tests are run against dockerized and in memory databases and GUI is tested on VNC screen on the CI platform, then quality checks are stored on code quality platform.

## Screenshots

```console
jsql
```

![jsql](images/jsql.png)
![jsql](images/admin.png)
![jsql](images/webshell.png)

## Source
- Path: kali-tools\jsql\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.956172
