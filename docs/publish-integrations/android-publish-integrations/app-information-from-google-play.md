---
title: App Information from Google Play
description: Check status of an app releases in Google Play Console.
tags: [android, approval, google play]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# App Information from Google Play

The **App Information from Google Play** step checks the status of the app releases in the [Google Play Console](https://play.google.com/console). This allows you to monitor the progress of your app.

:::tip

The **App Information from Google Play** step monitors the general status information of the app on Google Play. It is not limited to the specific version you sent.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-app-info-from-google-play-1.png'/>

## Prerequisites

To run the **App Information from Google Play** step, you need to have previously uploaded at least one version of the app to the Google Play Console. However, if you want to monitor the app information after publishing it to Google Play, you can add the [**Publish to Google Play**](/publish-integrations/android-publish-integrations/publish-to-google-play) step before this step in the publish flow.

You also need to have a Google Service Account and its key as a JSON file. Please refer to the following document for more information about service accounts:

<ContentRef url="/account/my-organization/security/credentials/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>

After completing the integration with Google Play Services, go to [Publishing Settings](/publish-module/publish-settings). In the [Store Credential](/publish-module/publish-settings#store-credentials) section, select the Google Play Store API Key you uploaded, from the drop-down list.

:::info

If you are using [Publish Variables](/publish-module/publish-settings#publish-variables), you should select them in the [Publishing Settings](/publish-module/publish-settings) window.

:::

## Input Variables

No input variables are required for the **App Information from Google Play** step. It will retrieve information from Google Play, based on the app you are running and the [Store Credential](/publish-module/publish-settings#store-credentials) you select in [Publishing Settings](/publish-module/publish-settings).

## Output Variables

**App Information from Google Play** step does not produce any output variables. However, you can check the logs to see detailed release statuses for your app.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-playstore-app-information.git