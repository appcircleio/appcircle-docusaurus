---
title: Publish Variables
tags: [publish, variables]
description: Publish Variables
keywords:
  [
    publish,
    variables,
    publish variables,
    appcircle,
    appcircle docs,
    appcircle publish variables,
  ]
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

### iOS Publish Reserved Variables

| Variable                | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| AC_XCODE_LIST_DIR       | Specifies the Xcode folder list directory                                                             |
| AC_XCODE_VERSION        | Specifies the Xcode version                                                                           |
| AC_VALIDATION_CONDITION | TestFlight's `internalBuildState` and `externalBuildState` will be checked according to the selection |
| AC_SUCCESS_STATUSES     | You can customize `Acceptable/Succeeded` App Store statuses for your app                              |
| AC_RELEASE_NOTES        | Filling out that area may effect the App Store submission process.                                    |
| AC_STACK_TYPE           | `App Store` or `TestFlight` stages                                                                    |
| AC_APPROVAL_EMAILS      | Enter an email address to send special `Approve` and `Reject` links                                   |

### Android Publish Reserved Variables

| Variable             | Description                                                                                                                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| AC_RELEASE_STATUS    | Allow you to specify `draft` or `completed` app statuses on the Google Play Console. The first upload may require a draft upload  |
| AC_TRACK_TO_CHECK    | It's recommended to check Track that you've sent the app in previous steps                                                        |
| AC_ACCEPTED_STATUSES | Statues of `completed`,`inProgress`,`draft`,`halted` can be used                                                                  |
| AC_HUAWEI_APP_ID     | Huawei requires `Huawei App ID` to be send to AppGallery                                                                          |
| AC_RELEASE_NOTES     | Filling out that area may effect `Huawei` or `Google Play` submission process                                                     |
| AC_STACK_TYPE        | Select a release track to which to send the binary. After the binary is uploaded, you can release it from the Google Play Console |
| AC_APPROVAL_EMAILS   | Enter an email address to send special `Approve` and `Reject` links                                                               |
