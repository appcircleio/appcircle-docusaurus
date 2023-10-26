---
title: Offline Install/Update
metaTitle: Offline Install/Update
metaDescription: Offline Install/Update
sidebar_position: 8
---

# Overview

Offline container images provide a solution for scenarios where an internet connection may not be readily available or reliable.

The primary purpose of providing offline container images is to enable seamless and efficient Appcircle server installations and updates in situations where connectivity to online container registries is limited or restricted.

Here you will find how to use the Appcircle server's offline container images.

## Requirements

### Software Requirements

To use `load` command , your self hosted script version must be `3.7.1` or greater.

You should install the tools below. But there is good news: these are already installed if you followed one of the installation pages and ran the command below.

:::caution
You must to follow one of the Appcircle server installation methods (docker or podman) and [configure](../install-server/docker.md#3-configure) `global.yaml` as your project's needs till the [run server](../install-server/docker.md#5-run-server) section.
Before running the server, you can install container images offline.
:::

#### For Downloading From Another Machine

- curl

#### For Loading Images On Appcircle Server Machine

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

### Configuration Requirement

You must configure your project before using offline container images.

Please refer to [configuration section](../install-server/docker.md#3-configure) from our installation pages.

After you have configured your project, you can refer to this page to run your server with offline container images.

## Installation

### Install on a Server With No Internet Access.

If your Appcircle server does not have access to any container registry and does not have internet access, you can still install the Appcircle server.

In this scenario, you should download the Appcircle server container images to another linux machine which should have an active internet access and copy them to the Appcircle server with any desired method like `ftp` or `scp`.

For downloading the Appcircle server offline container images, you should download the latest Appcircle server package.

:::caution
You should follow this steps on a linux server which should have an active internet connection until you copy the `container-images` directory to the Appcircle server.

After copying the `container-images` directory to the actual Appcircle server, follow the remaining steps on the Appcircle server.
:::

- Go to the [Appcircle server installation page](../install-server/docker.md#1-download)

- Download the zip file and unzip it according to the [documents](../install-server/docker.md#1-download).

- Your organization should have a `cred.json` file. Copy that `cred.json` file inside the `appcircle-server` directory that you just unzipped.

- Run the `ac-self-hosted.sh` script with the download subcommand.

```bash
./ac-self-hosted.sh download
```

- A file download process should start.

- After the file download process has finished, you will see a directory named `container-images` in the `appcircle-server` directory.

- You should copy this directory to the actual Appcircle server with any method you want, like `ftp` or `scp`.

- After this step, you should login to the Appcircle server and go to the `appcircle-server` directory.

- Now you should see the `container-images` directory, which is copied from the other machine, in the ` appcircle-server` directory on the Appcircle server.

- To import the container images into your project, run the Appcircle server installer script with your project name.

:::caution
The `spacetech` value in the code below is an example project name.

Please check your project name by listing the `./projects` directory, and **don't forget** to replace the spacetech value with your project name.
:::

```bash
./ac-self-hosted.sh -n spacetech load
```

- The script will ask you to automatically load offline container images. Click `y` to accept.

- After the load process completes, you can see the imported container images with your container engine.

```bash
# If you are using docker as container engine
docker image ls

# If you are using podman as container engine
podman image ls
```

- Now you are ready to `up` the Appcircle server. You can refer back to the [Run Server](../install-server/docker.md#5-run-server) section.

### Install on a Server With Internet Access

If the container registry that your organization has is not reliable or has connection issues, you can download and install offline container images directly with internet access.

For this scenario to work, you should have an internet access on the Appcircle server.

- Run the below command to install all required container images to your container engine.

```bash
./ac-self-hosted.sh -n "spacetech" load
```

:::info
If you have configured a custom registry url in the `global.yaml`, downloaded images will be re-tagged with your custom registry url.
So the offline installation step is compatible with your custom registries.
:::

:::info
The script will ask you if you want to import automatically.

If you want to import all the images, press `y` to accept.

If you don't want the all images but a few, you can press `n`. After this, you should handle the issues for your own.

This command will download container images and load them to the selected container engine in the "Installing Required Tools" section.
:::

- Now you are ready to `up` the Appcircle server. You can refer back to the [Run Server](../install-server/docker.md#5-run-server) section.

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

  - If your Appcircle server has no internet access, check the usage for [Install on a Server With No Internet Access](#install-on-a-server-with-no-internet-access)

  - If your Appcircle server has internet access, check the usage for [Install on a Server With Internet Access](#install-on-a-server-with-internet-access)

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
This steps will result in system downtime.
It is recommended to perform this update during a maintenance window when users have been notified and there is no active usage of the system.
Ideally, scheduling the update for a time such as 03:00 am, when user activity is typically minimal, will minimize disruptions.
:::
