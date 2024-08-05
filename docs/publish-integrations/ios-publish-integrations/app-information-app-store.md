---
title: App Information from App Store
description: Fetch and display your app's current listing information directly from the App Store to ensure all details are correct and up to date.
tags: [app information, app store, app store connect, testflight, app store version]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# App Information from App Store

This step enables you to view app version information from both [**TestFlight**](https://developer.apple.com/testflight/) and the [**App Store**](https://developer.apple.com/documentation/appstoreconnectapi/app_store) on a single screen, including the version you intend to submit. Upon running this step, it displays the latest version information from TestFlight and the App Store as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-infoDetail.png' />

Below are brief descriptions of the information provided on the App Information screen.

| Information          | Description                                                                                                                                                                                                                                                                         | Additional Info                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Bundle ID**        | The `bundleIds` resource represents the app's unique identifier that you can register, modify, and delete.                                                                                                                                                                          | [Apple's documentation](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids)        |
| **App Icon**         | Specifies the icon that will appear for the app on the selected platform.                                                                                                                                                                                                           | [Apple App Icon documentation](https://developer.apple.com/design/human-interface-guidelines/app-icons) |
| **App Name**         | The display name of the application on the selected platform.                                                                                                                                                                                                                       |                                                                                                         |
| **Version**          | The current available app versions. For example, `1.0.5`.                                                                                                                                                                                                                           |                                                                                                         |
| **Build Number**     | Version code information of your application. For example, `1.0.5(1)`.                                                                                                                                                                                                              |                                                                                                         |
| **Uploaded Date**    | Date the application was first uploaded. The **Release Candidate** version is based on the date it was uploaded to the **Publish module**.                                                                                                                                          |                                                                                                         |
| **Expire Date**      | The expiration date of the application version in TestFlight and the App Store. The **Release Candidate** version does not have an expiration date.                                                                                                                                 |                                                                                                         |
| **Release Type**     | Indicates the release type of your application. For example, if you have an application released to the market, you will see the type as **After Approval**.                                                                                                                        |                                                                                                         |
| **Processing State** | This indicates the status of your application; it will appear as **`Valid`** when there are no issues. For instance, if your application has expired in the TestFlight environment, the state will be **`Expire`**. If the application is rejected, the state will be **`Reject`**. |                                                                                                         |

:::caution
Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected in [**Publish Settings**](https://docs.appcircle.io/publish-module/#publish-settings).
:::

:::tip App Information from App Store

Since this step compares 3 different versions, it can be used in different scenarios. 

For example, your company's release management works with a certain approval mechanism. When a step is completed, you need to get approval and continue the process according to the next approval. At this point, you can present version information to the people responsible for Publish with this step, and then you can continue the process by getting approval from the relevant people with the [**Get Approval via Email step**](/publish-integrations/common-publish-integrations/get-approval-via-email). In this way, your entire Publish team will be able to see which version is the latest version in your production and beta test environments and compare it with your [**Release Candidate**](/publish-module/publish-information/marking-release-candidates) version. 

Likewise, the authorised person in your approval mechanism will also give approval to start your release process based on this comparison.

:::

### Prerequisites

This step does not depend on any other steps to function. However, it is advisable to use it as the initial step in your **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-appInfo.png' />

### Input Variables

This step does not need any input variable.

:::danger
This step requires only the [**App Store Connect API Key**](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/send-to-app-store#adding-an-app-store-connect-api-key-recommended-method) credentials. Ensure this API key is configured in Appcircle and selected for the appropriate flow.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-appstore-app-information
