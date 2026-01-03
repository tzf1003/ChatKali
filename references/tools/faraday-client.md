---
tool_id: faraday-client
title: faraday-client
categories: ["vulnerability-analysis", "reporting-tools", "defensive-tools"]
category_slugs: ["vulnerability-analysis", "reporting-tools", "defensive-tools"]
homepage: https://github.com/infobyte/faraday-client
repository: 
version: 1.1.0-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\faraday-client\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.895082
---

# Tool: faraday-client (faraday-client)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [reporting-tools](../reporting-tools.md)
- [defensive-tools](../defensive-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/infobyte/faraday-client](https://github.com/infobyte/faraday-client) |
| Repository |  |
| Version | 1.1.0-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **archived**: true
- **Repository**: https://gitlab.com/kalilinux/packages/faraday-client
- **PackagesInfo**: |
- ****Installed size**: ** `1.12 MB`
- ****How to install**: ** `sudo apt install faraday-client`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# fplugin -h
- **usage**: fplugin [-h] [-i] [-w WORKSPACE] [-u URL] [--username USERNAME]
- **options**: []
- **connection**: []
- **positional arguments**: []
- **command               Command to execute. Example**: ./fplugin getAllIps
- **(default**: http://localhost:5985)
- **-i, --interactive     Run in interactive mode (default**: False)
- **Workspace to use (default**: untitled)
- **-u URL, --url URL     Faraday Server URL. Example**: http://localhost:5985
- **--cert CERT_PATH      Path to the valid Faraday server certificate (default**: []
- **Available scripts**: ['autoclose_vulns: Closes vulns from the current workspace if a certain time has passed', 'change_vuln_status: Changes Vulns Status (to closed)', 'create_cred: Creates new credentials', 'create_executive_report: Creates a new executive report in current workspace', 'create_host: Creates a new host in current workspace', 'create_service: Creates a new service in a specified interface', 'create_vuln: Creates a new vulnerability', 'create_vulnweb: Creates a new website vulnerability in a specified service', 'create_xlsx_report: Creates a xls report from current workspace', 'del_all_hosts: Deletes all stored hosts', 'del_all_services_closed: Deletes all services with a non open port', 'del_all_vulns_with: Delete all vulnerabilities matched with regex', 'fbruteforce_services: Script to perform a brute force attack on different services in a workspace', 'filter_services: Filter services by port or service name', 'get_all_ips: Get all scanned interfaces', 'get_severitiy_by_cwe: Get Vulns filtered by Severity and change Severity based in CWE', 'import_csv: Import Faraday objects from CSV file', 'list_creds: Get all stored credentials', 'list_hosts: List hosts', 'list_ips: List all scanned IPs', 'list_os: Lists all scanned OSs', 'screenshot_server: Takes a Screenshot of the ip:ports of a given protocol']


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\faraday-client\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.895082
