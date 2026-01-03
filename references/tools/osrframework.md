---
tool_id: osrframework
title: osrframework
categories: ["information-gathering"]
category_slugs: ["information-gathering"]
homepage: https://pypi.org/project/osrframework/
repository: 
version: 0.20.5-0kali2
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything kali-tools-identify"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\osrframework\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.033025
---

# Tool: osrframework (osrframework)

## Categories
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://pypi.org/project/osrframework/](https://pypi.org/project/osrframework/) |
| Repository |  |
| Version | 0.20.5-0kali2 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-tools-identify |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/osrframework
- **PackagesInfo**: |
- ****Installed size**: ** `1.51 MB`
- ****How to install**: ** `sudo apt install osrframework`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# usufy.py -h
- **usage**: usufy (--info <action> | -b | -f <path_to_fuzzing_list> |
- **options**: []
- **Profile squatting arguments**: []
- **About arguments**: []
- **Input options (one required)**: []
- **Other options**: []
- **output folder for the generated files. Default**: ./.
- **or a regular expression. Default**: regexp.
- **follow us on Twitter in <http**: //twitter.com/i3visio>.
- **Processing arguments**: []
- **output extension for the summary files. Default**: csv.
- **None was provided the following will be used**: []
- **search amongst the following**: ['all', 'about',
- **SUBCOMMANDS**: []
- **ABOUT ARGUMENTS**: []
- **or follow us on Twitter in <http**: //twitter.com/i3visio>.
- **following**: list_platforms (list the details of the
- **line)**: <BASE_DOMAIN> <VALID_NICK>
- **Platform selection arguments**: []
- **the domains or the nicknames should come as**: <DOMAIN>,
- **select the verbosity level**: 0 - minimal; 1 - normal


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## osrframework Usage Examples

Check for the `-n kalilinux` username across all available services:

```console
root@kali:~# usufy.py -n kalilinux

  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_

                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)



usufy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt

2017-10-05 11:20:10.448178  Starting search in 297 platform(s)... Relax!

    Press <Ctrl + C> to stop...

[!] In skype.py, exception caught when checking information in Skype!

2017-10-05 11:20:30.854308  A summary of the results obtained are shown in the following table:

Sheet Name: Profiles recovered (2017-10-5_11h20m).
+-----------------------------------------------------------------+---------------+-------------------+
|                           i3visio_uri                           | i3visio_alias | i3visio_platform  |
+=================================================================+===============+===================+
| https://www.facebook.com/kalilinux                              | kalilinux     | Facebook          |
+-----------------------------------------------------------------+---------------+-------------------+
| http://twitter.com/kalilinux                                    | kalilinux     | Twitter           |
+-----------------------------------------------------------------+---------------+-------------------+
[...]
```

Search for a given email address.

```console
root@kali:~# mailfy.py -n ltorvalds

  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_

                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)


mailfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2016-2017

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt

2017-10-05 11:32:49.178753  Starting search in 22 different emails:
[
  "ltorvalds@000.com",
  "ltorvalds@111.com",
  "ltorvalds@000.cn",
[...]
```

Search for a given string across all OSRF services.

```console
root@kali:~$ searchfy.py -q "dookie2000ca"

  ___  ____  ____  _____                                            _
 / _ \/ ___||  _ \|  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| | | \___ \| |_) | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |_| |___) |  _ <|  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   <
 \___/|____/|_| \_\_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_

                Version:      OSRFramework 0.17.2
                Created by:   Felix Brezo and Yaiza Rubio, (i3visio)



searchfy.py Copyright (C) F. Brezo and Y. Rubio (i3visio) 2014-2017

This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you
are welcome to redistribute it under certain conditions. For additional info,
visit https://www.gnu.org/licenses/agpl-3.0.txt

2017-10-05 11:38:33.545680  Starting search in different platform(s)... Relax!

    Press <Ctrl + C> to stop...

[!] In skype.py, exception caught when checking information in Skype!

2017-10-05 11:38:36.672623  A summary of the results obtained are listed in the following table:

Sheet Name: Profiles recovered (2017-10-5_11h38m).
+---------------------------------+---------------+------------------+
|           i3visio_uri           | i3visio_alias | i3visio_platform |
+=================================+===============+==================+
| http://github.com/dookie2000ca  | dookie2000ca  | Github           |
+---------------------------------+---------------+------------------+
| http://twitter.com/dookie2000ca | dookie2000ca  | Twitter          |
+---------------------------------+---------------+------------------+

2017-10-05 11:38:36.685354  You can find all the information collected in the following files:
    ./profiles.csv

2017-10-05 11:38:36.685581  Finishing execution...

Total time used:    0:00:03.139901
Average seconds/query:  3.139901 seconds

Did something go wrong? Is a platform reporting false positives? Do you need to
integrate a new one and you don't know how to start? Then, you can always place
an issue in the Github project:
    https://github.com/i3visio/osrframework/issues
Note that otherwise, we won't know about it!
```


## Source
- Path: kali-tools\osrframework\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.033025
