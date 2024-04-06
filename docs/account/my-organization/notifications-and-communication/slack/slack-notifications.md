---
title: Slack Notifications
description: Set up Slack notifications for major events in Appcircle. Enhance your team's communication with module-based alerts.
tags: [notifications, communication, slack, slack notifications, slack integration]
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

An Appcircle organization can be associated with a single Slack workspace. To start, go to [My Organization](/account/my-organization) screen and press the "Connect" button next to Slack under the "Connections" section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (64).png' />

Provide permission to the Appcircle app on Slack so that the channel list can be fetched for selection and the status can be sent as a message.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (65).png' />

You will then see that Slack is connected. To manage the notification settings or to disconnect, press the "Manage" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (135).png' />

### Setting Up Module-Based Notifications in the Slack Settings

You can set up notifications for the major events in each module (Build, Signing Identities, Distribute and Store Submission).

To enable notifications for a specific event, first select the Slack channel that will receive the notifications for the specific module and then use the toggle to enable the event notifications.

:::caution

Due to a technical limitation, subscribing events to a private Slack channel(s) is not possible at this moment.

:::

:::info

You can customize which Slack events to get by selecting or deselecting specific events. You can also set different Slack channels for different kinds of events.

Keep scrolling down on Appcircle to see the full list of events.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (136).png' />

:::info
After completing the specified action in Appcircle, you have the option to share release notes via Slack.
To enable this feature, ensure you include the [**Publish Release Notes**](https://docs.appcircle.io/integrations/managing-release-notes/) step in your workflow.

Additionally, note that you can access download links for the release notes for a duration of 90 days.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/2446-ReleaseNotesViaEmail.png' />

:::info
After completing the specified action in Appcircle, you have the option to share the test results via Slack.
To enable this feature, ensure you include the [**Test Reports**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests#generating-test-report) step in your workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/2446-TestReportsViaEmail.png' />

### Disconnecting Slack

If you want to disconnect or reauthorize the Slack connection, scroll down to the end of the management screen and press the "Disconnect" button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (137).png' />
