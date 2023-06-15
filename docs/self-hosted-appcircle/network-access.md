---
title: Network Access
metaTitle: Network Access
metaDescription: Networks Access of Appcircle Server and Runner
sidebar_position: 7
---

# Overview

This page provides guidance on configuring and enabling external network access for self-hosted Appcircle server and runner. 

When deploying the self-hosted Appcircle server and runner, there are scenarios where the application needs to establish connections to external resources over the network. 
These connections may be required to download operating system dependencies, pull Docker images from registries or access external services such as mobile application build depedencies.

Enabling external network access is essential to ensure the smooth operation and functionality of self-hosted applications. 
By establishing connections to external resources, self-hosted applications can access the necessary components, data, and services that are vital for their execution.

You can see different scenerios below according to how would you want to install Appcircle server and runner. 

:::info
If you are hosting a yum or apt package repository locally, you do not need to allow external domains for RHEL and Ubuntu repos. 
:::

## Installing Appcircle Server on RHEL with Docker

This section covers the installation process of the Appcircle Server on the Red Hat Enterprise Linux (RHEL) operating system using Docker.

- `Appcircle server zip` and `Container Images`
  - cdn.appcircle.io
  - europe-west1-docker.pkg.dev

- `install script` and `docker rpm files`
  - storage.googleapis.com

- `tar`, `jq`, `curl`, `unzip` and `openssl`
  - subscription.rhsm.redhat.com
  - cdn.redhat.com

- `gomplate` and `yq`
  - github.com
  - objects.githubusercontent.com

## Installing Appcircle Server on RHEL with Podman

This section covers the installation process of the Appcircle Server on the Red Hat Enterprise Linux (RHEL) operating system using Podman.

- `Appcircle server zip` and `Container Images`
  - cdn.appcircle.io
  - europe-west1-docker.pkg.dev

- `jq`, `curl`, `unzip`, `openssl`, `socat`, `netavark`, `podman`
  - subscription.rhsm.redhat.com
  - cdn.redhat.com

- `gomplate`, `yq`
  - github.com
  - objects.githubusercontent.com

- `podman-compose`
  - pypi.python.org
  - pypi.org
  - files.pythonhosted.org

## Installing Appcircle Server on Ubuntu with Docker

This section covers the installation process of the Appcircle Server on the Ubuntu operating system using Docker.

- `Appcircle server zip` and `Container Images`
  - cdn.appcircle.io
  - europe-west1-docker.pkg.dev

- `jq`, `curl`, `unzip`, `openssl`
  - archive.ubuntu.com

- `gomplate`, `yq`
  - github.com
  - objects.githubusercontent.com

- `docker`
  - download.docker.com
  - tr.archive.ubuntu.com

You should 

## Installing Appcircle Server on Ubuntu with Podman

This section covers the installation process of the Appcircle Server on the Ubuntu operating system using Podman.

- `Appcircle server zip` and `Container Images`
  - cdn.appcircle.io
  - europe-west1-docker.pkg.dev

- `jq`, `curl`, `unzip`, `openssl`
  - archive.ubuntu.com

- `gomplate`, `yq`
  - github.com
  - objects.githubusercontent.com

- `Podman` and `podman-compose`
  - download.opensuse.org
  - archive.ubuntu.com
  - ftp.gwdg.de
  - pypi.python.org
  - pypi.org
  - files.pythonhosted.org

## Installing Appcircle Runner Macos Virtual Machine

This section covers the installation process of the Appcircle runner with virtual machine [Appcircle provides](./self-hosted-runner/installation#macos-vm).  

- `homebrew`
  - raw.githubusercontent.com
  - github.com
  - api.github.com
  - api.apple-cloudkit.com
  - formulae.brew.sh

- `tart`
  - github.com
  - api.github.com
  - objects.githubusercontent.com
  - api.apple-cloudkit.com
  - www.google-analytics.com
  - europe-west1-1.gcp.cloud2.influxdata.com

- `VM Image` and `Run Scripts`
  - storage.googleapis.com

## Runtime Externel Resources

### Dependencies

- Appcircle’s workflow `components` are hosted on Github.
  - github.com/appcircleio/

- Some of Appcircle’s dependencies such as `CocoaPods` and `Fastlane` use Ruby Gems.
  - rubygems.org

- All the `maven repositories` inside the `build.gradle` must be added to list. For example:
  - maven.google.com
  - repo.maven.apache.org/maven2

- If you’re using `Cocoapods`, and if your `Podfile` is using other spec repository they also must be allowed.
  - cdn.cocoapods.org
  - github.com/CocoaPods/Specs

### Test Distributions

- `Firebase`
  - firebaseappdistribution.googleapis.com

- `App Center`
  - api.appcenter.ms

### Store Submission

- Google Play
  - www.googleapis.com

- Huawei AppGallery
  - connect-api.cloud.huawei.com
  - developerfile7.hicloud.com

:::caution 
Please be aware that subdomain (developerfile7) may change in the future and it is dynamically returned by https//connect-api.cloud.huawei.com
:::

- App Store
  - For Appcircle, following endpoints must be allowed
    - https://contentdelivery.itunes.apple.com

:::caution
Apple App Store connects to several endpoints during upload. 

Those endpoints are documented at https://help.apple.com/itc/transporteruserguide/en.lproj/static.html Endpoints may change in future.
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