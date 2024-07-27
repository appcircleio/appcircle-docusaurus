---
title: Publish Variables
description: Learn how to set up and manage key-value pairs that are essential for the app publishing process in Appcircle
tags: [publish variables, publish, variables]
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The **Publish Variables** section within the Publish module is a feature that allows you to set up and manage key-value pairs that are essential for the app publishing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-variables.png' />

To use these defined variables, it will be necessary to select them from the [Publish Settings](/publish-module/publish-settings/).

Publish Variables are key-value pairs that can be used to store configuration settings, credentials, and other data required during the publish process. You can add new variables directly in the Publish Variables section without the need for an additional menu or button.

## How to Add a New Publish Variable

1. **Input the Key-Value Pair:**

   - Locate the input fields under the 'Publish Variables' header.
   - Enter the name of the variable in the 'Key' input field.
   - Enter the corresponding value in the 'Value' input field.

2. **Select Variable Type:**

   - Choose the type of variable you're adding. Options typically include:
     - **Text**: for string or numeric values.
     - **File**: if you're assigning a file as the variable's value.

3. **Add the Variable:**

   - Click the 'Add' button to save the new variable.

4. **Review and Confirm:**
   - Once added, the new variable will appear in the list of Publish Variables.
   - Ensure that the details are correct and the variable is saved properly.

## Example Variable

In the example provided:

- **Key Name**: `Foo`
- **Value**: `Bar`
- **Type**: `Text`

Remember to handle these variables with care, especially if they contain sensitive information such as passwords, tokens, or API keys.

## Reserved Variables

There are some reserved variables that are automatically defined by Appcircle and can be used in the publish flow.

### Common Publish Reserved Variables

| Variable                    | Description                                                                                                                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_RELEASE_NOTES            | Specifies the release notes from the [Build profile](/build) (if published from there) or from one of the Publish steps, to be published to the stores (`Google Play`, `Huawei AppGallary`, or `App Store`). |
| AC_ORGANIZATION_ID          | Specifies the organization ID where the publish process starts.                                                                                                                                              |
| AC_USER_ID                  | Specifies the user ID who started the publish process.                                                                                                                                                       |
| AC_USER_EMAIL               | Specifies the email address of the user who started the publish process.                                                                                                                                     |
| AC_STORE_NAME               | Name of the store where the app is being published.                                                                                                                                                          |
| AC_PLATFORM_TYPE            | Platform type (e.g., `iOS:1`, `Android:2`).                                                                                                                                                                  |
| AC_UNIQUE_NAME              | Unique name of the app (starts with `com.` for Android and iOS).                                                                                                                                             |
| AC_PUBLISH_APP_VERSION      | Version of the app being published (e.g., `1.0.1`).                                                                                                                                                          |
| AC_PUBLISH_APP_VERSION_ID   | App version ID being published on Appcircle.                                                                                                                                                                 |
| AC_PUBLISH_APP_VERSION_CODE | Version code of the app being published.                                                                                                                                                                     |
| AC_APP_VERSION_NAME         | Name of the app version being published.                                                                                                                                                                     |
| AC_STORE_CREDENTIAL_ID      | ID of the store credential where the app is being published.                                                                                                                                                 |
| AC_PUBLISH_PROFILE_ID       | Specifies the profile ID who started the publish process on Appcircle.                                                                                                                                       |
| AC_TASK_ID                  | Task ID associated with the publish process on Appcircle.                                                                                                                                                    |
| AC_PUBLISH_ID               | Publish ID on Appcircle.                                                                                                                                                                                     |
| AC_PUBLISH_STEP_ID          | Publish step ID on Appcircle.                                                                                                                                                                                |
| AC_RESOURCE_ID              | Resource ID used in the publishing process on Appcircle.                                                                                                                                                     |
| AC_ORGANIZATION_POOL_ID     | Pool ID of the organization where the publish process starts.                                                                                                                                                |
| AC_SOURCE_ID                | Source ID of the process (e.g., `Publish`).                                                                                                                                                                  |
| AC_MODULE_NAME              | Name of the module in the process (e.g., `Publish`).                                                                                                                                                         |
| AC_PUBLISH_PROFILE_NAME     | Specifies the Appcircle profile name who started the publish process.                                                                                                                                        |
| AC_PUBLISH_STEP_NAME        | Name of the publish flow step being run.                                                                                                                                                                     |
| AC_PUBLISH_WORKFLOW_NAME    | Name of the publish workflow being run.                                                                                                                                                                      |
| AC_APP_FILE_URL             | URL of the app file being published.                                                                                                                                                                         |
| AC_APP_FILE_NAME            | Name of the app file being published (with file extension).                                                                                                                                                  |

:::caution Release Notes

User can use `AC_RELEASE_NOTES` environment variable, if the `apk`, `aab` or `ipa` files comes from Build module.

:::

### iOS Publish Reserved Variables

| Variable                | Description                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_XCODE_LIST_DIR       | Specifies the Xcode folder list directory.                                                                                                                                                                               |
| AC_XCODE_VERSION        | Specifies the Xcode version.                                                                                                                                                                                             |
| AC_VALIDATION_CONDITION | Used for the [Get Approval from TestFlight](/publish-integrations/ios-publish-integrations/approval-test-flight). TestFlight's `internalBuildState` and `externalBuildState` will be checked according to the selection. |
| AC_SUCCESS_STATUSES     | You can customize `Acceptable/Succeeded` App Store statuses for your app.                                                                                                                                                |
| AC_STACK_TYPE           | `App Store` or `TestFlight` stages.                                                                                                                                                                                      |

### Android Publish Reserved Variables

| Variable             | Description                                                                                                                                                                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_RELEASE_STATUS    | Used for the [Send to Google Play](/publish-integrations/android-publish-integrations/publish-to-google-play) step. Allows you to specify `draft` or `completed` app statuses on the Google Play Console.                                  |
| AC_STACK_TYPE        | Used for the [Send to Google Play](/publish-integrations/android-publish-integrations/publish-to-google-play) step. Specifies the release track to send the binary. After the binary is uploaded, you can release it from the Google Play. |
| AC_TRACK_TO_CHECK    | Used for the [Get Approval from Google Play](/publish-integrations/android-publish-integrations/get-approval-from-google-play) step. It's recommended to check the track that you've sent the app in previous steps.                       |
| AC_ACCEPTED_STATUSES | Used for the [Get Approval from Google Play](/publish-integrations/android-publish-integrations/get-approval-from-google-play) step. Statuses of `completed`,`inProgress`,`draft`,`halted` can be used.                                    |
| AC_HUAWEI_APP_ID     | Used for the [Send to Huawei AppGallery](/publish-integrations/android-publish-integrations/publish-to-huawei-appgallery) step. Huawei requires `Huawei App ID` to be sent app to Huawei App Gallery.                                      |
