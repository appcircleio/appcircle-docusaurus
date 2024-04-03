---
title: Send to App Store
metaTitle: Send to App Store
metaDescription: Send to App Store
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# Send to App Store

This step enables you to submit your application to the [App Store](https://www.apple.com/app-store/).

:::caution
Ensure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is configured in Appcircle and chosen under [**Publish Settings**](https://docs.appcircle.io/publish-module/#publish-settings).
:::

### Prerequisites
Below are the prerequisite steps necessary for this operation, accompanied by their descriptions.

:::caution
Note: This is a standalone step. The steps listed below should precede this step if they are part of your Publish Flow.
:::

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**App Information from App Store**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/app-information-app-store) | This step compares the Release Candidate version with the TestFlight and the App Store versions. |
| [**Sent to Testflight**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/send-to-app-store) | This step allows you to submit your application to TestFlight. |
| [**Get Approval from TestFlight**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/approval-test-flight) | This step checks the TestFlight status of your application and advances the Publish Flow according to the specified acceptance condition. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2914-appStore.png' />

### Input Variables
Below are the parameters necessary for this step's operation, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2914-appStoreInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_XCODE_LIST_DIR`          | Specifies the Xcode folder list directory. Current Xcode folder structure examples: `/Applications/Xcode/14.3/Xcode` or `/Applications/Xcode/15.0/Xcode`. | Optional |
| `$AC_XCODE_VERSION`           | Specifies the Xcode version. | Required |
| `$AC_STACK_TYPE`              | App Store or TestFlight stages. The default value is `TestFlight`. | Optional |
| `$AC_RELEASE_NOTES`           | It is the parameter used to send a release note with the selected version. You can find detailed information about **Release Notes** [**here**](https://docs.appcircle.io/integrations/managing-release-notes). | Optional |

:::info
This step may also target **TestFlight** exclusively, depending on the chosen **Stack Type**. If your **Publish Flow** includes the **Send to TestFlight** step, ensure the **Stack Type** is set to **`Release`**.
:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-appstore