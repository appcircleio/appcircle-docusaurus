---
title: Get Approval From Google Play
description: Check status of an app release in Google Play Console.
tags: [android, approval, google play]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Get Approval From Google Play

Check status of an app release in [Google Play Console](https://play.google.com/console). This allows you to monitor the progress of your submission and take any necessary actions to address any issues or concerns that may arise during the review process.

## Prerequisites

The Publish flow steps that need to be executed before running the **Get Approval via Email** step, along with their respective reasons, are listed in the table below:

| Prerequisite Workflow Step                                                                                 | Description                                                                                             |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Publish to Google Play**](/publish-integrations/android-publish-integrations/send-to-googleplay)       | The app must be published to Google Play before checking the status of the app version in the Google Play Console. |

:::tip

If you have previously submitted this app version to the Google Play Console, you do not need to add the **Publish to Google Play** step.

:::

## Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-publish-google-play-1.png'/>

| Variable Name          | Description                                                                                                                     | Status    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| $AC_TRACK_TO_CHECK     | Select a Release Track to check the app status. It is recommended to choose the track to which you have sent the app in previous steps. | Optional  |
| $AC_ACCEPTED_STATUSES  | Customize the statuses to be accepted as passed by using commas. You can use statuses such as `completed`, `inProgress`, `draft`, `halted`. | Optional  |

## Output Variables

**Get Approval From Google Play** step does not produce any output variables. However, you can check the logs to see the detailed status and results of your app's approval process.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-googleplay-status-check.git