---
tool_id: phpggc
title: phpggc
categories: ["exploitation-tools"]
category_slugs: ["exploitation-tools"]
homepage: https://github.com/ambionics/phpggc
repository: 
version: 0.20230428-0kali1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\phpggc\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.048912
---

# Tool: phpggc (phpggc)

## Categories
- [exploitation-tools](../exploitation-tools.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/ambionics/phpggc](https://github.com/ambionics/phpggc) |
| Repository |  |
| Version | 0.20230428-0kali1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/phpggc
- **PackagesInfo**: |
- ****Installed size**: ** `650 KB`
- ****How to install**: ** `sudo apt install phpggc`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# phpggc -h
- **PHPGGC**: PHP Generic Gadget Chains


## Documentation (Upstream)
------------------------------
 
 USAGE
   ./phpggc [-h|-l|-i|...] <GadgetChain> [arguments]
 
 INFORMATION
   -h, --help Displays help
   -l, --list [filter] Lists available gadget chains
   -i, --information
      Displays information about a gadget chain
 
 OUTPUT
   -o, --output <file>
      Outputs the payload to a file instead of standard output
 
 PHAR
   -p, --phar <tar|zip|phar>
      Creates a PHAR file of the given format
   -pj, --phar-jpeg <file>
      Creates a polyglot JPEG/PHAR file from given image
   -pp, --phar-prefix <file>
      Sets the PHAR prefix as the contents of the given file.
      Generally used with -p phar to control the beginning of the generated file.
   -pf, --phar-filename <filename>
      Defines the name of the file contained in the generated PHAR (default: test.txt)
 
 ENHANCEMENTS
   -f, --fast-destruct
      Applies the fast-destruct technique, so that the object is destroyed
      right after the unserialize() call, as opposed to at the end of the
      script
   -a, --ascii-strings
      Uses the 'S' serialization format instead of the standard 's' for non-printable chars.
      This replaces every non-ASCII value to an hexadecimal representation:
        s:5:"A<null_byte>B<cr><lf>"; -> S:5:"A\00B\09\0D";
      This is experimental and it might not work in some cases.
   -A, --armor-strings
      Uses the 'S' serialization format instead of the standard 's' for every char.
      This replaces every character to an hexadecimal representation:
        s:5:"A<null_byte>B<cr><lf>"; -> S:5:"\41\00\42\09\0D";
      This is experimental and it might not work in some cases.
      Note: Since strings grow by a factor of 3 using this option, the payload can get
      really long.
   -n, --plus-numbers <types>
      Adds a + symbol in front of every number symbol of the given type.
      For instance, -n iO adds a + in front of every int and object name size:
      O:3:"Abc":1:{s:1:"x";i:3;} -> O:+3:"Abc":1:{s:1:"x";i:+3;}
      Note: Since PHP 7.2, only i and d (float) types can have a +
   -w, --wrapper <wrapper>
      Specifies a file containing at least one wrapper functions:
        - process_parameters(array $parameters): called right before object is created
        - process_object(object $object): called right before the payload is serialized
        - process_serialized(string $serialized): called right after the payload is serialized
 
 ENCODING
   -s, --soft   Soft URLencode
   -u, --url    URLencodes the payload
   -b, --base64 Converts the output into base64
   -j, --json   Converts the output into json
   Encoders can be chained, for instance -b -u -u base64s the payload,
   then URLencodes it twice
 
 CREATION
   -N, --new <framework> <type>
     Creates the file structure for a new gadgetchain for given framework
     Example: ./phpggc -N Drupal RCE
   --test-payload
     Instead of displaying or storing the payload, includes vendor/autoload.php and unserializes the payload.
     The test script can only deserialize __destruct, __wakeup, __toString and PHAR payloads.
     Warning: This will run the payload on YOUR system !
 
 EXAMPLES
   ./phpggc -l
   ./phpggc -l drupal
   ./phpggc Laravel/RCE1 system id
   ./phpggc SwiftMailer/FW1 /var/www/html/shell.php /path/to/local/shell.php
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\phpggc\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.048912
