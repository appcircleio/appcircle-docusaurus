---
title: Send to App Store
metaTitle: Send to App Store
metaDescription: Send to App Store
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# Send to App Store

This step allows you to submit your app to the App Store.

:::caution
Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected in [**Publish Settings**](https://docs.appcircle.io/publish-module/#publish-settings).
:::

### Prerequisites

The steps required for this step to work are given in the list below with their descriptions.

:::caution
Please note that this stepper is a stand-alone stepper. If the steps in the list below are available in your Publish Flow, they must be used before this step.
:::


| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**App Information from App Store**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/app-information-app-store) | This step compares the Release Candidate version with the TestFlight and the App Store versions. |
| [**Sent to Testflight**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/send-to-app-store) | This step allows you to submit your application to the TestFlight. |
| [**Get Approval from TestFlight**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/approval-test-flight) | This step checks the TestFlight status of your application and advances the Publish Flow according to the specified acceptance condition. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2914-appStore.png' />

### Input Variables

The parameters required for the operation of this step are listed in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2914-appStoreInput.png' />

:::info
This step can also be sent to `TestFlight` alone, according to the selected **Stack Type**. If you have the `Send to TestFlight` step in your **Publish Flow**, please set the Stack Type to **`Release`**.
:::

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_XCODE_LIST_DIR`          | Specifies the Xcode folder list directory. Current Xcode folder structure examples: `/Applications/Xcode/14.3/Xcode` or `/Applications/Xcode/15.0/Xcode`. | Optional |
| `$AC_XCODE_VERSION`           | Specifies the Xcode version. | Required |
| `$AC_STACK_TYPE`              | App Store or TestFlight stages. The default value is `TestFlight`. | Optional |
| `$AC_RELEASE_NOTES`           | It is the parameter used to send a relase note with the selected version. You can find detailed information about **Release Notes** [**here**](https://docs.appcircle.io/integrations/managing-release-notes). | Optional |