---
tool_id: aircrack-ng
title: aircrack-ng
categories: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
category_slugs: ["wireless-attacks", "sniffing-spoofing", "information-gathering"]
homepage: https://www.aircrack-ng.org/
repository: 
version: 1:1.7+git20230807.4bf83f1a-2
architectures: any all
license: 
binaries: []
metapackages: ["kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless"]
icon: images/aircrack-ng-logo.svg
source_path: kali-tools\aircrack-ng\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.777604
---

# Tool: aircrack-ng (aircrack-ng)

## Categories
- [wireless-attacks](../wireless-attacks.md)
- [sniffing-spoofing](../sniffing-spoofing.md)
- [information-gathering](../information-gathering.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://www.aircrack-ng.org/](https://www.aircrack-ng.org/) |
| Repository |  |
| Version | 1:1.7+git20230807.4bf83f1a-2 |
| Architectures | any all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-default kali-linux-everything kali-linux-headless kali-linux-large kali-linux-nethunter kali-tools-802-11 kali-tools-exploitation kali-tools-sniffing-spoofing kali-tools-social-engineering kali-tools-top10 kali-tools-wireless |
| Icon | images/aircrack-ng-logo.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/aircrack-ng
- **PackagesInfo**: |
- ****Installed size**: ** `99 KB`
- ****How to install**: ** `sudo apt install airgraph-ng`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# airodump-join -h
- **Original work**: Martin Beck
- **https**: //www.aircrack-ng.org
- **usage**: airodump-join [-h] [-o OUTPUT] [-i [FILENAME ...]]
- **Options**: []
- **-a bssid**: set Access Point MAC address
- **-i iface**: capture packets from this interface
- **-w WEP key**: use this WEP key to en-/decrypt packets
- **-h MAC**: source MAC address
- **-f disallow**: disallow specified client MACs (default: allow)
- **-W 0|1**: [don't] set WEP flag in beacons 0|1 (default: auto)
- **-q**: enable quiet mode (no status output)
- **-v**: verbose (print more messages)
- **-A**: Ad-Hoc Mode (allows other clients to peer)
- **-Y in|out|both**: external packet processing
- **-c channel**: sets the channel the AP is running on
- **-X**: disable  bruteforce   multithreading
- **-s**: show the key in ASCII while cracking
- **-S**: WPA cracking speed test
- **-L**: Caffe-Latte WEP attack (use if driver can't send frags)
- **-N**: cfrag WEP attack (recommended)
- **-x nbpps**: number of packets per second
- **-y**: experimental  single bruteforce mode
- **-0**: set all WPA,WEP,open tags. can't be used with -z & -Z
- **-z type**: sets WPA1 tags. 1=WEP40 2=TKIP 3=WRAP 4=CCMP 5=WEP104
- **-Z type**: same as -z, but for WPA2
- **-V type**: fake EAPOL 1=MD5 2=SHA1 3=auto
- **-F prefix**: write all sent and received frames into pcap file
- **-P**: respond to all probes, even when specifying ESSIDs
- **-I interval**: sets the beacon interval value in ms
- **-C seconds**: enables beaconing of probed ESSID values (requires -P)
- **-n hex**: User specified ANonce when doing the 4-way handshake
- **Filter options**: []
- **--bssid MAC**: BSSID to filter/use
- **--bssids file**: read a list of BSSIDs out of that file
- **--client MAC**: MAC of client to filter
- **--clients file**: read a list of MACs out of that file
- **--essid ESSID**: specify a single ESSID (default: default)
- **--essids file**: read a list of ESSIDs out of that file
- **--help**: Displays this usage screen
- **Common options**: []
- **-a <amode>**: force attack mode (1/WEP, 2/WPA-PSK)
- **-e <essid>**: target network SSID
- **-b <bssid>**: Set access point MAC address
- **-p <nbcpu>**: # of CPU to use  (default: all CPUs)
- **-C <macs>**: merge the given APs to a virtual one
- **-l <file>**: write key to file. Overwrites file.
- **Static WEP cracking options**: []
- **-c**: Do not crack the key
- **-t**: search binary coded decimal chr only
- **-h**: This help screen
- **-d <mask>**: use masking of the key (A1:XX:CF:YY)
- **-m <maddr>**: MAC address to filter usable packets
- **-n <nbits>**: WEP key length :  64/128/152/256/512
- **-i <index>**: WEP key index (1 to 4), default: any
- **-f <fudge>**: bruteforce fudge factor,  default: 2
- **-k <korek>**: disable one attack method  (1 to 17)
- **-x or -x0**: disable bruteforce for last keybytes
- **-x1**: last keybyte bruteforcing  (default)
- **-x2**: enable last  2 keybytes bruteforcing
- **-K**: use only old KoreK attacks (pre-PTW)
- **-M <num>**: specify maximum number of IVs to use
- **-D**: disable AP detection
- **-P <num>**: PTW debug:  1: disable Klein, 2: PTW
- **-1**: run only 1 try to crack key with PTW
- **-V**: run in visual inspection mode
- **WEP and WPA-PSK cracking options**: []
- **-w <words>**: path to wordlist(s) filename(s)
- **-N <file>**: path to new session filename
- **-R <file>**: path to existing session filename
- **WPA-PSK options**: []
- **-E <file>**: create EWSA Project file v3
- **-I <str>**: PMKID string (hashcat -m 16800)
- **-j <file>**: create Hashcat v3.6+ file (HCCAPX)
- **-J <file>**: create Hashcat file (HCCAP)
- **-Z <sec>**: WPA cracking speed test length of
- **-r <DB>**: path to airolib-ng database
- **SIMD selection**: []
- **--simd-list**: Show a list of the available
- **--simd=<option>**: Use specific SIMD architecture.
- **your platform**: []
- **Other options**: []
- **-u**: Displays # of CPUs & SIMD support
- **-l**: don't remove the 802.11 header
- **-o <fname>**: output file for decrypted packets (default <src>-dec)
- **WEP specific option**: []
- **-w <key>**: target network WEP key in hex
- **-c <fname>**: output file for corrupted WEP packets (default <src>-bad)
- **WPA specific options**: []
- **-p <pass>**: target network WPA passphrase
- **-k <pmk>**: WPA Pairwise Master Key in hex
- **options**: []
- **Mandatory**: []
- **-i <file>**: Input capture file
- **--ssid <ESSID>**: ESSID of the network to filter
- **--bssid <BSSID>**: BSSID of the network to filter
- **Optional**: []
- **-o <file>**: Output packets (valid) file (default: <src>-filtered.pcap)
- **-c <file>**: Output packets (cloaked) file (default: <src>-cloaked.pcap)
- **-u <file>**: Output packets (unknown/ignored) file (default: invalid_status.pcap)
- **--filters <filters>**: Apply filters (separated by a comma). Filters:
- **signal**: Try to filter based on signal.
- **duplicate_sn**: Remove all duplicate sequence numbers
- **duplicate_sn_ap**: Remove duplicate sequence number for
- **duplicate_sn_client**: Remove duplicate sequence number for the
- **consecutive_sn**: Filter based on the fact that IV should
- **duplicate_iv**: Remove all duplicate IV.
- **signal_dup_consec_sn**: Use signal (if available), duplicate and
- **--null-packets**: Assume that null packets can be cloaked.
- **--disable-base-filter**: Do not apply base filter.
- **--drop-frag**: Drop fragmented packets.
- **-b bssid**: MAC address, Access Point
- **-d dmac**: MAC address, Destination
- **-s smac**: MAC address, Source
- **-m len**: minimum packet length (default: 80)
- **-n len**: maximum packet length (default: 80)
- **-u type**: frame control, type    field
- **-v subt**: frame control, subtype field
- **-t tods**: frame control, To      DS bit
- **-f fromds**: frame control, From    DS bit
- **-w iswep**: frame control, WEP     bit
- **Replay options**: []
- **-p fctrl**: set frame control word (hex)
- **-c dmac**: set Destination  MAC address
- **-h smac**: set Source       MAC address
- **-g value**: change ring buffer size (default: 8)
- **-F**: choose first matching packet
- **Fakeauth attack options**: []
- **-e essid**: set target AP SSID
- **-o npckts**: number of packets per burst (0=auto, default: 1)
- **-q sec**: seconds between keep-alives
- **-Q**: send reassociation requests
- **-y prga**: keystream for shared key auth
- **-T n**: exit after retry fake auth request n time
- **Arp Replay attack options**: []
- **-j**: inject FromDS packets
- **Fragmentation attack options**: []
- **-k IP**: set destination IP in fragments
- **-l IP**: set source IP in fragments
- **Test attack options**: []
- **-B**: activates the bitrate test
- **Source options**: []
- **-r file**: extract packets from this pcap file
- **Miscellaneous options**: []
- **-R**: disable /dev/rtc usage
- **--ignore-negative-one**: Removes the message that says
- **--deauth-rc rc**: Deauthentication reason code [0-254] (Default: 7)
- **Attack modes (numbers can still be used)**: []
- **--deauth      count**: deauthenticate 1 or all stations (-0)
- **--fakeauth    delay**: fake authentication with AP (-1)
- **--interactive**: interactive frame selection (-2)
- **--arpreplay**: standard ARP-request replay (-3)
- **--chopchop**: decrypt/chopchop WEP packet (-4)
- **--fragment**: generates valid keystream   (-5)
- **--caffe-latte**: query a client for new IVs  (-6)
- **--cfrag**: fragments against a client  (-7)
- **--migmode**: attacks WPA migration mode  (-8)
- **--test**: tests injection and quality (-9)
- **--ivs**: Save only captured IVs
- **--gpsd**: Use GPSd
- **--write      <prefix>**: Dump file prefix
- **--beacons**: Record all beacons in dump file
- **--update       <secs>**: Display update delay in seconds
- **--showack**: Prints ack/cts/rts statistics
- **-f            <msecs>**: Time in ms between hopping channels
- **--berlin       <secs>**: Time before removing the AP/client
- **are received (Default**: 120 seconds)
- **-r             <file>**: Read packets from that file
- **--real-time**: While reading packets from a file,
- **-x            <msecs>**: Active Scanning Simulation
- **--manufacturer**: Display manufacturer from IEEE OUI list
- **--uptime**: Display AP Uptime from Beacon Timestamp
- **--wps**: Display WPS information (if any)
- **<formats>**: Output format. Possible values:
- **fixed channel <interface>**: -1
- **<seconds>**: Output file(s) write interval in seconds
- **--background <enable>**: Override background detection.
- **--encrypt   <suite>**: Filter APs by cipher suite,
- **--netmask <netmask>**: Filter APs by mask
- **--bssid     <bssid>**: Filter APs by BSSID,
- **--essid     <essid>**: Filter APs by ESSID,
- **--essid-regex <regex>**: Filter APs by ESSID using a regular
- **--min-packets   <int>**: Minimum AP packets recv'd before
- **displaying it (default**: 2)
- **--min-power     <int>**: Filter out APs with PWR less than
- **the specified value (default**: 0)
- **--min-rxq       <int>**: Filter out APs with RXQ less than
- **-a**: Filter out unassociated stations
- **-z**: Filter out associated stations
- **You can make it capture on other/specific channel(s) by using**: []
- **--ht20**: Set channel to HT20 (802.11n)
- **--ht40-**: Set channel to HT40- (802.11n)
- **--ht40+**: Set channel to HT40+ (802.11n)
- **--channel <channels>**: Capture on specific channels
- **--ignore-other-chans**: Filter out other channels
- **--band <abg>**: Band on which airodump-ng should hop
- **-C    <frequencies>**: Uses these frequencies in MHz to hop
- **--cswitch  <method>**: Set channel switching method
- **0**: FIFO (default)
- **1**: Round Robin
- **2**: Hop on last
- **Usage**: wpaclean <out.cap> <in.cap> [in2.cap] [...]
- **Operations**: []
- **--stats**: Output information about the database.
- **--sql <sql>**: Execute specified SQL statement.
- **--clean [all]**: Clean the database from old junk. 'all' will also
- **--batch**: Start batch-processing all combinations of ESSIDs
- **--verify [all]**: Verify a set of randomly chosen PMKs.
- **--import [essid|passwd] <file>**: []
- **--import cowpatty <file>**: []
- **--export cowpatty <essid> <file>**: []
- **-p  <port>**: TCP port to listen on (default:666)
- **-d <iface>**: Wifi interface to use
- **-c  <chan>**: Channel to use
- **-v <level>**: Debug level (1 to 3; default: 1)
- **-y file**: keystream-file for continuation
- **-w wepkey**: use this WEP-KEY to encrypt packets
- **-p pass**: use this WPA passphrase to decrypt packets
- **WDS/Bridge Mode options**: []
- **-s transmitter**: set Transmitter MAC address for WDS Mode
- **-b**: bidirectional mode. This enables communication
- **Repeater options**: []
- **--repeat**: activates repeat mode
- **--bssid <mac>**: BSSID to repeat
- **--netmask <mask>**: netmask for BSSID filter
- **-i <replay interface>**: Interface to listen and inject on
- **-d | --deauth**: Send active deauths to encrypted stations
- **-e | --essid <value>**: ESSID of target network
- **-p | --passphrase <val>**: WPA Passphrase of target network
- **-c | --icmp**: Respond to all ICMP frames (Debug)
- **-n | --dns**: IP to resolve all DNS queries to
- **-s | --hijack <URL>**: URL to look for in HTTP requests
- **eg**: *jquery*.js*
- **-r | --redirect <URL>**: URL to redirect to
- **-v | --verbose**: Verbose output
- **Use**: besside-ng-crawler <SearchDir> <CapFileOut>
- **-p**: Uses prng algorithm to generate IVs
- **[CMD] can be**: []
- **-v   <victim mac>**: Victim BSSID
- **-m      <src mac>**: Source MAC address
- **-i           <ip>**: Source IP address
- **-r    <router ip>**: Router IP address
- **-s     <buddy ip>**: Buddy-ng IP address (mandatory)
- **-f        <iface>**: Interface to use (mandatory)
- **-c      <channel>**: Lock card to this channel
- **-n**: Ignores weak IVs
- **-f <num>**: Number of first IV
- **-k <key>**: Target network WEP key in hex
- **-s <num>**: Seed used to setup random generator
- **-w <file>**: write packet to this pcap file
- **-c <num>**: Number of IVs to generate
- **-d <num>**: Percentage of dupe IVs
- **-e <num>**: Percentage of erroneous keystreams
- **-l <num>**: Length of keystreams
- **Forge packets**: ARP, UDP, ICMP or custom packets.
- **Forge options**: []
- **-p <fctrl>**: set frame control word (hex)
- **-a <bssid>**: set Access Point MAC address
- **-c <dmac>**: set Destination  MAC address
- **-h <smac>**: set Source       MAC address
- **-o**: clear ToDS bit
- **-e**: disables WEP encryption
- **-k <ip[**: port]> : set Destination IP [Port]
- **-l <ip[**: port]> : set Source      IP [Port]
- **-t ttl**: set Time To Live
- **-s <size>**: specify size of null packet
- **-n <packets>**: set number of packets to generate
- **-r <file>**: read packet from this raw file
- **-y <file>**: read PRGA from this file
- **Modes**: []
- **--arp**: forge an ARP packet    (-0)
- **--udp**: forge an UDP packet    (-1)
- **--icmp**: forge an ICMP packet   (-2)
- **--null**: build a null packet    (-3)
- **--custom**: build a custom packet  (-9)
- **-Z**: select packets manually
- **-M sec**: MIC error timeout in seconds [60]
- **Debug options**: []
- **-K prga**: keystream for continuation
- **-P pmk**: pmk for verification/vuln testing
- **-p psk**: psk to calculate pmk with essid
- **source options**: []
- **-i      <iface>**: Interface to use (mandatory)
- **-m      <my ip>**: My IP address
- **-n     <net ip>**: Network IP address
- **-a      <mymac>**: Source MAC Address
- **-p   <min prga>**: Minimum bytes of PRGA to gather
- **-v <victim mac>**: Victim BSSID
- **-t  <threshold>**: Cracking threshold
- **-f   <max chan>**: Highest scanned chan (default: 11)
- **-k      <txnum>**: Ignore acks and tx txnum times


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## aircrack-ng Usage Examples

### WPA Wordlist Mode

Specify the wordlist to use (`-w password.lst`) and the path to the capture file (`wpa.cap`) containing at least one 4-way handshake.

```console
root@kali:~# aircrack-ng -w password.lst wpa.cap

                               Aircrack-ng 1.5.2

      [00:00:00] 232/233 keys tested (1992.58 k/s)

      Time left: 0 seconds                                      99.57%

                           KEY FOUND! [ biscotte ]


      Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6
                       39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE

      Transient Key  : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49
                       73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08
                       AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97
                       D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD

      EAPOL HMAC     : 28 A8 C8 95 B7 17 E5 72 27 B6 A7 EE E3 E5 34 45
```

###  Basic WEP Cracking

To have aircrack-ng conduct a WEP key attack on a capture file, pass it the filename, either in .ivs or .cap/.pcap format:

```console
root@kali:~# aircrack-ng all-ivs.ivs
                                   Aircrack-ng 1.4


                   [00:00:00] Tested 1514 keys (got 30566 IVs)

   KB    depth   byte(vote)
    0    0/  9   1F(39680) 4E(38400) 14(37376) 5C(37376) 9D(37376)
    1    7/  9   64(36608) 3E(36352) 34(36096) 46(36096) BA(36096)
    2    0/  1   1F(46592) 6E(38400) 81(37376) 79(36864) AD(36864)
    3    0/  3   1F(40960) 15(38656) 7B(38400) BB(37888) 5C(37632)
    4    0/  7   1F(39168) 23(38144) 97(37120) 59(36608) 13(36352)

                         KEY FOUND! [ 1F:1F:1F:1F:1F ]
    Decrypted correctly: 100%
```

## airgraph-ng Usage Examples

### CAPR graph

Specify the input file to use (`-i dump-01.csv`), the output file to generate (`-o capr.png`) and the graph type (`-g CAPR`):

```console
root@kali:~# airgraph-ng -i dump-01.csv -o capr.png -g CAPR
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, capr.png
Depending on your system this can take a bit. Please standby......
```

### CPG graph

Specify the input file to use (`-i dump-01.csv`), the output file to generate (`-o cpg.png`) and the graph type (`-g CAG`):

```console
root@kali:~# airgraph-ng -i dump-01.csv -o cpg.png -g CPG
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, cpg.png
Depending on your system this can take a bit. Please standby......
```

## wpaclean Usage Example

Parse the provided capture files (`wpa-psk-linksys.cap wpa.cap`) and save any 4-way handshakes to a new file (`/root/handshakes.cap`):

```console
root@kali:/usr/share/doc/aircrack-ng/examples# wpaclean /root/handshakes.cap wpa-psk-linksys.cap wpa.cap
Pwning wpa-psk-linksys.cap (1/2 50%)
Net 00:0b:86:c2:a4:85 linksys
Pwning wpa.cap (2/2 100%)
Net 00:0d:93:eb:b0:8c test
Done
```

## wesside-ng Usage Example

Use the specified monitor mode interface (`-i wlan0mon`) and target a single BSSID (`-v de:ad:be:ef:ca:fe`):

```console
root@kali:~# wesside-ng -i wlan0mon -v de:ad:be:ef:ca:fe
[18:31:52] Using mac 3C:46:D8:4E:EF:AA
[18:31:52] Looking for a victim...
[18:32:13] Chan 04 -
```

## makeivs-ng Usage Example

Specify a BSSID (`-b de:ad:be:ef:ca:fe`), WEP key (`-k 123456789ABCDEF123456789AB`), and output filename (`-w makeivs.ivs`):

```console
root@kali:~# makeivs-ng -b de:ad:be:ef:ca:fe -k 123456789ABCDEF123456789AB -w makeivs.ivs
Creating 100000 IVs with 16 bytes of keystream each.
Estimated filesize: 2.29 MB
Using fake BSSID DE:AD:BE:EF:CA:FE
Done.
```

```console
root@kali:~# aircrack-ng makeivs.ivs
Opening makeivs.ivs
Read 100001 packets.

   #  BSSID              ESSID                     Encryption

   1  DE:AD:BE:EF:CA:FE                            WEP (100000 IVs)

Choosing first network as target.

Opening makeivs.ivs
Attack will be restarted every 5000 captured ivs.
Starting PTW attack with 100000 ivs.


                                   Aircrack-ng 1.2 rc4


                   [00:00:00] Tested 621 keys (got 100000 IVs)

   KB    depth   byte(vote)
    0    1/  2   76(113152) 1E(111104) 48(109824) 1C(109568) A6(109568)
    1    1/  3   F5(112640) 06(111616) 33(111616) F4(111616) 05(111104)
    2    0/  2   31(137216) F9(113664) 76(113152) DC(110336) B9(109568)
    3   10/  3   E1(108800) 0A(108544) 34(108032) 3E(108032) 48(108032)
    4    9/  4   7D(109312) BA(109056) 5E(108800) D6(108800) 11(108288)

             KEY FOUND! [ 12:34:56:78:9A:BC:DE:F1:23:45:67:89:AB ]
    Decrypted correctly: 100%
```

## ivstools Usage Examples

Strip out the initialization vectors of the provided .pcap capture and save them to a new file:

```console
root@kali:~# ivstools --convert wep_64_ptw.cap out.ivs
Opening wep_64_ptw.cap
Creating out.ivs
Read 65282 packets.
Written 30566 IVs.
Merge all .ivs files into one file.
```

```console
root@kali:~# ivstools --merge *.ivs /root/all-ivs.ivs
Creating /root/all-ivs.ivs
Opening out.ivs
916996 bytes written
Opening out2.ivs
1374748 bytes written
```

## easside-ng Usage Example

First, run buddy-ng, then launch the Easside-ng attack, specifying as many of the options as you can.

```console
root@kali:~# buddy-ng
Waiting for connexion
```

```console
root@kali:~# easside-ng -v de:ad:be:ef:ca:fe -m 3c:46:d8:4e:ef:aa -s 127.0.0.1 -f wlan0mon -c 6
Setting tap MTU
Sorting out wifi MAC
```

## besside-ng

Attack WPA only (`-W`), display verbose output (`-v`) and use monitor mode interface `wlan0mon`.

```console
root@kali:~# besside-ng -W -v wlan0mon
[18:39:34] mac 3c:46:d8:4e:ef:aa
[18:39:34] Let's ride
[18:39:34] Appending to wpa.cap
[18:39:34] Appending to wep.cap
[18:39:34] Logging to besside.log
[18:39:35] Found AP 44:3a:cb:38:51:42 [watwutwot] chan 1 crypto WPA dbm -49
[18:39:35] Found AP 4c:8b:30:83:ed:91 [TELUS3079-2.4G] chan 1 crypto WPA dbm -71
[18:39:35] Found AP 1c:87:2c:d3:34:18 [Kuroki] chan 3 crypto WPA dbm -89
[18:39:37] Found AP 4c:8b:30:24:71:75 [SAMUEL9] chan 8 crypto WPA dbm -73
[18:39:37] Found AP 0c:51:01:e6:01:c4 [fbi-van-24] chan 11 crypto WPA dbm -46
[18:39:37] Found AP 70:f1:96:8e:5c:02 [TELUS0455-2.4G] chan 11 crypto WPA dbm -78
[18:39:38] Found client for network [Kuroki] 90:06:28:cb:0f:f3
[18:39:41] Found AP f0:f2:49:3c:ec:a8 [fbi-van-24] chan 1 crypto WPA dbm -49
[18:39:42] Found AP bc:4d:fb:2c:6d:88 [SHAW-2C6D80] chan 6 crypto WPA dbm -77
[18:39:42] Found client for network [SHAW-2C6D80] 64:5a:04:98:e1:62
[18:39:43] Found AP 10:78:5b:e9:a4:e2 [TELUS2151] chan 11 crypto WPA dbm -49
[18:39:43] Found client for network [fbi-van-24] 60:6b:bd:5a:b6:6c
```

## airtun-ng Usage Examples

### wIDS

Specify the BSSID of the access point you wish to monitor (`-a DE:AD:BE:EF:CA:FE`) and its WEP key (`-w 1234567890`).

```console
root@kali:~# airtun-ng -a DE:AD:BE:EF:CA:FE -w 1234567890 wlan0mon
created tap interface at0
WEP encryption specified. Sending and receiving frames through wlan0mon.
FromDS bit set in all frames.
```

## airserv-ng Usage Example

Start a server instance on a specific port (`-p 4444`) using the `wlan0mon` interface on channel 6 (`-c 6`).

```console
root@kali:~# airserv-ng -p 4444 -d wlan0mon -c 6
Opening card wlan0mon
Setting chan 6
Opening sock port 4444
Serving wlan0mon chan 6 on port 4444
```

## airolib-ng Usage Examples

Specify the name of the database to use (`airolib-db`) and import a file containing the ESSIDs of the network(s) you are targeting (`–import essid /root/essid.txt`). If the database does not exist, it will be created.

```console
root@kali:~# airolib-ng airolib-db --import essid /root/essid.txt
Database <airolib-db> does not already exist, creating it...
Database <airolib-db> successfully created
Reading file...
Writing...
Done.
```


Import any wordlists you wish to use for PMK computation.

```console
root@kali:~# airolib-ng airolib-db --import passwd /usr/share/doc/aircrack-ng/examples/password.lst
Reading file...
Writing... read, 1814 invalid lines ignored.
Done
```

Use the `–batch` to compute all PMKs.

```console
root@kali:~# airolib-ng airolib-db --batch
Computed 233 PMK in 0 seconds (233 PMK/s, 0 in buffer). All ESSID processed.
```

To use the airolib-ng database with aircrack-ng, use the `-r` option and specify the database name.

```console
root@kali:~# aircrack-ng -r airolib-db /root/wpa.cap
Opening /root/wpa.cap
Read 13 packets.

   #  BSSID              ESSID                     Encryption

   1  00:0D:93:EB:B0:8C  test                      WPA (1 handshake)

Choosing first network as target.

Opening /root/wpa.cap
Reading packets, please wait...

                                 Aircrack-ng 1.4

      [00:00:00] 230/0 keys tested (106728.53 k/s)

      Time left: 0 seconds                                   inf%

                           KEY FOUND! [ biscotte ]


      Master Key     : CD D7 9A 5A CF B0 70 C7 E9 D1 02 3B 87 02 85 D6
                       39 E4 30 B3 2F 31 AA 37 AC 82 5A 55 B5 55 24 EE

      Transient Key  : 33 55 0B FC 4F 24 84 F4 9A 38 B3 D0 89 83 D2 49
                       73 F9 DE 89 67 A6 6D 2B 8E 46 2C 07 47 6A CE 08
                       AD FB 65 D6 13 A9 9F 2C 65 E4 A6 08 F2 5A 67 97
                       D9 6F 76 5B 8C D3 DF 13 2F BC DA 6A 6E D9 62 CD

      EAPOL HMAC     : 28 A8 C8 95 B7 17 E5 72 27 B6 A7 EE E3 E5 34 45


Quitting aircrack-ng...
```

## airodump-ng Usage Examples

Monitor all wireless networks, frequency hopping between all wireless channels.

```console
root@kali:~# airodump-ng wlan0mon

CH  8 ][ Elapsed: 4 s ][ 2018-11-22 13:44

BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID

54:A0:50:DA:7B:98  -76        1        0    0   1  54e  WPA2 CCMP   PSK  RTINC-24
FC:15:B4:CF:0A:55  -70        2        0    0   6  54e. WPA2 CCMP   PSK  HP-Print-55-ENVY 4500 series
A8:4E:3F:73:DD:88  -67        3        0    0   6  720  WPA2 CCMP   PSK  WAT-73DD80
4C:8B:30:83:ED:91  -71        2        0    0   1  54e  WPA2 CCMP   PSK  TELL-US-2.4G
4C:8B:30:D7:09:41  -76        2        0    0   1  54e  WPA2 CCMP   PSK  SAMUELL-2.4G
FA:8F:CA:89:90:39  -82        2        0    0   1  135  OPN              Raymond's TV.e102
AC:20:2E:CD:F4:88  -85        0        0    0   6  54e. WPA2 CCMP   PSK  BELL-CDF480
10:78:5B:2A:A1:21  -80        2        0    0   6  54e  WPA2 CCMP   PSK  COGECO-2.4G

BSSID              STATION            PWR   Rate    Lost    Frames  Probe

(not associated)   8C:85:90:0C:C5:D0  -44    0 - 1      1        5
(not associated)   A0:63:91:43:C2:D5  -70    0 - 1      0        1  TT-D59979
(not associated)   14:91:82:04:D9:74  -43    0 - 1      0        1  1
```

Sniff on channel 6 (-c 6) via monitor mode interface wlan0mon and save the capture to a file (-w /root/chan6).

```console
root@kali:~# airodump-ng -c 6 -w /root/chan6 wlan0mon

CH  6 ][ Elapsed: 8 s ][ 2017-11-12 13:49

BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID

BC:4D:FB:2C:6D:88  -68  28        9        3    0   6  54e. WPA2 CCMP   PSK  BELL-CDF4800
A8:4E:3F:73:DD:88  -74  33       19        0    0   6  54e. WPA2 CCMP   PSK  COGECO-2.4G
FC:15:B4:CF:0A:55  -77  61       31        0    0   6  54e. WPA2 CCMP   PSK  HP-Print-55-ENVY 4500 series
```

Filter for access points by a specific manufacturer, specifying the OUI and mask (-d FC:15:B4:00:00:00 -m FF:FF:FF:00:00:00).

```console
root@kali:~# airodump-ng -d FC:15:B4:00:00:00 -m FF:FF:FF:00:00:00 wlan0mon

CH 14 ][ Elapsed: 18 s ][ 2018-11-22 13:53

BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID

FC:15:B4:CF:0A:55  -76        9        0    0   6  54e. WPA2 CCMP   PSK  HP-Print-55-ENVY 4500 series

BSSID              STATION            PWR   Rate    Lost    Frames  Probe
```

## airodump-ng-oui-update Usage Example

airodump-ng-oui-update does not have any options. Run the command and wait for it to complete.

```console
root@kali:~# airodump-ng-oui-update
/usr/sbin/update-ieee-data
Updating /var/lib/ieee-data//oui.txt
    Checking permissions on /var/lib/ieee-data//oui.txt
    Downloading https://standards.ieee.org/develop/regauth/oui/oui.txt to /var/lib/ieee-data//oui.txt
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//oui.txt
    /var/lib/ieee-data//oui.txt updated.
Updating /var/lib/ieee-data//mam.txt
    Checking permissions on /var/lib/ieee-data//mam.txt
    Downloading https://standards.ieee.org/develop/regauth/oui28/mam.txt to /var/lib/ieee-data//mam.txt
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//mam.txt
    /var/lib/ieee-data//mam.txt updated.
Updating /var/lib/ieee-data//oui36.txt
    Checking permissions on /var/lib/ieee-data//oui36.txt
    Downloading https://standards.ieee.org/develop/regauth/oui36/oui36.txt to /var/lib/ieee-data//oui36.txt
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//oui36.txt
    /var/lib/ieee-data//oui36.txt updated.
Updating /var/lib/ieee-data//iab.txt
    Checking permissions on /var/lib/ieee-data//iab.txt
    Downloading https://standards.ieee.org/develop/regauth/iab/iab.txt to /var/lib/ieee-data//iab.txt
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//iab.txt
    /var/lib/ieee-data//iab.txt updated.
Updating /var/lib/ieee-data//oui.csv
    Checking permissions on /var/lib/ieee-data//oui.csv
    Downloading https://standards.ieee.org/develop/regauth/oui/oui.csv to /var/lib/ieee-data//oui.csv
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//oui.csv
    /var/lib/ieee-data//oui.csv updated.
Updating /var/lib/ieee-data//mam.csv
    Checking permissions on /var/lib/ieee-data//mam.csv
    Downloading https://standards.ieee.org/develop/regauth/oui28/mam.csv to /var/lib/ieee-data//mam.csv
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//mam.csv
    /var/lib/ieee-data//mam.csv updated.
Updating /var/lib/ieee-data//oui36.csv
    Checking permissions on /var/lib/ieee-data//oui36.csv
    Downloading https://standards.ieee.org/develop/regauth/oui36/oui36.csv to /var/lib/ieee-data//oui36.csv
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//oui36.csv
    /var/lib/ieee-data//oui36.csv updated.
Updating /var/lib/ieee-data//iab.csv
    Checking permissions on /var/lib/ieee-data//iab.csv
    Downloading https://standards.ieee.org/develop/regauth/iab/iab.csv to /var/lib/ieee-data//iab.csv
    Checking header
    Temporary location /tmp/ieee-data_y1vJ3E to be moved to /var/lib/ieee-data//iab.csv
    /var/lib/ieee-data//iab.csv updated.
    Running parsers from /var/lib/ieee-data//update.d
```

## airmon-ng Usage Examples

Entering the airmon-ng command without parameters will show the interfaces status.

```console
root@kali:~# airmon-ng

PHY Interface   Driver      Chipset

phy0    wlan0       ath9k_htc   Atheros Communications, Inc. AR9271 802.11n
```

A number of processes can interfere with Airmon-ng. Using the **check** option will display any processes that might be troublesome and the **check kill** option will kill them for you.

```console
root@kali:~# airmon-ng check

Found 3 processes that could cause trouble.
If airodump-ng, aireplay-ng or airtun-ng stops working after
a short period of time, you may want to run 'airmon-ng check kill'

   PID Name
   465 NetworkManager
   515 dhclient
  1321 wpa_supplicant

root@kali:~# airmon-ng check kill

Killing these processes:

   PID Name
   515 dhclient
  1321 wpa_supplicant
```


Enable monitor mode (start) on the given wireless interface (`wlan0`), fixed on channel `6`. A new interface will be created (`wlan0mon` in our case), which is the interface name you will need to use in other applications.

```console
root@kali:~# airmon-ng start wlan0 6


PHY Interface   Driver      Chipset

phy0    wlan0       ath9k_htc   Atheros Communications, Inc. AR9271 802.11n

        (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
        (mac80211 station mode vif disabled for [phy0]wlan0)
```

The **stop** option will destroy the monitor mode interface and place the wireless interface back into managed mode.

```console
root@kali:~# airmon-ng stop wlan0mon

PHY Interface   Driver      Chipset

phy0    wlan0mon    ath9k_htc   Atheros Communications, Inc. AR9271 802.11n

        (mac80211 station mode vif enabled on [phy0]wlan0)

        (mac80211 monitor mode vif disabled for [phy0]wlan0mon)
```

## airgraph-ng Usage Examples

### CAPR graph

Specify the input file to use (`-i dump-01.csv`), the output file to generate (`-o capr.png`) and the graph type (`-g CAPR`).

```console
root@kali:~# airgraph-ng -i dump-01.csv -o capr.png -g CAPR
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, capr.png
Depending on your system this can take a bit. Please standby......
```

### CPG graph

Specify the input file to use (`-i dump-01.csv`), the output file to generate (`-o cpg.png`) and the graph type (`-g CAG`).

```console
root@kali:~# airgraph-ng -i dump-01.csv -o cpg.png -g CPG
**** WARNING Images can be large, up to 12 Feet by 12 Feet****
Creating your Graph using, dump-01.csv and writing to, cpg.png
Depending on your system this can take a bit. Please standby......
```

## aireplay-ng Usage Examples

### Injection Test

Run the injection test (`-9`) via the monitor mode interface `wlan0mon`.

```console
root@kali:~# aireplay-ng -9 wlan0mon
22:55:44  Trying broadcast probe requests...
22:55:44  Injection is working!
22:55:46  Found 4 APs

22:55:46  Trying directed probe requests...
22:55:46  24:FB:95:FD:3D:7F - channel: 6 - 'America'
22:55:52   30/30: 100%

22:55:52  34:6D:A0:CD:45:10 - channel: 6 - 'ATT2b8i4UD'
22:55:58   27/30:  90%

22:55:58  50:64:3D:2A:F7:A0 - channel: 6 - 'FBI surveillance van'
22:56:04   12/30:  40%

22:56:04  16:6E:EF:29:67:46 - channel: 6 - 'dd-wrt_vap'
22:56:10   1/30:   3%
```

### Deauthentication Attack

Run the deauthentication attack (`-0`), sending `5` packets to the wireless access point (`-a 8C:7F:3B:7E:81:B6`) to deauthenticate a wireless client (`-c 00:08:22:B9:41:A1`) via the monitor mode interface `wlan0mon`.

```console
root@kali:~# aireplay-ng -0 5 -a 8C:7F:3B:7E:81:B6 -c 00:08:22:B9:41:A1 wlan0mon
12:41:56  Waiting for beacon frame (BSSID: 8C:7F:3B:7E:81:B6) on channel 6
12:41:57  Sending 64 directed DeAuth. STMAC: [00:08:22:B9:41:A1] [ 0| 0 ACKs]
12:41:58  Sending 64 directed DeAuth. STMAC: [00:08:22:B9:41:A1] [ 0| 0 ACKs]
12:41:58  Sending 64 directed DeAuth. STMAC: [00:08:22:B9:41:A1] [ 0| 0 ACKs]
12:41:59  Sending 64 directed DeAuth. STMAC: [00:08:22:B9:41:A1] [ 0| 0 ACKs]
12:42:00  Sending 64 directed DeAuth. STMAC: [00:08:22:B9:41:A1] [ 0| 0 ACKs]
```

### Fake Authentication

Run the fake authentication attack and re-authenticate every 6000 seconds (`-1 6000`) against the access point (`-a F0:F2:49:82:DF:3B`) with the given ESSID (`-e FBI-Van-24`), specifying our mac address (`-h 3c:46:d8:4e:ef:aa`), using monitor mode interface `wlan0mon`.

```console
root@kali:~# aireplay-ng -1 6000 -e FBI-Van-24 -a F0:F2:49:82:DF:3B -h 3c:46:d8:4e:ef:aa wlan0mon
12:49:59  Waiting for beacon frame (BSSID: F0:F2:49:82:DF:3B) on channel 6

12:50:06  Sending Authentication Request (Open System)
```

## airbase-ng Usage Examples

### Hirte Attack – Access Point Mode

The Hirte attack attempts to retrieve a WEP key via a client. This example creates an access point on channel 6 (`-c 6`) with the specified ESSID (`-e TotallyNotATrap`) and uses the cfrag WEP attack (`-N`), setting the WEP flag in the beacons (`-W 1`).

```console
root@kali:~# root@kali:~# airbase-ng -c 6 -e TotallyNotATrap -N -W 1 wlan0mon
15:51:11  Created tap interface at0
15:51:11  Trying to set MTU on at0 to 1500
15:51:11  Trying to set MTU on wlan0mon to 1800
15:51:11  Access Point with BSSID 3C:46:D8:4E:EF:AA started.
```

### Caffe Latte Attack – Access Point Mode

As with the Hirte attack, the Caffe Latte Attack attempts to retrieve a WEP key via a client. This example creates an access point on channel 6 (`-c 6`) with the specified ESSID (`-e AlsoNotATrap`) and uses the Caffe Latte WEP attack (`-L`), setting the WEP flag in the beacons (`-W 1`).

```console
root@kali:~# airbase-ng -c 6 -e AlsoNotATrap -L -W 1 wlan0mon
15:56:05  Created tap interface at0
15:56:05  Trying to set MTU on at0 to 1500
15:56:05  Access Point with BSSID 3C:46:D8:4E:EF:AA started.
```

## airdecap-ng

With a given ESSID (`-e test`) and password (`-p biscotte`), decrypt the specified WPA capture (`-r /usr/share/doc/aircrack-ng/examples/wpa.cap`).

```console
root@kali:~# tcpdump -r wpa.cap
reading from file wpa.cap, link-type PRISM_HEADER (802.11 plus Prism header)
03:01:06.609737 Beacon (test) [1.0* 2.0* 5.5* 11.0* Mbit] ESS CH: 7, PRIVACY[|802.11]
03:01:06.678714 EAPOL key (3) v1, len 95
03:01:06.678928 Acknowledgment RA:00:0d:93:eb:b0:8c (oui Unknown)
03:01:06.681525 EAPOL key (3) v1, len 119
03:01:06.681732 Acknowledgment RA:00:09:5b:91:53:5d (oui Unknown)
03:01:06.684370 EAPOL key (3) v1, len 119
03:01:06.684584 Acknowledgment RA:00:0d:93:eb:b0:8c (oui Unknown)
03:01:06.685502 EAPOL key (3) v1, len 95
03:01:06.685708 Acknowledgment RA:00:09:5b:91:53:5d (oui Unknown)
03:01:06.686775 Data IV:12000 Pad 20 KeyID 0
03:01:06.686984 Acknowledgment RA:00:0d:93:eb:b0:8c (oui Unknown)
03:01:06.688139 Data IV:12000 Pad 20 KeyID 0
03:01:06.688344 Acknowledgment RA:00:09:5b:91:53:5d (oui Unknown)
```

```console
root@kali:~# airdecap-ng -e test -p biscotte wpa.cap
Total number of packets read            13
Total number of WEP data packets         0
Total number of WPA data packets         2
Number of plaintext data packets         0
Number of decrypted WEP  packets         0
Number of corrupted WEP  packets         0
Number of decrypted WPA  packets         2
```

```console
root@kali:~# tcpdump -r wpa-dec.cap
reading from file wpa-dec.cap, link-type EN10MB (Ethernet)
03:01:06.686775 EAPOL key (3) v1, len 127
03:01:06.688139 EAPOL key (3) v1, len 95
```


## Source
- Path: kali-tools\aircrack-ng\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.777604
