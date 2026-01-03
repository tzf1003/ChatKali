---
tool_id: sipp
title: sipp
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://sipp.sourceforge.net/
repository: 
version: 3.3-1kali6
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\sipp\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.107973
---

# Tool: sipp (sipp)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://sipp.sourceforge.net/](https://sipp.sourceforge.net/) |
| Repository |  |
| Version | 3.3-1kali6 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything kali-linux-large kali-tools-voip kali-tools-vulnerability |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/sipp
- **PackagesInfo**: |
- ****Installed size**: ** `735 KB`
- ****How to install**: ** `sudo apt install sipp`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# sipp -h
- **Usage**: []
- **sipp remote_host[**: remote_port] [options]
- **Available options**: []
- **-v**: Display version and copyright information.
- **-aa**: Enable automatic 200 OK answer for INFO, UPDATE and
- **-auth_uri**: Force the value of the URI for authentication.
- **remote_ip**: remote_port.
- **-au**: Set authorization username for authentication challenges.
- **-ap**: Set the password for authentication challenges. Default
- **-base_cseq**: Start value of [cseq] for each call.
- **-bg**: Launch SIPp in background mode.
- **-bind_local**: Bind socket to local IP address, i.e. the local IP
- **-buff_size**: Set the send and receive buffer size.
- **-calldebug_file**: Set the name of the call debug file.
- **-calldebug_overwrite**: Overwrite the call debug file (default true).
- **-cid_str**: Call ID string (default %u-%p@%s).  %u=call_number,
- **-ci**: Set the local control IP address
- **-cp**: Set the local control port number. Default is 8888.
- **-d**: Controls the length of calls. More precisely, this
- **-deadcall_wait**: How long the Call-ID and final status of calls should be
- **-default_behaviors**: Set the default behaviors that SIPp will use.  Possbile
- **values are**: ['all\tUse all default behaviors', 'none\tUse no default behaviors', 'bye\tSend byes for aborted calls', 'abortunexp\tAbort calls on unexpected messages', 'pingreply\tReply to ping requests']
- **off.  Example**: all,-bye
- **-error_file**: Set the name of the error log file.
- **-error_overwrite**: Overwrite the error log file (default true).
- **-f**: Set the statistics report frequency on screen. Default is
- **-fd**: Set the statistics dump log report frequency. Default is
- **-i**: Set the local IP address for 'Contact:','Via:', and
- **'From**: ' headers. Default is primary host IP address.
- **-inf**: Inject values from an external CSV file during calls into
- **Several CSV files can be used simultaneously (syntax**: []
- **-infindex**: file field
- **-ip_field**: Set which field from the injection file contains the IP
- **-l**: Set the maximum number of simultaneous calls. Once this
- **of open calls goes down. Default**: []
- **-log_file**: Set the name of the log actions log file.
- **-log_overwrite**: Overwrite the log actions log file (default true).
- **-lost**: Set the number of packets to lose by default (scenario
- **-rtcheck**: Select the retransmisison detection method: full
- **-m**: Stop the test and exit when 'calls' calls are processed
- **-mi**: Set the local media IP address (default: local primary
- **-master**: 3pcc extended mode: indicates the master number
- **-max_recv_loops**: Set the maximum number of messages received read per
- **-max_sched_loops**: Set the maximum number of calsl run per event loop.
- **-max_reconnect**: Set the the maximum number of reconnection.
- **-max_retrans**: Maximum number of UDP retransmissions before call ends on
- **-max_invite_retrans**: Maximum number of UDP retransmissions for invite
- **-max_non_invite_retrans**: Maximum number of UDP retransmissions for non-invite
- **-max_log_size**: What is the limit for error and message log file sizes.
- **-max_socket**: Set the max number of sockets to open simultaneously.
- **-mb**: Set the RTP echo buffer size (default: 2048).
- **-message_file**: Set the name of the message log file.
- **-message_overwrite**: Overwrite the message log file (default true).
- **-mp**: Set the local RTP echo port number. Default is 6000.
- **-nd**: No Default. Disable all default behavior of SIPp which
- **are the following**: ['On UDP retransmission timeout, abort the call by']
- **-nr**: Disable retransmission in UDP mode.
- **-nostdin**: Disable stdin.
- **-p**: Set the local port number.  Default is a random free port
- **-pause_msg_ign**: Ignore the messages received during a pause defined in
- **-periodic_rtd**: Reset response time partition counters each logging
- **-plugin**: Load a plugin.
- **-r**: Set the call rate (in calls per seconds).  This value can
- **-rp**: Specify the rate period for the call rate.  Default is 1
- **Example**: []
- **-rate_scale**: Control the units for the '+', '-', '*', and '/' keys.
- **-rate_increase**: Specify the rate increase every -fd units (default is
- **-rate_max**: If -rate_increase is set, then quit after the rate
- **-no_rate_quit**: If -rate_increase is set, do not quit after the rate
- **-recv_timeout**: Global receive timeout. Default unit is milliseconds. If
- **-send_timeout**: Global send timeout. Default unit is milliseconds. If a
- **-sleep**: How long to sleep for at startup. Default unit is
- **-reconnect_close**: Should calls be closed on reconnect?
- **-reconnect_sleep**: How long (in milliseconds) to sleep between the close and
- **-ringbuffer_files**: How many error/message files should be kept after
- **-ringbuffer_size**: How large should error/message files be before they get
- **-rsa**: Set the remote sending address to host:port for sending
- **-rtp_echo**: Enable RTP echo. RTP/UDP packets received on port defined
- **-rtt_freq**: freq is mandatory. Dump response times every freq calls
- **-s**: Set the username part of the resquest URI. Default is
- **-sd**: Dumps a default scenario (embeded in the sipp executable)
- **-sf**: Loads an alternate xml scenario file.  To learn more
- **-shortmessage_file**: Set the name of the short message log file.
- **-shortmessage_overwrite**: Overwrite the short message log file (default true).
- **-oocsf**: Load out-of-call scenario.
- **-oocsn**: Load out-of-call scenario.
- **-skip_rlimit**: Do not perform rlimit tuning of file descriptor limits.
- **Default**: false.
- **-slave**: 3pcc extended mode: indicates the slave number
- **-slave_cfg**: 3pcc extended mode: indicates the file where the master
- **-sn**: Use a default scenario (embedded in the sipp executable).
- **Available values in this version**: ["'uac'      : Standard SipStone UAC (default).", "'uas'      : Simple UAS responder.", "'regexp'   : Standard SipStone UAC - with regexp and"]
- **Default 3pcc scenarios (see -3pcc option)**: ["'3pcc-C-A' : Controller A side (must be started after"]
- **-stat_delimiter**: Set the delimiter for the statistics file
- **-stf**: Set the file name to use to dump statistics
- **-t**: Set the transport mode:
- **-timeout**: Global timeout. Default unit is seconds.  If this option
- **-timeout_error**: SIPp fails if the global timeout is reached is set
- **-timer_resol**: Set the timer resolution. Default unit is milliseconds.
- **-T2**: Global T2-timer in milli seconds
- **-sendbuffer_warn**: Produce warnings instead of errors on SendBuffer
- **-trace_msg**: Displays sent and received SIP messages in <scenario file
- **-trace_shortmsg**: Displays sent and received SIP messages as CSV in
- **-trace_screen**: Dump statistic screens in the
- **-trace_err**: Trace all unexpected messages in <scenario file
- **-trace_calldebug**: Dumps debugging information about aborted calls to
- **-trace_stat**: Dumps all statistics in <scenario_name>_<pid>.csv file.
- **-trace_counts**: Dumps individual message counts in a CSV file.
- **-trace_rtt**: Allow tracing of all response times in <scenario file
- **-trace_logs**: Allow tracing of <log> actions in <scenario file
- **-users**: Instead of starting calls at a fixed rate, begin 'users'
- **-watchdog_interval**: Set gap between watchdog timer firings.  Default is 400.
- **-watchdog_reset**: If the watchdog timer has not fired in more than this
- **-watchdog_minor_threshold**: If it has been longer than this period between watchdog
- **-watchdog_major_threshold**: If it has been longer than this period between watchdog
- **-watchdog_major_maxtriggers**: How many times the major watchdog timer can be tripped
- **-watchdog_minor_maxtriggers**: How many times the minor watchdog timer can be tripped
- **-3pcc**: Launch the tool in 3pcc mode ("Third Party call
- **connect to this address**: port to send the twin command
- **this address**: port to listen for twin command.
- **-tdmmap**: Generate and handle a table of TDM circuits.
- **Format**: -tdmmap {0-3}{99}{5-8}{1-31}
- **-key**: keyword value
- **-set**: variable value
- **-dynamicStart**: variable value
- **-dynamicMax**: variable value
- **-dynamicStep**: variable value
- **Signal handling**: []
- **are handled**: []
- **USR1**: Similar to press 'q' keyboard key. It triggers a soft exit
- **USR2**: Triggers a dump of all statistics screens in
- **Exit code**: []
- **code**: []
- **0**: All calls were successful
- **1**: At least one call failed
- **97**: exit on internal command. Calls may have been processed
- **99**: Normal exit without calls processed
- **-1**: Fatal error
- **-2**: Fatal error binding a socket
- **Run sipp with embedded server (uas) scenario**: []


## Documentation (Upstream)

{{% hidden-comment "<!--Do not edit anything above this line-->" %}}

## sipp Usage Example

Run sipp using the embedded server (`-sn uas`) scenario:

```console
root@kali:~# sipp -sn uas
Warning: open file limit > FD_SETSIZE; limiting max. # of open files to FD_SETSIZE = 1024
------------------------------ Scenario Screen -------- [1-9]: Change Screen --
  Port   Total-time  Total-calls  Transport
  5060      11.94 s            0  UDP

  0 new calls during 0.926 s period      1 ms scheduler resolution
  0 calls                                Peak was 0 calls, after 0 s
  0 Running, 2 Paused, 2 Woken up
  0 dead call msg (discarded)
  3 open sockets

                                 Messages  Retrans   Timeout   Unexpected-Msg
  ----------> INVITE             0         0         0         0

  <---------- 180                0         0
  <---------- 200                0         0         0
  ----------> ACK         E-RTD1 0         0         0         0

  ----------> BYE                0         0         0         0
  <---------- 200                0         0
  [   4000ms] Pause              0                             0
```


## Source
- Path: kali-tools\sipp\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.107973
