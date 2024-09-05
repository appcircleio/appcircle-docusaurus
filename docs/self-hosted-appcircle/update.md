---
title: Upgrading Server
description: Learn how to upgrade self-hosted Appcircle server
tags: [self-hosted server, update, upgrade]
sidebar_position: 3
---

import RedisDomainCaution from '@site/docs/self-hosted-appcircle/configure-server/\_redis-domain-caution.mdx';

# Overview

As in cloud, we're releasing regular updates for self-hosted Appcircle server. You should keep your instance up-to-date in order to get latest features, bug fixes and improvements.

When a new version of self-hosted Appcircle is released, you can update with below steps.

:::info

Prerequisites and dependencies are all same as installation steps. So we will keep it short in this page, try to document only update related details, and give references to installation when required.

When you're in trouble with update, it will be useful to review details and warnings written in [installation](/self-hosted-appcircle/install-server/docker) docs.

:::

:::info

Below steps does not affect or destroy your data. Update process keeps your data and schema compatible with latest self-hosted Appcircle server by using incremental migrations all handled automatically.

:::

:::info

To determine the current version of either a project or the script itself, use the version command provided with the script. This will display the script version and any docker image hashes associated with the project. If no docker images are found, the command will output script version only.

Note that a project name is required to execute the version command.

For example, to find the version for a project named "spacetech", run the following command:

```bash
./ac-self-hosted.sh -n "spacetech" version
```

:::

:::tip

#### ✨ Auto-upgrading Server

If you want to update the Appcircle server in an automated way, you can check out the [Auto-upgrading Server](/self-hosted-appcircle/configure-server/auto-updating) documents.

You can effortlessly manage all the commands listed below.

Additionally, you can set up recurring cron jobs (daily or weekly) to automatically check if Appcircle's server needs updating.
:::

:::caution
If you are using the Appcircle DMZ structure and upgrading an Appcircle server, it is critical to also update the Appcircle DMZ server. If you don't, Enterprise App Store and Testing Distribution may not function as expected.

For more information about the DMZ structure, you can check the [Appcircle DMZ documentation](/self-hosted-appcircle/configure-server/advanced-configuration/store-dist-dmz).
:::

#### Version History

Below is the version history of the self-hosted Appcircle server. This table helps you track the latest updates and releases since your current version.

| Version | Release Date |
|---------|--------------|
| 3.20.4  | 26/08/2024   |
| 3.20.3  | 20/08/2024   |
| 3.20.2  | 16/08/2024   |
| 3.20.1  | 07/08/2024   |
| 3.19.1  | 19/07/2024   |
| 3.18.0  | 14/06/2024   |
| 3.17.2  | 30/05/2024   |
| 3.17.1  | 25/05/2024   |
| 3.17.0  | 21/05/2024   |
| 3.16.0  | 14/05/2024   |
| 3.15.1  | 11/05/2024   |
| 3.15.0  | 26/04/2024   |
| 3.14.0  | 17/04/2024   |
| 3.13.2  | 15/03/2024   |
| 3.13.1  | 07/03/2024   |
| 3.12.3  | 21/02/2024   |
| 3.12.2  | 19/02/2024   |
| 3.12.1  | 12/02/2024   |

### 1. Download Latest

To download the licensed Appcircle Server package for your organization, you must copy the `cred.json` file to the directory where you want to install the package. This typically means copying the `cred.json` file to the same directory containing the `appcircle-server` directory.

:::info
Without the `cred.json` file, you will not be able to access the licensed Appcircle Server package.

If you have not yet obtained the `cred.json` file, please contact us for assistance.
:::

Download the latest self-hosted Appcircle package.

```bash
curl -fsSL https://cdn.appcircle.io/self-hosted/download-server.sh | bash
```

:::tip
By default, the command above downloads the latest available Appcircle server version.

You can specify a specific version using the `--package-version` option or `AC_SERVER_VERSION` environment variable..

For instance, suppose there are multiple versions available (e.g. `3.14.0`, `3.14.1`, `3.14.2`, and `3.15.0`) and you want to download version `3.14.1`. To achieve this, simply run the command below:

```bash
curl -fsSL https://cdn.appcircle.io/self-hosted/download-server.sh | AC_SERVER_VERSION=3.14.1 bash
```

Alternatively, if you wish to download the latest package in the 3.14.x series (which would be version 3.14.2), use the following command:

```bash
curl -fsSL https://cdn.appcircle.io/self-hosted/download-server.sh | AC_SERVER_VERSION=3.14 bash
```

:::

:::caution

Upgrading from older versions to `3.14.0` or later requires MinIO migration, which should be done interactively while upgrading.

In order to migrate to single-node single drive MinIO configuration or stay with the deprecated multi-node single drive MinIO configuration, **you must follow the instructions** that are defined in the [MinIO Migration](/self-hosted-appcircle/configure-server/minio-migration) document.

:::

<RedisDomainCaution/>

Extract self-hosted Appcircle package into folder.

```bash
unzip -o -u appcircle-server-linux-x64-${version}-${build}.zip -d appcircle-server
```

:::info

You should use the downloaded `zip` archive while extracting so that the actual `${version}` and `${build}` will come from there. You can find the relevant data in the previously executed download command output.

:::

Change directory into extracted `appcircle-server` folder for following steps.

```bash
cd appcircle-server
```

For other details and troubleshooting, you can refer to [download](/self-hosted-appcircle/install-server/docker#1-download) section in installation docs.

:::info

After version `3.7.1`, the container image versions, pulled from the Appcircle artifact registry, will be the same version of the Appcircle zip package you downloaded.

In this case, if you download an older version of the Appcircle zip package, the container images will also be older versions.

So as a result, you will downgrade the Appcircle server if you download an older version zip package.

:::

### 2. Update Packages

Although it's rare, update may have new packages or package updates. Those are the tools that self-hosted Appcircle depends on. So they should be kept up-to-date same as Appcircle server.

:::caution

You need to have root access on your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

:::

In order to update packages, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

You can also use the long option `--install-package` for the same purpose.

For other details and troubleshooting, you can refer to [packages](/self-hosted-appcircle/install-server/docker#2-packages) section in installation docs.

### 3. Update Server

:::info

We're going on with the same sample scenario as in [installation](/self-hosted-appcircle/install-server/docker#3-configure) steps.

Let's assume we have company named as Space Tech and our project name is "spacetech". For the following steps, we will give examples based on this fictive company for better understanding.

:::

If update has new features with their configuration options or you want to make some minor changes in your configuration, first edit your `global.yaml` file.

```txt
projects
└── spacetech
    ├── export
    ├── generated-secret.yaml
    ├── global.yaml
    └── user-secret
```

In most cases, you don't need to change anything in your configuration. So, above step is optional.

Then execute below command to update server.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

For other details and troubleshooting, you can refer to [configuration](/self-hosted-appcircle/install-server/docker#3-configure) section in installation docs.

:::info

Although it's rare, self-hosted Appcircle may have a new service with its dedicated subdomain.

If it was announced in release notes, you need to add new subdomain to your DNS server.

All process is same as in installation, so refer to [DNS settings](/self-hosted-appcircle/install-server/docker#4-dns-settings) section in installation docs for details.

:::

### 4. Update Images

In order to get docker image updates for Appcircle server services, we need to pull them from remote artifact repository.

To activate image updates, first stop all running docker containers.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

Upgrade images.

```bash
./ac-self-hosted.sh -n "spacetech" upgrade
```

:::caution
If you are using a proxy on the server, then you should maintain the proxy variables.

Please head to the [Maintenance of Proxy Variables](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration.md#maintenance-of-no_proxy-variables) for more details.
:::

Then start with below command.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

When complete, check service statuses.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You may also print the image hashes and script's version by using the below command.

```bash
./ac-self-hosted.sh -n "spacetech" version
```

:::caution

Please keep in mind that, restarting docker containers will stop all services until all started again. So, it will take some time and during that duration self-hosted Appcircle server will be unreachable.

For this reason, you may prefer to execute this step on an idle time in order to minimize its negative effects on your users.

:::

For other details and troubleshooting, you can refer to [run server](/self-hosted-appcircle/install-server/docker#6-run-server) section in installation docs.

## Notes

:::info

Above explained update steps keep all your data consistent and compatible. On most cases, data loss is an undesired case for an update scenario.

But if you want or need to reset your data for some reason, you can follow [reset configuration](/self-hosted-appcircle/install-server/docker#reset-configuration) steps in installation docs.

:::

:::info

Although it's rare, self-hosted Appcircle may require also self-hosted runner update. Because on some cases, it may bring some breaking changes for older runners.

If it's required, it will be announced in self-hosted Appcircle release notes with minimum supported runner version.

In order to update your self-hosted runners, refer to [update self-hosted runner](/self-hosted-appcircle/self-hosted-runner/update) section in docs.

For other details and troubleshooting, you can refer to [connecting runners](/self-hosted-appcircle/install-server/docker#connecting-runners) section in installation docs.

:::
