---
title: Get Approval from TestFlight
metaTitle: Get Approval from TestFlight
metaDescription: Get Approval from TestFlight
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Get Approval from TestFlight

This step allows you to check the status of your application after sending it to [**TestFlight**](https://developer.apple.com/testflight/). It is a **scheduled job** and periodically checks the status of the relevant version on TestFlight. Informs you of the version status in internal, external, or both test groups.

:::info
After this step, once the application is uploaded to **TestFlight**, it will successfully terminate or fail the step according to the selected status. There are four different options for this:

- **`One of the External or Internal`**
- **`Internal Only`**
- **`External Only`**
- **`Both`**

For example, if your application was submitted to the **`Internal`** test group in TestFlight and you have selected **`Internal or External`** status from the step, when your application is sent to the **`Internal`** test group, its status will be In Testing and the Appcircle step will be successful. The same situation applies to the other options. If you select **`Internal Only`** or **`External Only`** Only, it will be sufficient for the application to be **`In Testing`** in one of the two test groups. However, if you select **`Both`**, the step will be successful only after the **`In Testing`** requirement is met in both test groups.
:::

### Prerequisites

This step is one of the dependent steps. Below is a table of the dependent steps with their descriptions.

| Prerequisite Workflow Step                                                                                                                  | Description                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Send to TestFlight**](https://docs.appcircle.io/publish-integrations/ios-publish-integrations/send-to-app-store#send-apps-to-testflight) | This step sends the relevant application version to TestFlight. Ensure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2919-approvelTestFlight.png' />

### Input Variables

The parameters required for this step to work as expected are listed below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2919-approvalTestInput.png' />

| Variable Name              | Description                                                                                                                                                                                     | Status   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_VALIDATION_CONDITION` | This parameter determines which condition must be met for the step to be successful. There are four different options: as `One of the External or Internal`, `Internal`, `External`, or `Both`. | Required |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-testflight-status-check
