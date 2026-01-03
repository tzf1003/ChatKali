---
tool_id: radare2
title: radare2
categories: ["reverse-engineering", "utilities"]
category_slugs: ["reverse-engineering", "utilities"]
homepage: https://www.radare.org
repository: 
version: 6.0.4+dfsg-1
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-hardware kali-tools-respond kali-tools-reverse-engineering"]
icon: images/radare2-logo.svg
source_path: kali-tools\radare2\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.070126
---

# Tool: radare2 (radare2)

## Categories
- [reverse-engineering](../reverse-engineering.md)
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.radare.org](https://www.radare.org) |
| Repository |  |
| Version | 6.0.4+dfsg-1 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-forensics kali-tools-hardware kali-tools-respond kali-tools-reverse-engineering |
| Icon | images/radare2-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/radare2
- **PackagesInfo**: |
- ****Installed size**: ** `3.58 MB`
- ****How to install**: ** `sudo apt install radare2`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# radiff2 -h
- **Usage**: radiff2 [-options] [-A[A]] [-B #] [-g sym] [-m graph_mode][-t %] [file] [file]
- **-C           file is host**: port (alias for -c+=http://%s/cmd/)
- **-t        user**: password authentication file
- **Commands**: []
- **Supported test types**: @asm @json @unit @fuzz @arch @cmd
- **OS/Arch for archos tests**: linux-x86_64
- **usage**: sdb [-0cCdDehjJrtv|-D A B] [-|db] [.file]|[-=]|==||[-+][(idx)key[:json|=value] ..]
- **[-C F**: C:D] [-f str] [-m addr] [-n str] [-N m:M] [-P[-P] pdb]
- **-C [fmt**: C:D]    create [elf,mach0,pe] with Code and Data hexpairs (see -a)
- **-k [sdb-query]  run sdb query. for example**: *
- **-N [min**: max]    force min:max number of chars per string (see -z and -zz)
- **Environment**: []
- **RABIN2_DEMANGLE_TRYLIB	e bin.demangle.trylib # load Swift libs to demangle (default**: false)
- **-C         graphdiff code (columns**: off-A, match-ratio, off-B) (see -A)
- **-o [addr]  specify initial offset for diffing, can use A**: B format


## Documentation (Upstream)
+++)
   -U         unified output using system 'diff'
   -v         show version information
   -V         be verbose (current only for -s)
 ```
 
 - - -
 
 ##### rafind2
 
 Advanced command-line byte pattern search in files
 
 ```
 root@kali:~# rafind2 -h
 Usage: rafind2 [-mBXnzZhqv] [-a align] [-b sz] [-f/t from/to] [-[e|s|S] str] [-x hex] -|file|dir ..
  -a [align] only accept aligned hits
  -b [size]  set block size
  -B         use big endian instead of the little one (See -V)
  -c         disable colourful output (mainly for for -X)
  -e [regex] search for regex matches (can be used multiple times)
  -E         perform a search using an esil expression
  -f [from]  start searching from address 'from'
  -F [file]  read the contents of the file and use it as keyword
  -h         show this help
  -i         identify filetype (r2 -nqcpm file)
  -j         output in JSON
  -L         list all io plugins (same as r2 for now)
  -m         magic search, file-type carver
  -M [str]   set a binary mask to be applied on keywords
  -n         do not stop on read errors
  -r         print using radare commands
  -s [str]   search for a string (more than one string can be passed)
  -S [str]   search for a wide string (more than one string can be passed).
  -t [to]    stop search at address 'to'
  -q         quiet: fewer output do not show headings or filenames.
  -v         print version and exit
  -V [s:num | s:num1,num2] search for a value or range in the specified endian (-V 4:123 or -V 4:100,200)
  -x [hex]   search for hexpair string (909090) (can be used multiple times)
  -X         show hexdump of search results
  -z         search for zero-terminated strings
  -Z         show string found on each search hit
 ```
 
 - - -
 
 ##### ragg2
 
 Radare2 Frontend for r_egg; Compiles Programs into Tiny Binaries for x86 and ARM Architectures
 
 ```
 root@kali:~# ragg2 -h
 Usage: ragg2 [-FOLsrxhvz] [-a arch] [-b bits] [-k os] [-o file] [-I path]
              [-i sc] [-E enc] [-B hex] [-c k=v] [-C file] [-p pad] [-q off]
              [-S string] [-f fmt] [-nN dword] [-dDw off:hex] [-e expr] file|f.asm|-
  -a [arch]       select architecture (x86, mips, arm)
  -b [bits]       register size (32, 64, ..)
  -B [hexpairs]   append some hexpair bytes
  -c [k=v]        set configuration options
  -C [file]       append contents of file
  -d [off:dword]  patch dword (4 bytes) at given offset
  -D [off:qword]  patch qword (8 bytes) at given offset
  -e [egg-expr]   take egg program from string instead of file
  -E [encoder]    use specific encoder. see -L
  -f [format]     output format (raw, c, pe, elf, mach0, python, javascript)
  -F              output native format (osx=mach0, linux=elf, ..)
  -h              show this help
  -H ([var])      display variable
  -i [shellcode]  include shellcode plugin, uses options. see -L
  -I [path]       add include path
  -k [os]         operating system's kernel (linux,bsd,osx,w32)
  -L              list all plugins (shellcodes and encoders)
  -n [dword]      append 32bit number (4 bytes)
  -N [dword]      append 64bit number (8 bytes)
  -o [file]       output file
  -O              use default output file (filename without extension or a.out)
  -p [padding]    add padding after compilation (padding=n10s32)
                  ntas : begin nop, trap, 'a', sequence
                  NTAS : same as above, but at the end
  -P [size]       prepend debruijn pattern
  -q [fragment]   debruijn pattern offset
  -r              show raw bytes instead of hexpairs
  -s              show assembler
  -S [string]     append a string
  -v              show version
  -w [off:hex]    patch hexpairs at given offset
  -x              execute
  -X [hexpairs]   execute rop chain, using the stack provided
  -z              output in C string syntax
 R2_NOPLUGINS	do not load any plugin
 ```
 
 - - -
 
 ##### rahash2
 
 Block-Based Hashing, Encoding, and Encryption Utility
 
 ```
 root@kali:~# rahash2 -h
 Usage: rahash2 [-BehjkLqrvX] [-b S] [-a A] [-c H] [-E A] [-s S] [-f O] [-t O] [file] ...
  -a algo     comma separated list of algorithms (default is 'sha256')
  -b bsize    specify the size of the block (instead of full file)
  -B          show per-block hash
  -c hash     compare with this hash
  -e          swap endian (use little endian)
  -E algo     encrypt. Use -S to set key and -I to set IV
  -D algo     decrypt. Use -S to set key and -I to set IV
  -f from     start hashing at given address
  -i num      repeat hash N iterations (f.ex: 3DES)
  -I iv       use give initialization vector (IV) (hexa or s:string)
  -j          output in json
  -J          new simplified json output (same as -jj)
  -S seed     use given seed (hexa or s:string) use ^ to prefix (key for -E)
              (- will slurp the key from stdin, the @ prefix points to a file
  -k          show hash using the openssh's randomkey algorithm
  -q          run in quiet mode (-qq to show only the hash)
  -L          list muta plugins (combines with -q, used by -a, -E and -D)
  -r          output radare commands
  -s string   hash this string instead of files
  -t to       stop hashing at given address
  -x hexstr   hash this hexpair string instead of files
  -X          output in hexpairs instead of binary/plain
  -v          show version information
 ```
 
 - - -
 
 ##### rapatch2
 
 
 ```
 root@kali:~# rapatch2 -h
 Usage: rapatch2 [-p N] [-sv] [-R] [patchfile] ([targetfile])
   -p N       patch level, skip N directories
   -R         reverse patch
   -s         sandbox mode, disable scripts and r2 command execution
   -q         be quiet
   -v         show version
 ```
 
 - - -
 
 ##### rarun2
 
 Radare2 utility to run programs in exotic environments
 
 ```
 root@kali:~# rarun2 -h
 Usage: rarun2 -v|-t|script.rr2 [directive ..]
 program=/bin/ls
 arg1=/bin
 # arg2=hello
 # arg3="hello\nworld"
 # arg4=:048490184058104849
 # arg5=:!ragg2 -p n50 -d 10:0x8048123
 # arg6=@arg.txt
 # arg7=@300@ABCD # 300 chars filled with ABCD pattern
 # system=r2 -
 # daemon=false
 # aslr=no
 setenv=FOO=BAR
 # unsetenv=FOO
 # clearenv=true
 # envfile=environ.txt
 timeout=3
 # timeoutsig=SIGTERM # or 15
 # connect=localhost:8080
 # listen=8080
 # pty=false
 # fork=true
 # bits=32
 # pid=0
 # pidfile=/tmp/foo.pid
 # #sleep=0
 # #maxfd=0
 # #execve=false
 # #maxproc=0
 # #maxstack=0
 # #core=false
 # #stdio=blah.txt
 # #stderr=foo.txt
 # #stderrout=false
 # stdout=foo.txt
 # stdin=input.txt # or !program to redirect input from another program
 # input=input.txt
 # chdir=/
 # chroot=/mnt/chroot
 # libpath=$PWD:/tmp/lib
 # r2preload=yes
 # preload=/lib/libfoo.so # you can load more than one lib by using this directive many times
 # setuid=2000
 # seteuid=2000
 # setgid=2001
 # setegid=2001
 # nice=5
 ```
 
 - - -
 
 ##### rasign2
 
 Radare2 signature management tool
 
 ```
 root@kali:~# rasign2 -h
 Usage: rasign2 [options] [file]
  -a               make signatures from all .o files in the provided .a file
  -A[AAA]          same as r2 -A, the more 'A's the more analysis is performed
  -f               interpret the file as a FLIRT .sig file and dump signatures
  -h               help menu
  -j               show signatures in json
  -i script.r2     execute this script in the 
  -o sigs.sdb      add signatures to file, create if it does not exist
  -q               quiet mode
  -r               show output in radare commands
  -S               perform operation on sdb signature file ('-o -' to save to same file)
  -s signspace     save all signatures under this signspace
  -c               add collision signatures before writing file
  -v               show version information
  -m               merge/overwrite signatures with same name
 Examples:
   rasign2 -o libc.sdb libc.so.6
 ```
 
 - - -
 
 ##### rasm2
 
 Radare2 Assembler and Disassembler Tool
 
 ```
 root@kali:~# rasm2 -h
 Usage: rasm2 [-ACdDehHLBvw] [-a arch] [-b bits] [-s addr] [-S syntax]
    [-f file] [-o file] [-F fil:ter] [-i skip] [-l len] 'code'|hex|0101b|-
  -a [arch]    set architecture to assemble/disassemble (see -L)
  -A           show Analysis information from given hexpairs
  -b [bits]    set cpu register size (8, 16, 32, 64) (RASM2_BITS)
  -B           binary input/output (-l is mandatory for binary input)
  -c [cpu]     select specific CPU (depends on arch)
  -C           output in C format
  -d, -D       disassemble from hexpair bytes (-D show hexpairs)
  -e           use big endian instead of little endian
  -E           display ESIL expression (same input as in -d)
  -f [file]    read data from file
  -F [parser]  specify which parse filter use (see -LL)
  -h, -hh      show this help, -hh for long
  -H ([var])   display variable
  -i [len]     ignore/skip N bytes of the input buffer
  -j           output in json format
  -k [kernel]  select operating system (linux, windows, darwin, android, ios, ..)
  -l [len]     input/Output length
  -L ([name])  list RArch plugins: (a=asm, d=disasm, e=esil)
  -LL ([name]) list RAsm parse plugins
  -N           same as r2 -N (or R2_NOPLUGINS) (not load any plugin)
  -o [file]    output file name (rasm2 -Bf a.asm -o a)
  -p           run SPP over input for assembly
  -q           quiet mode
  -r           output in radare commands
  -s,-@ [addr] define initial start/seek address (default 0)
  -S [syntax]  select syntax (intel, att)
  -v           show version information
  -x           use hex dwords instead of hex pairs when assembling.
  -w           what's this instruction for? describe opcode
  If '-l' value is greater than output length, output is padded with nops
  If the last argument is '-' reads from stdin
 Environment:
 R2_NOPLUGINS	do not load shared plugins (speedup loading)
 R2_LOG_LEVEL	change the log level
 R2_DEBUG	if defined, show error messages and crash signal
 R2_DEBUG_ASSERT	lldb -- r2 to get proper backtrace of the runtime assert
 RASM2_ARCH	same as rasm2 -a
 RASM2_BITS	same as rasm2 -b
 ```
 
 - - -
 
 ##### ravc2
 
 Radare2 Version Control Interface
 
 ```
 root@kali:~# ravc2 -h
 Usage: ravc2 [-qvh] [action] [args ...]
 Flags:
  -q         quiet mode
  -v         show version
  -h         display this help message
  -H ([var]) display variable
  -j         json output
 Actions:
  init       [git | rvc]          initialize a repository with the given vc
  branch     [name]               if a name is provided, create a branch with that name otherwise list branches
  commit     [message] [files...] commit the files with the message
  checkout   [branch]             set the current branch to the given branch
  status                        print a status message
  reset                         remove all uncommited changes
  log                           print all commits
 RAVC2_USER	override cfg.user value to author commit
 ```
 
 - - -
 
 ##### rax2
 
 Radare2 Base Converter
 
 ```
 root@kali:~# rax2 -h
 Usage: rax2 [-h|...] [- | expr ...] # convert between numeric bases
   int        ->  hex              ;  rax2 10
   hex        ->  int              ;  rax2 0xa
   -int       ->  hex              ;  rax2 -77
   -hex       ->  int              ;  rax2 0xffffffb3
   int        ->  bin              ;  rax2 b30
   int        ->  ternary          ;  rax2 t42
   bin        ->  int              ;  rax2 1010d
   ternary    ->  int              ;  rax2 1010dt
   float      ->  hex              ;  rax2 3.33f
   hex        ->  float            ;  rax2 Fx40551ed8
   oct        ->  hex              ;  rax2 35o
   hex        ->  oct              ;  rax2 Ox12 (O is a letter)
   bin        ->  hex              ;  rax2 1100011b
   hex        ->  bin              ;  rax2 Bx63
   ternary    ->  hex              ;  rax2 212t
   hex        ->  ternary          ;  rax2 Tx23
   raw        ->  hex              ;  rax2 -S < /binfile
   hex        ->  raw              ;  rax2 -s 414141
   -a         show ascii table     ;  rax2 -a
   -b <base>  output in <base>     ;  rax2 -b 10 0x46
   -c         output in C string   ;  rax2 -c 0x1234 # \x34\x12\x00\x00
   -C         dump as C byte array ;  rax2 -C < bytes
   -d         force integer        ;  rax2 -d 3 -> 3 instead of 0x3
   -e         swap endianness      ;  rax2 -e 0x33
   -D         base64 decode        ;  rax2 -D "aGVsbG8="
   -E         base64 encode        ;  rax2 -E "hello"
   -f         floating point       ;  rax2 -f 6.3+2.1
   -F         stdin slurp code hex ;  rax2 -F < shellcode.[c/py/js]
   -h         help                 ;  rax2 -h
   -H         hash string          ;  rax2 -H linux osx
   -i         IP address <-> LONG  ;  rax2 -i 3530468537
   -j         json format output   ;  rax2 -j 0x1234 # same as r2 -c '?j 0x1234'
   -k         keep base            ;  rax2 -k 33+3 -> 36
   -K         randomart            ;  rax2 -K 0x34 1020304050
   -n         newline              ;  append newline to output (for -E/-D/-r/..)
   -o         octalstr -> raw      ;  rax2 -o \162 \62 # r2
   -q         quiet mode           ;  rax2 -qC < /etc/hosts # be quiet
   -r         r2 style output      ;  rax2 -r 0x1234 # same as r2 -c '? 0x1234'
   -s         hexstr -> raw        ;  rax2 -s 43 4a 50
   -S         raw -> hexstr        ;  rax2 -S < /bin/ls > ls.hex
   -rS        raw -> hex.r2        ;  rax2 -rS < /bin/ls > ls.r2
   -t         tstamp -> str        ;  rax2 -t 1234567890
   -u         units                ;  rax2 -u 389289238 # 317.0M
   -v         version              ;  rax2 -v
   -w         signed word          ;  rax2 -w 0xffff 0xffff_ffff '0xff&0xfffff'
   -x         output in hexpairs   ;  rax2 -x 0x1234 # 34120000
   -X         bin -> hex(bignum)   ;  rax2 -X 111111111 # 0x1ff
   -z         str -> bin           ;  rax2 -z hello
   -Z         bin -> str           ;  rax2 -Z 01000101 01110110
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\radare2\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.070126
