---
tool_id: kubernetes-helm
title: kubernetes-helm
categories: ["utilities"]
category_slugs: ["utilities"]
homepage: https://github.com/helm/helm
repository: 
version: 3.19.0+ds1-0kali1
architectures: any
license: 
binaries: []
metapackages: ["kali-linux-everything"]
icon: /images/kali-tools-icon-missing.svg
source_path: kali-tools\kubernetes-helm\index.md
source_commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
generated_at: 2026-01-03T15:46:06.962108
---

# Tool: kubernetes-helm (kubernetes-helm)

## Categories
- [utilities](../utilities.md)


## Quick Facts
| Field | Value |
| --- | --- |
| Homepage | [https://github.com/helm/helm](https://github.com/helm/helm) |
| Repository |  |
| Version | 3.19.0+ds1-0kali1 |
| Architectures | any |
| License |  |
| Binaries |  |
| Metapackages | kali-linux-everything |
| Icon | /images/kali-tools-icon-missing.svg |

## Install
*(No installation information found)*

## Official Info (Extracted)
- **Repository**: https://gitlab.com/kalilinux/packages/kubernetes-helm
- **PackagesInfo**: |
- **Use Helm to**: []
- ****Installed size**: ** `57.42 MB`
- ****How to install**: ** `sudo apt install kubernetes-helm`
- **root@kali**: ~# helm -h
- **Common actions for Helm**: ['helm search:    search for charts', 'helm pull:      download a chart to your local directory to view', 'helm install:   upload the chart to Kubernetes', 'helm list:      list releases of charts']
- **Environment variables**: []


## Documentation (Upstream)
---------------------------------|------------------------------------------------------------------------------------------------------------|
 | $HELM_CACHE_HOME                   | set an alternative location for storing cached files.                                                      |
 | $HELM_CONFIG_HOME                  | set an alternative location for storing Helm configuration.                                                |
 | $HELM_DATA_HOME                    | set an alternative location for storing Helm data.                                                         |
 | $HELM_DEBUG                        | indicate whether or not Helm is running in Debug mode                                                      |
 | $HELM_DRIVER                       | set the backend storage driver. Values are: configmap, secret, memory, sql.                                |
 | $HELM_DRIVER_SQL_CONNECTION_STRING | set the connection string the SQL storage driver should use.                                               |
 | $HELM_MAX_HISTORY                  | set the maximum number of helm release history.                                                            |
 | $HELM_NAMESPACE                    | set the namespace used for the helm operations.                                                            |
 | $HELM_NO_PLUGINS                   | disable plugins. Set HELM_NO_PLUGINS=1 to disable plugins.                                                 |
 | $HELM_PLUGINS                      | set the path to the plugins directory                                                                      |
 | $HELM_REGISTRY_CONFIG              | set the path to the registry config file.                                                                  |
 | $HELM_REPOSITORY_CACHE             | set the path to the repository cache directory                                                             |
 | $HELM_REPOSITORY_CONFIG            | set the path to the repositories file.                                                                     |
 | $KUBECONFIG                        | set an alternative Kubernetes configuration file (default "~/.kube/config")                                |
 | $HELM_KUBEAPISERVER                | set the Kubernetes API Server Endpoint for authentication                                                  |
 | $HELM_KUBECAFILE                   | set the Kubernetes certificate authority file.                                                             |
 | $HELM_KUBEASGROUPS                 | set the Groups to use for impersonation using a comma-separated list.                                      |
 | $HELM_KUBEASUSER                   | set the Username to impersonate for the operation.                                                         |
 | $HELM_KUBECONTEXT                  | set the name of the kubeconfig context.                                                                    |
 | $HELM_KUBETOKEN                    | set the Bearer KubeToken used for authentication.                                                          |
 | $HELM_KUBEINSECURE_SKIP_TLS_VERIFY | indicate if the Kubernetes API server's certificate validation should be skipped (insecure)                |
 | $HELM_KUBETLS_SERVER_NAME          | set the server name used to validate the Kubernetes API server certificate                                 |
 | $HELM_BURST_LIMIT                  | set the default burst limit in the case the server contains many CRDs (default 100, -1 to disable)         |
 | $HELM_QPS                          | set the Queries Per Second in cases where a high number of calls exceed the option for higher burst values |
 
 Helm stores cache, configuration, and data based on the following configuration order:
 
 - If a HELM_*_HOME environment variable is set, it will be used
 - Otherwise, on systems supporting the XDG base directory specification, the XDG variables will be used
 - When no other location is set a default location will be used based on the operating system
 
 By default, the default directories depend on the Operating System. The defaults are listed below:
 
 | Operating System | Cache Path                | Configuration Path             | Data Path               |
 |------------------|---------------------------|--------------------------------|-------------------------|
 | Linux            | $HOME/.cache/helm         | $HOME/.config/helm             | $HOME/.local/share/helm |
 | macOS            | $HOME/Library/Caches/helm | $HOME/Library/Preferences/helm | $HOME/Library/helm      |
 | Windows          | %TEMP%\helm               | %APPDATA%\helm                 | %APPDATA%\helm          |
 
 Usage:
   helm [command]
 
 Available Commands:
   completion  generate autocompletion scripts for the specified shell
   create      create a new chart with the given name
   dependency  manage a chart's dependencies
   env         helm client environment information
   get         download extended information of a named release
   help        Help about any command
   history     fetch release history
   install     install a chart
   lint        examine a chart for possible issues
   list        list releases
   package     package a chart directory into a chart archive
   plugin      install, list, or uninstall Helm plugins
   pull        download a chart from a repository and (optionally) unpack it in local directory
   push        push a chart to remote
   registry    login to or logout from a registry
   repo        add, list, remove, update, and index chart repositories
   rollback    roll back a release to a previous revision
   search      search for a keyword in charts
   show        show information of a chart
   status      display the status of the named release
   template    locally render templates
   test        run tests for a release
   uninstall   uninstall a release
   upgrade     upgrade a release
   verify      verify that a chart at the given path has been signed and is valid
   version     print the client version information
 
 Flags:
       --burst-limit int                 client-side default throttling limit (default 100)
       --debug                           enable verbose output
   -h, --help                            help for helm
       --kube-apiserver string           the address and the port for the Kubernetes API server
       --kube-as-group stringArray       group to impersonate for the operation, this flag can be repeated to specify multiple groups.
       --kube-as-user string             username to impersonate for the operation
       --kube-ca-file string             the certificate authority file for the Kubernetes API server connection
       --kube-context string             name of the kubeconfig context to use
       --kube-insecure-skip-tls-verify   if true, the Kubernetes API server's certificate will not be checked for validity. This will make your HTTPS connections insecure
       --kube-tls-server-name string     server name to use for Kubernetes API server certificate validation. If it is not provided, the hostname used to contact the server is used
       --kube-token string               bearer token used for authentication
       --kubeconfig string               path to the kubeconfig file
   -n, --namespace string                namespace scope for this request
       --qps float32                     queries per second used when communicating with the Kubernetes API, not including bursting
       --registry-config string          path to the registry config file (default "/root/.config/helm/registry/config.json")
       --repository-cache string         path to the directory containing cached repository indexes (default "/root/.cache/helm/repository")
       --repository-config string        path to the file containing repository names and URLs (default "/root/.config/helm/repositories.yaml")
 
 Use "helm [command] --help" for more information about a command.
 ```
 
 - - -
 
---
{{% hidden-comment "<!--Do not edit anything above this line-->" %}}


## Source
- Path: kali-tools\kubernetes-helm\index.md
- Commit: 6a986bc96e156a34ddc47f758a4449202a8e475d
- Generated at: 2026-01-03T15:46:06.962108
