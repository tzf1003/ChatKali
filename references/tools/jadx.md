---
tool_id: jadx
title: jadx
categories: ["reverse-engineering"]
category_slugs: ["reverse-engineering"]
homepage: https://github.com/skylot/jadx
repository: 
version: 1.5.3-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering"]
icon: images/jadx-logo.svg
source_path: kali-tools\jadx\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.951977
---

# Tool: jadx (jadx)

## Categories
- [reverse-engineering](../reverse-engineering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/skylot/jadx](https://github.com/skylot/jadx) |
| Repository |  |
| Version | 1.5.3-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-forensics kali-tools-respond kali-tools-reverse-engineering |
| Icon | images/jadx-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/jadx
- **PackagesInfo**: |
- **Main features**: ['decompile Dalvik bytecode to java classes from APK, dex, aar and zip files', 'decode AndroidManifest.xml and other resources from resources.arsc', 'deobfuscator included']
- **jadx-gui features**: ['view decompiled code with highlighted syntax', 'jump to declaration', 'find usage', 'full text search']
- ****Installed size**: ** `121.62 MB`
- ****How to install**: ** `sudo apt install jadx`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# jadx-gui -h
- **jadx - dex to java decompiler, version**: 1.5.3
- **usage**: jadx [command] [options] <input files> (.apk, .dex, .jar, .class, .smali, .zip, .aar, .arsc, .aab, .xapk, .apkm, .jadx.kts)
- **commands (use '<command> --help' for command options)**: []
- **options**: []
- **-j, --threads-count                           - processing threads count, default**: 3
- **--output-format                               - can be 'java' or 'json', default**: java
- **--export-gradle-type                          - Gradle project template for export**: []
- **-m, --decompilation-mode                      - code output mode**: []
- **--mappings-path                               - deobfuscation mappings file or directory. Allowed formats**: Tiny and Tiny v2 (both '.tiny'), Enigma (.mapping) or Enigma directory
- **--mappings-mode                               - set mode for handling the deobfuscation mapping file**: []
- **--deobf-min                                   - min length of name, renamed if shorter, default**: 3
- **--deobf-max                                   - max length of name, renamed if longer, default**: 64
- **--deobf-whitelist                             - space separated list of classes (full name) and packages (ends with '.*') to exclude from deobfuscation, default**: android.support.v4.* android.support.v7.* android.support.v4.os.* android.support.annotation.Px androidx.core.os.* androidx.annotation.Px
- **--deobf-cfg-file                              - deobfuscation mappings file used for JADX auto-generated names (in the JOBF file format), default**: same dir and name as input file with '.jobf' extension
- **--deobf-cfg-file-mode                         - set mode for handling the JADX auto-generated names' deobfuscation map file**: []
- **--deobf-res-name-source                       - better name source for resources**: []
- **--use-source-name-as-class-name-alias         - use source name as class name alias**: []
- **--source-name-repeat-limit                    - allow using source name if it appears less than a limit number, default**: 10
- **--use-kotlin-methods-for-var-names            - use kotlin intrinsic methods to rename variables, values**: disable, apply, apply-and-hide, default: apply
- **--rename-flags                                - fix options (comma-separated list of)**: []
- **--integer-format                              - how integers are displayed**: []
- **--comments-level                              - set code comments level, values**: error, warn, info, debug, user-only, none, default: info
- **--log-level                                   - set log level, values**: quiet, progress, error, warn, info, debug, default: info
- **--disable-plugins                             - comma separated list of plugin ids to disable, default**: []
- **Plugin options (-P<name>=<value>)**: []
- **dex-input**: Load .dex and .apk files
- **java-convert**: Convert .class, .jar and .aar files to dex
- **kotlin-metadata**: Use kotlin.Metadata annotation for code generation
- **kotlin-smap**: Use kotlin.SourceDebugExtension annotation for rename class alias
- **rename-mappings**: various mappings support
- **smali-input**: Load .smali files
- **Environment variables**: []
- **JADX_ZIP_MAX_ENTRIES_COUNT - maximum allowed number of entries in zip files (default**: 100 000)
- **Examples**: []
- **-sc, --select-class                           - GUI**: Open the selected class and show the decompiled code


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\jadx\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.951977
