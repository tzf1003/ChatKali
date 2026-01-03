---
tool_id: sleuthkit
title: sleuthkit
categories: ["forensics"]
category_slugs: ["forensics"]
homepage: https://www.sleuthkit.org/sleuthkit
repository: 
version: 4.12.1+dfsg-0kali6
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sleuthkit\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.110851
---

# Tool: sleuthkit (sleuthkit)

## Categories
- [forensics](../forensics.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.sleuthkit.org/sleuthkit](https://www.sleuthkit.org/sleuthkit) |
| Repository |  |
| Version | 4.12.1+dfsg-0kali6 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-respond |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sleuthkit
- **PackagesInfo**: |
- ****Installed size**: ** `1.63 MB`
- ****How to install**: ** `sudo apt install sleuthkit`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# jpeg_extract --help
- **blkcalc**: invalid option -- 'h'
- **Invalid argument**: (null)
- **usage**: jls [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-vV] image [inode]
- **One of the following must be given**: []
- **-d**: Display deleted entries only
- **-s**: Display slack space at end of file
- **-u**: Display undeleted entries only
- **-f fstype**: File system type (use '-f list' for supported types)
- **-i imgtype**: The format of the image file (use '-i list' for supported types)
- **-b dev_sector_size**: The size (in bytes) of the device sectors
- **-o imgoffset**: The offset of the file system in the image (in sectors)
- **-P pooltype**: Pool container type (use '-p list' for supported types)
- **-B pool_volume_block**: Starting block (for pool volumes only)
- **-v**: verbose output to stderr
- **-V**: print version
- **blkcat**: invalid option -- '-'
- **-a**: Allocated inodes
- **-h**: Do not display holes in sparse files
- **-w**: displays in web-like (html) fashion
- **-u usize**: size of each data unit in image (for raw, blkls, swap)
- **blkls**: invalid option -- 'h'
- **-e**: Display all inodes
- **-l**: Linked inodes
- **-A**: Unallocated inodes
- **blkstat**: invalid option -- 'h'
- **fcat**: invalid option -- '-'
- **-R**: Recover deleted file and suppress recovery errors
- **ffind**: invalid option -- 'h'
- **Default behavior**: Just print the file system statistics and exit.
- **options**: []
- **example**: -n .jpeg -n .jpg will find all JPEG files
- **Ways to make this program run faster**: []
- **Ways to make this program run slower**: []
- **Output options**: []
- **Misc**: []
- **SleuthKit Version**: 4.12.1
- **AFFLIB Version**: 3.7.22
- **LIBEWF Version**: 20140816
- **fls**: invalid option -- '-'
- **-D**: Display only directories
- **-F**: Display only files
- **-m**: Display output in the mactime format
- **-S snap_id**: Snapshot ID (for APFS only)
- **-p**: Display orphan inodes (unallocated with no file name)
- **-r**: display run list instead of list of block addresses
- **-z**: Unused inodes
- **-s seconds**: Time skew of original machine (in seconds)
- **-k password**: Decryption password for encrypted volumes
- **fsstat**: invalid option -- 'h'
- **-t**: display type only
- **hfind**: invalid option -- 'h'
- **-q**: Quick mode - where a 1 is printed if it is found, else 0
- **-c db_name**: Create new database with the given name.
- **-f lookup_file**: File with one hash per line to lookup
- **-i db_type**: Create index file for a given hash database type
- **db_file**: The path of the hash database, must have .kdb extension for -c option
- **[hashes]**: hashes to lookup (STDIN is used otherwise)
- **Supported index types**: nsrl-md5, nsrl-sha1, md5sum, encase, hk
- **icat**: invalid option -- '-'
- **ifind**: invalid option -- 'h'
- **-d unit_addr**: Find the meta data given the data unit
- **-n file**: Find the meta data given the file name
- **-p par_addr**: Find UNALLOCATED MFT entries given the parent's meta address (NTFS only)
- **-z ZONE**: Time zone setting when -l -p is given
- **ils**: invalid option -- 'h'
- **-O**: Display inodes that are unallocated, but were sill open (UFS/ExtX only)
- **-L**: Unlinked inodes
- **-Z**: Used inodes
- **img_cat**: invalid option -- 'h'
- **-s start_sector**: The sector number to start at
- **-e stop_sector**: The sector number to stop at
- **img_stat**: invalid option -- 'h'
- **istat**: invalid option -- 'h'
- **-N num**: force the display of NUM address of block pointers
- **-z zone**: time zone of original machine (i.e. EST5EDT or GMT)
- **jcat**: invalid option -- 'h'
- **blk**: The journal block to view
- **inode**: The file system inode where the journal is located
- **jls**: invalid option -- 'h'


## Documentation (Upstream)
v,---version-------------------Display-software-version
 ---i,---ids-----------------------Show-IDs-instead-of-tag-names
 ---t,---tag=tag-------------------Select-tag
 --------ifd=IFD-------------------Select-IFD
 ---l,---list-tags-----------------List-all-EXIF-tags
 ---|,---show-mnote----------------Show-contents-of-tag-MakerNote
 --------remove--------------------Remove-tag-or-ifd
 ---s,---show-description----------Show-description-of-tag
 ---e,---extract-thumbnail---------Extract-thumbnail
 ---r,---remove-thumbnail----------Remove-thumbnail
 ---n,---insert-thumbnail=FILE-----Insert-FILE-as-thumbnail
 --------no-fixup------------------Do-not-fix-existing-tags-in-files
 ---o,---output=FILE---------------Write-data-to-FILE
 --------set-value=STRING----------Value-of-tag
 ---c,---create-exif---------------Create-EXIF-data-if-not-existing
 ---m,---machine-readable----------Output-in-a-machine-readable--tab-delimited-
 ----------------------------------format
 ---w,---width=WIDTH---------------Width-of-output
 ---x,---xml-output----------------Output-in-a-XML-format
 ---d,---debug---------------------Show-debugging-messages
 
 Help-options-
 ---?,---help----------------------Show-this-help-message
 --------usage---------------------Display-brief-usage-message
 ```
 
 - - -
 
 ##### mactime
 
 Create an ASCII time line of file activity
 
 ```
 root@kali:~# mactime --help
 Unknown option: --help
 mactime [-b body_file] [-p password_file] [-g group_file] [-i day|hour idx_file] [-d] [-h] [-V] [-y] [-z TIME_ZONE] [DATE]
 		-b: Specifies the body file location, else STDIN is used
 		-d: Output in comma delimited format
 		-h: Display a header with session information
 		-i [day | hour] file: Specifies the index file with a summary of results
 		-y: Dates are displayed in ISO 8601 format
 		-m: Dates have month as number instead of word (does not work with -y)
 		-z: Specify the timezone the data came from (in the local system format) (does not work with -y)
 		-g: Specifies the group file location, else GIDs are used
 		-p: Specifies the password file location, else UIDs are used
 		-V: Prints the version to STDOUT
 		[DATE]: starting date (yyyy-mm-dd) or range (yyyy-mm-dd..yyyy-mm-dd) 
 		[DATE]: date with time (yyyy-mm-ddThh:mm:ss), using with range one or both can have time
 ```
 
 - - -
 
 ##### mmcat
 
 Output the contents of a partition to stdout
 
 ```
 root@kali:~# mmcat -h
 mmcat: invalid option -- 'h'
 Unknown argument
 usage: mmcat [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-vV] [-t vstype] image [images] part_num
 	-t vstype: The type of partition system (use '-t list' for list of supported types)
 	-i imgtype: The format of the image file (use '-i list' for list of supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-o imgoffset: Offset to the start of the volume that contains the partition system (in sectors)
 	-v: verbose output
 	-V: print the version
 ```
 
 - - -
 
 ##### mmls
 
 Display the partition layout of a volume system (partition tables)
 
 ```
 root@kali:~# mmls -h
 mmls: invalid option -- 'h'
 Unknown argument
 usage: mmls [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-BrvV] [-aAmM] [-t vstype] image [images]
 	-t vstype: The type of volume system (use '-t list' for list of supported types)
 	-i imgtype: The format of the image file (use '-i list' for list supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-o imgoffset: Offset to the start of the volume that contains the partition system (in sectors)
 	-B: print the rounded length in bytes
 	-r: recurse and look for other partition tables in partitions (DOS Only)
 	-v: verbose output
 	-V: print the version
 Unless any of these are specified, all volume types are shown
 	-a: Show allocated volumes
 	-A: Show unallocated volumes
 	-m: Show metadata volumes
 	-M: Hide metadata volumes
 ```
 
 - - -
 
 ##### mmstat
 
 Display details about the volume system (partition tables)
 
 ```
 root@kali:~# mmstat -h
 mmstat: invalid option -- 'h'
 Unknown argument
 usage: mmstat [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-vV] [-t vstype] image [images]
 	-t vstype: The volume system type (use '-t list' for list of supported types)
 	-i imgtype: The format of the image file (use '-i list' for list of supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-o imgoffset: Offset to the start of the volume that contains the partition system (in sectors)
 	-v: verbose output
 	-V: print the version
 ```
 
 - - -
 
 ##### pstat
 
 
 ```
 root@kali:~# pstat -h
 pstat: invalid option -- 'h'
 Invalid argument: (null)
 usage: pstat [-tvV] [-p pooltype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] image
 	-t: display type only
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-P pooltype: Pool container type (use '-P list' for supported types)
 	-o imgoffset: The offset of the file system in the image (in sectors)
 	-v: verbose output to stderr
 	-V: Print version
 ```
 
 - - -
 
 ##### sigfind
 
 Find a binary signature in a file
 
 ```
 root@kali:~# sigfind -h
 sigfind: invalid option -- 'h'
 sigfind [-b bsize] [-o offset] [-t template] [-lV] [hex_signature] file
 	-b bsize: Give block size (default 512)
 	-o offset: Give offset into block where signature should exist (default 0)
 	-l: Signature will be little endian in image
 	-V: Version
 	-t template: The name of a data structure template:
 		dospart, ext2, ext3, ext4, fat, hfs, hfs+, ntfs, ufs1, ufs2
 ```
 
 - - -
 
 ##### sorter
 
 Sort files in an image into categories based on file type
 
 ```
 root@kali:~# sorter -h
 Missing image argument
 
 sorter [-b size] [-E] [-e] [-h]  [-l] [-md5] [-s] [-sha1] [-U] [-v] [-V] [-a hash_alert] [-c config] [-C config] [-d dir] [-m mnt] [-n nsrl_db] [-x hash_exclude] [-o imgoffset] [-f fstype] [-i imgtype] image [images] [dir_meta_addr] 
 
     -b size: Minimum size.  Ignore files smaller than 'size'
 	-E: Perform category indexing only (no extension checks - was '-i')
 	-e: Perform extension checks only (no category index files)
 	-h: HTML Format
 	-l: List index to STDOUT (no files are ever written)
 	-md5: Print the MD5 value with the index output
 	-s: Save files to category directories
 	-sha1: Print the SHA-1 value with the index output
 	-U: Ignore the unknown category - only save catgories in config files
 	-v: verbose debugging output
 	-V: print version information
 	-a hash_alert: hash database of hashes to alert on
 	-c config: specify a config file to use (in addition to default files)
 	   NOTE: This config file has priority over default files
 	-C config: specify the ONLY config file to use
 	-d dir: Save category index files in the specified directory
 	-f fstype: file system type (Sleuth Kit types) of image
 	-i imgtype: Format of image file
 	-o imgoffset: Offset of file system in image (in sectors)
 	-m mnt: The mounting point of the image
 	-n nsrl_db: The NIST NSRL database file (NSRLFile.txt) (hashes to ignore)
 	-x hash_exclude: hash database of hashes to ignore
 	dir_meta_addr: Address of directory to start analyzing from 
 	image: image to analyze
 ```
 
 - - -
 
 ##### srch_strings
 
 Display printable strings in files
 
 ```
 root@kali:~# srch_strings -h
 Usage: srch_strings [option(s)] [file(s)]
  Display printable strings in [file(s)] (stdin by default)
  The options are:
   -a -                 Scan the entire file, not just the data section
   -f       Print the name of the file before each string
   -n number       Locate & print any NUL-terminated sequence of at
   -<number>                 least [number] characters (default 4).
   -t {o,x,d}        Print the location of the string in base 8, 10 or 16
   -o                        An alias for --radix=o
   -e {s,S,b,l,B,L} Select character size and endianness:
                             s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
   -h                  Display this information
   -v               Print the program's version number
 ```
 
 - - -
 
 ##### tsk_comparedir
 
 Compare the contents of a directory with the contents of an image or local device.
 
 ```
 root@kali:~# tsk_comparedir -h
 tsk_comparedir: invalid option -- 'h'
 Invalid argument: (null)
 usage: tsk_comparedir [-f fstype] [-i imgtype] [-b dev_sector_size] [-o sector_offset] [-P pooltype] [-B pool_volume_block] [-n start_inum] [-vV] image [image] comparison_directory
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-f fstype: The file system type (use '-f list' for supported types)
 	-o sector_offset: sector offset for file system to compare
 	-P pooltype: Pool container type (use '-P list' for supported types)
 	-B pool_volume_block: Starting block (for pool volumes only)
 	-n start_inum: inum for directory in image file to start compare at
 	-v: verbose output to stderr
 	-V: Print version
 ```
 
 - - -
 
 ##### tsk_gettimes
 
 Collect MAC times from a disk image into a body file.
 
 ```
 root@kali:~# tsk_gettimes -h
 tsk_gettimes: invalid option -- 'h'
 Invalid argument: (null)
 usage: tsk_gettimes [-vVm] [-i imgtype] [-b dev_sector_size] [-z zone] [-s seconds] image [image]
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-m: Calculate MD5 hash in output (slow)
 	-v: verbose output to stderr
 	-V: Print version
 	-z: Time zone of original machine (i.e. EST5EDT or GMT) (only useful with -l)
 	-s seconds: Time skew of original machine (in seconds) (only useful with -l & -m)
 ```
 
 - - -
 
 ##### tsk_imageinfo
 
 
 ```
 root@kali:~# tsk_imageinfo -h
 tsk_imageinfo: invalid option -- 'h'
 Invalid argument: (null)
 usage: tsk_imageinfo [-vV] [-i imgtype] [-b dev_sector_size] image
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-v: verbose output to stderr
 	-V: Print version
 ```
 
 - - -
 
 ##### tsk_loaddb
 
 Populate a SQLite database with metadata from a disk image
 
 ```
 root@kali:~# tsk_loaddb --help
 tsk_loaddb: invalid option -- '-'
 Invalid argument: --help
 usage: tsk_loaddb [-ahkvV] [-i imgtype] [-b dev_sector_size] [-d database] [-z ZONE] image [image]
 	-a: Add image to existing database, instead of creating a new one (requires -d to specify database)
 	-k: Don't create block data table
 	-h: Calculate hash values for the files
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-d database: Path for the database (default is the same directory as the image, with name derived from image name)
 	-v: verbose output to stderr
 	-V: Print version
 	-z: Time zone of original machine (i.e. EST5EDT or GMT)
 ```
 
 - - -
 
 ##### tsk_recover
 
 Export files from an image into a local directory
 
 ```
 root@kali:~# tsk_recover -h
 tsk_recover: invalid option -- 'h'
 Invalid argument: (null)
 usage: tsk_recover [-vVae] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o sector_offset] [-P pooltype] [-B pool_volume_block] [-d dir_inum] image [image] output_dir
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-f fstype: The file system type (use '-f list' for supported types)
 	-v: verbose output to stderr
 	-V: Print version
 	-a: Recover allocated files only
 	-e: Recover all files (allocated and unallocated)
 	-o sector_offset: sector offset for a volume to recover (recovers only that volume)
 	-P pooltype: Pool container type (use '-P list' for supported types)
 	-B pool_volume_block: Starting block (for pool volumes only)
 	-d dir_inum: Directory inum to recover from (must also specify a specific partition using -o or there must not be a volume system)
 ```
 
 - - -
 
 ##### usnjls
 
 List the contents of a NTFS Update Sequence Number journal
 
 ```
 root@kali:~# usnjls -h
 usnjls: invalid option -- 'h'
 Invalid argument: (null)
 usage: usnjls [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-lmvV] image [inode]
 	-i imgtype: The format of the image file (use '-i list' for supported types)
 	-b dev_sector_size: The size (in bytes) of the device sectors
 	-f fstype: File system type (use '-f list' for supported types)
 	-o imgoffset: The offset of the file system in the image (in sectors)
 	-l: Long output format with detailed information
 	-m: Time machine output format
 	-v: verbose output to stderr
 	-V: print version
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\sleuthkit\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.110851
