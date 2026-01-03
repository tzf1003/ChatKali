---
tool_id: util-linux
title: util-linux
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/util-linux/util-linux
repository: []
version: 2.41.2-4
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-linux-wsl kali-tools-802-11 kali-tools-bluetooth kali-tools-crypto-stego kali-tools-database kali-tools-detect kali-tools-exploitation kali-tools-forensics kali-tools-fuzzing kali-tools-hardware kali-tools-identify kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-protect kali-tools-recover kali-tools-reporting kali-tools-respond kali-tools-reverse-engineering kali-tools-rfid kali-tools-sdr kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-voip kali-tools-vulnerability kali-tools-web kali-tools-windows-resources kali-tools-wireless"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\util-linux\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.157847
---

# Tool: util-linux (util-linux)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/util-linux/util-linux](https://github.com/util-linux/util-linux) |
| Repository |  |
| Version | 2.41.2-4 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-core kali-linux-default kali-linux-everything kali-linux-headless kali-linux-labs kali-linux-large kali-linux-nethunter kali-linux-wsl kali-tools-802-11 kali-tools-bluetooth kali-tools-crypto-stego kali-tools-database kali-tools-detect kali-tools-exploitation kali-tools-forensics kali-tools-fuzzing kali-tools-hardware kali-tools-identify kali-tools-information-gathering kali-tools-passwords kali-tools-post-exploitation kali-tools-protect kali-tools-recover kali-tools-reporting kali-tools-respond kali-tools-reverse-engineering kali-tools-rfid kali-tools-sdr kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-voip kali-tools-vulnerability kali-tools-web kali-tools-windows-resources kali-tools-wireless |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/debian/util-linux
- **PackagesInfo**: |
- **This package contains some extra BSD utilities**: col, colcrt, colrm, column,
- ****Installed size**: ** `223 KB`
- ****How to install**: ** `sudo apt install uuid-runtime`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# uuidparse -h
- **Usage**: []
- **Options**: []
- **Spreadsheet**: :WriteExcel::Chart::A writer class for Excel Column charts.
- **Arguments**: []
- **Values for <length> and <offset> may be followed by a suffix**: KiB, MiB,
- **system**: renice, script, scriptlive, scriptreplay and wall. The
- **Values for <size> may be followed by a suffix**: KiB, MiB,
- **Key bindings**: []
- **-u, --units[=<unit>]          display units**: 'cylinders' or 'sectors' (default)
- **Available output columns**: []
- **gpt**: Device Start End Sectors Size Type Type-UUID Attrs Name UUID
- **dos**: Device Start End Sectors Cylinders Size Type Id Attrs Boot End-C/H/S
- **bsd**: Slice Start End Sectors Cylinders Size Type Bsize Cpg Fsize
- **sgi**: Device Start End Sectors Cylinders Size Type Id Attrs
- **sun**: Device Start End Sectors Cylinders Size Type Id Flags
- **Commands**: []
- **changing effective user or group IDs, including**: []
- **BACK-MAJ**: MIN  backing file major:minor device number
- **MAJ**: MIN  loop device major:minor number
- **--map-groups <inner>**: <outer>:<count>
- **--map-users <inner>**: <outer>:<count>
- **Operations**: []
- **The <spec> parameter**: []
- **Available discard policy types (for --discard)**: []
- **once**: only single-time area discards are issued
- **pages**: freed pages are discarded before they are reused
- **Values for <num> may be followed by a suffix**: KiB, MiB,
- **-o, --output <format>      output format; can be one of**: []
- **value, device, export, json or full; (default**: full)
- **Low-level probing options**: []
- **Values for <size> and <offset> may be followed by a suffix**: KiB, MiB,
- **<dev> specify device(s) to probe (default**: all devices)
- **Available commands**: []
- **Set policy**: []
- **Get policy**: []
- **Policy options**: []
- **Scheduling options**: []
- **Other options**: []
- **--time-format <format>  show timestamp using the given format**: []
- **Supported log facilities**: []
- **Supported log levels (priorities)**: []
- **Data sources**: []
- **Data filters**: []
- **-S, --source <string>  the device to mount (by name, maj**: min,
- **0**: none, 1: realtime, 2: best-effort, 3: idle
- **Resource options**: []
- **Output options**: []
- **--ct <name>[**: <param>[:<func>]] define a custom counter
- **-e, --exclude <list> exclude devices by major number (default**: RAM disks)
- **methods used to gather data (default**: file,udev,blkid)
- **Available output columns for -e or -p**: []
- **Available output columns for -C**: []
- **Generic System V columns**: []
- **Generic POSIX columns**: []
- **System V Shared-memory columns (--shmems)**: []
- **System V Message-queue columns (--queues)**: []
- **System V Semaphore columns (--semaphores)**: []
- **POSIX Semaphore columns (--posix-semaphores)**: []
- **Summary columns (--global)**: []
- **-d, --fs-devno     print maj**: min device number of the filesystem
- **-x, --devno        print maj**: min device number of the block device
- **partx [-a|-d|-s|-u] [--nr <n**: m> | <partition>] <disk>
- **-n, --nr <n**: m>       specify the range of partitions (e.g. --nr 2:4)
- **Resources**: []
- **<limit> is defined as a range soft**: hard, soft:, :hard or a value to
- **define both limits (e.g. -e=0**: 10 -r=:10).
- **-m, --mapfile <mapfile>   (defaults**: "/boot/System.map" and
- **-p, --profile <pro-file>  (default**: "/proc/profile")
- **Landlock accesses**: []
- **Access**: fs
- **Rule types**: path-beneath
- **Rules**: execute,write-file,read-file,read-dir,remove-dir,remove-file,make-char,make-dir,make-reg,make-sock,make-fifo,make-block,make-sym,refer,truncate
- **<color>**: black blue cyan green grey magenta red white yellow
- **-t, --timeout <seconds>  max time to wait for a password (default**: no limit)
- **The default behavior is to run a new command**: []
- **You can retrieve the mask of an existing task**: []
- **Or set it**: []
- **List format uses a comma-separated list instead of a mask**: []
- **Ranges in list format can take a stride argument**: []
- **e.g. 0-31**: 2 is equivalent to mask 0x55555555
- **Utilization value range is [0**: 1024]. Use special -1 value to reset to system's default.
- **--map-users <inneruid>**: <outeruid>:<count>
- **--map-groups <innergid>**: <outergid>:<count>
- **<alg> is the name of an algorithm; supported are**: []
- **COMP-RATIO  compression ratio**: DATA/TOTAL
- **with certain hardware, for example**: []
- **Output modes**: []
- **<cmd> is a command; available commands are**: []
- *** register**: This command registers a new reservation if the key argument
- *** reserve**: This command reserves the device and thus restricts access for
- *** release**: This command releases the reservation specified by key and flags
- *** preempt**: This command releases the existing reservation referred to by
- *** preempt-abort**: This command works like preempt except that it also aborts
- *** clear**: This command unregisters both key and any other reservation
- **<flag> is a command flag; available flags are**: []
- *** ignore-key**: Ignore the existing reservation key.  This is commonly
- **<type> is a command type; available types are**: []
- *** write-exclusive**: Only the initiator that owns the reservation can
- *** exclusive-access**: Only the initiator that owns the reservation can
- *** write-exclusive-reg-only**: Only initiators with a registered key can
- *** exclusive-access-reg-only**: Only initiators with a registered key can
- *** write-exclusive-all-regs**: Only initiators with a registered key can
- *** exclusive-access-all-regs**: Only initiators with a registered key can
- **Values for <sector> and <sectors> may be followed by a suffix**: KiB, MiB,
- **Supported zones**: []
- **Functions**: []
- **Can be one of the following**: pid, tgid or pgid.
- **-a, --advice <advice> applying advice to the file (default**: "dontneed")
- **Available values for advice**: []
- **<param> is either a numeric RTC parameter value or one of these aliases**: ['features: supported features (0x0)', 'correction: time correction (0x1)', 'bsm: backup switch mode (0x2)']
- **Options relevant to GSM0710**: []
- **Known <ldisc> names**: []
- **Known <iflag> names**: []
- **-C, --counter <name>**: <expr>  define custom counter for --summary output
- **Default columns**: []
- **Default**: COMMAND,PID,USER,ASSOC,XMODE,TYPE,SOURCE,MNTID,INODE,NAME
- **With --threads**: COMMAND,PID,TID,USER,ASSOC,XMODE,TYPE,SOURCE,MNTID,INODE,NAME
- **available namespaces**: @dns @url @oid @x500


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\util-linux\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.157847
