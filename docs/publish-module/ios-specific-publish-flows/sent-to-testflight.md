---
title: Send to TestFlight
metaTitle: Send to TestFlight
metaDescription: Send to TestFlight
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# Send to TestFlight

This step allows you to send the selected application package to [**TestFlight**](https://developer.apple.com/testflight/).

:::info
Please note that if you try to submit a version that already exists on **TestFlight**, this step will prompt you to upgrade the **version** or **build number**.
:::

:::caution
Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected in [**Publish Settings**](https://docs.appcircle.io/publish-module/#publish-settings).
:::

### Prerequisites

The steps required for this step are listed below. 

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**App Information from App Store**](https://docs.appcircle.io/publish-module/ios-specific-publish-flows/app-information-app-store) | This step provides information about the version you want to send and your versions in both [**TestFlight**](https://developer.apple.com/testflight/) and the [**App Store**](https://developer.apple.com/documentation/appstoreconnectapi/app_store). |

:::info
The **App Information from App Store** step is not a mandatory step to be used before the **Send to TestFlight** step. If you have this step in your workflow, please use it before the **TestFlight** step.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2913-testFlight.png' />

### Input Variables

The parameters required for the operation of this step are listed below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2913-testFlightInfo.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_XCODE_LIST_DIR`          | Specifies the Xcode folder list directory. Current Xcode folder structure examples: `./Applications/Xcode/14.2/Xcode` or `./Applications/Xcode/15.2/Xcode` | Optional |
| `$AC_XCODE_VERSION`           | This parameter takes the Xcode version value. It sends the selected Xcode version. You can find detailed information about Xcode versions [**here**](https://docs.appcircle.io/infrastructure/ios-build-infrastructure#available-xcode-versions). | Required |
| `$AC_RELEASE_NOTES`           | It is the parameter used to send a release note with the selected version. You can find detailed information about **Release Notes** [**here**](https://docs.appcircle.io/integrations/managing-release-notes). | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-testflight