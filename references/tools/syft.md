---
tool_id: syft
title: syft
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/anchore/syft
repository: 
version: 1.38.0+ds-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\syft\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.135024
---

# Tool: syft (syft)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/anchore/syft](https://github.com/anchore/syft) |
| Repository |  |
| Version | 1.38.0+ds-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/syft
- **PackagesInfo**: |
- ****Installed size**: ** `82.28 MB`
- ****How to install**: ** `sudo apt install syft`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# syft -h
- **Usage**: []
- **Examples**: []
- **syft scan alpine**: latest -o template -t my_format.tmpl  show a SBOM formatted according to given template file
- **Supports the following image sources**: []
- **syft scan yourrepo/yourimage**: tag     defaults to using images from a Docker daemon. If Docker is not present, the image is pulled directly from the registry.
- **You can also explicitly specify the scheme to use**: []
- **syft scan docker**: yourrepo/yourimage:tag            explicitly use the Docker daemon
- **syft scan podman**: yourrepo/yourimage:tag            explicitly use the Podman daemon
- **syft scan registry**: yourrepo/yourimage:tag          pull image directly from a registry (no container runtime required)
- **syft scan docker-archive**: path/to/yourimage.tar     use a tarball from disk for archives created from "docker save"
- **syft scan oci-archive**: path/to/yourimage.tar        use a tarball from disk for OCI archives (from Skopeo or otherwise)
- **syft scan oci-dir**: path/to/yourimage                read directly from a path on disk for OCI layout directories (from Skopeo or otherwise)
- **syft scan singularity**: path/to/yourimage.sif        read directly from a Singularity Image Format (SIF) container on disk
- **syft scan dir**: path/to/yourproject                  read directly from a path on disk (any directory)
- **syft scan file**: path/to/yourproject/file            read directly from a path on disk (any single file)
- **Available Commands**: []
- **Flags**: []
- **--enrich stringArray                        enable package data enrichment from local and online sources (options**: all, golang, java, javascript, python)
- **--file string                               file to write the default report output to (default is STDOUT) (DEPRECATED**: use: --output FORMAT=PATH)


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\syft\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.135024
