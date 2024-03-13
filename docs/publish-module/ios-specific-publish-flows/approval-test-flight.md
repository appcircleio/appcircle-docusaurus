---
title: Get Approval from TestFlight
metaTitle: Get Approval from TestFlight
metaDescription: Get Approval from TestFlight
sidebar_position: 3
---
import Screenshot from '@site/src/components/Screenshot';

# Get Approval from TestFlight

This step allows you to check the status of your application after sending it to [**TestFlight**](https://developer.apple.com/testflight/). It is a **scheduled job** and periodically checks the status of the relevant version on TestFlight. Informs you of the version status in internal, external, or both test groups.

### Prerequisites

This step is one of the dependent steps. The dependent steps are given in the table below with their explanations.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Send to TestFlight**](https://docs.appcircle.io/publish-module/send-to-appstore#send-apps-to-testflight) | This step sends the relevant application version to TestFlight. Make sure the [**App Store Connect API Key**](https://docs.appcircle.io/account/adding-an-app-store-connect-api-key#linking-appcircle-with-app-store-connect) is added to Appcircle and selected. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2919-approvelTestFlight.png' />

### Input Variables

The parameters required for this step to work as expected are listed below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2919-approvalTestInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_VALIDATION_CONDITION`    | This parameter determines which condition must be met for the step to be successful. There are four different options: as `Internal`, `External`, or `Both`. | Required |

:::info
Please note that the selected condition determines the **success** of the step. For example, if the application is sent to the **`Internal`** test group and its status is **`In Testing`**, this step will be successful, and it will move on to the next step.
:::


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-testflight-status-check


