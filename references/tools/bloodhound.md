---
tool_id: bloodhound
title: bloodhound
categories: ["information-gathering", "post-exploitation"]
category_slugs: ["information-gathering", "post-exploitation"]
homepage: https://github.com/SpecterOps/BloodHound
repository: 
version: 8.3.1-0kali1
architectures: amd64 arm64
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: images/bloodhound-logo.svg
source_path: kali-tools\bloodhound\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.807832
---

# Tool: bloodhound (bloodhound)

## Categories
- [information-gathering](../information-gathering.md)
- [post-exploitation](../post-exploitation.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/SpecterOps/BloodHound](https://github.com/SpecterOps/BloodHound) |
| Repository |  |
| Version | 8.3.1-0kali1 |
| Architectures | amd64 arm64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | images/bloodhound-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/bloodhound
- **PackagesInfo**: |
- ****Installed size**: ** `236.48 MB`
- ****How to install**: ** `sudo apt install bloodhound`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# bloodhound-setup -h
- **Directories in use**: []
- **home**: /usr/share/neo4j
- **config**: /usr/share/neo4j/conf
- **logs**: /etc/neo4j/logs
- **plugins**: /usr/share/neo4j/plugins
- **import**: /usr/share/neo4j/import
- **data**: /etc/neo4j/data
- **certificates**: /usr/share/neo4j/certificates
- **licenses**: /usr/share/neo4j/licenses
- **run**: /var/lib/neo4j/run
- **Started neo4j (pid**: 3342471). It is available at http://localhost:7474
- **Default credentials are user**: neo4j password:neo4j
- **[!] IMPORTANT**: Once you have setup the new password, please update /etc/bhapi/bhapi.json with the new password before running bloodhound


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## How to install and run Bloodhound

Update your package list and install BloodHound from the official Kali repository::

```console
┌──(kali㉿kali)-[~]
└─$ sudo apt update && sudo apt install -y bloodhound
```

After installation, run BloodHound's configuration script:

```console
┌──(kali㉿kali)-[~]
└─$ sudo bloodhound-setup
```

This will initialize the necessary services and configurations.

![](images/bloodhound-setup.png)

1. Open a browser and navigate to http://localhost:7474.
2. Login using the default credentials:

Bloodhound's default credentials:
```plain
  username: neo4j
  password: neo4j
```

![](images/login-neo4j.png)

You will be prompted to set a new password. Choose a secure one and remember it.

![](images/neo4j-change-password.png)

Now that you've updated the Neo4j password, update the BloodHound API config file to reflect the change (replace the password `"secret": "neo4j"`).

```console
┌──(kali㉿kali)-[~]
└─$ sudo vim /etc/bhapi/bhapi.json
```

![](images/neo4j-password.png)

You can finally run bloodhound with the default credentials. You will be asked to set a new secure password.

```console
┌──(kali㉿kali)-[~]
└─$ sudo bloodhound
```


```plain
username: admin
password: admin
```

![](images/bloodhound-run.png)

## Reset Bloodhound's admin password:

```console
┌──(kali㉿kali)-[~]
└─$ sudo env bhe_recreate_default_admin=true bloodhound
```


## Source
- Path: kali-tools\bloodhound\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.807832
