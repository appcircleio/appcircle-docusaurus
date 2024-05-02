---
title: Auto Upgrading Server
description: Learn how to upgrade self-hosted Appcircle server with an automated way.
tags: [self-hosted server, update, upgrade, auto-update, auto-upgrade]
sidebar_position: 15
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';

## Overview

In this document, you will see how to update the Appcircle server in a automated way.

The auto update tool will handle the downloading, extracting, applying the new configurations, stopping the Appcircle server, pulling the new Appcircle server container images and starting the Appcircle server if there is minor or patch upgrade.

:::info
Auto update tool doesn't update the Appcircle server if there is a major Appcircle server update.
:::

:::info
The auto update tool is included in the Appcircle server packages that version is `v3.16.0` or later.
:::

## Updating the Appcircle Server Semi-Automated

If you want to update the Appcircle Server manually but with a single command, you can use the auto update tool.

The auto update tool will do the following jobs automatically:

- Downloads the latest available Appcircle Server package for your organization.
- Checks if there is an major update. If yes, exits the script since the major upgrade may require a manual jobs. Please check release page for detailed information.
- Unzips the downloaded Appcircle server package.
- Stops the Appcircle Server.
- Exports the new updated configurations.
- Pulls the upgraded Appcircle Server container images.
- Starts the Appcircle Server.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

Change directory to the Appcircle Server.

```bash
cd appcircle-server
```

Run the auto update tool for your project.

<SpacetechExampleInfo/>

```bash
./helper-tools/auto-update.sh -n "spacetech"
```

## Updating the Appcircle Server Automated with Cronjob

If you want to fully automate the update process of the Appcircle, you can use the auto update tool to create a cronjob on the Appcircle Server.

Crontab is a scheduling utility that allows users to schedule tasks and commands to run at specified intervals. With crontab, you can fully automate the minor or patch update processes of the Appcircle Server.

### Enabling Passwordless Sudo

:::caution
To use the crontab, you **must** enable the passwordless sudo commands.
:::

To activate passwordless sudo, you should edit the `sudoers` file.

```bash
sudo visudo
```

Find the line below.

```bash
...
%wheel ALL=(ALL)       ALL
...
```

Add `NOPASSWD:` to activate the passwordless sudo.

```bash
...
%wheel  ALL=(ALL)       NOPASSWD: ALL
...
```

### Creating the Crontab Job

To create a cronjob, you can simple use the auto update script.

<SpacetechExampleInfo/>

Create the crontab job with the command below.

```bash
./helper-tools/auto-update.sh -n "spacetech" install
```

Check if crontab job is activated.

```bash
crontab -l
```

You should see an example output like below:

```bash
...
0 3 * * 6 /home/user/appcircle-server/helper-tools/auto-update.sh -n "spacetech" &>> /home/user/appcircle-server/appcircle-server-auto-update.log
```

:::info
As you can see, the logs will be saved into a file named `appcircle-server-auto-update.log` in the `appcircle-server` directory. You can check the logs if you have any issues with the automated update.
:::

You can remove the crontab job if you don't need it.

```bash
./helper-tools/auto-update.sh -n "spacetech" remove
```

:::info
By default, the crontab job is defined to check and update the Appcircle Server at 3:00 AM every Saturday.
:::

You can change the cron time if you want to check and update the Appcircle Server at 3:00 AM every day.

```bash
./helper-tools/auto-update.sh -n "spacetech" --cron-time "0 3 * * *" install
```

Some sample cron times:

- At 3:00 AM every Sunday: `"0 3 * * 0"`
- At 3:00 AM first day of every month: `"0 3 1 * *"`

If you have enabled automated Appcircle Server update, you might want to consider cleaning the unused old Appcircle Server container images since this images will consume the disk.

You can and should delete all unused container images while the Appcircle Server is running.

```bash
docker image prune -a
```
