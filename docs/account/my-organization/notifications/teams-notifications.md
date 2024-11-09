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
import NeedHelp from '@site/docs/\_need-help.mdx';

# Microsoft Teams Notifications

Appcircle supports sending notifications to Microsoft Teams for the major events in all modules. You can connect Appcircle to your Microsoft Team channel to set up module-based event notifications to be sent to the selected channel.

## Adding Incoming Webhook to Microsoft Teams

In order to get notifications, the administrator of the channel should add an incoming webhook to the given channel.

- Click the ••• button to the right of `General` under the channel and then click `Manage Channel` [2].

- On the openned screen, click on the `Edit` button under the `Connector` header [3].

<Screenshot url="https://cdn.appcircle.io/docs/assets/msteams-configure1.png" />

- Search for **Incoming Webhook** and click Configure.

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure2.png' />

- Give your webhook a name and save it. It will give you a webhook URL.

<Screenshot url='https://cdn.appcircle.io/docs/assets/msteams-configure3.png' />

### Connecting Appcircle to Microsoft Teams

An Appcircle organization can be associated with a single Teams channel. To start, go to [My Organization](/account/my-organization) > Notifications screen and press the "Connect" button next to Microsoft Teams under the "Notification Providers" section.

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

## Troubleshooting & FAQ

### Notifications are not delivered when using self-hosted Appcircle.

If your Microsoft Teams notifications are not delivered while using the self-hosted Appcircle, there can be 3 reasons for this to check.

**1.** Proxy Requirement

If you are using a proxy to connect to the internet on the host, the proxy must also be enabled for the Appcircle services too, that is, in the containers. You can refer to the [**Proxy Configuration**](/self-hosted-appcircle/configure-server/integrations-and-access/proxy-configuration.md) documentation to see how to configure proxy for the self-hosted Appcircle server.

**2.** Network Access

The Appcircle server may not have network access to the Microsoft Teams webhook URL you provided. For example, if you are using a firewall or proxy, you must have permission to access this URL. Please contact your network administrator for the required network access permission.

**3.** Untrusted SSL Certificate

When the Appcircle server sends a request to the webhook URL through the proxy, it might encounter an error due to the untrusted SSL certificate of the proxy. In this case, you should refer to the [**Connecting External Services**](/self-hosted-appcircle/configure-server/integrations-and-access/ssl-configuration.md#external-services) section in the self-hosted Appcircle documents to see how to trust your self-signed certificates.

<NeedHelp />
