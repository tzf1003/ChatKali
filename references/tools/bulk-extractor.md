---
tool_id: bulk-extractor
title: bulk-extractor
categories: ["forensics"]
category_slugs: ["forensics"]
homepage: https://github.com/simsong/bulk_extractor
repository: 
version: 2.1.1-0kali2
architectures: amd64 arm64
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: images/bulk-extractor-logo.svg
source_path: kali-tools\bulk-extractor\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.819055
---

# Tool: bulk-extractor (bulk-extractor)

## Categories
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/simsong/bulk_extractor](https://github.com/simsong/bulk_extractor) |
| Repository |  |
| Version | 2.1.1-0kali2 |
| Architectures | amd64 arm64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | images/bulk-extractor-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bulk-extractor
- **PackagesInfo**: |
- ****Installed size**: ** `15.79 MB`
- ****How to install**: ** `sudo apt install bulk-extractor`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bulk_extractor -h
- **bulk_extractor version 2.1.1**: A high-performance flexible digital forensics program.
- **Usage**: []
- **(default**: 16)
- **-d, --debug arg               enable debugging (default**: 1)
- **-G, --pagesize arg            page size in bytes (default**: 16777216)
- **-g, --marginsize arg          margin size in bytes (default**: 4194304)
- **-j, --threads arg             number of threads (default**: 6)
- **-M, --max_depth arg           max recursion depth (default**: 12)
- **max bad allocation errors (default**: 3)
- **data are read (default**: 60)
- **-p, --path arg                print the value of <path>[**: length][/h][/r] with
- **-s, --sampling arg            random sampling parameter frac[**: passes]
- **Global config options**: []
- **These scanners enabled; disable with -x**: []
- **These scanners disabled; enable with -e**: []
- **Options for setting carve mode in feature recorders that support carving**: []
- **Carve mode 0**: do not carve; mode 1: carve encoded data; mode 2: carve everything.


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## bulk_extractor Usage Example

Extract files to the output directory (`-o bulk-out`) after analyzing the image file (`xp-laptop-2005-07-04-1430.img`):

```console
root@kali:~# bulk_extractor -o bulk-out xp-laptop-2005-07-04-1430.img
bulk_extractor version: 1.3
Hostname: kali
Input file: xp-laptop-2005-07-04-1430.img
Output directory: bulk-out
Disk Size: 536715264
Threads: 1
Phase 1.
13:02:46 Offset 0MB (0.00%) Done in n/a at 13:02:45
13:03:39 Offset 67MB (12.50%) Done in  0:06:14 at 13:09:53
13:04:43 Offset 134MB (25.01%) Done in  0:05:50 at 13:10:33
13:04:55 Offset 201MB (37.51%) Done in  0:03:36 at 13:08:31
13:06:01 Offset 268MB (50.01%) Done in  0:03:15 at 13:09:16
13:06:48 Offset 335MB (62.52%) Done in  0:02:25 at 13:09:13
13:07:04 Offset 402MB (75.02%) Done in  0:01:25 at 13:08:29
13:07:20 Offset 469MB (87.53%) Done in  0:00:39 at 13:07:59
All Data is Read; waiting for threads to finish...
Time elapsed waiting for 1 thread to finish:
     (please wait for another 60 min .)
Time elapsed waiting for 1 thread to finish:
    6 sec (please wait for another 59 min 54 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    12 sec (please wait for another 59 min 48 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    18 sec (please wait for another 59 min 42 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    24 sec (please wait for another 59 min 36 sec.)
Thread 0: Processing 520093696

Time elapsed waiting for 1 thread to finish:
    30 sec (please wait for another 59 min 30 sec.)
Thread 0: Processing 520093696

All Threads Finished!
Producer time spent waiting: 335.984 sec.
Average consumer time spent waiting: 0.143353 sec.
*******************************************
** bulk_extractor is probably CPU bound. **
**    Run on a computer with more cores  **
**      to get better performance.       **
*******************************************
Phase 2. Shutting down scanners
Phase 3. Creating Histograms
   ccn histogram...   ccn_track2 histogram...   domain histogram...
   email histogram...   ether histogram...   find histogram...
   ip histogram...   tcp histogram...   telephone histogram...
   url histogram...   url microsoft-live...   url services...
   url facebook-address...   url facebook-id...   url searches...

Elapsed time: 378.5 sec.
Overall performance: 1.418 MBytes/sec.
Total email features found: 899
```


## Source
- Path: kali-tools\bulk-extractor\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.819055
