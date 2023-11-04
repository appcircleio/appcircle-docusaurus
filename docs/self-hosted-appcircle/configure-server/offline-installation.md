---
title: Offline Install/Upgrade
metaTitle: Offline Install/Upgrade
metaDescription: Offline Install/Upgrade
sidebar_position: 8
---

# Overview

Offline container images provide a solution for scenarios where an internet connection may not be readily available or reliable.

The primary purpose of providing offline container images is to enable seamless and efficient Appcircle server installations and updates in situations where connectivity to online container registries is limited or restricted.

Here you will find how to use the Appcircle server's offline container images.

## Requirements

### Software Requirements

To use the `download` or `load` commands, the self-hosted Appcircle server version must be `3.8.1` or greater.

You need some tools for offline installation or upgrade. These are already installed if you followed one of the installation pages and ran the command below.

```bash
sudo ./ac-self-hosted.sh -i
```

#### For Downloading From Another Machine

- curl

#### For Loading Images On Appcircle Server Machine

- curl
- unzip
- docker | podman

:::caution
You must follow one of the Appcircle server installation methods (Docker or Podman) and [configure](../install-server/docker.md#3-configure) `global.yaml` as your project's needs until the [run server](../install-server/docker.md#5-run-server) section.

Before running the server, you can install container images offline and then run the server.
:::

### Auth Requirement

During the installation of the self-hosted Appcircle server, it is essential to have the `cred.json` file provided to you upon purchasing the license. This `cred.json` file is necessary to access offline container images.

Without this file, you will not be able to access the offline container images required for the installation.

### Configuration Requirement

You must configure your project before using offline container images.

Please refer to [configuration section](../install-server/docker.md#3-configure) from our installation pages.

After you have configured your project, you can refer to this page to run your server with offline container images.

## Installation

### Install on a Server With No Internet Access

If your Appcircle server does not have access to any container registry and does not have internet access, you can still install the Appcircle server.

In this scenario, you should download the Appcircle server container images to another Linux machine that should have active internet access and copy them to the Appcircle server with any desired method, like `ftp` or `scp`.

For downloading the Appcircle server offline container images, you should download the latest Appcircle server package.

:::caution
You should follow these steps on a Linux server that should have an active internet connection until you copy the `container-images` directory to the Appcircle server.

After copying the `container-images` directory to the actual Appcircle server, follow the remaining steps on the Appcircle server.
:::

- Go to the Appcircle server [installation](../install-server/docker.md#1-download) page.

- Download the zip file and `unzip` it according to the [instructions](../install-server/docker.md#1-download) there.

- Your organization should have a `cred.json` file. Copy that `cred.json` file inside the `appcircle-server` directory that you just unzipped.

- Run the `ac-self-hosted.sh` script with the `download` subcommand.

```bash
./ac-self-hosted.sh download
```

- A file download process should start.

- After the file download process has finished, you will see a directory named `container-images` in the `appcircle-server` directory.

- You should copy this directory to the actual Appcircle server with any method you want, like `ftp` or `scp`.

- After this step, you should login to the actual Appcircle server and go to the `appcircle-server` directory.

- Now you should see the `container-images` directory, which is copied from the other machine, in the `appcircle-server` directory on the Appcircle server.

- To import the container images into your project, run the `load` subcommand with the project argument.

:::caution
The `spacetech` value in the code below is an example project name.

Please check your project name by listing the `./projects` directory, and **don't forget** to replace the "spacetech" value with your project name.
:::

```bash
./ac-self-hosted.sh -n "spacetech" load
```

After the load process completes, you should see the imported container images with your container engine.

If you are using Docker as container engine;

```bash
docker image ls
```

If you are using Podman as container engine;

```bash
podman image ls
```

Now you are ready to `up` (start) the Appcircle server. You can refer back to the [Run Server](../install-server/docker.md#5-run-server) section for details.

### Install on a Server With Internet Access

If the container registry that your organization has is not reliable or has connection issues, you can download and install offline container images directly with internet access.

For this scenario to work, you should have an internet access on the Appcircle server.

Run the below command to install all required container images to your container engine.

```bash
./ac-self-hosted.sh -n "spacetech" load
```

:::info
If you have configured a custom registry url in `global.yaml`, downloaded images will be re-tagged with your custom registry url.

So the offline installation step is compatible with your custom registries.
:::

:::info
This command will download container images and load them into the container engine that you use in your system. (Docker or Podman)
:::

Now you are ready to `up` (start) the Appcircle server. You can refer back to the [Run Server](../install-server/docker.md#5-run-server) section for details.

## Upgrade

If you installed a self-hosted Appcircle server before and you want to upgrade your self-hosted Appcircle server but you can't somehow download container images, you can update your container images with this method too.

:::info
You don't need to change your `global.yaml` or reset your data.

Upgrading your Appcircle server with offline container images is fully compatible with your already-installed Appcircle server.
:::

First, you need to update your self-hosted Appcircle server package. After you [download and unzip](../update.md#1-download-latest) the Appcircle server package, you can return to this page and follow the instructions below.

- Go into the self-hosted Appcircle server directory.

```bash
cd appcircle-server
```

- You can check the server version. So you will see which Appcircle server version images will be downloaded and loaded into the container engine.

```bash
./ac-self-hosted.sh --version
```

- Shutdown the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

:::caution
You should change the "spacetech" value in above command with your project name.
:::

- Get the offline container images and update your local images.

  - If your Appcircle server has no internet access, follow the instructions at [Install on a Server With No Internet Access](#install-on-a-server-with-no-internet-access) section.

  - If your Appcircle server has internet access, follow the instructions at [Install on a Server With Internet Access](#install-on-a-server-with-internet-access) section.

- Start the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

- Check that your services are healthy and the Appcircle server is ready-to-use.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

- Check your image IDs and digests.

```bash
./ac-self-hosted.sh -n "spacetech" version
```

:::caution
Those steps above will result in system downtime.

It is recommended to perform those operations during a maintenance window when users have been notified and there is no active usage of the system.

Ideally, scheduling the update for a time such as 03:00 am, when user activity is typically minimal, will minimize service disruptions.
:::
