---
title: Get Approval From Google Play
description: Ensure your app release is approved by checking its status on the Google Play Console.
tags: [android, approve, google play]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Get Approval From Google Play

The **Get Approval From Google Play** step ensures that your app release is approved by checking its status on the [Google Play Console](https://play.google.com/console). This allows you to monitor the progress of your submission and take any necessary actions to address any issues or concerns that may arise during the review process.

## Prerequisites

The Publish flow steps that need to be executed before running the **Get Approval via Email** step, along with their respective reasons, are listed in the table below:

| Prerequisite Workflow Step                                                                          | Description                                                                                             |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Publish to Google Play**](/publish-integrations/android-publish-integrations/publish-to-google-play) | The app must be published to Google Play before checking the status of the app version in the Google Play Console. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-approve-from-google-play-0.png'/>

:::warning

If you have previously submitted this app version to the Google Play Console, you do not need to add the **Publish to Google Play** step.

:::

You also need to have a Google Service Account and its key as a JSON file. Please refer to the following document for more information about service accounts:

<ContentRef url="/account/my-organization/integrations/credentials/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>

After completing the integration with Google Play Services, go to [Publishing Settings](/publish-module/publish-settings). In the [`Store Credential`](/publish-module/publish-settings#store-credentials) section, select the Google Play Store API Key you uploaded, from the drop-down list.

:::info

If you are using [Publish Variables](/publish-module/publish-settings#publish-variables), you should select them in the [Publishing Settings](/publish-module/publish-settings) window.

:::

## Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-approve-from-google-play-1.png'/>

| Variable Name          | Description                                                                                                                     | Status    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `$AC_TRACK_TO_CHECK`   | Select a release track to check the app's status. It is recommended to choose the track to which you have sent the app in the previous steps. Options: `alpha`, `beta`, `production`, and `internal`. | Optional |
| `$AC_ACCEPTED_STATUSES` | Customize the statuses to be accepted as passed by using commas. You can use statuses such as `completed`, `inProgress`, `draft`, `halted`. | Optional |

:::tip

Please follow the document to get information about the [Release Lifecycle](https://developers.google.com/assistant/console/releases#lifecycle) on Google Play.

:::

## Output Variables

The **Get Approval from Google Play** step does not produce any output variables. However, the step will succeed or fail, based on whether your application is in the correct status according to the [inputs](#input-variables) you provide.

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-approve-from-google-play-2.png'/>

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-googleplay-status-check.git