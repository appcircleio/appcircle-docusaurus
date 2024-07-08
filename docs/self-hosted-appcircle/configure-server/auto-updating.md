---
title: Auto-upgrading Server
description: Learn how to upgrade a self-hosted Appcircle server automatically.
tags: [self-hosted server, update, upgrade, auto-update, auto-upgrade, crontab]
sidebar_position: 15
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';

## Overview

In this document, you will learn how to update the Appcircle server automatically.

The automated update tool streamlines the process of keeping your Appcircle server up-to-date. It takes care of seamlessly downloading the latest release, extracting the necessary files, and applying any new configurations.

In the event of a minor or patch upgrade, the tool will gracefully stop the existing Appcircle server, pull the updated container images, and restart the Appcircle server with the new changes.

This automated approach ensures a smooth transition to the latest version, minimizing downtime and maximizing efficiency.

:::caution
The auto-update tool does not update the Appcircle server in the event of a major Appcircle server update.
:::

:::caution
The auto-update tool does not currently support the handling of proxy environment variables. Therefore, it is not recommended to use this tool on an Appcircle server that use proxy environment variables.
:::

:::info
The auto-update tool is included in the Appcircle server package version `3.16.0` or later.
:::

## Updating the Server on Demand

For a manual yet simplified update process of the Appcircle server, you can leverage the auto-update via a single command.

The auto-update will do the following jobs automatically:

- Downloads the latest available Appcircle server package for your organization.
- Checks the package version for a possible major upgrade.
  - _If yes, exits gracefully since the major upgrade might require manual jobs. Please check the release notes for detailed information in this case._
- Extracts the downloaded Appcircle server package.
- Stops the Appcircle server.
- Exports the updated configurations.
- Pulls the updated container images.
- Starts the Appcircle server.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

In order to perform above operations with a single command call, follow the steps below.

Change the directory to the Appcircle server.

```bash
cd appcircle-server
```

<SpacetechExampleInfo/>

Run the auto-update tool for your project.

```bash
./helper-tools/auto-update.sh -n "spacetech" update
```

## Updating the Server Scheduled

To fully automate the update process of the Appcircle, you can leverage the auto-update tool to create a cronjob on the Appcircle server.

Crontab is a scheduling utility that enables users to schedule tasks and commands to run at predetermined intervals.

By utilizing crontab, you can seamlessly automate minor or patch updates for the Appcircle server, ensuring your application remains up-to-date without manual intervention.

:::caution
If you are updating the Appcircle server with the [Offline Upgrade](/self-hosted-appcircle/configure-server/offline-installation.md#upgrade) method, then you can't use auto-update tool since it requires some network access to download the Appcircle server package and up-to-date container images.
:::

### Enable Passwordless Sudo

:::caution
To use the crontab, you **must** enable the passwordless `sudo` commands.
:::

Passwordless `sudo` allows authorized users or scripts to execute commands with superuser privileges without being prompted for a password, enhancing the automation capabilities of administrative tasks.

To activate passwordless `sudo`, you should edit the `sudoers` file.

```bash
sudo visudo
```

Find the line below in the `sudoers` file.

```txt
%wheel ALL=(ALL)       ALL
```

:::caution
The **`wheel`** in the example output above is the privileged group name that depends on the Linux distribution you use.

For RHEL or its derivatives, it is generally `wheel`. For Ubuntu or Debian derivatives, it can be one of `admin` or `sudo`.

You can also enable passwordless sudo only for a user. Please refer to your Linux distribution's user manuals for details.
:::

Add `NOPASSWD:` to activate the passwordless sudo.

```txt
%wheel  ALL=(ALL)       NOPASSWD: ALL
```

### Create the Crontab Job

To create a cronjob, you can simply use the auto-update tool commands.

Change the directory to the Appcircle server.

```bash
cd appcircle-server
```

<SpacetechExampleInfo/>

Create the crontab job with the command below.

```bash
./helper-tools/auto-update.sh -n "spacetech" install
```

Check if crontab job is activated.

```bash
crontab -l
```

You should see the newly added crontab entry in the list of jobs, like below:

```txt
0 3 * * 6 /home/user/appcircle-server/helper-tools/auto-update.sh -n "spacetech" update &>> /home/user/appcircle-server/appcircle-server-auto-update.log
```

:::info
As you can see in the above job definition, the logs will be saved into a file named

- `appcircle-server-auto-update.log`

in the `appcircle-server` directory. You can check the logs if you have any issues with the automated update.
:::

:::tip
By default, the crontab job is defined to check and update the Appcircle server at 3:00 AM every Saturday.
:::

You can remove the crontab job if you don't need it anymore with the below command.

```bash
./helper-tools/auto-update.sh -n "spacetech" remove
```

You can change the crontab schedule if you want to check and update the Appcircle server, for instance, at 3:00 AM every day.

```bash
./helper-tools/auto-update.sh -n "spacetech" install --cron-time "0 3 * * *"
```

Below are some sample crontab schedules that can be used for scheduled upgrades.

- At 3:00 AM every Sunday: `0 3 * * 0`
- At 3:00 AM first day of every month: `0 3 1 * *`

:::tip

If you have enabled automated Appcircle server updates, you might want to consider cleaning the unused old Appcircle server container images since these images will consume the disk and won't be used at runtime.

You can use the below command for this purpose to clean up unused container images. However **it should be called while the Appcircle server is running** smoothly.

```bash
docker image prune -a
```

It will remove all images without at least one container associated with them so that the container images that are used by containers will not be affected.

:::
