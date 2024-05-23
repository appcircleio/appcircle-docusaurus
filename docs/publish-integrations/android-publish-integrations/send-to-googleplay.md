---
title: Publish to Google Play
description: Publish your Android applications to the Google Play Store with Appcircle's Publish module.
tags: [android, publish google play, android publish integrations]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Publish to Google Play

Appcircle supports sending APK and AAB binaries to [Google Play](https://play.google.com) through the Publish module.

Google Play no longer supports APK submission; however, Appcircle retains the APK submission feature for exceptional cases. For more details about APK submission, please refer to this document:
> [Google Play requires new apps to be published with the Android App Bundle starting August 2021](https://android-developers.googleblog.com/2021/06/the-future-of-android-app-bundles-is.html)

## Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Google Play and the initial binary is manually uploaded with the same keystore and the application ID (package name). Otherwise, the store upload process will fail. This is a known limitation of Google Play that is in place for security purposes.

You also need to have a Google Service Account and its key as a JSON file. Please refer to the following document for more information about service accounts.

<ContentRef url="/account/my-organization/api-integrations/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>

After completing the integration with Google Play Services, go to [Publishing Settings](/publish-module/publish-settings). In the [`Store Credential`](/publish-module/publish-settings#store-credentials) section, select the Google Play Store API Key you uploaded, from the drop-down list.

If you are using [Publish Variables](http://localhost:3000/publish-module/publish-settings#publish-variables), you should select them in the [Publishing Settings](/publish-module/publish-settings) window.

## Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-publish-google-play-1.png'/>

| Variable Name      | Description                                                                                                      | Status    |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- | --------- |
| $AC_STACK_TYPE     | `Track type for submit` refers to the [distribution channel](https://developers.google.com/android-publisher/tracks) through which you release your app for testing or production. Options: `Internal`, `Alpha`, `Beta`, `Production`. Default: `Alpha`. | Optional  |
| $AC_RELEASE_STATUS | The `Play Store App Status` refers to the stage of the app's [publication process](https://support.google.com/googleplay/android-developer/answer/9859751?hl=en#zippy=%2Capp-status). Options: `completed`, `draft`. | Optional  |
| $AC_RELEASE_NOTES  | Provides release notes for the submission to Google Play.                                                        | Optional  |

## Output Variables

**Publish to Google Play** step does not produce any output. However, you can check the logs to see whether your app has successfully accessed Google Play.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-playstore