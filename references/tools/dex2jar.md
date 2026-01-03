---
tool_id: dex2jar
title: dex2jar
categories: ["reverse-engineering"]
category_slugs: ["reverse-engineering"]
homepage: https://github.com/pxb1988/dex2jar/tree/2.x
repository: 
version: 2.1~nightly-28-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-reverse-engineering"]
icon: images/dex2jar-logo.svg
source_path: kali-tools\dex2jar\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.864912
---

# Tool: dex2jar (dex2jar)

## Categories
- [reverse-engineering](../reverse-engineering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/pxb1988/dex2jar/tree/2.x](https://github.com/pxb1988/dex2jar/tree/2.x) |
| Repository |  |
| Version | 2.1~nightly-28-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-reverse-engineering |
| Icon | images/dex2jar-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/dex2jar
- **PackagesInfo**: |
- **dex2jar contains 4 compments**: []
- ****Installed size**: ** `5.80 MB`
- ****How to install**: ** `sudo apt install dex2jar`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# d2j_invoke --help
- **usage**: d2j-std-zip [options] <zip>
- **options**: []
- **online help**: https://sourceforge.net/p/dex2jar/wiki/Smali
- **Usage**: java [options] <mainclass> [args...]
- **e like**: La/b;->decrypt(III)Ljava/lang/Stri
- **the stings, example**: java.lang.String
- **crypt the stings, example1**: Ljava/lang/Str
- **ing; example2**: III, default is Ljava/lang/
- **-t,--arg-types <type>                comma-separated list of types**: boolean,byte
- **https**: //bitbucket.org/pxb1988/dex2jar/wiki/DecryptStrings
- **where options include**: []
- **A**: separated list of elements, each element is a file path
- **-verbose**: ['class|module|gc|jni']
- **-ea[**: <packagename>...|:<classname>]
- **-enableassertions[**: <packagename>...|:<classname>]
- **-da[**: <packagename>...|:<classname>]
- **-disableassertions[**: <packagename>...|:<classname>]
- **-agentlib**: <libname>[=<options>]
- **load native agent library <libname>, e.g. -agentlib**: jdwp
- **see also -agentlib**: jdwp=help
- **-agentpath**: <pathname>[=<options>]
- **-javaagent**: <jarpath>[=<options>]
- **-splash**: <imagepath>


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## d2j-dex2jar Usage Example

```console
root@kali:~# d2j-dex2jar /usr/share/metasploit-framework/data/android/apk/classes.dex
dex2jar /usr/share/metasploit-framework/data/android/apk/classes.dex -> classes-dex2jar.jar
```

## d2j-jar-remap

```console
root@kali:~# d2j-jar-remap -h
d2j-jar-remap -- rename package/class/method/field name in a jar
usage: d2j-jar-remap [options] jar
options:
 -c,--config <config>    config file for remap, this is REQUIRED
 -f,--force              force overwrite
 -h,--help               Print this help message
 -o,--output <out-jar>   output .jar file, default is $current_dir/[jar-name]-re
                         map.jar
version: 0.0.9.15
online help: https://code.google.com/p/dex2jar/wiki/DeObfuscateJarWithDexTool
```

## dex2jar

```console
root@kali:~# dex2jar
this cmd is deprecated, use the d2j-dex2jar if possible
dex2jar version: translator-0.0.9.15
dex2jar file1.dexORapk file2.dexORapk ...
```

## d2j-dex-dump

```console
root@kali:~# d2j-dex-dump -h
Dump in.dexORapk out.dump.jar
```

## d2j-init-deobf

```console
root@kali:~# d2j-init-deobf -h
d2j-init-deobf -- generate an init config file for deObfuscate a jar
usage: d2j-init-deobf [options] <jar>
options:
 -f,--force                force overwrite
 -h,--help                 Print this help message
 -max,--max-length <MAX>   do the rename if the length > MIN, default is 40
 -min,--min-length <MIN>   do the rename if the length < MIN, default is 2
 -o,--output <out-file>    output .jar file, default is $current_dir/[file-name]
                           -deobf-init.txt
version: 0.0.9.15
```


## Source
- Path: kali-tools\dex2jar\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.864912
