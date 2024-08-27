---
title: Microsoft Teams Notifications
description: Appcircle supports sending notifications to Microsoft Teams for the major events in all modules. You can connect Appcircle to your Microsoft Team channel to set up module-based event notifications to be sent to the selected channel.
tags:
  [
    notifications,
    communication,
    microsoft teams,
    teams notifications,
    teams integration,
    webhooks,
    hooks
  ]
sidebar_position: 4
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

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure2.png' />

- Give your webhook a name and save it. It will give you a webhook URL

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure3.png' />

### Connecting Appcircle to Microsoft Teams

An Appcircle organization can be associated with a single Teams channel. To start, go to [My Organization](/account/my-organization) screen and press the "Connect" button next to Microsoft Teams under the "Connections" section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/integrations-teams.png' />

Write the webhook URL that you created in the previous step and select the events you want to receive. You can set up notifications for the major events in each module (Build, Signing Identities, Distribute and Store Submission).

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure4.png' />

:::info
After completing the specified action in Appcircle, you have the option to share release notes via Microsoft Teams.
To enable this feature, ensure you include the [**Publish Release Notes**](https://docs.appcircle.io/workflows/common-workflow-steps/publish-release-notes/) step in your workflow.

Additionally, note that you can access download links for the release notes for a duration of 90 days.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/2446-ReleaseNotesViaEmail.png' />

:::info
After completing the specified action in Appcircle, you have the option to share the test results via Microsoft Teams.
To enable this feature, ensure you include the [**Test Reports**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests#generating-test-report) step in your workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/2446-TestReportsViaEmail.png' />

### Disconnecting Microsoft Teams

If you want to disconnect or reauthorize the Microsoft Teams connection, scroll down to the end of the management screen and press the "Disconnect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure5.png' />
