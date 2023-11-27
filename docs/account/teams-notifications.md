---
title: Microsoft Teams Notifications
metaTitle: Microsoft Teams Notifications
metaDescription: Microsoft Teams Notifications
sidebar_position: 9
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Microsoft Teams Notifications

Appcircle supports sending notifications to Microsoft Teams for the major events in all modules. You can connect Appcircle to your Microsoft Team channel to set up module-based event notifications to be sent to the selected channel.

## Adding Incoming Webhook to Microsoft Teams

In order to get notifications, the administrator of the channel should add an incoming webhook to the given channel. 

- Open the channel and click ••• from the upper-right corner and then click Connectors.

<NarrowImage width="200" src="https://cdn.appcircle.io/docs/assets/msteams-configure1.png" />

- Search for **Incoming Webhook** and click Configure

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure2.png' width='1592px' height='1558px' />

- Give your webhook a name and save it. It will give you a webhook URL

<ExternalScreenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure3.png' width='1594px' height='1483px' />

### Connecting Appcircle to Microsoft Teams

An Appcircle organization can be associated with a single Teams channel. To start, go to [My Organization](./my-organization.md) screen and press the "Connect" button next to Microsoft Teams under the "Connections" section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integrations-teams.png' />

Write the webhook URL that you created in the previous step and select the events you want to receive. You can set up notifications for the major events in each module (Build, Signing Identities, Distribute and Store Submission).

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure4.png' />


### Disconnecting Microsoft Teams

If you want to disconnect or reauthorize the Microsoft Teams connection, scroll down to the end of the management screen and press the "Disconnect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure5.png' />
