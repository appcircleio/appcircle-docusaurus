---
title: MinIO Migration Update
metaTitle: MinIO Migration Update
metaDescription: MinIO Migration Update
sidebar_class_name: hidden
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';

## Overview

By default, the Appcircle server utilizes MinIO in a single node single drive (`snsd`) configuration, employing version v3.14.0. Previous versions of the Appcircle server utilized MinIO in a multi-node single drive (`mnsd`) setup, which resulted in increased disk usage. However, with the transition to Appcircle server v3.14.0 and the adoption of `snsd` MinIO, disk consumption is anticipated to decrease by approximately 20%.

This documentation provides comprehensive instructions on migrating from the `mnsd` MinIO configuration to the `snsd` MinIO setup within the new Appcircle server version.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

## Prerequisites for Migrating

For a successful migration from mnsd MinIO to snsd MinIO, it's essential to ensure adequate free disk space on the Appcircle server.

To determine the required disk space, follow the steps below:

- SSH into the Appcircle server.

- Check the total disk space.
  - Check the "Used" and "Available" disk spaces where your container engine data is located.

```bash
df -h
```

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

- Check the disk usage of the container engine.

:::info
Change `docker` to `podman` if your container engine is Podman.
:::

```bash
docker system df
```

```bash
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          39        38        12.77GB   1.081GB (8%)
Containers      45        41        12.08MB   4.055kB (0%)
Local Volumes   576       29        7.431GB   4.649GB (62%)
Build Cache     38        0         831.5MB   831.5MB
```

- Make sure you have half of the "Local Volumes" size of "Available" free disk space from the `df -h` command output.

  - In our example, we have `60G` free disk space and `7.4GB` free disk space which is fine for the migration.

:::caution

If you don't have enough free disk space, the migration may fail, interrupted and stop.

Your old data will be untouched and saved. So you can add free disk space and run the migration command again to migrate.

:::

## Updating the Appcircle Server

### Download Latest

Download the latest self-hosted Appcircle package.

```bash
curl -O -L https://cdn.appcircle.io/self-hosted/appcircle/appcircle-server-linux-x64-3.10.1.zip
```

Extract self-hosted Appcircle package into folder.

```bash
unzip -o -u appcircle-server-linux-x64-3.10.1.zip -d appcircle-server
```

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

Although it's rare, update may have new packages or package updates. Those are the tools that self-hosted Appcircle depends on. So they should be kept up-to-date same as Appcircle server.

:::caution

You need to have root access on your system for this step. Being able to run `sudo` is sufficient for the following step. (sudoer)

:::

In order to update packages, execute the script using the `-i` argument as shown below.

```bash
sudo ./ac-self-hosted.sh -i
```

### Update Server

<Tabs>
  <TabItem value="snsd" label="Migrate to SNSD MinIO (Recommended)" default>

Migrating to `snsd` MinIO does not necessitate any additional configuration adjustments in the global.yaml file of the project.

Execute below command to apply new configurations.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

### MinIO Migrate

Migration from `mnsd` to `snsd` can be accomplished seamlessly with a single command.

```bash
./ac-self-hosted.sh -n "spacetech" minio-migrate "mnsd" "snsd"
```

Upon successful completion of the migration process, you should see an output like in the example:

```text
...
Migration logs are being saved into the minio-migration-20240329082833 file.
Migration command completed successfully.
```

Detailed migration logs are being saved into a file named `minio-migration-datetime` where datetime is the current system date time in a format like `20240329082833`.
You can access and review the comprehensive migration logs from this file for further insights into the migration process.

  </TabItem>

  <TabItem value="mnsd" label="Stay With MNSD MinIO">

To remain with the `mnsd` MinIO configuration and not proceed with migration, it's necessary to specify the MinIO type in the `global.yaml` file of the project.

Edit the `global.yaml` file.

```bash
vi ./projects/spacetech/global.yaml
```

Add the `minio` and `type` keys. Specify the `mnsd` as the type.

```yaml
minio:
  type: mnsd
```

Then execute below command to apply new configurations.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

  </TabItem>

</Tabs>

### Update Images

In order to get container image updates for Appcircle server services, we need to pull them from remote artifact repository.

Upgrade the container images.

```bash
./ac-self-hosted.sh -n "spacetech" upgrade
```

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

## Notes

### If the Disk is Full-Filled While Migration

If you can connect to the server via SSH, you can delete the **new** `snsd` minio volume to free up disk space for initial stable system operation.

```bash
docker volume ls | grep -i "snsd"
docker volume rm spacetech_minio_snsd_data
```

Then if you want to migrate to `snsd` minio, you should clear the system and check the free disk space. Check the [Prerequirements](#prerequisites-for-migrating) section for the needed disk space. If needed, you can increase the disk size of the server.

If you want to update without the migration, you can follow the "Stay With MNSD MinIO" title.

### Testing the Migration

To test if the migration is successful and the data is consisted, you can check the steps below.

- Open an "Build Profile" and check the build logs.

- Open an "Publish Profile" and check the publish logs.

- Open an "Testing Distribution Profile" and check the app icons.

- Open the "Enterprise App Store" and check the app icons.

### If you face an migration error.

This migration operation doesn't delete the old minio volumes. So if you face any error while migrating or after migrated to the `SNSD` minio type, you can head back to the old `MNSD` minio type.

To go back to `MNSD` minio type, edit the `global.yaml` file of your project and change the minio type.

Stop the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

```yaml
minio:
  type: mnsd
```

Then apply the new configurations.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

Start the Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" start
```

### Deleting the Old Volumes

If there is no errors while [Testing the Migration](#testing-the-migration), you can delete the old minio volumes to save disk space.

- To delete the old volumes, you can simple run the command below.

:::info
Please change the `spacetech` with your actual project name and change the `docker` to `podman` if you are using podman.
:::

```bash
docker volume rm spacetech_minio_data1 spacetech_minio_data2 spacetech_minio_data3 spacetech_minio_data4
```
