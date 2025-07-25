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

### Store APIs

Although Appcircle runners are responsible for the submission of the apps to the mobile application stores, the server also has some features that need access to the application store APIs, like runners.

For example, verify uploaded API keys, get devices from the App Store, get certificates or provisioning profiles, verify the uploaded certificates, etc.

So, you should enable the below API access on the server for each store you want to publish your apps.

#### Google Play Store

- `oauth2.googleapis.com`
- `androidpublisher.googleapis.com`

#### Huawei AppGallery

- `connect-api.cloud.huawei.com`

#### App Store

- `api.appstoreconnect.apple.com`

:::info
If you are using an Enterprise API Key as detailed in the [App Store Connect API Key](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key) documentation, ensure that network access is also permitted to the following address:

- `api.enterprise.developer.apple.com`

:::

## Appcircle Runner Runtime

This section addresses the utilization of external resources during the build, publish, and other processes on the Appcircle runner.

### Appcircle Server

Appcircle runners should access the self-hosted Appcircle server to get jobs and send artifacts.

:::caution
Be aware that the URLs below should be the URLs of the self-hosted Appcircle server in your organization.

Below are the sample URLs that show the required subdomains compatible with the sample configuration in the installation documents.
:::

- `api.appcircle.spacetech.com`
- `resource.appcircle.spacetech.com`
- `redis.appcircle.spacetech.com`

Appcircle runners connect to the self-hosted Appcircle server over the ports below:

If your self-hosted server is configured as HTTPS:

- `443`

If your self-hosted server is configured as HTTP:

- `80`
- `6379`

### Build

Appcircle’s workflow components are hosted on GitHub and they're `git` cloned while running the pipeline.

- `github.com/appcircleio/`

Some of the dependencies such as `CocoaPods` and `Fastlane` use Ruby Gems.

- `rubygems.org`
- `index.rubygems.org`

The Gradle wrapper needs access to the below URL to download Gradle.

- `services.gradle.org`

Android Build Tools need access to the following URLs to download new build tools and NDKs:

- `dl-ssl.google.com/android/repository`
- `dl.google.com/android/repository`

All the maven repositories inside `build.gradle` must be added to the allow-list.

For example;

- `maven.google.com`
- `repo.maven.apache.org/maven`2`

If you’re using CocoaPods and if your `Podfile` is using another spec repository, they also must be allowed.

- `cdn.cocoapods.org`
- `github.com/CocoaPods/Specs`

### Testing Distribution

#### Firebase:

- `firebaseappdistribution.googleapis.com`

### Publish

**Disclaimer:** The URLs provided below were last verified on 3 June 2025, and are subject to change by the respective services. Please consult official documentation of the stores for the most up-to-date information.

#### Google Play Store

- `www.googleapis.com`
- `androidpublisher.googleapis.com`

#### Huawei AppGallery

- `connect-api.cloud.huawei.com`
- `nsp-appgallery-agcfs-dre.obs.eu-de.otc.t-systems.com` (dynamic)

:::caution
The second domain starting with `nsp-appgallery-`, may vary depending on your region. It is dynamically returned by the AppGallery Connect API.

To determine the exact URL used in your case, monitor your network traffic during the publishing process.
:::

#### App Store

- `contentdelivery.itunes.apple.com`
- `api.appstoreconnect.apple.com`
- `appstoreconnect.apple.com`

:::info
If you are using an Enterprise API Key as detailed in the [App Store Connect API Key](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key) documentation, ensure that network access is also permitted to the following address:

- `api.enterprise.developer.apple.com`

:::

:::caution
The Apple App Store connects to several endpoints during upload. It is important to allow access to all of them.

Those endpoints are documented at [here](https://help.apple.com/itc/transporteruserguide/en.lproj/static.html). The endpoints may change in the future.
:::

| **Server**                              | **TCP Port** |
| --------------------------------------- | ------------ |
| contentdelivery.itunes.apple.com        | 443          |
| idmsa.apple.com                         | 443          |
| northamerica-1.object-storage.apple.com | 443          |
| store-037.blobstore.apple.com           | 443          |
| store-036.blobstore.apple.com           | 443          |
| store-035.blobstore.apple.com           | 443          |
| store-033.blobstore.apple.com           | 443          |
| store-032.blobstore.apple.com           | 443          |
| store-030.blobstore.apple.com           | 443          |
| store-028.blobstore.apple.com           | 443          |
| store-026.blobstore.apple.com           | 443          |
| store-025.blobstore.apple.com           | 443          |
| store-004.blobstore.apple.com           | 443          |
| transporter.amp.apple.com               | 443          |

<!-- "Upcoming Expansion for Uploads" row didn't included in this table since it doesn't have domain name, only stated as IP ranges. -->

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

- `api.appcircle.spacetech.com`
- `auth.appcircle.spacetech.com`
- `monitor.appcircle.spacetech.com`

Appcircle DMZ server connect to the self-hosted Appcircle server over the ports below:

If your self-hosted Appcircle server is configured as HTTPS:

- `443`

If your self-hosted Appcircle server is configured as HTTP:

- `80`