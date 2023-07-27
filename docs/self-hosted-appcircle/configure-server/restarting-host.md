---
title: Restarting Host
metaTitle: Restarting Host and Appcircle Server
metaDescription: Restarting Host and Appcircle Server
sidebar_position: 6
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Overview

In this section, we will discuss how to enable automatic startup of your Appcircle server.

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

## Docker

With Docker, you can rely on the built-in restart policies to handle the automatic startup of your Appcircle server.

Docker will automatically restart the server services if the host reboots.

This eliminates the need for any additional steps or configurations to ensure your application restarts upon host restart.

</TabItem>

<TabItem value="podman">

## Podman

When using Podman, you will need to create a systemd unit service to enable the automatic startup of your application containers.

By creating a systemd unit file and configuring it to launch your Appcircle server, you can ensure that your application starts automatically upon host reboot.

To create a systemd unit service for automatic startup of the Appcircle server, you can follow these steps:

:::caution
You need to have root access on your system for the steps below. Being able to run `sudo` is required. (sudoer)
:::

- Create a unit service file.

```bash
sudo vi /etc/systemd/system/appcircle-server.service
```

- Add the following content to the file.

```systemd
[Unit]
Description=Appcircle Server
Wants=network-online.target
After=network-online.target
RequiresMountsFor=%t/containers

[Service]
Environment=PODMAN_SYSTEMD_UNIT=%n
User=${USER}
Group=${GROUP}
ExecStartPre=/usr/bin/loginctl enable-linger ${USER}
ExecStart=/bin/bash ${APPCIRCLE_SERVER_DIR}/ac-self-hosted.sh -n spacetech up
Type=oneshot
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

As seen above, some fields have variables(`${.}`) that **must be replaced with the exact values**, according to your runtime environment.

:::caution
You must edit the fields in the service file before enabling the service.
::::

- **User:** Replace `${USER}` with your logged in user which is expected to be the owner of the Appcircle server directory.

```bash
stat -c "%U" appcircle-server
```

- **Group:** Replace `${GROUP}` with your logged in user's group which is expected to be the owner of the Appcircle server directory.

```bash
stat -c "%G" appcircle-server
```

- **PreStart:** Replace `${USER}` with your logged in user. It should have the same value as **User** field above.

- **ExecStart:** Replace `${APPCIRCLE_SERVER_DIR}` with the absolute path of the Appcircle server directory.

```bash
realpath appcircle-server
```

Also, do not forget to **change the project name to your project**, since "spacetech" is our sample project in the documents.

You can get a list of your projects in Appcircle server directory with the command below.

```bash
ls -d -1 appcircle-server/projects/*/ | xargs -n 1 basename
```

When the systemd unit file is ready, we need to enable it with the commands below:

- Reload the systemd daemon to make it aware that a new service exists.

```bash
sudo systemctl daemon-reload
```

- Enable the service.

```bash
sudo systemctl enable appcircle-server.service
```

Now, the service is supposed to start on boot, and it should start the Appcircle server when triggered.

</TabItem>

</Tabs>
