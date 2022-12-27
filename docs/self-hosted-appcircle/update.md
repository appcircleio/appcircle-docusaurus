---
title: Update
metaTitle: Update Self-hosted Appcircle
metaDescription: Update Self-hosted Appcircle
sidebar_position: 3
---

# Overview

As in cloud, we're releasing regular updates for self-hosted appcircle server. You should keep your instance up-to-date in order to get latest features, bug fixes and improvements.

When a new version of self-hosted appcirle is released, you can update with below steps.

:::info

Prerequisites and dependencies are all same as installation steps. So we will keep it short in this page, try to document only update related details, and give references to installation when required.

When you're in trouble with update, it will be useful to review details and warnings written in [installation](./installation.md) docs.

:::

:::info

Below steps does not affect or destroy your data. Update process keeps your data and schema compatible with latest self-hosted appcircle server by using incremental migrations all handled automatically.

:::

### 1. Download Latest

Download the latest self-hosted appcircle package.

```bash
curl -o appcircle-server-linux-x64-1.0.2.zip -L https://cdn.appcircle.io/self-hosted/appcircle/appcircle-server-linux-x64-1.0.2.zip
```

Extract self-hosted appcircle package into folder.

```bash
unzip -o -u appcircle-server-linux-x64-1.0.2.zip -d appcircle-server
```

Change directory into extracted `appcircle-server` folder for following steps.

```bash
cd appcircle-server
```

For other details and troubleshooting, you can refer to [download](./installation.md#1-download) section in installation docs.

### 2. Update Packages

Although it's rare, update may have new packages or package updates. Those are the tools that self-hosted appcircle depends on. So they should be kept up-to-date same as appcircle server.

:::caution

You need to have root access on your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

:::

In order to update packages, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

You can also use the long option `--install-package` for the same purpose.

For other details and troubleshooting, you can refer to [packages](./installation.md#2-packages) section in installation docs.

### 3. Update Server

:::info

We're going on with the same sample scenario as in [installation](./installation.md#3-configure) steps.

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
./ac-self-hosted.sh -n "spacetech"
```

For other details and troubleshooting, you can refer to [configuration](./installation.md#3-configure) section in installation docs.

:::info

Although it's rare, self-hosted appcircle may have a new service with its dedicated subdomain.

If it was announced in release notes, you need to add new subdomain to your DNS server.

All process is same as in installation, so refer to [DNS settings](./installation.md#4-dns-settings) section in installation docs for details.

:::

### 4. Update Images

In order to get docker image updates for appcircle server services, we need to pull them from remote artifact repository.

`projects/your-project/export` path has all the exported envrionment for self-hosted appcircle services along with `compose.yaml`. For example,

```text
projects/
└── spacetech
    ├── export
    │   ├── agent-cache
    │   ├── api-gateway
    │   ├── build
    │   ├── common.env
    │   ├── compose.yaml
    │   ├── distribution
    │   ├── keycloak
    │   ├── keycloak-migration
    │   ├── license
    │   ├── minio
    │   ├── mongo
    │   ├── nginx
    │   ├── notification
    │   ├── postgres
    │   ├── report
    │   ├── rijndael
    │   ├── signing-identity
    │   ├── store
    │   ├── store-submit
    │   ├── tester-web
    │   ├── vault
    │   ├── webApp
    │   └── webhook
    ├── generated-secret.yaml
    ├── global.yaml
    └── user-secret
```

Change into the directory that exists `compose.yaml` file.

```bash
cd projects/spacetech/export
```

Pull docker images.

```bash
docker compose pull
```

To activate image updates, first stop all running docker containers.

```bash
docker compose down
```

Then start with below command.

```bash
docker compose up -d
```

When complete, check service statuses.

```bash
docker compose ps
```

If everything is okay, then you should see service statuses as "running", "running (healthy)" or "exited (0)".

:::caution

Please keep in mind that, restarting docker containers will stop all services until all started again. So, it will take some time and during that duration self-hosted appcircle server will be unreachable.

For this reason, you may prefer to execute this step on an idle time in order to minimize its negative effects on your users.

:::

For other details and troubleshooting, you can refer to [run server](./installation.md#5-run-server) section in installation docs.

## Notes

:::info

Above explained update steps keep all your data consistent and compatible. On most cases, data loss is an undesired case for an update scenario.

But if you want or need to reset your data for some reason, you can follow [reset configuration](./installation.md#reset-configuration) steps in installation docs.

:::

:::info

Although it's rare, self-hosted appcircle may require also self-hosted runner update. Because on some cases, it may bring some breaking changes for older runners.

If it's required, it will be announced in self-hosted appcircle release notes with minimum supported runner version.

In order to update your self-hosted runners, refer to [update self-hosted runner](../self-hosted-runner/update.md) section in docs.

For other details and troubleshooting, you can refer to [connecting runners](./installation.md#connecting-runners) section in installation docs.

:::
