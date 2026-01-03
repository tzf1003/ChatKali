---
tool_id: pocsuite3
title: pocsuite3
categories: ["vulnerability-analysis", "exploitation-tools", "web-application-analysis"]
category_slugs: ["vulnerability-analysis", "exploitation-tools", "web-application-analysis"]
homepage: https://pocsuite.org
repository: 
version: 2.1.0-1
architectures: all
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\pocsuite3\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:07.052816
---

# Tool: pocsuite3 (pocsuite3)

## Categories
- [vulnerability-analysis](../vulnerability-analysis.md)
- [exploitation-tools](../exploitation-tools.md)
- [web-application-analysis](../web-application-analysis.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://pocsuite.org](https://pocsuite.org) |
| Repository |  |
| Version | 2.1.0-1 |
| Architectures | all |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://salsa.debian.org/pkg-security-team/pocsuite3
- **PackagesInfo**: |
- ****Installed size**: ** `943 KB`
- ****How to install**: ** `sudo apt install pocsuite3`
- **{{< spoiler "Dependencies**: " >}}
- **root@kali**: ~# pocsuite -h
- **The full documentation for pocsuite3 is maintained at**: []
- **https**: //pocsuite.org


## Documentation (Upstream)
---.                        ,--. ,--.       ,----.   {2.1.0-e389ecf}
 |  .--. ',---. ,---.,---.,--.,--`--,-'  '-.,---.'.-.  |
 |  '--' | .-. | .--(  .-'|  ||  ,--'-.  .-| .-. : .' <
 |  | --'' '-' \ `--.-'  `'  ''  |  | |  | \   --/'-'  |
 `--'     `---' `---`----' `----'`--' `--'  `----`----'   https://pocsuite.org
 usage: pocsuite [options]
 
 options:
   -h, --help            show this help message and exit
   --version             Show program's version number and exit
   --update              Update Pocsuite3
   -n, --new             Create a PoC template
   -v {0,1,2,3,4,5,6}    Verbosity level: 0-6 (default 1)
 
 Target:
   At least one of these options has to be provided to define the target(s)
 
   -u, --url URL [URL ...]
                         Target URL/CIDR (e.g.
                         "http://www.site.com/vuln.php?id=1")
   -f, --file URL_FILE   Scan multiple targets given in a textual file (one per
                         line)
   -p, --ports PORTS     add additional port to each target ([proto:]port, e.g.
                         8080,https:10000)
   -s                    Skip target's port, only use additional port
   -r POC [POC ...]      Load PoC file from local or remote from seebug website
   -k POC_KEYWORD        Filter PoC by keyword, e.g. ecshop
   -c CONFIGFILE         Load options from a configuration INI file
   -l                    Show all PoC file from local
 
 Mode:
   Pocsuite running mode options
 
   --verify              Run poc with verify mode
   --attack              Run poc with attack mode
   --shell               Run poc with shell mode
 
 Request:
   Network request options
 
   --cookie COOKIE       HTTP Cookie header value
   --host HOST           HTTP Host header value
   --referer REFERER     HTTP Referer header value
   --user-agent AGENT    HTTP User-Agent header value (default random)
   --proxy PROXY         Use a proxy to connect to the target URL
                         (protocol://host:port)
   --proxy-cred PROXY_CRED
                         Proxy authentication credentials (name:password)
   --timeout TIMEOUT     Seconds to wait before timeout connection (default 10)
   --retry RETRY         Time out retrials times (default 0)
   --delay DELAY         Delay between two request of one thread
   --headers HEADERS     Extra headers (e.g. "key1: value1\nkey2: value2")
   --http-debug HTTP_DEBUG
                         HTTP debug level (default 0)
   --session-reuse       Enable requests session reuse
   --session-reuse-num REQUESTS_SESSION_REUSE_NUM
                         Requests session reuse number
 
 Account:
   Account options
 
   --ceye-token CEYE_TOKEN
                         CEye token
   --oob-server OOB_SERVER
                         Interactsh server to use (default "interact.sh")
   --oob-token OOB_TOKEN
                         Authentication token to connect protected interactsh
                         server
   --seebug-token SEEBUG_TOKEN
                         Seebug token
   --zoomeye-token ZOOMEYE_TOKEN
                         ZoomEye token
   --shodan-token SHODAN_TOKEN
                         Shodan token
   --fofa-user FOFA_USER
                         Fofa user
   --fofa-token FOFA_TOKEN
                         Fofa token
   --quake-token QUAKE_TOKEN
                         Quake token
   --hunter-token HUNTER_TOKEN
                         Hunter token
   --censys-uid CENSYS_UID
                         Censys uid
   --censys-secret CENSYS_SECRET
                         Censys secret
 
 Modules:
   Modules options
 
   --dork DORK           Zoomeye dork used for search
   --dork-zoomeye DORK_ZOOMEYE
                         Zoomeye dork used for search
   --dork-shodan DORK_SHODAN
                         Shodan dork used for search
   --dork-fofa DORK_FOFA
                         Fofa dork used for search
   --dork-quake DORK_QUAKE
                         Quake dork used for search
   --dork-hunter DORK_HUNTER
                         Hunter dork used for search
   --dork-censys DORK_CENSYS
                         Censys dork used for search
   --max-page MAX_PAGE   Max page used in search API
   --page-size PAGE_SIZE
                         Page size used in search API
   --search-type SEARCH_TYPE
                         search type used in search API, v4,v6 and web
   --vul-keyword VUL_KEYWORD
                         Seebug keyword used for search
   --ssv-id SSVID        Seebug SSVID number for target PoC
   --lhost CONNECT_BACK_HOST
                         Connect back host for target PoC in shell mode
   --lport CONNECT_BACK_PORT
                         Connect back port for target PoC in shell mode
   --tls                 Enable TLS listener in shell mode
   --comparison          Compare popular web search engines
   --dork-b64            Whether dork is in base64 format
 
 Optimization:
   Optimization options
 
   -o, --output OUTPUT_PATH
                         Output file to write (JSON Lines format)
   --plugins PLUGINS     Load plugins to execute
   --pocs-path POCS_PATH
                         User defined poc scripts path
   --threads THREADS     Max number of concurrent network requests (default
                         150)
   --batch BATCH         Automatically choose defaut choice without asking
   --requires            Check install_requires
   --quiet               Activate quiet mode, working without logger
   --ppt                 Hiden sensitive information when published to the
                         network
   --pcap                use scapy capture flow
   --rule                export suricata rules, default export reqeust and
                         response
   --rule-req            only export request rule
   --rule-filename RULE_FILENAME
                         Specify the name of the export rule file
   --no-check            Disable URL protocol correction and honeypot check
 
 Docker Environment:
   Docker Environment options
 
   --docker-start        Run the docker for PoC
   --docker-port DOCKER_PORT
                         Publish a container's port(s) to the host
   --docker-volume DOCKER_VOLUME
                         Bind mount a volume
   --docker-env DOCKER_ENV
                         Set environment variables
   --docker-only         Only run docker environment
 
 Web Hook:
   Web Hook Options
 
   --dingtalk-token DINGTALK_TOKEN
                         Dingtalk access token
   --dingtalk-secret DINGTALK_SECRET
                         Dingtalk secret
   --wx-work-key WX_WORK_KEY
                         Weixin Work key
 
 Poc options:
   definition options for PoC
 
   --options             Show all definition options
 
 [*] shutting down at 10:48:43
 
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\pocsuite3\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:07.052816
