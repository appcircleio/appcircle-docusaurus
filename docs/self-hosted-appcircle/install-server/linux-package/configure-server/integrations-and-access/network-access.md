---
title: Network Access
description: Learn how to configure and enable external network access for a self-hosted Appcircle server and runner
tags: [self-hosted, network access, server, runner]
sidebar_position: 4
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Overview

This page provides guidance on configuring and enabling external network access for a self-hosted Appcircle server and runner.

When deploying a self-hosted Appcircle server and runner, there are scenarios where the application needs to establish connections to external resources over the network. These connections are required to download operating system dependencies, pull Docker images from registries, or access external services such as mobile application build dependencies.

Enabling external network access is essential to ensuring the smooth operation and functionality of self-hosted applications. By establishing connections to external resources, self-hosted applications can access the necessary components, data, and services that are vital for their execution.

You can see different scenarios below according to how you want to install the Appcircle server and runner.

:::info
If you are hosting a yum or apt package repository locally on your network, you do not need to allow external domains for RHEL and Ubuntu repos.
:::

## Appcircle Server Install and Update

Below you can find the network access details required when installing or upgrading a self-hosted Appcircle server.

<Tabs>
  
  <TabItem value="rhel-podman" label="RHEL with Podman" default>

This section covers the external resource domains during the installation process of the Appcircle Server on the RHEL distribution using Podman.

##### `podman-compose` tool:

- You must download the podman-compose tool from python pip repositories.

```access_list
pypi.python.org/simple/podman-compose
pypi.org/simple/podman-compose/
pypi.python.org/simple/python-dotenv/
pypi.org/simple/python-dotenv/
pypi.python.org/pypi/pip/json
pypi.org/pypi/pip/json
files.pythonhosted.org/packages/
```

##### System tools:

- The Appcircle server requires some tools to be installed.

- These tools are `tar`, `curl`, `unzip`, `socat`, `netavark` and `Podman`.

- If you are hosting a `yum` repository locally on your network, you don't need these URLs.

```access_list
subscription.rhsm.redhat.com
cdn.redhat.com
```

  </TabItem>

  <TabItem value="rhel-docker" label="RHEL with Docker">

This section covers the external resource domains during the installation process of the Appcircle Server on the RHEL distribution using Docker.

##### Offline docker install script and docker `rpm` files:

- If you want to install `Docker` on your RHEL from Appcircle resources, then the Appcircle server host needs to access these URLs.

```access_list
storage.googleapis.com/appcircle-dev-common/self-hosted
```

##### System tools:

- The Appcircle server requires some tools to be installed.

- These tools are `tar`, `curl` and `unzip`.

- If you are hosting a `yum` repository locally on your network, you don't need these URLs.

```access_list
subscription.rhsm.redhat.com
cdn.redhat.com
```

  </TabItem>
  
  <TabItem value="ubuntu-docker" label="Ubuntu with Docker">

This section covers the external resource domains during the installation process of the Appcircle Server on the Ubuntu distribution using Docker.

##### `docker` installation:

- If you want to install `Docker` on your Ubuntu, then the Appcircle server host needs to access these URLs.

```access_list
download.docker.com
archive.ubuntu.com
```

##### System tools:

- The Appcircle server requires some tools to be installed.

- These tools are `tar`, `curl` and `unzip`.

- If you are hosting an `apt` repository locally on your network, you don't need these URLs.

```access_list
archive.ubuntu.com
```

  </TabItem>
  
</Tabs>

##### If you are an enterprise-licensed or PoC customer, Appcircle server `zip` package:

- If you are an enterprise-licensed or PoC customer and want to install or update the Appcircle server, the Appcircle server host needs to access this URL to download the Appcircle server `zip` package.

- If you want to download the `zip` package and copy it manually (with `scp` or `ftp`), then the Appcircle server host doesn't need this access.

```access_list
cdn.appcircle.io
storage.googleapis.com/storage/v1/b/appcircle-self-hosted
www.googleapis.com/oauth2/v4/token
```

##### If you don't have a proxy registry like `Harbor` or `Nexus`, and want to use container images directly from Appcircle:

- If you have your own proxy registry and want to mirror the Appcircle container images, then your Appcircle server doesn't need to access the origin container image registry directly.

- If you don't have an image registry, the Appcircle server needs to access this URL.

```access_list
europe-west1-docker.pkg.dev/appcircle/docker-registry
```

##### If you want to install the Appcircle server using offline packages:

- If you want to install the Appcircle server without an internet connection, a `zip` package should be downloaded and transferred to the Appcircle server host.

- This `zip` package can be downloaded from another host and transferred to the actual Appcircle server. If you plan to do that, the Appcircle server doesn't need to access these URLs.

```access_list
storage.googleapis.com/appcircle-self-hosted
www.googleapis.com/oauth2/v4/token
```

## Appcircle Runner Install as Ready-to-Use MacOS Virtual Machine

This section covers the external resource domains during the installation process of the Appcircle runner using an Appcircle-provided [virtual machine](/self-hosted-appcircle/self-hosted-runner/installation#macos-vm).

- `homebrew` tool (required):

```access_list
raw.githubusercontent.com
github.com
api.github.com
api.apple-cloudkit.com
formulae.brew.sh
swcdn.apple.com
xp.apple.com
pancake.apple.com
gdmf.apple.com
swdist.apple.com
swscan.apple.com
ocsp2.apple.com
```

:::info

Homebrew installs the latest version of Xcode Command Line Tools as a dependency. `*.apple.com` domains are used for that purpose.

:::

- `tart` tool (required):

_Tart is a registered trademark of Cirrus Labs, Inc._

```access_list
github.com
api.github.com
objects.githubusercontent.com
api.apple-cloudkit.com
google-analytics.com
europe-west1-1.gcp.cloud2.influxdata.com
```

:::info

Homebrew gathers anonymous analytics using InfluxDB. The below domains are related to Homebrew analytics when installing a package via the `brew` command.

- google-analytics.com
- europe-west1-1.gcp.cloud2.influxdata.com

If you don't want to enable these URLs or you aren’t comfortable with this, you can opt out of Homebrew analytics by following the instructions [here](https://docs.brew.sh/Analytics#opting-out).

:::

- macOS VM image and the runner starter script (required):

```access_list
storage.googleapis.com/appcircle-dev-common/self-hosted
```

- macOS VM install script (_required if you prefer automatic installation_):

```access_list
cdn.appcircle.io
storage.googleapis.com/storage/v1/b/appcircle-dev-common
```

## Appcircle Server Runtime

Although Appcircle runners are responsible for the submission of iOS apps to the App Store, the server also has some features that need access to the App Store Connect API, like runners.

For example, get devices from the App Store, get certificates or provisioning profiles, verify the uploaded certificates, etc.

So, you should enable the below API access on the server for those features:

- api.appstoreconnect.apple.com

## Appcircle Runner Runtime

This section addresses the utilization of external resources during the build, publish, store submit, and other processes on the Appcircle runner.

### Appcircle Server

Appcircle runners should access the self-hosted Appcircle server to get jobs and send artifacts.

:::caution
Be aware that the URLs below should be the URLs of the self-hosted Appcircle server in your organization.

Below are the sample URLs that show the required subdomains compatible with the sample configuration in the installation documents.
:::

- api.appcircle.spacetech.com
- resource.appcircle.spacetech.com
- redis.appcircle.spacetech.com

Appcircle runners connect to the self-hosted Appcircle server over the ports below:

If your self-hosted server is configured as HTTPS:

- `443`

If your self-hosted server is configured as HTTP:

- `80`
- `6379`

### Build

Appcircle’s workflow components are hosted on GitHub and they're `git` cloned while running the pipeline.

- github.com/appcircleio/

Some of the dependencies such as `CocoaPods` and `Fastlane` use Ruby Gems.

- rubygems.org

The Gradle wrapper needs access to the below URL to download Gradle.

- services.gradle.org

Android Build Tools need access to the following URLs to download new build tools and NDKs:

- dl-ssl.google.com/android/repository
- dl.google.com/android/repository

All the maven repositories inside `build.gradle` must be added to the allow-list.

For example;

- maven.google.com
- repo.maven.apache.org/maven2

If you’re using CocoaPods and if your `Podfile` is using another spec repository, they also must be allowed.

- cdn.cocoapods.org
- github.com/CocoaPods/Specs

### Testing Distribution

#### Firebase:

- firebaseappdistribution.googleapis.com

#### App Center:

- api.appcenter.ms
- file.appcenter.ms

### Store Submit (Publish)

**Disclaimer:** The URLs provided below were last verified on 09/01/2024, and are subject to change by the respective services. Please consult official documentation of the stores for the most up-to-date information.

#### Google Play

- `www.googleapis.com`
- `androidpublisher.googleapis.com`

#### Huawei AppGallery

- connect-api.cloud.huawei.com
- nsp-appgallery-agcfs-dre.obs.eu-de.otc.t-systems.com

:::caution
Please be aware that the URL above starting with `nsp-appgallery`, may change in the future. It is dynamically returned by the `https://connect-api.cloud.huawei.com` endpoint.
:::

#### App Store

- contentdelivery.itunes.apple.com
- api.appstoreconnect.apple.com

:::caution
The Apple App Store connects to several endpoints during upload.

Those endpoints are documented at [here](https://help.apple.com/itc/transporteruserguide/en.lproj/static.html). The endpoints may change in the future.
:::

| **Server**                                     | **IP Address** | **TCP Port** | **UDP Port** |
| ---------------------------------------------- | -------------- | ------------ | ------------ |
| [vgr501.apple.com](http://vgr501.apple.com/)   | 17.110.248.141 | 33001        | 33001-33500  |
| [vgr502.apple.com](http://vgr502.apple.com/)   | 17.110.248.142 | 33001        | 33001-33500  |
| [vgr503.apple.com](http://vgr503.apple.com/)   | 17.110.248.143 | 33001        | 33001-33500  |
| [vgr504.apple.com](http://vgr504.apple.com/)   | 17.110.248.144 | 33001        | 33001-33500  |
| [vgr505.apple.com](http://vgr505.apple.com/)   | 17.110.248.145 | 33001        | 33001-33500  |
| [vgr506.apple.com](http://vgr506.apple.com/)   | 17.110.248.146 | 33001        | 33001-33500  |
| [vgr507.apple.com](http://vgr507.apple.com/)   | 17.110.248.147 | 33001        | 33001-33500  |
| [vgr508.apple.com](http://vgr508.apple.com/)   | 17.110.248.148 | 33001        | 33001-33500  |
| [vgr701.apple.com](http://vgr701.apple.com/)   | 17.133.233.141 | 33001        | 33001-33500  |
| [vgr702.apple.com](http://vgr702.apple.com/)   | 17.133.233.142 | 33001        | 33001-33500  |
| [vgr703.apple.com](http://vgr703.apple.com/)   | 17.133.233.143 | 33001        | 33001-33500  |
| [vgr704.apple.com](http://vgr704.apple.com/)   | 17.133.233.144 | 33001        | 33001-33500  |
| [vgr705.apple.com](http://vgr705.apple.com/)   | 17.133.233.145 | 33001        | 33001-33500  |
| [vgr706.apple.com](http://vgr706.apple.com/)   | 17.133.233.146 | 33001        | 33001-33500  |
| [vgr707.apple.com](http://vgr707.apple.com/)   | 17.133.233.147 | 33001        | 33001-33500  |
| [vgr708.apple.com](http://vgr708.apple.com/)   | 17.133.233.148 | 33001        | 33001-33500  |
| [vgr0901.apple.com](http://vgr0901.apple.com/) | 17.57.20.141   | 33001        | 33001-33500  |
| [vgr0902.apple.com](http://vgr0902.apple.com/) | 17.57.20.142   | 33001        | 33001-33500  |
| [vgr0903.apple.com](http://vgr0903.apple.com/) | 17.57.20.143   | 33001        | 33001-33500  |
| [vgr0904.apple.com](http://vgr0904.apple.com/) | 17.57.20.144   | 33001        | 33001-33500  |
| [vgr0905.apple.com](http://vgr0905.apple.com/) | 17.57.20.145   | 33001        | 33001-33500  |
| [vgr0906.apple.com](http://vgr0906.apple.com/) | 17.57.20.146   | 33001        | 33001-33500  |
| [vgr0907.apple.com](http://vgr0907.apple.com/) | 17.57.20.147   | 33001        | 33001-33500  |
| [vgr0908.apple.com](http://vgr0908.apple.com/) | 17.57.20.148   | 33001        | 33001-33500  |

## Appcircle DMZ Server Install & Update

Below you can find the network access details required when installing or upgrading a self-hosted Appcircle DMZ server.


<Tabs>
  
  <TabItem value="rhel-podman" label="RHEL with Podman" default>

This section covers the external resource domains during the installation process of the Appcircle DMZ Server on the RHEL distribution using Podman.

##### `podman-compose` tool:

- You must download the podman-compose tool from python pip repositories.

```access_list
pypi.python.org/simple/podman-compose
pypi.org/simple/podman-compose/
pypi.python.org/simple/python-dotenv/
pypi.org/simple/python-dotenv/
pypi.python.org/pypi/pip/json
pypi.org/pypi/pip/json
files.pythonhosted.org/packages/
```

##### System tools:

- The Appcircle DMZ server requires some tools to be installed.

- These tools are `tar`, `curl`, `unzip`, `socat`, `netavark` and `Podman`.

- If you are hosting a `yum` repository locally on your network, you don't need these URLs.

```access_list
subscription.rhsm.redhat.com
cdn.redhat.com
```

  </TabItem>

  <TabItem value="rhel-docker" label="RHEL with Docker">

This section covers the external resource domains during the installation process of the Appcircle DMZ Server on the RHEL distribution using Docker.

##### System tools:

- The Appcircle DMZ server requires some tools to be installed.

- These tools are `tar`, `curl` and `unzip`.

- If you are hosting a `yum` repository locally on your network, you don't need these URLs.

```access_list
subscription.rhsm.redhat.com
cdn.redhat.com
```

  </TabItem>
  
  <TabItem value="ubuntu-docker" label="Ubuntu with Docker">

This section covers the external resource domains during the installation process of the Appcircle DMZ Server on the Ubuntu distribution using Docker.

##### `docker` installation:

- If you want to install `Docker` on your Ubuntu, then the Appcircle server host needs to access these URLs.

```access_list
download.docker.com
archive.ubuntu.com
```

##### System tools:

- The Appcircle DMZ server requires some tools to be installed.

- These tools are `tar`, `curl` and `unzip`.

- If you are hosting an `apt` repository locally on your network, you don't need these URLs.

```access_list
archive.ubuntu.com
```

  </TabItem>
  
</Tabs>

### Appcircle Server

Appcircle DMZ server should access the self-hosted Appcircle server to get required information for Enterprise App Store and Testing Distribution services.

:::caution
Be aware that the URLs below should be the URLs of the self-hosted Appcircle server in your organization.

Below are the sample URLs that show the required subdomains compatible with the sample configuration in the installation documents.
:::

- api.appcircle.spacetech.com
- auth.appcircle.spacetech.com
- monitor.appcircle.spacetech.com

Appcircle DMZ server connect to the self-hosted Appcircle server over the ports below:

If your self-hosted Appcircle server is configured as HTTPS:

- `443`

If your self-hosted Appcircle server is configured as HTTP:

- `80`