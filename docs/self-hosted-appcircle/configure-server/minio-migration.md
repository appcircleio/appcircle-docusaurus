---
title: MinIO Migration
description: Instructions on migrating from a multi-node single drive MinIO configuration to a single-node single drive MinIO configuration
tags: [minio, minio migration, single-node minio, multi-node minio]
sidebar_class_name: hidden
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

Older versions of the Appcircle server utilized MinIO in a multi-node single drive (**`mnsd`**) setup, which resulted in increased disk usage. By default, the Appcircle server utilizes MinIO in a single-node single drive (**`snsd`**) configuration with the Appcircle server version `3.14.0` or later.

With the transition to Appcircle server `3.14.0` and the adoption of single-node single drive (**`snsd`**) MinIO, disk consumption is anticipated to decrease by approximately 20%.

This documentation provides comprehensive instructions on migrating from a multi-node single drive MinIO configuration to a single-node single drive MinIO configuration that can be applied to recent versions of the Appcircle server.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

:::tip

Fresh self-hosted server installations do not require any manual intervention for the MinIO configuration.

The single-node single drive MinIO configuration is applied by default on fresh installations.

:::

## Prerequisites

For a successful migration from multi-node single drive MinIO to single-node single drive MinIO, it's essential to ensure adequate free disk space on the Appcircle server.

To determine the required disk space, follow the steps below:

- Log in to Appcircle server with SSH or remote connection.

- Get information about the "Used" and "Available" disk spaces where your container engine data is stored.

```bash
df -h
```

Below is a sample output for the command above.

```bash
Filesystem      Size  Used Avail Use% Mounted on
devtmpfs        5.7G     0  5.7G   0% /dev
tmpfs           5.8G     0  5.8G   0% /dev/shm
tmpfs           5.8G   20M  5.8G   1% /run
tmpfs           5.8G     0  5.8G   0% /sys/fs/cgroup
/dev/vda3        80G   21G   60G  26% /
/dev/vda2       100M  5.8M   95M   6% /boot/efi
tmpfs           1.2G     0  1.2G   0% /run/user/1000
```

- Get information about the disk usage of the container engine.

<Tabs groupId="container-engine">
  <TabItem value="docker" label="Docker" default>

```bash
docker system df
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
podman system df
```

  </TabItem>
</Tabs>

Below is a sample output for the command above.

```bash
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          39        38        12.77GB   1.081GB (8%)
Containers      45        41        12.08MB   4.055kB (0%)
Local Volumes   576       29        7.431GB   4.649GB (62%)
Build Cache     38        0         831.5MB   831.5MB
```

- Make sure you have half of the "Local Volumes" size of "Available" (free) disk space.
  - In our example above, we have 60 GB of "Available" (free) disk space, which should be sufficient for the migration since the "Local Volumes" have a size of 7.4 GB.

:::caution

If you don't have enough free disk space, the migration may fail, be interrupted, and stop.

Your data before the migration will be untouched and safe. So you can add some more free disk space and run the migration command again to migrate.

:::

## Migration

### Download Latest

Download the latest self-hosted Appcircle package.

To download the licensed Appcircle Server package for your organization, you must copy the `cred.json` file to the directory where you want to install the package.

:::info
Without the `cred.json` file, you will not be able to access the licensed Appcircle Server package.

If you have not yet obtained the `cred.json` file, please contact us for assistance.
:::

Download the latest self-hosted Appcircle package.

```bash
curl -fsSL https://cdn.appcircle.io/self-hosted/download-server.sh | bash
```

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

<SpacetechExampleInfo />

Shutdown the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

### Update Packages

Although it's rare, updates may have new packages or package updates. Those are the tools that the self-hosted Appcircle depends on. So they should be kept up-to-date, just like the Appcircle server.

:::caution

You need to have root access to your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

:::

In order to update packages, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

### Update Configuration

Migrating to a single-node single drive MinIO does not necessitate any additional configuration adjustments in the `global.yaml` file of the project.

Execute the below command to apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

### Update Images

In order to get container image updates for Appcircle server services, you need to pull them from the remote artifact repository.

:::caution
If you are updating the Appcircle server with the [Offline Upgrade](/self-hosted-appcircle/configure-server/offline-installation) method, you should `load` the new container images before the MinIO migration.

For more details, please head to the [Offline Upgrade](/self-hosted-appcircle/configure-server/offline-installation#upgrade) documentation and follow the steps before the MinIO migration.
:::

- Upgrade the container images.

```bash
./ac-self-hosted.sh -n "spacetech" upgrade
```

### MinIO Migration

:::info

You must apply one of the options below while updating the self-hosted Appcircle server.

:::

<Tabs>
  <TabItem value="snsd" label="Migrating to SNSD MinIO (recommended)" default>

Migration from multi-node single drive (**`mnsd`**) to single-node single drive (**`snsd`**) configuration can be accomplished seamlessly with a single command.

```bash
./ac-self-hosted.sh -n "spacetech" minio-migrate "mnsd" "snsd"
```

Upon successful completion of the migration process, you should see an output like in the example:

```text
...
Migration logs are being saved into the minio-migration-20240329082833.log file.
...
...
The migration command was completed successfully.
```

Detailed migration logs are being saved into a file named `minio-migration-${datetime}.log` where the `datetime` part is the current system date time in a format like `20240329082833`.

You can access and review the comprehensive migration logs from this file for further insights into the migration process.

:::caution
If you are using a proxy on the Appcircle server, then you should update the `no_proxy` variables.

Please follow the [No Proxy for Internal Container Network](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration.md#edit-no_proxy-for-internal-container-network) to update your proxy configuration for the new SNSD MinIO service.
:::

  </TabItem>

  <TabItem value="mnsd" label="Staying with MNSD MinIO">

:::note

Although that's not recommended, you can prefer to stay with a multi-node single drive MinIO.

Keep in mind that this type of MinIO usage is **deprecated**, and later versions of the self-hosted Appcircle server might drop support for multi-node single drive MinIO.

:::

In order to stay with the multi-node single drive (**`mnsd`**) MinIO configuration and not proceed with migration, it's necessary to specify the MinIO type in the `global.yaml` file of the project.

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add the below section to `global.yaml` and specify the `mnsd` value as the `minio.type`.

```yaml
minio:
  type: mnsd
```

- Then execute the below command to apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

  </TabItem>

</Tabs>

### Start the Server

- Start the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

:::tip
You should check the status of the Appcircle server after boot for any possible errors.

```bash
./ac-self-hosted.sh -n "spacetech" check
```

You should see the message: _"All services are running successfully."_

:::

## Troubleshooting & FAQ

### There is no space left on disk while migrating

If you can connect to the server via SSH, you can delete the **newly created** single-node single drive MinIO volume to free up disk space for stable system operations.

- List and filter the **`snsd`** volume from container volumes.

<Tabs groupId="container-engine">
  <TabItem value="docker" label="Docker" default>

```bash
docker volume ls | grep -i "snsd"
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
podman volume ls | grep -i "snsd"
```

  </TabItem>
</Tabs>

- Remove the your project's **`snsd`** volume. For example;

<Tabs groupId="container-engine">
  <TabItem value="docker" label="Docker" default>

```bash
docker volume rm spacetech_minio_snsd_data
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
podman volume rm spacetech_minio_snsd_data
```

  </TabItem>
</Tabs>

After that, you can cleanup the disk or add some more disk space for a successful migration.

Check the **[prerequisites](#prerequisites)** section for the required disk space.

If you want to go on without any migration and stay with an older configuration, you should follow the **[Staying with MNSD MinIO](#update-configuration)** section for configuration details.

### Possible checks that can be done after migration

In order to check if the migration is successful and the data is consistent, you can check some modules on the Appcircle dashboard.

Below is a short list of common modules that can be checked.

- [ ] Open a "Build Profile" and check the build logs.
- [ ] Open a "Publish Profile" and check the publish logs.
- [ ] Open a "Testing Distribution Profile" and check the app icons.
- [ ] Open "Enterprise App Store" module and check the app icons.

The migration command also prints output about the result of the migration operation on the command line.

### When you get an error while or after migrating

The migration operation does not delete the old MinIO volumes automatically. Your data before the migration is untouched and safe.

So if you face any error while migrating or after migrating to the SNSD MinIO, you can revert to the old MNSD MinIO configuration.

In this case follow the steps below to stay with MNSD MinIO configuration.

- Log in to Appcircle server with SSH or remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

<SpacetechExampleInfo />

- Stop the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add the below configuration section to `global.yaml`, or change the value as below if the `minio` section existed before.

```yaml
minio:
  type: mnsd
```

- Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

- Start the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

### Deleting the unused MinIO volumes after migration

If there are no errors while migrating and you are satisfied with the results after migration, you can delete the obsolete MinIO volumes to save free disk space.

In order to delete the unused MinIO volumes that were left from MNSD MinIO configuration, run the command below.

<SpacetechExampleInfo/>

<Tabs groupId="container-engine">
  <TabItem value="docker" label="Docker" default>

```bash
docker volume rm \
  spacetech_minio_data1 \
  spacetech_minio_data2 \
  spacetech_minio_data3 \
  spacetech_minio_data4
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
podman volume rm \
  spacetech_minio_data1 \
  spacetech_minio_data2 \
  spacetech_minio_data3 \
  spacetech_minio_data4
```

  </TabItem>
</Tabs>

<NeedHelp />

Have questions? [Contact us here.](https://appcircle.io/support/)
