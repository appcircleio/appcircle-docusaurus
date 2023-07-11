---
title: Network Access
metaTitle: Network Access
metaDescription: Networks Access of Appcircle Server and Runner
sidebar_position: 4
---

# Overview

This page provides guidance on configuring and enabling external network access for self-hosted Appcircle server and runner.

When deploying the self-hosted Appcircle server and runner, there are scenarios where the application needs to establish connections to external resources over the network. These connections are required to download operating system dependencies, pull Docker images from registries, or access external services such as mobile application build dependencies.

Enabling external network access is essential to ensuring the smooth operation and functionality of self-hosted applications. By establishing connections to external resources, self-hosted applications can access the necessary components, data, and services that are vital for their execution.

You can see different scenarios below according to how you want to install the Appcircle server and runner.

:::info
If you are hosting a yum or apt package repository locally on your network, you do not need to allow external domains for RHEL and Ubuntu repos.
:::

## External Resources Access When Installing or Upgrading

Below you can find the network access details required when installing or upgrading a self-hosted Appcircle server and runner.

### Appcircle Server on RHEL with Docker

This section covers the external resource domains during the installation process of the Appcircle Server on the RHEL operating system using Docker.

- Appcircle server `zip` archive and container images:

  - cdn.appcircle.io
  - storage.googleapis.com/appcircle-dev-common/self-hosted
  - europe-west1-docker.pkg.dev/appcircle/docker-registry

- Offline docker install script and docker `rpm` files:

  - storage.googleapis.com/appcircle-dev-common/self-hosted

- `tar`, `curl` and `unzip` tools:
  - subscription.rhsm.redhat.com
  - cdn.redhat.com

### Appcircle Server on RHEL with Podman

This section covers the external resource domains during the installation process of the Appcircle Server on the RHEL operating system using Podman.

- Appcircle server `zip` archive and container images:

  - cdn.appcircle.io
  - storage.googleapis.com/appcircle-dev-common/self-hosted
  - europe-west1-docker.pkg.dev/appcircle/docker-registry

- `curl`, `unzip`, `socat`, `netavark` and `podman` tools:

  - subscription.rhsm.redhat.com
  - cdn.redhat.com

- `podman-compose` tool:
  - pypi.python.org
  - pypi.org
  - files.pythonhosted.org

### Appcircle Server on Ubuntu with Docker

This section covers the external resource domains during the installation process of the Appcircle Server on the Ubuntu operating system using Docker.

- Appcircle server `zip` archive and container images:

  - cdn.appcircle.io
  - storage.googleapis.com/appcircle-dev-common/self-hosted
  - europe-west1-docker.pkg.dev/appcircle/docker-registry

- `curl` and `unzip` tools:

  - archive.ubuntu.com

- `docker`:
  - download.docker.com
  - archive.ubuntu.com

### Appcircle Server on Ubuntu with Podman

This section covers the external resource domains during the installation process of the Appcircle Server on the Ubuntu operating system using Podman.

- Appcircle server `zip` archive and container images:

  - cdn.appcircle.io
  - storage.googleapis.com/appcircle-dev-common/self-hosted
  - europe-west1-docker.pkg.dev/appcircle/docker-registry

- `curl`, `unzip`, `netavark` and `socat` tools:

  - archive.ubuntu.com

- `podman` and `podman-compose` tool:
  - download.opensuse.org
  - archive.ubuntu.com
  - ftp.gwdg.de
  - pypi.python.org
  - pypi.org
  - files.pythonhosted.org

### Appcircle Runner as Ready-to-Use MacOS Virtual Machine

This section covers the external resource domains during the installation process of the Appcircle runner using an Appcircle-provided [virtual machine](../self-hosted-runner/installation.md#macos-vm).

- `homebrew` tool:

  - raw.githubusercontent.com
  - github.com
  - api.github.com
  - api.apple-cloudkit.com
  - formulae.brew.sh
  - swcdn.apple.com
  - xp.apple.com
  - pancake.apple.com
  - gdmf.apple.com
  - swdist.apple.com
  - swscan.apple.com
  - ocsp2.apple.com

:::info

Homebrew installs the latest version of Xcode Command Line Tools as a dependency. `*.apple.com` domains are used for that purpose.

:::

- `tart` tool:
  - github.com
  - api.github.com
  - objects.githubusercontent.com
  - api.apple-cloudkit.com
  - google-analytics.com
  - europe-west1-1.gcp.cloud2.influxdata.com

:::info

Homebrew gathers anonymous analytics using InfluxDB. The below domains are related to Homebrew analytics when installing a package via the `brew` command.

- google-analytics.com
- europe-west1-1.gcp.cloud2.influxdata.com

If you don't want to enable these URLs or you aren’t comfortable with this, you can opt out of Homebrew analytics by following the instructions [here](https://docs.brew.sh/Analytics#opting-out).

:::

- macOS VM image and the `run.sh` script:
  - storage.googleapis.com/appcircle-dev-common/self-hosted

## External Resources Access When Running Build Pipeline

This section addresses the utilization of external resources during the build, publish, store submit, and other processes on the Appcircle runner.

### Build

Appcircle’s workflow components are hosted on GitHub and they're `git` cloned while running pipeline.

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

Firebase:

- firebaseappdistribution.googleapis.com

App Center:

- api.appcenter.ms

### Store Submit

Google Play

- `www.googleapis.com`

Huawei AppGallery

- connect-api.cloud.huawei.com
- developer.huawei.com
- developerfile7.hicloud.com

:::caution

Please be aware that the subdomain above (`developerfile7`) may change in the future, and it is dynamically returned by the `https://connect-api.cloud.huawei.com` endpoint.

:::

App Store

- contentdelivery.itunes.apple.com
- api.appstoreconnect.apple.com

:::caution
Apple App Store connects to several endpoints during upload.

Those endpoints are documented at [here](https://help.apple.com/itc/transporteruserguide/en.lproj/static.html). The endpoints may change in future.
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

:::caution

Although Appcircle runners are responsible for the submission of iOS apps to the App Store, the **server also has some features that need access to the App Store Connect API**, like runners. For example, get devices from the App Store, get certificates or provisioning profiles, etc.

So, you should enable the **below API access on the server** for those features:

- api.appstoreconnect.apple.com

:::
