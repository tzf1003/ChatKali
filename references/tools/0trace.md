---
tool_id: 0trace
title: 0trace
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://lcamtuf.coredump.cx
repository: 
version: 0.01-3kali5
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-information-gathering"]
icon: images/0trace-logo.svg
source_path: kali-tools\0trace\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.772490
---

# Tool: 0trace (0trace)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://lcamtuf.coredump.cx](https://lcamtuf.coredump.cx) |
| Repository |  |
| Version | 0.01-3kali5 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-information-gathering |
| Icon | images/0trace-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/0trace
- **PackagesInfo**: |
- ****Installed size**: ** `43 KB`
- ****How to install**: ** `sudo apt install 0trace`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# man usleep
- **Usage**: sendprobe src_ip dst_ip sport dport seq ack
- **Feature Test Macro Requirements for glibc (see feature_test_macros(7))**: []
- **usleep()**: []
- **Since glibc 2.12**: []
- **|| /* glibc >= 2.19**: */ _DEFAULT_SOURCE
- **|| /* glibc <= 2.19**: */ _BSD_SOURCE
- **Before glibc 2.12**: []


## Documentation (Upstream)
-----------------------------------------+---------------+---------+
        | Interface                                  | Attribute     | Value   |
        +--------------------------------------------+---------------+---------+
        | usleep()                                   | Thread safety | MT-Safe |
        +--------------------------------------------+---------------+---------+
 
 STANDARDS
        None.
 
 HISTORY
        4.3BSD, POSIX.1-2001.  POSIX.1-2001  declares  it  obsolete,  suggesting
        nanosleep(2) instead.  Removed in POSIX.1-2008.
 
        On  the  original BSD implementation, and before glibc 2.2.2, the return
        type of this function is void.  The POSIX version returns int, and  this
        is also the prototype used since glibc 2.2.2.
 
        Only the EINVAL error return is documented by SUSv2 and POSIX.1-2001.
 
 CAVEATS
        The interaction of this function with the SIGALRM signal, and with other
        timer  functions such as alarm(2), sleep(3), nanosleep(2), setitimer(2),
        timer_create(2), timer_delete(2), timer_getoverrun(2), timer_gettime(2),
        timer_settime(2), ualarm(3) is unspecified.
 
 SEE ALSO
        alarm(2), getitimer(2), nanosleep(2), select(2), setitimer(2), sleep(3),
        ualarm(3), useconds_t(3type), time(7)
 
 Linux man-pages 6.16               2025-09-21                         usleep(3)
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\0trace\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.772490
