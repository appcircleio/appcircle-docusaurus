---
title: Slack Notifications
metaTitle: Slack Notifications
metaDescription: Slack Notifications
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Slack Notifications

Appcircle supports sending notifications to Slack for the major events in all modules. You can connect Appcircle to your Slack workspace to set up module based event notifications to be sent to the selected channels.

:::info

There is currently no Slack integration available on the self-hosted Appcircle. However, we are actively working on it and it will be available for use on the self-hosted Appcircle in the near future.

:::

### Connecting Appcircle to Slack

An Appcircle organization can be associated with a single Slack workspace. To start, go to [My Organization](../my-organization.md) screen and press the "Connect" button next to Slack under the "Connections" section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (64).png' />

Provide permission to the Appcircle app on Slack so that the channel list can be fetched for selection and the status can be sent as a message.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (65).png' />

You will then see that Slack is connected. To manage the notification settings or to disconnect, press the "Manage" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (135).png' />


### Setting Up Module-Based Notifications in the Slack Settings

You can set up notifications for the major events in each module (Build, Signing Identities, Distribute and Store Submission).

To enable notifications for a specific event, first select the Slack channel that will receive the notifications for the specific module and then use the toggle to enable the event notifications.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (136).png' />

### Disconnecting Slack

If you want to disconnect or reauthorize the Slack connection, scroll down to the end of the management screen and press the "Disconnect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (137).png' />

The full list of the available options can be viewed as follows:

<NarrowImage src="https://cdn.appcircle.io/docs/assets/screenshot-my.appcircle.io-2021.02.11-00_01_23.png" />
