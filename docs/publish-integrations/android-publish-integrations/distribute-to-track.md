---
title: Distribute to Track
description: Seamlessly release apps to different testing or production tracks via Google Play Console.
tags: [android, track, google play]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Distribute to Track

The **Distribute to Track** step in Appcircle enables automated deployment of Android applications to specific tracks within the Google Play Console. This functionality allows developers to manage releases efficiently, targeting different user groups such as internal testers, beta users, or the general public.

## Prerequisites

The Publish flow steps that need to be executed before running the **Distribute to Track** step, along with their respective reasons, are listed in the table below:

| Prerequisite Workflow Step                                                                          | Description                                                                                             |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Publish to Google Play**](/publish-integrations/android-publish-integrations/publish-to-google-play) | The app must be published to Google Play before checking the status of the app version in the Google Play Console. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4602-track1.png'/>

:::warning

If you have previously submitted this app version to the Google Play Console, you do not need to add the **Publish to Google Play** step.

:::

## Input Variables

Following input configurations are required for the **Distribute to Track** step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4602-track.png'/>

| Variable Name        | Description                                                                                                                                                                                                                                                                                                                                                 | Status    |
| -------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| --------- |
| `$AC_STACK_TYPE`     | The `Track type for submit` specifies the [distribution channel](https://developers.google.com/android-publisher/tracks) for submitting your app for testing or production. Options are dynamic and retrieved from the Google Play Console. They may vary for each app. Options: `Internal`, `Alpha`, `Beta`, `TEST-TRACK`, `Production`. Default: `Alpha`. | Optional |
| `$AC_RELEASE_STATUS` | The `Play Store App Status` refers to the stage of the app's [publication process](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en#zippy=%2Capp-status) on the Play Store. Options: `completed`, `partial`, `draft`.                                                                                                           | Optional  |
| `$AC_AUTO_SEND_PLAYSTORE_REVIEW` | The `Auto Send for Review` where you select whether your changes should automatically go for review on the Google Play Console. Options: `Send for Review Automatically but Rescue Errors`, `Don't Send for Review Automatically but Rescue Errors`, `Always Send for Review Automatically`, `Never Send for Review Automatically`.                         | Optional  |
| `$AC_RELEASE_NOTES`  | Provides release notes for the submission to Google Play. Use the `$AC_RELEASE_NOTES` variable to include the current release notes for the app version. Check or edit your app version's release notes in Binary Information.                                                                                                                              | Optional  |

For detailed information about **Auto Send for Review** setting, please refer to the [Auto Send for Review](/publish-module/publish-information/google-play-information#auto-send-for-review) documentation.

## Output Variables

The **Distribute to Track** publish step in Appcircle provides a custom UI that allows users to:

- Observe Google Play Information and edit Release Notes on default language or localized.

- See the Track Name and status which defines the Google Play track where the app is being deployed (e.g., `alpha` status: `in progress` ).

- Control the percentage of users receiving the update initially. A slider is available to adjust the rollout percentage (e.g., 10%).

:::info
Rollout Percentage slider is only available for `partial` Play Store app Status.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4602-track2.png'/>

:::tip 
You can see the Play Store App Status for your tracks on Google Play Console by checking the **Publishing overview** section.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4602-track3.png'/>