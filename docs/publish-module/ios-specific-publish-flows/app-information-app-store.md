---
title: App Information from App Store
metaTitle: App Information from App Store
metaDescription: App Information from App Store
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# App Information from App Store

This step allows you to see app version information from [**TestFlight**](https://developer.apple.com/testflight/) and the [**App Store**](https://developer.apple.com/documentation/appstoreconnectapi/app_store) on the same screen, along with the version you want to submit. When the step runs, your latest version information in TestFlight and the App Store will be displayed as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-infoDetail.png' />

:::info
You can find brief descriptions of some of the information we provide on the App Information screen below.

- **`Bundle ID`**: The `bundleIds` resource represents the app's unique identifier that you can register, modify, and delete. For further information, please check [**Apple's documentation**](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids).
- **`App Icon`**: Specifies the icon that will appear for the app on the selected platform. For further information, please check the [**Apple App Icon documentation**](https://developer.apple.com/design/human-interface-guidelines/app-icons).
- **`App Name`**: The display name of the application on the selected platform.
- **`Version`**: The current available app versions. For example, `1.0.5`.
- **`Build Number`**: Version code information of your application. For example, `1.0.5(1)`.
- **`Uploaded Date`**: Date the application was first uploaded. The **Release Candidate** version is based on the date it was uploaded to the **Publish module**.
- **`Expire Date`**: It is the expiration date of the application version in TestFlight and the App Store. There is no expiration date in the **Release Candidate** version. 
- **`Release Type`**: Indicates the release type of your application. For example, if you have an application released to the market, you will see the type as **After Approval**.
- **`Processing State`**: The processing state shows the status of your application; you will see it as **`Valid`** when there is no problem. For example, if your application has expired in the TestFlight environment, you will see the state as **`Expire`**. Or if the application is rejected, the state is **`Reject`**.
:::

:::caution
Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected in [**Publish Settings**](https://docs.appcircle.io/publish-module/#publish-settings).
:::

### Prerequisites

This stepper is not dependent on any other stepper for operation. However, it is recommended to use it as the first step in your **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-appInfo.png' />

### Input Variables

This step does not need any input variable.

:::warning
The only thing this step needs is [**App Store Connect API Key**](https://docs.appcircle.io/publish-module/send-to-appstore#adding-an-app-store-connect-api-key-recommended-method) credentials information. Please make sure that this API key is installed in Appcircle and selected for the relevant flow.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-appstore-app-information