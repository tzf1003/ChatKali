---
tool_id: iodine
title: iodine
categories: ["tunneling-exfiltration"]
category_slugs: ["tunneling-exfiltration"]
homepage: https://code.kryo.se/iodine
repository: 
version: 0.7.0-12
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation"]
icon: images/iodine-logo.svg
source_path: kali-tools\iodine\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.948421
---

# Tool: iodine (iodine)

## Categories
- [tunneling-exfiltration](../tunneling-exfiltration.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://code.kryo.se/iodine](https://code.kryo.se/iodine) |
| Repository |  |
| Version | 0.7.0-12 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-tools-post-exploitation |
| Icon | images/iodine-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://git.toastfreeware.priv.at/debian/iodine.git/
- **PackagesInfo**: |
- ****Installed size**: ** `245 KB`
- ****How to install**: ** `sudo apt install iodine`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# iodine-client-start -h
- **Usage**: iodine-client-start [option]
- **Options to try if connection doesn't work**: []
- **-T force dns type**: NULL, PRIVATE, TXT, SRV, MX, CNAME, A (default: autodetect)
- **-O force downstream encoding for -T other than NULL**: Base32, Base64, Base64u,
- **Base128, or (only for TXT**: ) Raw  (default: autodetect)
- **-L 1**: use lazy mode for low-latency (default). 0: don't (implies -I1)
- **-m max size of downstream fragments (default**: autodetect)
- **-M max size of upstream hostnames (~100-255, default**: 255)
- **Other options**: []
- **or invoke the script with those environment variables set**: []
- **starting with '#', or settings of the form VAR="val". Valid VARs are**: []
- **Sample value**: password_for_that_tunnel (no default, must be set)
- **Hostname to ping when testing if network is working (default**: []
- **tunnel (default**: false)
- **(default**: true)
- **pinging the host at the other end (default**: true)
- **up by trying to ping an external host (default**: true)


## Documentation (Upstream)
should be found
     automatically, set this if that fails and the program guesses wrong.
 
 interface
     Interface to use (e.g., eth1, eth0, etc) for connection to DNS
     server used for the iodine tunnel---should be found automatically,
     set this if that fails and the program guesses wrong.
 
 mtu
     Set if tunnel MTU needs to be manually changed (lowered). Should
     not be necessary anymore, as recent versions of iodine negotiate
     an appropriate MTU during tunnel setup. But if that negotiation
     does not happen, or if you are using an older version of iodine,
     the default tunnel MTU is 1024, and if the local DNS server
     restricts to 512 byte packets you might need to use an MTU of 220.
 
 skip_raw_udp_mode
     Set "-r" option in iodine command line. With this option, iodine
     does not try to establish a direct UDP socket to the iodine server
     on port 53. (default: true).
 
 continue_on_error
     Set if the script should continue even if a command fails.
     Use to test script when running as non-root. Defaults to false
     if running as root, true otherwise.
 ```
 
 - - -
 
 ##### iodined
 
 Tunnel IPv4 over DNS
 
 ```
 root@kali:~# iodined -h
 iodine IP over DNS tunneling server
 Usage: iodined [-v] [-h] [-c] [-s] [-f] [-D] [-u user] [-t chrootdir] [-d device] [-m mtu] [-z context] [-l ip address to listen on] [-p port] [-n external ip] [-b dnsport] [-P password] [-F pidfile] tunnel_ip[/netmask] topdomain
   -v to print version info and exit
   -h to print this help and exit
   -c to disable check of client IP/port on each request
   -s to skip creating and configuring the tun device, which then has to be created manually
   -f to keep running in foreground
   -D to increase debug level
      (using -DD in UTF-8 terminal: "LC_ALL=C luit iodined -DD ...")
   -u name to drop privileges and run as user 'name'
   -t dir to chroot to directory dir
   -d device to set tunnel device name
   -m mtu to set tunnel device mtu
   -z context to apply SELinux context after initialization
   -l ip address to listen on for incoming dns traffic (default 0.0.0.0)
   -p port to listen on for incoming dns traffic (default 53)
   -n ip to respond with to NS queries
   -b port to forward normal DNS queries to (on localhost)
   -P password used for authentication (max 32 chars will be used)
   -F pidfile to write pid to a file
   -i maximum idle time before shutting down
 tunnel_ip is the IP number of the local tunnel interface.
    /netmask sets the size of the tunnel network.
 topdomain is the FQDN that is delegated to this server.
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\iodine\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.948421
