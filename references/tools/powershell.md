---
tool_id: powershell
title: powershell
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://microsoft.com/powershell
repository: 
version: 7.5.4-1.deb
architectures: amd64
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large"]
icon: images/powershell-logo.svg
source_path: kali-tools\powershell\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.055339
---

# Tool: powershell (powershell)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://microsoft.com/powershell](https://microsoft.com/powershell) |
| Repository |  |
| Version | 7.5.4-1.deb |
| Architectures | amd64 |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large |
| Icon | images/powershell-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: []
- **PackagesInfo**: |
- ****Installed size**: ** `183.55 MB`
- ****How to install**: ** `sudo apt install powershell`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pwsh -h
- **Usage**: pwsh[.exe] [-Login] [[-File] <filePath> [args]]
- **PowerShell Online Help https**: //aka.ms/powershell-docs
- **Get-Script.ps1 script file**: -File .\Get-Script.ps1 -All
- **colon and the boolean value, such as the following**: []
- **"-File .\Get-Script.ps1 -All**: $False".
- **syntax**: pwsh -File .\test.ps1 -TestParam %windir%
- **In contrast, running "pwsh -File .\test.ps1 -TestParam $env**: windir" in
- **cmd.exe results in the script receiving the literal string "$env**: windir"
- **"$env**: windir" style of environment variable reference can be used inside a
- **execution directory**: "pwsh -File %~dp0test.ps1 -TestParam %windir%". If you
- **string, the call operator "&" can be used**: []
- **with standard input. For example**: []
- **This example produces the following output**: []
- **For example**: []
- **pwsh -CommandWithArgs '$args | % { "arg**: $_" }' arg1 arg2
- **arg**: arg2
- **Example**: pwsh -SettingsFile c:\myproject\powershell.config.json
- **$command = 'dir "c**: \program files" '
- **$bytes = [System.Text.Encoding]**: :Unicode.GetBytes($command)
- **$encodedCommand = [Convert]**: :ToBase64String($bytes)
- **the $env**: PSExecutionPolicyPreference environment variable. This parameter
- **$env**: PSExecutionPolicyPreference environment variable does not exist on
- **To set up pwsh as the login shell on UNIX-like operating systems**: ['Verify that the full absolute path to pwsh is listed under /etc/shells', 'This path is usually something like /usr/bin/pwsh on Linux or']
- **To start PowerShell in your home directory, use**: pwsh -WorkingDirectory ~


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\powershell\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.055339
