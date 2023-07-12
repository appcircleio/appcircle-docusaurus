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

Docker will automatically restart them if the host server reboots.

This eliminates the need for any additional steps or configurations to ensure your application restarts upon server restart.

</TabItem>

<TabItem value="podman">

## Podman

When using Podman, you will need to create a systemd unit service to enable automatic startup of your application containers.

By creating a systemd unit file and configuring it to launch your Appcircle server, you can ensure that your application starts automatically upon server reboot.

To create a systemd unit service for automatic startup of Appcircle server, you can follow these steps:

:::info
For the steps below, you need sudo permission.
:::

- Create a unit service file and edit it:

```bash
sudo vim /etc/systemd/system/appcircle-server.service
```

- Add the following content to the file:

```systemd
[Unit]
Description=Appcircle Server
Wants=network-online.target
After=network-online.target
RequiresMountsFor=%t/containers

[Service]
Environment=PODMAN_SYSTEMD_UNIT=%n
User=spacetech-user
Group=spacetech-group
TimeoutStopSec=1000
PreStart=/usr/bin/loginctl enable-linger spacetech-user
ExecStart=/bin/bash /home/spacetech-user/appcircle-server/ac-self-hosted.sh -n spacetech up

Type=oneshot

[Install]
WantedBy=multi-user.target
```

:::caution
Please change the the fields below in the service file:

- User > Change to your username
- Group > Change to your group
- PreStart > change the spacetech-user to your username
- ExecStart > change the script path and project name which is spacetech in the example

:::

- Reload the systemd daemon and enable the Appcircle service:

```bash
sudo systemctl daemon-relaod
sudo systemctl enable appcircle-server.service
```

</TabItem>

</Tabs>

### Common Steps

These steps are common to both Docker and Podman installations:

1. Common Step 1
2. Common Step 2
3. Common Step 3

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">
## Docker title again

This is docker title

</TabItem>

<TabItem value="podman">
## Podman title again

This is podman title

</TabItem>

</Tabs>
