---
title: Publish Settings
description: Configure the publish settings for your app in Appcircle
tags: [publish settings, publish, settings]
---

# Publish Settings

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

When a build is completed on the Build module and its artifacts are distributed to the Publish module, we can start the publish process to the stores using the **Auto Publish** toggle in **Settings**.

Your configured publish flow will be executed automatically when you enable **Auto Publish**.

You can also select a runner pool from the **SELECT A POOL** dropdown list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5053-priority3.png' alt="Publish Pool Selection" />

"Appcircle Linux Pool (x86_64)" and "Appcircle Standard macOS Pool (arm64)" are Appcircle cloud-hosted pools and only available for the cloud services.

:::info

You can use both cloud-hosted pools for the Android publish profiles.

On the other hand, for iOS publish profiles, the only option for Appcircle Cloud is Apple Silicon-based "Appcircle Standard macOS Pool (arm64)".

"Appcircle Linux Pool (x86_64)" support is not available for the iOS publish profiles.

:::

If there are any self-hosted pools in your organization, you can also select them from the list. Self-hosted Appcircle users will only see the self-hosted pools in this list.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools">
  Self-hosted Pools
</ContentRef>

:::info
If group or variable definitions have been made in **Publish Variables**, you will see the list of variable groups in **Settings**, and you can select one or more of them to use in your publish flow.
:::

## Auto Publish

This switch, when enabled, automatically starts the publishing process for new app versions as they become available.

## Select a Pool

You can select a runner pool from the dropdown list to execute the publish flow.

There are two default pools available for cloud services:

- Appcircle Linux Pool (x86_64)
- Appcircle Standard macOS Pool (arm64)

:::info

You can use both cloud-hosted pools for the Android publish profiles.

On the other hand, for iOS publish profiles, the only option for Appcircle Cloud is Apple Silicon-based "Appcircle Standard macOS Pool (arm64)".

"Appcircle Linux Pool (x86_64)" support is not available for the iOS publish profiles.

:::

Self-hosted Appcircle users will see their self-hosted pools in this list.

## Publish Variables

Publish Variables are key-value pairs that can be used to store configuration settings, credentials, and other data required during the publish process. You can add new variables directly in the Publish Variables section without the need for an additional menu or button.

For detailed information on Publish Variables, follow the link below.

<ContentRef url="/publish-module/publish-variables">
  Publish Variables
</ContentRef>

## Store Credentials

Store credentials are the connection details for the stores that you will publish your app to.

For detailed information on store connections, follow the links below.

| Store             | Connection                                                                                                                  |
| ----------------- |-----------------------------------------------------------------------------------------------------------------------------|
| App Store         | [Adding an App Store Connect API Key](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key.md) |
| Google Play       | [Adding Google Play Service Account](/account/my-organization/security/credentials/adding-google-play-service-account.md)   |
| Huawei AppGallery | [Adding Huawei API Key](/account/my-organization/security/credentials/adding-huawei-api-key)                                |
| Microsoft Intune  | [Adding Microsoft Intune API Credentials](/account/my-organization/security/credentials/adding-microsoft-intune-api-key)    |

#### Publish Priority

The publish priority configuration feature includes three levels: Low, Medium, and High.

These priority levels influence the starting order of queued publish processes, ensuring that higher-priority publish processes are initiated first.

For instance, if a high-priority publish is added to the queue after a low-priority publish, the high-priority publish will commence before the low-priority one.

This functionality allows for better management of publish processes, enabling teams to prioritize critical updates and enhancements efficiently.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5053-priority1.png' alt="Publish Priority" />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5053-priority2.png' alt="Publish Priority Selection" />

:::info
This feature is only available for organizations with Enterprise license.
:::