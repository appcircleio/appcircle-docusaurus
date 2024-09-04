---
title: Publish to Microsoft Intune
description: Learn how to submit your app to Microsoft Intune using Appcircle’s streamlined integration process.
tags: [android,ios, android integrations, android publish integrations, microsoft intune]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Publish to Microsoft Intune

This step enables you to submit your line of business apps to the [Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune).

### Prerequisites

Below are the prerequisite steps necessary for this operation, accompanied by their descriptions.

### Providing Microsoft Intune API Credentials for Accessing Intune

To send an app from Appcircle to Microsoft Intune, you need to register an application with the Microsoft Identity Platform and provide this application's credentials.

<ContentRef url="/account/my-organization/integrations/credentials/adding-microsoft-intune-api-key">
  Adding Microsoft Intune API Credentials
</ContentRef>

After completing the integration with Microsoft Intune, go to [Publishing Settings](/publish-module/publish-settings). In the [Store Credential](/publish-module/publish-settings#store-credentials) section, select the Microsoft Intune Credential you integrated, from the drop-down list.

### Input Variables

## iOS

Below are the parameters necessary for this step's operation for iOS, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/send-to-microsoft-intune-inputs-ios-light.png' />

| Variable Name        | Description                                                                                                                                                                                                                       | Status   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_INTUNE_PUBLISHER_NAME`  | This parameter is used to specify the publisher name for the selected version. By default, it takes the name of your organization or the email address of the user initiating the step. | Optional |
| `$AC_INTUNE_TARGETED_PLATFORM`     | The `Applicable Device Type` specifies the the device types that can install this app. Options: `Both`, `iPad`, `iPhone and iPod`. Default: `Both`. | Optional |
| `$AC_INTUNE_MIN_OS_VERSION`     | The `Minimum Operating System` specifies the earliest operating system version on which the app can be installed. If you assign the app to a device with an earlier operating system, it will not be installed. Default: `iOS 8.0`. | Optional |

:::warning
If you choose to create a new application in Microsoft Intune while marking the app version as release candidate and execute this step before updating the [metadata information](https://docs.appcircle.io/publish-module/publish-information/meta-data-information#microsoft-intune-metadata-information), these values will be assigned to the application being created by default.

<Screenshot url='https://cdn.appcircle.io/docs/assets/send-to-intune-select-app-light-v2.png' />
:::
---

## Android

Below are the parameters necessary for this step's operation for Android, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/send-to-microsoft-intune-inputs-android-light.png' />

| Variable Name        | Description                                                                                                                                                                                                                       | Status   |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_INTUNE_PUBLISHER_NAME`  | This parameter is used to specify the publisher name for the selected version. By default, it takes the name of your organization or the email address of the user initiating the step. | Optional |
| `$AC_INTUNE_TARGETED_PLATFORM`     | The `Targeted Platform` specifies the the device types that can install this app. Options: `Android device administrator`, `Android (AOSP)`. Default: `Android (AOSP)`. | Optional |
| `$AC_INTUNE_MIN_OS_VERSION`     | The `Minimum Operating System` specifies the earliest operating system version on which the app can be installed. If you assign the app to a device with an earlier operating system, it will not be installed. Default: `Android 4.0 (Ice Cream Sandwich)`. | Optional |

:::danger
If you choose to create a new application in Microsoft Intune while marking the app version as release candidate and execute this step before updating the [metadata information](https://docs.appcircle.io/publish-module/publish-information/meta-data-information#microsoft-intune-metadata-information), these values will be assigned to the application being created by default.
 - The `Targeted Platform` is set when the application is first created in Microsoft Intune and cannot be changed afterwards. Ensure that you select the correct platform before executing this step.
<Screenshot url='https://cdn.appcircle.io/docs/assets/send-to-intune-select-app-light-v2.png' />
:::

:::danger
Microsoft Intune does not support the distribution of  Android App Bundle (AAB) files. If your release candidate version is an AAB file, this step will fail.
:::
---
To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-intune-ios
https://github.com/appcircleio/appcircle-publish-send-to-intune-android

