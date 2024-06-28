---
title: Enterprise App Store and Testing Distribution in DMZ
description: Learn how to create a server in DMZ for Appcircle Enterprise App Store and Testing Distribution for accessing from internet.
tags: [self-hosted, advanced configuration, dmz, enterprise app store, testing distribution]
sidebar_position: 12
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';
import LingerOption from '@site/docs/self-hosted-appcircle/configure-server/\_linger-option.mdx';
import SocatConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_socat-configuration.mdx';
import NetavarkConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_podman-netavark-configuration.mdx';
import FirewalldConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_firewalld-configuration.mdx';
import SwapConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_swap-configuration.mdx';

## Overview

A Demilitarized Zone (DMZ) in networking is a segment of an internal network that is exposed to external networks, typically over the internet. By isolating Appcircle DMZ server from the internal network, you ensure that it remains secure. 

This is particularly useful when users need to access Testing Distribution and Enterprise App Store but not all features for business operations within the private network.

The Testing Distribution module and Enterprise App Store module hosted on the Appcircle DMZ server can be accessed by users from the internet, ensuring they have secure access to these critical features while keeping sensitive business data within your private network. This setup provides a balance between security and productivity in an organization's IT environment.

@TODO: Diagram will be here.

We assume that you have already set up an Appcircle private server successfully. This document will guide you through creating Appcircle DMZ server and Appcircle private server configurations.

In this document:

- We will call the "Appcircle DMZ server" to the server, which is located in the DMZ and host the Appcircle Enterprise App Store and Testing Distribution services. 

- We will call the "Appcircle private server" to the server, which is located in the private network and host the Appcircle core services.

## Appcircle DMZ Server Pre-requirements

Below are the hardware and OS requirements for self-hosted Appcircle DMZ server installation.

### Supported Linux Distributions

Self-hosted Appcircle DMZ server, can only be installed on Linux operating system.

If you have installed the Appcircle private server with Podman:

- CentOS Stream 8 or later
- RHEL 8 or later

If you have installed the Appcircle private server with Docker:

- Ubuntu 20.04 or later
- Debian 11 or later
- CentOS 8 or later
- RHEL 8 or later

### Hardware Requirements

Minimum hardware requirements for self-hosted Appcircle can be:

- 20GB or more free disk space
- 4 or more cores CPU
- 8 or more gigabytes (GB) RAM

:point_up: These hardware specs are minimum requirements for basic execution and it can be used only for quick evaluation or development purposes.

:::caution
CPU architecture must be AMD or Intel 64-bit arch (`x86_64`).
:::

:::info
If you have enough RAM and a recent CPU, performance of Appcircle server can be limited by hard drive seek times. So, having a fast drive like a solid state drive (SSD) improves runtime.
:::

Higher numbers will be better especially for increased number of users.

For an enterprise installation, **minimum** hardware requirements are

- 50GB SSD
- 8 CPU
- 16GB RAM

For production environments, **recommended** hardware requirements are

- 50GB SSD
- 32 CPU
- 64GB RAM

:::caution

#### Swap

<SwapConfiguration/>

:::

### Software Requirements

#### Container Engine

You must use the same container engine with on the Appcircle private server and the Appcircle DMZ server. 

If you have installed the Appcircle private server with Podman, you **must** use Podman on the Appcircle DMZ server. 

If you have installed the Appcircle private server with Docker, you **must** use Docker on the Appcircle DMZ server.

#### SeLinux

You must use the same SeLinux mode on the Appcircle private server and the Appcircle DMZ server.

If 

## Creating Appcircle DMZ server Configuration

To create the Appcircle DMZ server configuration, you should login to the Appcircle private server. 

You will create all the configuration files on the Appcircle private server and then move the created configuration files to the Appcircle DMZ server.

To create the Appcircle DMZ server configuration, you can follow the steps below.

- Login to the Appcircle private server with SSH.

- Go to the Appcircle server directory

```bash
cd appcircle-server
```

- Stop the running Appcircle server.

<SpacetechExampleInfo />

```bash
./ac-self-hosted.sh -n spacetech down
```

- Create the new configuration files for the Appcircle DMZ and the Appcircle private server.

```bash
./ac-self-hosted.sh -n spacetech export --dmz
```

:::info
The `--dmz` flag in the `export` subcommand above creates the configuration files according to your `global.yaml` file of your project for the both the Appcircle DMZ server and the private server. 
:::

- Check the exported DMZ directory that contains the required files to create Appcircle DMZ server.

```bash
ls -lah projects/spacetech/export/dmz/
```

- Transfer the contents of the `projects/spacetech/export/dmz/` directory to the Appcircle DMZ server.

- Compress the directory into a tarball in the Appcircle private server, transfer and extract it in the Appcircle DMZ server.

```bash
tar -czf dmz.tar.gz -C projects/spacetech/export/dmz/ .
```

- Transfer the `dmz.tar.gz` file to the Appcircle DMZ server.


## Creating the Appcircle DMZ Server

### Create Appcircle DMZ Directory

You need to create a directory for the Appcircle DMZ server and extract the transferred configuration files.

- Create a Appcircle DMZ server.

```bash
mkdir appcircle-server-dmz
```

- Extract the tarball.

```bash
tar -xzf dmz.tar.gz -C appcircle-server-dmz
```

- Change directory into the new directory and list the contents.

```bash
cd appcircle-server-dmz && ls -l
```

### Configure the System


<Tabs>
  
  <TabItem value="podman" label="Podman" default>

#### Enabling the Linger Option

<LingerOption/>

#### Overcoming Privileged Port Limitations

<SocatConfiguration/>

#### Podman Network Stack

<NetavarkConfiguration/>

#### Firewalld Requirements

<FirewalldConfiguration/>

  </TabItem>

  
  <TabItem value="docker" label="Docker" default>

#### Docker Configuration

For Docker, you don't need to do anything manually. You can move on to the next section. 

  </TabItem>

</Tabs>

## Appcircle DMZ Server Monitoring

By default, Appcircle DMZ server will try to send the container logs to the Appcircle private server.

You can check the container logs from the Appcircle monitoring page. For more details about checking the logs, you can check the [Monitoring](/docs/self-hosted-appcircle/configure-server/monitoring.md) page.
