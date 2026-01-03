---
tool_id: python-virtualenv
title: python-virtualenv
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://virtualenv.pypa.io/
repository: 
version: 20.35.4+ds-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\python-virtualenv\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.064931
---

# Tool: python-virtualenv (python-virtualenv)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://virtualenv.pypa.io/](https://virtualenv.pypa.io/) |
| Repository |  |
| Version | 20.35.4+ds-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/python-team/packages/python-virtualenv
- **PackagesInfo**: |
- **offer all features of this library, to name just a few more prominent ones**: []
- ****Installed size**: ** `14 KB`
- ****How to install**: ** `sudo apt install virtualenv`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# virtualenv -h
- **usage**: virtualenv [--version] [--with-traceback] [-v | -q] [--read-only-app-data] [--app-data APP_DATA] [--reset-app-data] [--upgrade-embed-wheels] [--discovery {builtin}] [-p py] [--try-first-with py_exe]
- **options**: []
- **--with-traceback              on failure also display the stacktrace internals of virtualenv (default**: False)
- **--read-only-app-data          use app data folder in read-only mode (write operations will fail with error) (default**: False)
- **--app-data APP_DATA           a data folder used as cache by the virtualenv (default**: /root/.local/share/virtualenv)
- **--reset-app-data              start with empty app data folder (default**: False)
- **--upgrade-embed-wheels        trigger a manual update of the embedded wheels (default**: False)
- **verbosity**: []
- **-v, --verbose                 increase verbosity (default**: 2)
- **-q, --quiet                   decrease verbosity (default**: 0)
- **discovery**: []
- **--discovery {builtin}         interpreter discovery method (default**: builtin)
- **-p, --python py               interpreter based on what to create environment (path/identifier) - by default use the interpreter where the tool is installed - first found wins (default**: [])
- **--try-first-with py_exe       try first these interpreters before starting the discovery (default**: [])
- **creator**: []
- **create environment via (builtin = cpython3-posix) (default**: builtin)
- **--clear                       remove the destination directory if exist before starting (will overwrite files otherwise) (default**: False)
- **--no-vcs-ignore               don't create VCS ignore directive in the destination directory (default**: False)
- **--system-site-packages        give the virtual environment access to the system site-packages dir (default**: False)
- **--symlinks                    try to use symlinks rather than copies, when symlinks are not the default for the platform (default**: True)
- **--copies, --always-copy       try to use copies rather than symlinks, even when symlinks are the default for the platform (default**: False)
- **seeder**: []
- **--seeder {app-data,pip}       seed packages install method (default**: app-data)
- **--no-seed, --without-pip      do not install seed packages (default**: False)
- **pass to disable download of the latest pip/setuptools/wheel from PyPI (default**: True)
- **--download                    pass to enable download of the latest pip/setuptools/wheel from PyPI (default**: False)
- **--extra-search-dir d [d ...]  a path containing wheels to extend the internal wheel list (can be set 1+ times) (default**: [])
- **--pip version                 version of pip to install as seed**: embed, bundle, none or exact version (default: bundle)
- **--setuptools version          version of setuptools to install as seed**: embed, bundle, none or exact version (default: none)
- **--no-pip                      do not install pip (default**: False)
- **--no-setuptools               do not install setuptools (default**: False)
- **--no-periodic-update          disable the periodic (once every 14 days) update of the embedded wheels (default**: True)
- **--symlink-app-data            symlink the python packages from the app-data folder (requires seed pip>=19.3) (default**: False)
- **activators**: []
- **--activators comma_sep_list   activators to generate - default is all supported (default**: bash,cshell,fish,nushell,powershell,python)
- **--prompt prompt               provides an alternative prompt prefix for this environment (value of . means name of the current working directory) (default**: None)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\python-virtualenv\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.064931
