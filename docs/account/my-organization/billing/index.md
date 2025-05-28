---
title: Billing
description:  Monitor your usage of various modules within the Appcircle from the Billing section.
tags:
  [
    account,
    usage,
    billing
  ]
---

import Screenshot from '@site/src/components/Screenshot';

# Billing

The Billing section allows you to monitor your usage summary, including builds, publishes, team members, and other module usages. You can also view your license plan and renewal date of your account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5909-billing1.png' alt="Billing" />

## Usage Summary

- **Builds** : Number of builds initiated from the build module in a single billing cycle.
- **Testing Distribution** : Number of app downloads from the Testing Portal in a single billing cycle.
- **Publishes** : Number of publishes initiated from the Publish module in a single billing cycle.
- **Enterprise App Store** : Number of app downloads from the Enterprise App Store in a single billing cycle.
- **Team Members** : Number of team members allowed in a single organization.
- **Sub Organizations** : Number of Sub-Organizations allowed.
- **Artifact Storage** : Total storage size for all the build and distribution artifacts across the platform.
- **Build Concurrency** : Number of builds that can run simultaneously.
- **Build Time Limit** : Number of minutes allowed per build and publish before it is automatically cancelled with a timeout status.

:::info Usage Count
Please note that the module usage counts displayed here, such as builds, testing distribution, and publishes, represent the combined totals for the organization and its sub-organizations.
:::

:::warning Limit Warnings
When the usage limits exceed 85% of the allocated quota, notification emails will be sent to the organization’s Owner and the Billing Manager.
:::

### Sub-Organization Usage

The Billing page for a Sub-Organization displays the same summary metrics as the root organization, except for: 

- **Team Members** 
- **Sub-Organizations**
- **Artifact Storage**

:::warning
The usage counts shown on this page reflect only the usage of the Sub-Organization. To view overall usage against limits, please refer to the Billing page of the root organization.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6066-ss1.png'/>