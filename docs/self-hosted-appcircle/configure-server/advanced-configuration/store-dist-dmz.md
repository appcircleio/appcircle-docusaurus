---
title: Enterprise App Store and Testing Distribution in DMZ
description: Learn how to create a server in DMZ for Appcircle Enterprise App Store and Testing Distribution for accessing from internet.
tags:
  [
    self-hosted,
    advanced configuration,
    dmz,
    enterprise app store,
    testing distribution,
  ]
sidebar_position: 12
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';
import LingerOption from '@site/docs/self-hosted-appcircle/configure-server/\_linger-option.mdx';
import SocatConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_socat-configuration.mdx';
import NetavarkConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_podman-netavark-configuration.mdx';
import FirewalldConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_firewalld-configuration.mdx';
import UFWConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_ufw-configuration.mdx';
import SwapConfiguration from '@site/docs/self-hosted-appcircle/configure-server/\_swap-configuration.mdx';
import DowntimeCaution from '@site/docs/self-hosted-appcircle/configure-server/\_appcircle-server-downtime-caution.mdx';
import Screenshot from '@site/src/components/Screenshot';

## Overview

A Demilitarized Zone (DMZ) in networking is a segment of an internal network that is exposed to external networks, typically over the internet. By isolating Appcircle DMZ server from the internal network, you ensure that it remains secure.

This is particularly useful when users need to access Testing Distribution and Enterprise App Store but not all features for business operations within the private network.

The Testing Distribution module and Enterprise App Store module hosted on the Appcircle DMZ server can be accessed by users from the internet, ensuring they have secure access to these critical features while keeping sensitive business data within your private network. This setup provides a balance between security and productivity in an organization's IT environment.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3008-dmz-detailed-diagram.png' />

We assume that you have already set up an Appcircle server successfully. This document will guide you through creating Appcircle DMZ server and Appcircle server configurations.

In this document:

- We will call the "Appcircle DMZ server" to the server, which is located in the DMZ and host the Appcircle Enterprise App Store and Testing Distribution services.

- We will call the "Appcircle server" to the server, which is located in the private network and host the Appcircle core services.

:::info
When you convert to the DMZ architecture, both the Enterprise App Store and the Testing Distribution will be transferred to the Appcircle DMZ server. We currently do not support using only one of them in the Appcircle DMZ server.
:::

## Appcircle DMZ Server Pre-requirements

Below are the hardware and OS requirements for self-hosted Appcircle DMZ server installation.

### Supported Linux Distributions

Self-hosted Appcircle DMZ server, can only be installed on Linux operating system.

If you have installed the Appcircle server with Podman:

- CentOS Stream 8 or later
- RHEL 8 or later

If you have installed the Appcircle server with Docker:

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

You must use the same container engine with on the Appcircle server and the Appcircle DMZ server.

If you have installed the Appcircle server with Podman, you **must** use Podman on the Appcircle DMZ server.

If you have installed the Appcircle server with Docker, you **must** use Docker on the Appcircle DMZ server.

<Tabs>
  
  <TabItem value="podman" label="Podman" default>

#### Tools

You need to have the following tools installed on your system:

- curl
- tar
- podman
- podman-compose

You can install these dependencies from your package repository depending on your distro.

#### Enabling the Linger Option

<LingerOption/>

#### Overcoming Privileged Port Limitations

<SocatConfiguration/>

#### Podman Network Stack

<NetavarkConfiguration/>

  </TabItem>

  <TabItem value="docker" label="Docker" default>

#### Tools

You need to have the following tools installed on your system:

- curl
- tar
- docker
- docker compose

You can install these dependencies from your package repository depending on your distro.

  </TabItem>

</Tabs>

### Firewall Configuration

<Tabs>
  
  <TabItem value="rhel" label="RHEL/CentOS" default>

If you are using `Firewalld`, you need to open the ports below according to your server configuration.

- If you plan to run the Appcircle DMZ server with HTTPS:

```bash
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --add-port=443/tcp --permanent
sudo firewall-cmd --reload
```

- If you plan to run the Appcircle DMZ server with HTTP:

```bash
sudo firewall-cmd --add-port=80/tcp --permanent
sudo firewall-cmd --reload
```

To check if the ports are open, you can run the following command:

```bash
sudo firewall-cmd --list-ports
```

  </TabItem>

  <TabItem value="debian" label="Ubuntu/Debian" default>

If you are using `UFW (Uncomplicated Firewall)`, you need to open the 80 and 443 ports for the Appcircle DMZ server.

Check if the `ufw` is active.

```bash
sudo ufw status
```

If you see `Status: active` as the output, you should allow TCP 80 and TCP 443 ports for Appcircle DMZ server to accept connections.

```bash
sudo ufw allow 80 && \
sudo ufw allow 443
```

To check if the ports are open, you can run the following command:

```bash
sudo ufw status verbose
```

  </TabItem>

</Tabs>

#### SELinux

You must use the same SELinux mode on the Appcircle server and the Appcircle DMZ server.

You can check the SELinux mode with the command below.

```bash
getenforce
```

### DNS Entries

For Appcircle DMZ server to work successfully, you should configure the DNS records.

For the clients that will connect to the Appcircle DMZ server should resolve 3 domains; Enterprise App Store, Testing Distribution and authentication domains.

These domains should be resolved to the Appcircle DMZ server IP. The domains may vary according to the Appcircle server configuration. To check the current configured domains, you can follow the steps below:

- Login to the Appcircle server with SSH.

- Go to the Appcircle server directory.

```bash
cd appcircle-server
```

<SpacetechExampleInfo />

- Update the environment variable `PATH` with the required dependencies.

```bash
export PATH=$PATH:$(pwd)/deps/bin
```

- Check if your Enterprise App Store custom domain is enabled.

```bash
yq '.storeWeb.customDomain.enabled' ./projects/spacetech/export/.global.yaml
```

<Tabs>
  
  <TabItem value="custom-store-domain-enabled" label="Enterprise App Store Custom Domain Enabled" default>

- Check the Enterprise App Store custom domain.

```bash
yq '.storeWeb.customDomain.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
store.spacetech.com
```

  </TabItem>

  <TabItem value="custom-store-domain-disabled" label="Enterprise App Store Custom Domain Disabled" default>

- Check the Enterprise App Store default domain.

```bash
yq '.storeWeb.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
store.appcircle.spacetech.com
```

  </TabItem>

</Tabs>

- Check if your Testing Distribution custom domain is enabled.

```bash
yq '.testerWeb.customDomain.enabled' ./projects/spacetech/export/.global.yaml
```

<Tabs>
  
  <TabItem value="custom-tester-domain-enabled" label="Testing Distribution Custom Domain Enabled" default>

- Check the Testing Distribution custom domain.

```bash
yq '.testerWeb.customDomain.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
dist.spacetech.com
```

  </TabItem>

  <TabItem value="custom-store-domain-disabled" label="Enterprise App Store Custom Domain Disabled" default>

- Check the Testing Distribution default domain.

```bash
yq '.testerWeb.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
dist.appcircle.spacetech.com
```

  </TabItem>

</Tabs>

- Check the authentication domain of the Appcircle server.

```bash
yq '.keycloak.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
auth.appcircle.spacetech.com
```

- Check the API domain of the Appcircle server.

```bash
yq '.apiGateway.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
api.appcircle.spacetech.com
```

According to the sample outputs above, the needed domains that clients accessing via the internet should know are as follows:

- `store.spacetech.com`: Custom Enterprise App Store domain.
- `dist.spacetech.com`: Custom Testing Distribution domain.
- `auth.appcircle.spacetech.com`: Appcircle authentication domain.

Also the Appcircle DMZ server should be resolving some of the Appcircle server domains such as authentication and API domains.

These domains should be resolved to the Appcircle server IP. The domains may vary according to the Appcircle server configuration.

According to the sample outputs above, the needed domains that Appcircle DMZ server should know are as follows:

- `api.appcircle.spacetech.com`: Appcircle API domain.
- `auth.appcircle.spacetech.com`: Appcircle authentication domain.

:::caution
There is a common domain here. Be aware that the `auth` subdomain that the clients that will access from the internet and the Appcircle DMZ server will connect to should mean two different things.
:::

:::tip

You can change the Appcircle authentication domain for the users access from the internet and make it different from the internal domain using a custom domain. See the [FAQ](#how-can-we-change-the-appcircle-authentication-domain-on-the-dmz-server-for-internet-users) below for details.

:::

## Creating the Appcircle DMZ Server Configuration

To create the Appcircle DMZ server configuration, you should login to the Appcircle server.

You will create all the configuration files on the Appcircle server and then move the created configuration files to the Appcircle DMZ server.

To create the Appcircle DMZ server configuration, you can follow the steps below.

:::caution
If you modify the `global.yaml` configuration file for the Appcircle server, you **must** also update the configuration on the Appcircle DMZ server. Otherwise, Appcircle services may exhibit unusual behavior or malfunction.
:::

- Login to the Appcircle server with SSH.

- Go to the Appcircle server directory.

```bash
cd appcircle-server
```

- Stop the running Appcircle server.

<SpacetechExampleInfo />

```bash
./ac-self-hosted.sh -n spacetech down
```

- Create the new configuration files for the Appcircle DMZ and the Appcircle server.

```bash
./ac-self-hosted.sh -n spacetech export --dmz
```

:::info
The `--dmz` flag in the `export` subcommand above creates the configuration files according to your `global.yaml` file of your project for the both the Appcircle DMZ server and the Appcircle server.
:::

- Check the exported DMZ directory that contains the required files to create Appcircle DMZ server.

```bash
ls -lah projects/spacetech/export/dmz/
```

- Start the Appcircle server.

```bash
./ac-self-hosted.sh -n spacetech up
```

- Compress the directory into a tarball in the Appcircle server.

```bash
tar -czf dmz.tar.gz -C projects/spacetech/export/dmz/ .
```

- Transfer the `dmz.tar.gz` file to the Appcircle DMZ server with a file transfer protocol like `scp` or `ftp`.

## Creating the Appcircle DMZ Server

### Create Appcircle DMZ Directory

You need to create a directory for the Appcircle DMZ server and extract the transferred configuration files.

- Create a Appcircle DMZ server.

```bash
mkdir -p appcircle-server-dmz
```

- Extract the tarball you transferred from the Appcircle server.

```bash
tar -xzf dmz.tar.gz -C appcircle-server-dmz
```

- Change directory into the new directory.

```bash
cd appcircle-server-dmz
```

### Configure the System

Install the required packages and configurations on the system.

:::caution

You need to have root access on your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

Run the command without `sudo`. The script will ask for the user password if it's required.

:::

```bash
./ac-self-hosted-dmz.sh -i
```

### Starting the Appcircle DMZ Server

After you have configured the system with the steps above, you are ready to run the Appcircle DMZ server.

- Start the Appcircle DMZ server.

```bash
./ac-self-hosted-dmz.sh up
```

- Check the health of the Appcircle DMZ services.

```bash
./ac-self-hosted-dmz.sh check
```

:::caution
Be sure that all the services are running and healthy. If there are connection problems between the Appcircle DMZ server and the Appcircle server, the services won't be healthy.
:::

## Stopping the Appcircle DMZ Server

If you need to stop the Appcircle DMZ server in a case, you can run the the command below:

```bash
./ac-self-hosted-dmz.sh down
```

## Upgrading Appcircle DMZ and Appcircle server

If there is a new Appcircle server version available and you want to update, you can follow the steps below to update the Appcircle server and the Appcircle DMZ server.

:::caution
When upgrading an Appcircle server, it is critical to also update the Appcircle DMZ server. If you don't, Enterprise App Store and Testing Distribution may not function as expected.
:::

<DowntimeCaution />

- Login to the Appcircle DMZ server.

- Go to the Appcircle DMZ server directory.

```bash
cd appcircle-server-dmz
```

- Stop the Appcircle DMZ Server.

```bash
./ac-self-hosted-dmz.sh down
```

- Delete the Appcircle DMZ server directory.

```bash
cd .. && rm -rf appcircle-server-dmz
```

- Update the Appcircle server by following the [Update document](/self-hosted-appcircle/install-server/linux-package/update).

- Create the updated Appcircle DMZ configuration files by following the [Creating the Appcircle DMZ Server Configuration](#creating-the-appcircle-dmz-server-configuration) section.

- Create the new Appcircle DMZ server by following the [Creating the Appcircle DMZ Server](#creating-the-appcircle-dmz-server) section.

- Re-configure the Appcircle DMZ server by following the [Configure the System](#configure-the-system) section.

- Start the Appcircle DMZ server with the updated configurations by following the [Starting the Appcircle DMZ Server](#starting-the-appcircle-dmz-server) section.

## Appcircle DMZ Server Monitoring

By default, the Appcircle DMZ server will try to send the container logs to the Appcircle server.

You can check the container logs on the Appcircle monitoring page. For more details about checking the logs, you can check the [Monitoring](/self-hosted-appcircle/configure-server/monitoring) page.

## Restarting the Appcircle DMZ Server Host

For Docker users, there are built-in mechanisms that handle container restarts, eliminating the need for manual intervention.

However, Podman users will need to create a systemd unit service to ensure the application starts automatically upon server reboot.

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">

With Docker, you can rely on the built-in restart policies to handle the automatic startup of your Appcircle server.

Docker will automatically restart the server services if the host reboots.

This eliminates the need for any additional steps or configurations to ensure your application restarts upon host restart.

</TabItem>

<TabItem value="podman">

When using Podman, you will need to create a systemd unit service to enable the automatic startup of your application containers.

We have a dedicated section where we explain how to create the systemd file for Appcircle DMZ server services to start automatically when the host reboots.

You can follow the [Restarting Host](../restarting-host.md) document but there are two things to watch out on the "Restarting Host" document.

You will see the `ExecStart` line in the systemd service file like in the example below:

```bash
ExecStart=/bin/bash ${APPCIRCLE_SERVER_DIR}/ac-self-hosted.sh -n spacetech up
```

For the Appcircle DMZ server:

- The `ExecStart` line should contain Appcircle DMZ server directory and `ac-self-hosted-dmz.sh` as the command.
- There shouldn't be any project name. In the example above, you should remove the `-n spacetech` section.

A full example of `ExecStart` line should be:

```bash
ExecStart=/bin/bash /app/appcircle-server-dmz/ac-self-hosted-dmz.sh up
```

</TabItem>

</Tabs>

## Troubleshooting & FAQ

### How can we change the Appcircle authentication domain on the DMZ server for internet users?

You can use an additional custom domain for Appcircle authentication so that internet users can  access authentication services from the internet without using the internal `auth` [subdomain](/self-hosted-appcircle/install-server/linux-package/docker#4-dns-settings).

:::caution
The custom domain applies to the Appcircle DMZ server only. When connecting to the Appcircle server located within the private network, you should continue to utilize the default `auth` sudomain for Appcircle authentication services.
:::

Follow the steps below to make relevant configurations on the Appcircle server.

:::info

This feature is supported for Appcircle server version `3.22.0` or later.

:::

<DowntimeCaution/>

- Login to the Appcircle server with SSH.

- Change directory to Appcircle server.

```bash
cd appcircle-server
```

<SpacetechExampleInfo />

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add or update the `keycloak.dmzCustomDomain` parameter as below.

:::info

Please keep in mind that the `keycloak` key might already exist in your `global.yaml` file. In that case, find the key to add or update the `dmzCustomDomain` part.

If `keycloak` does not exist, then you can add it to the `global.yaml` file of your project.

:::

```yaml
keycloak:
  dmzCustomDomain:
    enabled: true
    domain: auth-ac.spacetech.com
```

- **[Upgrade](#upgrading-appcircle-dmz-and-appcircle-server)** the Appcircle server and DMZ server for changes to be applied.

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />