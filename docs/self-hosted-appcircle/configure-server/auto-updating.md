---
title: Auto Upgrading Server
description: Learn how to upgrade self-hosted Appcircle server with an automated way.
tags: [self-hosted server, update, upgrade, auto-update, auto-upgrade]
sidebar_position: 15
---

import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/configure-server/\_spacetech-example-info.mdx';

## Overview

In this document, you will see how to update the Appcircle server in a automated way.

The automated update tool streamlines the process of keeping your Appcircle Server up-to-date. It takes care of seamlessly downloading the latest release, extracting the necessary files, and applying any new configurations.

In the event of a minor or patch upgrade, the tool will gracefully stop the existing Appcircle Server, pull the updated container images, and restart the Appcircle Server with the new changes.

This automated approach ensures a smooth transition to the latest version, minimizing downtime and maximizing efficiency.

:::caution
The auto-update does not update the Appcircle server if there is a major AppCircle server update.
:::

:::info
The auto-update is included in App server package versions v3.16.0 and later.
:::

## Updating the Appcircle Server Semi-Automated

For a manual yet simplified update process of the App Server, you can leverage the auto-update via a single command.

The auto-update will do the following jobs automatically:

- Downloads the latest available Appcircle Server package for your organization.
- Checks if there is a major update. If yes, exits the script since the major upgrade may require a manual jobs. Please check the release page for detailed information.
- Unzips the downloaded Appcircle server package.
- Stops the Appcircle Server.
- Exports the updated configurations.
- Pulls the upgraded Appcircle Server container images.
- Starts the Appcircle Server.

:::caution
Please note that this process will cause downtime since it requires a restart of the Appcircle server.
:::

Change directory to the Appcircle Server.

```bash
cd appcircle-server
```

Run the auto-update tool for your project.

<SpacetechExampleInfo/>

```bash
./helper-tools/auto-update.sh -n "spacetech" update
```

## Updating the Appcircle Server Automated with Cronjob

To fully automate the update process of the App, you can leverage the auto-update tool to create a cronjob on the App Server.

Crontab is a scheduling utility that enables users to schedule tasks and commands to run at predetermined intervals.

By utilizing crontab, you can seamlessly automate minor or patch updates for the App Server, ensuring your application remains up-to-date without manual intervention.

### Enabling Passwordless Sudo

:::caution
To use the crontab, you **must** enable the passwordless sudo commands.
:::

Passwordless sudo allows authorized users or scripts to execute commands with superuser privileges without being prompted for a password, enhancing the automation capabilities of administrative tasks.

To activate passwordless sudo, you should edit the `sudoers` file.

```bash
sudo visudo
```

Find the line below.

:::info
The `wheel` in the example output below is the privileged group name that depends on the Linux distro you use.

For RHEL, it is generally `wheel`.
For Ubuntu, it might me `admin` or `sudo`.

You can also make sudo passwordless only for a user.
:::

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
0 3 * * 6 /home/user/appcircle-server/helper-tools/auto-update.sh -n "spacetech" update &>> /home/user/appcircle-server/appcircle-server-auto-update.log
...
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
./helper-tools/auto-update.sh -n "spacetech" install --cron-time "0 3 * * *"
```

Some sample cron times:

- At 3:00 AM every Sunday: `"0 3 * * 0"`
- At 3:00 AM first day of every month: `"0 3 1 * *"`

:::info

If you have enabled automated Appcircle Server update, you might want to consider cleaning the unused old Appcircle Server container images since this images will consume the disk.

You can and should delete all unused container images while the Appcircle Server is running.

```bash
docker image prune -a
```

:::
