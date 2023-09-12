---
title: Offline Install/Update
metaTitle: Offline Install/Update
metaDescription: Offline Install/Update
sidebar_position: 8
---

# Overview

Offline container images provide a solution for scenarios where an internet connection may not be readily available or reliable.

The primary purpose of providing offline container images is to enable seamless and efficient software deployments in situations where connectivity to online container registries is limited or restricted.

Here you will find how to use the Appcircle server's offline container images.

## Requirements

### Software Requirements

You should install the tools below. But there is good news: these are already installed if you followed one of the installation pages and ran the command below.

:::caution
You must to follow one of the Appcircle server installation methods (docker or podman) and [configure](../install-server/docker.md#3-configure) `global.yaml` as your project's needs till the [run server](../install-server/docker.md#5-run-server) section.
Before running the server, you can install container images offline.
:::

```bash
sudo ./ac-self-hosted.sh -i`
```

- curl
- unzip
- docker | podman

### Auth Requirement

During the installation of the Self-Hosted Appcircle Server, it is essential to have the `cred.json` file provided to you upon purchasing the license.
This `cred.json` file is necessary to access offline container images.
Without this file, you will not be able to access the offline container images required for the installation.

## Installation

Installing Appcircle server with offline container images is pretty easy.
After you [configured](../install-server/docker.md#3-configure) your project and you want the container images to be downloaded and ready to run before [running the server](../install-server/docker.md#5-run-server).
Run the below command to install all required container images to your container engine.

```bash
./ac-self-hosted.sh -n "spacetech" load
```

This command will download container images and load them to the selected container engine in the "Installing Required Tools" section.

:::info
If you configured a registry url for container engine in `global.yaml`, downloaded images will be re-tagged with your custom registry url.
So the offline installation step is compatible with your custom registries.
:::

## Update

If you installed self-hosted Appcircle server before and you want to update your self-hosted Appcircle server but you can't download container images somehow.
You can update your container images with this method too.

:::info
You don't need to change your `global.yaml` or reset your data.
Updating your Appcircle server with offline container images is fully compatible with your already-installed Appcircle server.
:::

Firstly, you need to update your Appcircle server package.

After you install and unzip the Appcircle server package, you can return to this page to continue with the update process.

To do that, you can go to the [Upgrade Server page](../update#1-download-latest).

After you update the self-hosted package:

- You can go into the Appcircle server directory.

```bash
cd appcircle-server
```

- You can check your script's version.
  So you will see which Appcircle server version images will be downloaded and loaded to container engine.

```bash
./ac-self-hosted.sh -n "spacetech" version
```

:::info
You should change the "spacetech" as your project name.
:::

- Down your system.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Get the offline container images and update your local images.

```bash
./ac-self-hosted.sh -n "spacetech" load
```

- Run your server again.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check that your services are healthy.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

- Check your image IDs and digests.

```bash
./ac-self-hosted.sh -n "spacetech" version
```

:::caution
Updating your server using offline images may result in a server downgrade.
The downloaded and installed images will override the existing images that were installed with offline packages or downloaded to your system.
It is important to note that the offline container images to be installed are specifically tied to your ac-self-hosted.sh script version.

However, updating the script version to the latest does not guarantee that you will download the latest images with minor updates or patches.

To ensure you obtain the latest version of container images, please follow the instructions provided in the update section.
:::

:::caution
This steps will result in system downtime.
It is recommended to perform this update during a maintenance window when users have been notified and there is no active usage of the system.
Ideally, scheduling the update for a time such as 03:00 am, when user activity is typically minimal, will minimize disruptions.
:::
