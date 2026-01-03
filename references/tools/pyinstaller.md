---
tool_id: pyinstaller
title: pyinstaller
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://pyinstaller.org/en/stable/
repository: 
version: 6.16.0+ds-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: images/pyinstaller-logo.svg
source_path: kali-tools\pyinstaller\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.061688
---

# Tool: pyinstaller (pyinstaller)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://pyinstaller.org/en/stable/](https://pyinstaller.org/en/stable/) |
| Repository |  |
| Version | 6.16.0+ds-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | images/pyinstaller-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/python-team/packages/pyinstaller
- **PackagesInfo**: |
- ****Installed size**: ** `2.33 MB`
- ****How to install**: ** `sudo apt install python3-pyinstaller`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pyinstaller -h
- **usage**: pyinstaller [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
- **positional arguments**: []
- **options**: []
- **-l, --list         List the archive contents and exit (default**: False).
- **-r, --recursive    Recursively print an archive log (default**: False).
- **(default**: first script's basename)
- **ERROR, FATAL (default**: INFO). Also settable via and
- **[--add-data SOURCE**: DEST] [--add-binary SOURCE:DEST]
- **What to generate**: []
- **--specpath DIR        Folder to store the generated spec file (default**: []
- **What to bundle, where to search**: []
- **--add-data SOURCE**: DEST
- **value should be in form of "source**: dest_dir", where
- **both paths are separated by a colon (**: ). To put a file
- **--add-binary SOURCE**: DEST
- **Multiple paths are allowed, separated by ``'**: '``, or
- **How to generate**: []
- **all**: All three of the following options. - imports:
- **https**: //docs.python.org/3/using/cmdline.html#id4.
- **bootloader**: tell the bootloader to issue progress
- **noarchive**: instead of storing all frozen Python source
- **Windows and macOS specific options**: []
- **Windows and macOS**: do not provide a console window for
- **Windows only**: in console-enabled executable, have
- **FILE.ico**: apply the icon to a Windows executable.
- **FILE.exe,ID**: extract the icon with ID from an exe.
- **FILE.icns**: apply the icon to the .app bundle on macOS.
- **default (default**: apply PyInstaller's icon). This
- **Windows specific options**: []
- **macOS specific options**: []
- **notation. For example**: []
- **com.mycompany.department.appname (default**: first
- **Target architecture (macOS only; valid values**: x86_64,
- **Rarely used special options**: []
- **--distpath DIR        Where to put the bundled app (default**: ./dist)
- **and etc. (default**: ./build)
- **-y, --noconfirm       Replace output directory (default**: []
- **--upx-dir UPX_DIR     Path to UPX utility (default**: search the execution


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\pyinstaller\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.061688
