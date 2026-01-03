---
tool_id: afflib
title: afflib
categories: ["forensics", "utilities"]
category_slugs: ["forensics", "utilities"]
homepage: https://github.com/sshock/AFFLIBv3
repository: 
version: 3.7.22-1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\afflib\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.775934
---

# Tool: afflib (afflib)

## Categories
- [forensics](../forensics.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/sshock/AFFLIBv3](https://github.com/sshock/AFFLIBv3) |
| Repository |  |
| Version | 3.7.22-1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/afflib
- **PackagesInfo**: |
- **computer forensic information. Critical features of AFF include**: ['AFF allows you to store both computer forensic data and associated']
- **working with computer forensic information. Using these tools you can**: []
- *** Interconvert disk images between a variety of formats, including**: ['raw or "dd";', 'splitraw (in which a single image is split between multiple files);', 'AFF format (in which the entire disk image is stored in a single']
- **The AFF Toolkit provides these executables**: affcat, affcompare, affconvert,
- ****Installed size**: ** `613 KB`
- ****How to install**: ** `sudo apt install afflib-tools`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# affcat -h
- **usage**: affcat [options] infile [... more infiles]
- **options**: []


## Documentation (Upstream)
 Just output segment name
     -p ###  --- just output data page number ###
     -S ###  --- Just output data sector ### (assumes 512-byte sectors). Sector #0 is first
     -q      --- quiet; don't print to STDERR if a page is skipped
     -n      --- noisy; tell when pages are skipped.
     -l      --- List all of the segment names
     -L      --- List segment names, lengths, and args
     -d      --- debug. Print the page numbers to stderr as data goes to stdout
     -b      --- Output BADFALG for bad blocks (default is NULLs)
     -v      --- Just print the version number and exit.
     -r offset:count --- seek to offset and output count characters in each file; may be repeated
 ```
 
 - - -
 
 ##### affcompare
 
 Compare the contents of an ISO file to an AFF file
 
 ```
 root@kali:~# affcompare -h
 affcompare version 3.7.22
 
 usage: affcompare [options] file1 file2
        compares file1 with file2
 
 or     affcompare [options] -r dir1 dir2
        compares similarly-named files in dir1 and dir2
 
 or     affcompare [options] -s file1 file2...
        Reports if file was successfully copied to Amazon S3
        checking only for existence, not reading back the bytes.
        (Because all writes to S3 are validated by the MD5 of the object
 fast options:
 (These compare segments but not their contents.)
        -p        --- report about the results of preening
        -e        --- Just report about existence (use with -r)
        -s        --- Just see if all of the segments are present, but don't
                      validate the contents. (Primarily for use with Amazon S3)
 other options:
        -V        --- just print the version number and exit
        -v        --- Verbose; each file as it is compared.
        -q        --- Quiet. No output except for errors
        -a        --- print what's the same (all)
        -b        --- print the numbers of differing sectors
        -c        --- print the contents of differing sectors
        -m        --- Just report about the data (ignore metadata)
        -P ###    --- Just examine the differences on page ###
 
 Options documented above:
        -r dir1 dir2 --- recursively compare what's in dir1 with dir2, and
                        report what's in dir1 that's not in dir2
        -s        --- Check to see if named files are on Amazon S3
 
   affcompare file1.aff file2.aff           --- compare file1.aff and file2.aff
   affcompare f1.aff f2.aff dir1/           --- compare f1.aff with dir1/f1.aff and f2.aff with dir2/f2.aff
                                               note: dir1/ must end with a slash.
   affcompare -b img file.aff               --- compare file.aff and file.img
   affcompare -b img file1.aff file2.aff... --- compare file1.aff, file1.img, etc.
   affcompare -re dir1 dir2                --- report AFF files in dir1 but not in dir2
   affcompare -rse dir1 s3:///             --- report AFF files in dir1 but not on S3 (low bandwidth)
   affcompare -rs dir1 s3:///              --- report AFF files in dir1 but incomplete on on S3 (more bandwidth)
 
 ```
 
 - - -
 
 ##### affconvert
 
 Convert files between RAW and AFF formats
 
 ```
 root@kali:~# affconvert -h
 affconvert version 3.7.22
 
 usage:   affconvert [options] file1 [... files] 
 
 Please, see more info in manpage.
 ```
 
 - - -
 
 ##### affcopy
 
 Reorder and recompress AFF files
 
 ```
 root@kali:~# affcopy -h
 affcopy version 3.7.22
 usage: affcopy [options] file1 file
                     Copies file1 to file2
        affcopy [options] file1 file2 file3 ... dir
                     Copies file1.. into dir
        affcopy [options] file1 file2 file3 ... dir1 dir2...
                     Copies file1.. into dirs1, dir2, ...
 
 By default, all page MACs are verified on read and all segments
 are verified after write.
 Options:
    -v = verbose: print each file as it is copied
    -vv = very verbose: print each segment as it is copied
    -d = print debugging information as well
    -x = don't verify hashes on reads
    -y = don't verify writes
    -Xn = recompress pages (preen) with zlib level n
    -L  = recompress pages (preen) with LZMA (smaller but slower)
 
    -h = help; print this message.
    -V = print the program version and exit.
    -z = zap; copy even if the destination exists.
    -m = just copy the missing segments
 
 Signature Options:
    -k filename.key   = specify private key for signing
    -c filename.cer   = specify a X.509 certificate that matches the private key
                        (by default, the file is assumed to be the same one
                        provided with the -k option.)
    -n  = read notes to accompany the copy from standard in.
 
 
 Encryption Options:   Specify passphrase encryption for filename.aff with:
       file://:passphrase@/filename.aff
 
 Examples:
        affcopy  file.aff   file://:mypassword@/file-encrypted.aff   - encrypt file.aff
        affcopy -vy -X9 *.aff s3:///     Copy all files in current
                                directory to S3 default bucket with X9 compression
 ```
 
 - - -
 
 ##### affcrypto
 
 Handle encryption issues
 
 ```
 root@kali:~# affcrypto -h
 affcrypto version 3.7.22
 usage: affcrypto [options] filename.aff [filename2.aff ... ]
    prints if each file is encrypted or not.
 options:
     -x      --- output in XML
     -j      --- Just print the number of encrypted segments
     -J      --- Just print the number of unencrypted segments
 
 Data conversion options:
     -e      --- encrypt the unencrypted non-signature segments
     -d      --- decrypt the encrypted non-signature segments
     -r      --- change passphrase (take old and new from stdin)
     -O old  --- specify old passphrase
     -N new  --- specify new passphrase
     -K mykey.key  -- specifies a private keyfile for unsealing (may not be repeated)
     -C mycert.crt -- specifies a certificate file for sealing (may be repeated)
     -S      --- add symmetric encryptiong (passphrase) to AFFILE encrypted with public key
                     (requires a private key and a specified passphrase).
     -A      --- add asymmetric encryption to a AFFILE encrypted with a passphrase
                     (requires a certificate file spcified with the -C option
 
 Password Cracking Options:
     -p passphrase --- checks to see if passphrase is the passphrase of the file
                 exit code is 0 if it is, -1 if it is not
     -k      --- attempt to crack passwords by reading a list of passwords from ~/.affpassphrase
     -f file --- Crack passwords but read them from file.
 
 Debugging:
     -V      --- Just print the version number and exit.
     -D      --- debug; print out each key as it is tried
     -l      --- List the installed hash and encryption algorithms 
 Note: This program ignores the environment variables:
 AFFLIB_PASSPHRASE
 AFFLIB_PASSPHRASE_FILE
 AFFLIB_PASSPHRASE_FD
 AFFLIB_DECRYPTING_PRIVATE_KEYFILE
 ```
 
 - - -
 
 ##### affdiskprint
 
 Create a diskprint AFF structure
 
 ```
 root@kali:~# affdiskprint -h
 affdiskprint version 3.7.22
 usage: affdiskprint [options] infile 
    -x XML     =   Verify the diskprint
    -V         =   Just print the version number and exit.
    -h         =   Print this help.
 ```
 
 - - -
 
 ##### affinfo
 
 Print information about an AFF file
 
 ```
 root@kali:~# affinfo -h
 affinfo version 3.7.22
 usage: affinfo [options] infile
    -a = print ALL segments (normally data segments are suppressed)
    -b = print how many bad blocks in each segment (implies -a)
    -i = identify the files, don't do info on them.
    -w = wide output; print more than 1 line if necessary.
    -s segment =   Just print information about 'segment'.
                     (may be repeated)
    -m = validate MD5 hash of entire image
    -S = validate SHA1 hash of entire image
    -v = validate the hash of each page (if present)
    -y = don't print segments of lengths 16 and 20 as hex)
    -p<passphrase> = Specify <passphrase> to decrypt file
    -l = Just print the segment names and exit
    -V = Just print the version number and exit.
 
 Preview Options:
    -X = no data preview; just print the segment names
    -x = print binary values in hex (default is ASCII)
 
 Misc:
    -d = debug
    -A = if infile is a device, print the number of sectors
         and sector size to stdout in XML. Otherwise error
 
 Compilation:
     LZMA compression: Enabled
     QEMU enabled
     FUSE enabled
     Amazon S3 enabled
     HAVE_LIBEXPAT 
 ```
 
 - - -
 
 ##### affix
 
 Fix a corrupted AFF file
 
 ```
 root@kali:~# affix -h
 usage: affix [options] file1 [...]
   -y = Actually modify the files; normally just reports the problems
   -v = Just print the version number and exit.
 ```
 
 - - -
 
 ##### affrecover
 
 Recover broken pages of an AFF file
 
 ```
 root@kali:~# affrecover -h
 usage: affrecover filename
 ```
 
 - - -
 
 ##### affsegment
 
 Segment manipulation tool
 
 ```
 root@kali:~# affsegment -h
 affsegment version 3.7.22
 usage: affsegment [options] file1.aff [file2.aff ...]
 options:
     -c              Create AFF files if they do not exist
     -ssegval        Sets the value of a segment; may be repeated
     -psegname       Prints the contents of the segment name for each file
     -V              Just print the version number and exit.
     -dname          Delete segment 'name'
     -h, -?          Print this message
     -Q              interpert 8-byte segments as a 64-bit value
     -A              Print the 32-bit arg, not the segment value
     -x              Print the segment as a hex string
 
 Values for segval:
 
 Setting the segment values:
     -sname=-        Take the new value of segment 'name' from stdin
     -sname=val      Sets segment 'name' to be 'val'  
     -sname=<val     Sets segment 'name' to be contents of file 'val'
 
 Setting the segment args:
     -sname/arg       Sets segment 'name' arg to be 'arg'  (may be repeated)
 
 Setting both the segment value and the arg:
     -sname/arg=val   Sets both arg and val for segment 'name'
     -sname/arg=<file Sets the arg and take contents from file 'file'
     -sname/arg=-     Sets the arg of segment 'name' and take the contents from stdin
 
 Note: All deletions are done first, then all updates. Don't specify the
 same segment twice on one command line.
 ```
 
 - - -
 
 ##### affsign
 
 Sign an existing AFF file
 
 ```
 root@kali:~# affsign -h
 affsign version 3.7.22
 usage: affsign [options] filename.aff
 This program will:
   * Sign each segment if there are no segment signatures.
   * Write signed chain-of-custody Bill of Materials segment.
 
 Signature Options:
    -k filename.key   = specify private key for signing
    -c filename.cer   = specify a X.509 certificate that matches the private key
                        (by default, the file is assumed to be the same one
                        provided with the -k option.)
    -Z                = ZAP (remove) all signature segments.
 options:
     -n      --- ask for a chain-of-custody note.
     -v      --- Just print the version number and exit.
 ```
 
 - - -
 
 ##### affstats
 
 Print specific statistics about one or more AFF files
 
 ```
 root@kali:~# affstats -h
 affstats version 3.7.22
 
 usage: affstats [options] infile(s)
       -m = print all output in megabytes
       -V = Just print the version number and exit.
 ```
 
 - - -
 
 ##### affuse
 
 Provide access to AFF containers
 
 ```
 root@kali:~# affuse -h
 affuse version 3.7.22
 Usage: affuse [<FUSE library options>] af_image mount_point
 
 Use fusermount3 -u mount_point, to unmount
 ```
 
 - - -
 
 ##### affverify
 
 Verify the digital signature on a signed file
 
 ```
 root@kali:~# affverify -h
 affverify version 3.7.22
 usage: affverify [options] filename.aff
 Verifies the digital signatures on a file
 options:
     -a      --- print all segments
     -V      --- Just print the version number and exit.
     -v      --- verbose
   SHA256 is operational
 ```
 
 - - -
 
 ##### affxml
 
 Print AFF information as XML
 
 ```
 root@kali:~# affxml -h
 affxml version 3.7.22
 usage: affxml [options] infile... 
    -V         =   Just print the version number and exit
    -x         =   Don't include the infile filename in output.
    -j segname =   Just print information about segname 
                   (may be repeated)
    -s         =   output 'stats' for the file data (may a long time)
 ```
 
 - - -
 
 ### libafflib-dev
 
 **Advanced Forensics Format Library (development files)**  
  The Advanced Forensic Format (AFF) is on-disk format for storing
  computer forensic information. Critical features of AFF include:
   
   - AFF allows you to store both computer forensic data and associated
     metadata in one or more files.
   - AFF allows files to be digital signed, to provide for
     chain-of-custody and long-term file integrity.
   - AFF allows for forensic disk images to stored encrypted and
     decrypted on-the-fly for processing. This allows disk images
     containing privacy sensitive material to be stored on the Internet.
   
  This package provides the development files.
 
 **Installed size:** `964 KB`  
 **How to install:** `sudo apt install libafflib-dev`  
 
 {{< spoiler "Dependencies:" >}}
 * libafflib0t64 
 {{< /spoiler >}}
 
 
 - - -
 
 ### libafflib0t64
 
 **Advanced Forensics Format Library**  
  The Advanced Forensic Format (AFF) is on-disk format for storing
  computer forensic information. Critical features of AFF include:
   
   - AFF allows you to store both computer forensic data and associated
     metadata in one or more files.
   - AFF allows files to be digital signed, to provide for
     chain-of-custody and long-term file integrity.
   - AFF allows for forensic disk images to stored encrypted and
     decrypted on-the-fly for processing. This allows disk images
     containing privacy sensitive material to be stored on the Internet.
 
 **Installed size:** `621 KB`  
 **How to install:** `sudo apt install libafflib0t64`  
 
 {{< spoiler "Dependencies:" >}}
 * libc6 
 * libcurl4t64 
 * libexpat1 
 * libgcc-s1 
 * libssl3t64 
 * libstdc++6 
 * zlib1g 
 {{< /spoiler >}}
 
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\afflib\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.775934
