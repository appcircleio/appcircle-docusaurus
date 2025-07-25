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
sidebar_position: 50
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_spacetech-example-info.mdx';
import DmzHttpsRequirement from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-dmz-https-requirement.mdx';
import PortRedirection from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-dmz-port-redirection.mdx';
import LingerOption from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_linger-option.mdx';
import SocatConfiguration from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_socat-configuration.mdx';
import NetavarkConfiguration from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_podman-netavark-configuration.mdx';
import FirewalldConfiguration from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_firewalld-configuration.mdx';
import UFWConfiguration from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_ufw-configuration.mdx';
import SwapConfiguration from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_swap-configuration.mdx';
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-server-downtime-caution.mdx';
import Screenshot from '@site/src/components/Screenshot';

## Overview

A Demilitarized Zone (DMZ) in networking is a segment of an internal network that is exposed to external networks, typically over the internet. By isolating Appcircle DMZ server from the internal network, you ensure that it remains secure.

This is particularly useful when users need to access Testing Distribution and Enterprise App Store but not all features for business operations within the private network.

The Testing Distribution module and Enterprise App Store module hosted on the Appcircle DMZ server can be accessed by users from the internet, ensuring they have secure access to these critical features while keeping sensitive business data within your private network. This setup provides a balance between security and productivity in an organization's IT environment.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-5590-dmz-detailed-diagram.png' />

We assume that you have already set up an Appcircle server successfully. This document will guide you through creating Appcircle DMZ server and Appcircle server configurations.

In this document:

- We will call the "Appcircle DMZ server" to the server, which is located in the DMZ and host the Appcircle Enterprise App Store and Testing Distribution services.

- We will call the "Appcircle server" to the server, which is located in the private network and host the Appcircle core services.

:::info
The Appcircle DMZ server does not serve any content on port `80`. For more information on the use of `HTTP` port `80` by the Appcircle DMZ server, please refer to the [Firewall Configuration](#firewall-configuration).
:::

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

#### SELinux

You must use the same SELinux mode on the Appcircle server and the Appcircle DMZ server.

You can check the SELinux mode with the command below.

```bash
getenforce
```

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

:::info
<PortRedirection/>
:::

### HTTPS Requirement

<DmzHttpsRequirement/>

Due to this requirement, it is mandatory for the Appcircle DMZ server to be configured with `HTTPS`. For detailed instructions on configuring custom domains and `HTTPS` for the Enterprise App Store and Testing Distribution, please refer to the [SSL Configuration Guide](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/ssl-configuration). This guide will help you set up the necessary configurations in your Appcircle server's `global.yaml` file.

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

---

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

---

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

---

- Check if your DMZ Authentication custom domain is enabled.

```bash
yq '.keycloak.dmzCustomDomain.enabled' ./projects/spacetech/export/.global.yaml
```

<Tabs>
  
  <TabItem value="custom-dmz-auth-domain-enabled" label="Authentication DMZ Custom Domain Enabled" default>

- Check the Appcircle DMZ authentication custom domain.

```bash
yq '.keycloak.dmzCustomDomain.domain' ./projects/spacetech/export/.global.yaml
```

:::tip

You can change the Appcircle authentication domain for the users access from the internet and make it different from the internal domain using a custom domain. See the [FAQ](#how-can-we-change-the-appcircle-authentication-domain-on-the-dmz-server-for-internet-users) below for details.

:::

Output:

```
auth-appcircle.spacetech.com
```

  </TabItem>

  <TabItem value="custom-dmz-auth-domain-disabled" label="Authentication DMZ Custom Domain Disabled" default>

- Check the Appcircle DMZ default authentication domain.

```bash
yq '.keycloak.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
auth.appcircle.spacetech.com
```

  </TabItem>

</Tabs>

---

According to the sample outputs above, **when all the custom domains are enabled**, the domains that clients accessing via the internet should use are as follows:

- `store.spacetech.com`: Enterprise App Store custom domain.
- `dist.spacetech.com`: Testing Distribution custom domain.
- `auth-appcircle.spacetech.com`: DMZ Authentication custom domain.

According to the sample outputs above, **when all the custom domains are disabled**, the default domains that clients should use are:

- `store.appcircle.spacetech.com`: Enterprise App Store default domain.
- `dist.appcircle.spacetech.com`: Testing Distribution default domain.
- `auth.appcircle.spacetech.com`: DMZ default authentication domain.

:::tip
It's perfectly acceptable for **some custom domains to be enabled while others are disabled**.

For example, you might have a custom domain for the Enterprise App Store but use the default domain for Testing Distribution or DMZ Authentication.  
:::

:::info

#### CodePush (optional)

There is an optional domain name if you want to use the Appcircle server [CodePush](/code-push/) feature in the Appcircle DMZ server. You will configure this domain name in the Appcircle server `global.yaml` file in the following sections.

If you don't want to use the [CodePush](/code-push/) feature, you can skip the CodePush domain name configuration.

:::

---

Also the Appcircle DMZ server should be resolving some of the Appcircle server domains such as authentication, API and monitoring domains.

These domains should be resolved to the Appcircle server IP. The domains may vary according to the Appcircle server configuration.

- Check the authentication domain of the Appcircle server.

```bash
yq '.keycloak.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
auth.appcircle.spacetech.com
```

---

- Check the API domain of the Appcircle server.

```bash
yq '.apiGateway.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
api.appcircle.spacetech.com
```

---

- Check the monitoring domain of the Appcircle server.

```bash
yq '.grafana.external.domain' ./projects/spacetech/export/.global.yaml
```

Output:

```
monitor.appcircle.spacetech.com
```

According to the sample outputs above, the needed domains that Appcircle DMZ server should know are as follows:

- `api.appcircle.spacetech.com`: Appcircle API domain.
- `auth.appcircle.spacetech.com`: Appcircle authentication domain.
- `monitor.appcircle.spacetech.com`: Appcircle monitoring domain.

:::caution
There is a common domain here. Be aware that the `auth` subdomain that the clients that will access from the internet and the Appcircle DMZ server will connect to should mean two different things.
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

- (optional) If you want to use the [CodePush](/code-push/) feature in the Appcircle DMZ server, you need to configure the CodePush domain name and its SSL certificate in the Appcircle server `global.yaml` file.

<details>
    <summary>Click to see how to configure the CodePush feature in the Appcircle DMZ server.</summary>

:::note
CodePush DMZ server configuration requires Appcircle server `3.28.2` or later.
:::

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="podman">

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add or update the `codepushProxy` key as below.

```yaml
codepushProxy:
  enabled: true # Set to true to enable the CodePush feature on the Appcircle DMZ server
  external:
    port: 8443 # Set to 8443 to use the CodePush feature with HTTPS
    scheme: https # Set to https to use the CodePush feature with HTTPS
    domain: codepush.spacetech.com # Set the CodePush domain name as you want
    publicKey: | # Set the SSL certificate public key for the CodePush domain
      -----BEGIN CERTIFICATE-----
      MIIDqjCCAzCgAwIBAgISBiQ+pg7gN4ODAcGcxqy6+ZvtMAoGCCqGSM49BAMDMDIx
      ...
      RxFkhGCZddnB9p9x1p+ZJurRu13naXmHPpq+j3X1
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIEVzCCAj+gAwIBAgIRALBXPpFzlydw27SHyzpFKzgwDQYJKoZIhvcNAQELBQAw
      ...
      Ig46v9mFmBvyH04=
      -----END CERTIFICATE-----
    privateKey: | # Set the SSL certificate private key for the CodePush domain
      -----BEGIN PRIVATE KEY-----
      ...
      bSo6Ae6pgnQsFYyDGHQxHUwiNT7yXW0fel+k+yEHhXeLcDs40cPzr5c=
      -----END PRIVATE KEY-----
```

:::caution
The `codepushProxy.external.port` must be `8443` and `codepushProxy.external.scheme` must be `https` to use the CodePush feature in the Appcircle DMZ server with HTTPS.

Since we forward the `TCP/443` to the `TCP/8443` port with [Socat](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/installation/podman#overcoming-privileged-port-limitations) on the host, you will connect to the CodePush with the `TCP/443` port as usual from the internet.
:::

</TabItem>

<TabItem value="docker">

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add or update the `codepushProxy` key as below.

```yaml
codepushProxy:
  enabled: true # Set to true to enable the CodePush feature on the Appcircle DMZ server
  external:
    port: 443 # Set to 443 to use the CodePush feature with HTTPS
    scheme: https # Set to https to use the CodePush feature with HTTPS
    domain: codepush.spacetech.com # Set the CodePush domain name as you want
    publicKey: | # Set the SSL certificate public key for the CodePush domain
      -----BEGIN CERTIFICATE-----
      MIIDqjCCAzCgAwIBAgISBiQ+pg7gN4ODAcGcxqy6+ZvtMAoGCCqGSM49BAMDMDIx
      ...
      RxFkhGCZddnB9p9x1p+ZJurRu13naXmHPpq+j3X1
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIEVzCCAj+gAwIBAgIRALBXPpFzlydw27SHyzpFKzgwDQYJKoZIhvcNAQELBQAw
      ...
      Ig46v9mFmBvyH04=
      -----END CERTIFICATE-----
    privateKey: | # Set the SSL certificate private key for the CodePush domain
      -----BEGIN PRIVATE KEY-----
      ...
      bSo6Ae6pgnQsFYyDGHQxHUwiNT7yXW0fel+k+yEHhXeLcDs40cPzr5c=
      -----END PRIVATE KEY-----
```

:::caution
The `codepushProxy.external.port` must be `443` and `codepushProxy.external.scheme` must be `https` to use the CodePush feature in the Appcircle DMZ server with HTTPS.
:::

</TabItem>

</Tabs>

- After you have configured the CodePush feature on the Appcircle DMZ server with a new domain name, you need to update the `CodePushServerUrl` in the [CodePush SDK configuration](https://docs.appcircle.io/code-push/code-push-sdk#codepush-configurations-in-project) of your mobile application.

  - For example, if you have configured the CodePush feature on the Appcircle DMZ server with the `codepush.spacetech.com` domain name, you need to update the `CodePushServerUrl` in the [CodePush SDK configuration](https://docs.appcircle.io/code-push/code-push-sdk#codepush-configurations-in-project) of your mobile application to `https://codepush.spacetech.com` from the default `https://api.appcircle.spacetech.com/codepush` URL.

:::caution
Please make sure to remove the `/codepush` path from the `CodePushServerUrl`.
:::

</details>

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

You can check the container logs on the Appcircle monitoring page. For more details about checking the logs, you can check the [Monitoring](/self-hosted-appcircle/install-server/linux-package/configure-server/monitoring) page.

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

You can follow the [Restarting Host](../restarting-host) document but there are two things to watch out on the "Restarting Host" document.

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

You can use an additional custom domain for Appcircle authentication so that internet users can  access authentication services from the internet without using the internal `auth` [subdomain](/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings).

:::caution
The custom domain applies to the Appcircle DMZ server only. When connecting to the Appcircle server located within the private network, you should continue to utilize the default `auth` sudomain for Appcircle authentication services.
:::

Follow the steps below to make relevant configurations on the Appcircle server.

:::info

This feature is supported for Appcircle server version `3.26.1` or later.

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

:::info  

The authentication domain must always operate over HTTPS to ensure secure communication. Providing `.keycloak.dmzCustomDomain.publicKey` and `.keycloak.dmzCustomDomain.privateKey` is optional. You may define a custom SSL certificate specifically for the DMZ custom domain or rely on the existing certificate configured under `.nginx.sslCertificate`, as long as it also covers the DMZ custom domain.  

:::  

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">

```yaml
keycloak:
  dmzCustomDomain:
    enabled: true
    domain: auth-appcircle.spacetech.com
    port: 443
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
      ...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
      ...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
      ...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
      ...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `keycloak.dmzCustomDomain.port` must be `443` for Docker.
:::

</TabItem>

<TabItem value="podman">

```yaml
keycloak:
  dmzCustomDomain:
    enabled: true
    domain: auth-appcircle.spacetech.com
    port: 8443
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
      ...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
      ...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
      ...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
      ...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `keycloak.dmzCustomDomain.port` must be `8443` for Podman.

Since we forward the `TCP/443` to the `TCP/8443` port with [Socat](/self-hosted-appcircle/install-server/linux-package/installation/podman#overcoming-privileged-port-limitations) on the host, you will connect to the custom authentication domain with the `TCP/443` port.
:::

</TabItem>

</Tabs>

:::caution
If you enable the **DMZ custom domain** and configure **Single Sign-On (SSO)**, you must add the DMZ custom domain to your SSO provider's list of authorized redirect URLs.

Without this update, authentication requests from the DMZ domain will be blocked, causing SSO login failures due to unrecognized redirect URIs.
:::

- **[Upgrade](#upgrading-appcircle-dmz-and-appcircle-server)** the Appcircle server and DMZ server for changes to be applied.

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
