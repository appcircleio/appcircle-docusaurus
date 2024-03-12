---
title: App Information from App Store
metaTitle: App Information from App Store
metaDescription: App Information from App Store
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# App Information from App Store

This step allows you to see app version information from TestFlight and the App Store on the same screen, along with the version you want to submit. When the step runs, your latest version information in TestFlight and App Store will be displayed as follows.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-infoDetail.png' />

:::caution
Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected.
:::

### Prerequisites

This stepper is not dependent on any other stepper for operation. However, it is recommended to use it as the first step in your **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2917-appInfo.png' />

### Input Variables

This step does not need any input variable.

:::warning
The only thing this step needs is [**App Store Connect**](https://docs.appcircle.io/publish-module/send-to-appstore#adding-an-app-store-connect-api-key-recommended-method) API Key credentials information. Please make sure that this API Key is installed in Appcircle and selected for the relevant flow.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-appstore-app-information