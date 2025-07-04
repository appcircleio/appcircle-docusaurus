---
title: Publish Variables
description: Learn how to set up and manage key-value pairs that are essential for the app publishing process in Appcircle
tags: [publish variables, publish, variables]
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The **Publish Variables** section within the Publish module is a feature that allows you to set up and manage key-value pairs that are essential for the app publishing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5631-Publish-Variables-annotated.png' />

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

:::info

Please note that Publish Variables can only be used within the Publish module.

:::

### Downloading environment variables

You can download and view environment variables in **JSON** format. For this, you can use the "Download" button by clicking on the three dots next to one of the variable groups under "Publish > Publish Variables > Variable Groups".

In the downloaded file content, you will see a structure with **key-value** pairs.

In addition, if the value part of the environment variable is set to hidden during the text-based environment variable addition process, the "isSecret" value will be `true` and the key, along with the value **will not** be listed in the downloaded file. The same rule is valid for file type variables. If it is not hidden, this value will be `false`, and the value will be visible.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6155-variable4.png' />

:::info
An example of publish variable downloaded as a JSON file:

```json
[
  {
    "key": "API_URL",
    "value": "https://api.example.com",
    "isSecret": false,
    "isFile": false,
    "id": "API_URL"
  }
]
```

As seen in the example above;

- if the **isSecret** value is `false`, it has visible value
- if the **isSecret** value is `true` or **isFile** value is `true` , the key and the value will not be downloaded.
  :::

### Uploading environment variables

The Upload feature allows users to bulk-import environment variables into any existing Variable Group (e.g., Staging, Prod, or Dev) within the Publish > Publish Variables > Variable Groups section.

This feature streamlines the process of configuring variables by enabling users to upload a predefined JSON file instead of manually entering each variable.

The uploadable file must be a `.json` file with an array of variable objects. Each variable object must include the following fields:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6155-variable5.png' />

```json
[
{
"key": "API_URL",
"value": "https://api.example.com",
"isSecret": false,
"isFile": false,
"id": "API_URL"
},
{
"key": "API_KEY",
"value": "12345-abcde-67890-fghij",
"isSecret": true,
"isFile": false,
"id": "API_KEY"
}
]
```

:::warning
-	File type variables (isFile: `true`) cannot be uploaded using JSON. These must be added manually via the UI.
-	The Download feature does not include secret values or file contents for security reasons.
-	You can edit your own JSON files to update variables in a group. However, duplicated keys are not allowed.
:::

## Reserved Variables

There are some reserved variables that are automatically defined by Appcircle and can be used in the publish flow.

:::tip Additional Environment Variables Reference

This documentation also includes additional output environment variables from publish flow steps that may be useful to users.

For any input or output variables not listed here, please refer to the "Input Variables" or "Output Variables" sections on each publish flow step’s [documentation](/publish-integrations).

If there is an environment variable you believe should be included here, please [contact us here](https://appcircle.io/support/).

:::

### Common Publish Reserved Variables

| Variable                            | Description                                                                                                                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_RELEASE_NOTES                    | Specifies the release notes from the [Build profile](/build) (if published from there) or from one of the Publish steps, to be published to the stores (`Google Play`, `Huawei AppGallary`, or `App Store`). |
| AC_ORGANIZATION_ID                  | Specifies the organization ID where the publish process starts.                                                                                                                                              |
| AC_USER_ID                          | Specifies the user ID who started the publish process.                                                                                                                                                       |
| AC_USER_EMAIL                       | Specifies the email address of the user who started the publish process.                                                                                                                                     |
| AC_STORE_NAME                       | Name of the store where the app is being published.                                                                                                                                                          |
| AC_PLATFORM_TYPE                    | Platform type (e.g., `iOS:1`, `Android:2`).                                                                                                                                                                  |
| AC_UNIQUE_NAME                      | Unique name of the app (starts with `com.` for Android and iOS).                                                                                                                                             |
| AC_PUBLISH_APP_VERSION              | Version of the app being published (e.g., `1.0.1`).                                                                                                                                                          |
| AC_PUBLISH_APP_VERSION_ID           | App version ID being published on Appcircle.                                                                                                                                                                 |
| AC_PUBLISH_APP_VERSION_CODE         | Version code of the app being published.                                                                                                                                                                     |
| AC_APP_VERSION_NAME                 | Name of the app version being published.                                                                                                                                                                     |
| AC_STORE_CREDENTIAL_ID              | ID of the store credential where the app is being published.                                                                                                                                                 |
| AC_PUBLISH_PROFILE_ID               | Specifies the profile ID who started the publish process on Appcircle.                                                                                                                                       |
| AC_TASK_ID                          | Task ID associated with the publish process on Appcircle.                                                                                                                                                    |
| AC_PUBLISH_ID                       | Publish ID on Appcircle.                                                                                                                                                                                     |
| AC_PUBLISH_STEP_ID                  | Publish step ID on Appcircle.                                                                                                                                                                                |
| AC_RESOURCE_ID                      | Resource ID used in the publishing process on Appcircle.                                                                                                                                                     |
| AC_ORGANIZATION_POOL_ID             | Pool ID of the organization where the publish process starts.                                                                                                                                                |
| AC_SOURCE_ID                        | Source ID of the process (e.g., `Publish`).                                                                                                                                                                  |
| AC_MODULE_NAME                      | Name of the module in the process (e.g., `Publish`).                                                                                                                                                         |
| AC_PUBLISH_PROFILE_NAME             | Specifies the Appcircle profile name who started the publish process.                                                                                                                                        |
| AC_PUBLISH_STEP_NAME                | Name of the publish flow step being run.                                                                                                                                                                     |
| AC_PUBLISH_FLOW_NAME                | Name of the publish workflow being run.                                                                                                                                                                      |
| AC_PUBLISH_STEPS_STATUS             | Provides detailed information about the status of the publish steps executed so far. Steps that are disabled will not appear in this environment variable. The JSON output for executed steps includes the following fields: <br />- **StepName**: The name of the executed step. <br />- **StepId**: The unique ID of the executed step. <br />- **StepStatus**: The status of the step. Possible values: `Success`, `Warning`, `Failed`, `NotStarted`, or `Stopped`. <br />- **Duration**: The time taken to complete the step, represented in seconds (e.g., `0.0000000`). <br />- **StartDate**: The start time of the step, formatted as an ISO 8601 timestamp (e.g., `2024-12-13T15:45:59.6426984Z`). <br />- **FinishDate**: The completion time of the step, also formatted as an ISO 8601 timestamp (e.g., `2024-12-13T15:45:59.6426984Z`). <br /> For additional details and instructions on how to format this output for readability, refer to the [**How can I print the status of publish steps with detailed information?**](/publish-integrations/common-publish-integrations/custom-script#how-can-i-print-the-status-of-publish-steps-with-detailed-information) documentation. |
| AC_APP_FILE_URL                     | URL of the app file being published.                                                                                                                                                                         |
| AC_APP_FILE_NAME                    | Name of the app file being published (with file extension).                                                                                                                                                  |
| AC_STACK_TYPE                       | The type of software stack used during the publishing process, such as Xcode, Gradle, etc. Please follow the necessary mapping values below:  <br />- **App Store = 12** <br />- **TestFlight = 10** <br />- **Alpha = 0** <br />- **Beta = 1** <br />- **Production = 2** <br />- **Internal = 3**                                                                                           |
| AC_AUTHORIZATION                    | (Removed, redundant)                                                                                                                                                                                         |
| AC_PURPOSE                          | The intended purpose of the app, detailing its functionality or target audience.                                                                                                                             |
| AC_PUBLISH_ENVIRONMENT_VARIABLE_IDS | A list of environment variable identifiers used during the app publishing process, ensuring that the correct configuration is applied.                                                                       |

:::caution Release Notes

User can use `AC_RELEASE_NOTES` environment variable, if the `apk`, `aab` or `ipa` files comes from Build module.

:::

### Marketplace Reserved Variables

#### Huawei AppGallery

| Variable             | Description                                                                                                                        |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------|
| AC_HUAWEI_APP_ID     | The unique identifier assigned to the application registered in the Huawei AppGallery for integration purposes.                    |
| AC_API_KEY           | A secret key used by Appcircle to authenticate API requests and provide secure access to third-party services, such as app stores. |
| AC_API_KEY_FILE_NAME | The name of the file that stores the API key, used for secure access during integration.                                           |
| AC_GEM_FILE          | The configuration or dependency file for Ruby's gem package manager, used in the Appcircle build process.                          |
| AC_PLUGIN_FILE       | The file containing plugins or extensions for Appcircle, used to extend functionality during the build or distribution process.    |
| AC_MARKETPLACE_TYPE  | Specifies the type of app marketplace, such as Google Play, App Store, or Huawei AppGallery, where the app will be distributed.    |
| AC_FASTFILE_CONFIG   | Configuration file for Fastlane’s Fastfile, used to automate app release and build processes in Appcircle.                         |
 
#### Google Play Store

| Variable             | Description                                                                                                                                                          |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_RELEASE_STATUS    | Represents the current release status of the application, indicating whether the app is in development, in testing, or has been released to a specific marketplace.  |
| AC_APP_FILE_CONFIG   | Configuration settings related to the app's file management, including details about file formats, paths, and settings required during the build or release process. |
| AC_API_KEY           | A secure key used to authenticate API requests and authorize access to specific Appcircle services.                                                                  |
| AC_API_KEY_FILE_NAME | The name of the file that contains the API key, typically used for secure integration with external services.                                                        |
| AC_MARKETPLACE_TYPE  | Defines the app marketplace type, such as Google Play, Apple App Store, or Huawei AppGallery, where the app is distributed.                                          |

#### App Store Connect

| Variable                       | Description                                                                                                                                    |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_API_KEY_FILE_NAME           | The name of the file that contains the App Store Connect API key, used for authenticating App Store Connect integrations.                      |
| AC_API_KEY                     | A secure API key for accessing App Store Connect services.                                                                                     |
| AC_APPLE_APP_SPECIFIC_USERNAME | The Apple username specifically used for app-related tasks and authentication in App Store Connect.                                            |
| AC_APPLE_APP_SPECIFIC_PASSWORD | The application-specific password for secure access to Apple services such as App Store Connect.                                               |
| AC_APPLE_ID                    | The unique Apple ID associated with the developer account used to manage app releases and distribution.                                        |
| AC_APPLE_STORE_SUBMIT_API_TYPE | Specifies the type of API used for submitting apps to the Apple App Store, typically defining the submission process.                          |
| AC_BUNDLE_ID                   | The unique identifier (Bundle ID) for the app, used for identifying the app in App Store Connect and during submission.                        |
| AC_MARKETPLACE_TYPE            | Defines the marketplace type, such as Apple App Store, where the app will be distributed.                                                      |
| AC_XCODE_VERSION               | The version of Xcode used for building and submitting the app to the App Store.                                                                |
| AC_FASTFILE_CONFIG             | Configuration for Fastlane’s Fastfile, used to automate the app release and build process.                                                     |
| AC_SCREEN_SHOT_LIST            | A list of app screenshots required for submission to the App Store, showcasing the app's interface and functionality.                          |
| AC_APP_PREVIEW_LIST            | A list of app preview videos required for submission to the App Store, highlighting the app's features.                                        |
| AC_METADATA_LOCALIZATION_LIST  | A list of metadata localizations for the app, containing translated descriptions, keywords, and other localized content for different regions. |

#### Microsoft Intune

| Variable                       | Description                                                                                                               |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| AC_ORGANIZATION_NAME           | The name of the organization or team that owns the app and is associated with the Apple Developer account.                |
| AC_BUNDLE_ID                   | The unique identifier (Bundle ID) for the app, used for identifying the app in App Store Connect and during submission.   |
| AC_ICON_RESOURCE_REFERENCE_ID  | The reference ID for the app's icon resource, used to associate the correct icon during the build and submission process. |
| AC_MARKETPLACE_TYPE            | Defines the marketplace type, such as Apple App Store, where the app will be distributed.                                 |
| AC_XCODE_VERSION               | The version of Xcode used for building and submitting the app to the App Store.                                           |


### iOS Publish Reserved Variables

| Variable                       | Description                                                                                                                                                                                                              |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_XCODE_LIST_DIR              | Specifies the Xcode folder list directory.                                                                                                                                                                               |
| AC_XCODE_VERSION               | Specifies the Xcode version.                                                                                                                                                                                             |
| AC_VALIDATION_CONDITION        | Used for the [Get Approval from TestFlight](/publish-integrations/ios-publish-integrations/approval-test-flight). TestFlight's `internalBuildState` and `externalBuildState` will be checked according to the selection. |
| AC_SUCCESS_STATUSES            | You can customize `Acceptable/Succeeded` App Store statuses for your app.                                                                                                                                                |
| AC_STACK_TYPE                  | `App Store` or `TestFlight` stages.                                                                                                                                                                                      |
| AC_APP_FILE_URL                | The URL where the IPA file for the app is hosted, used for distribution or submission purposes.                                                                                                                          |
| AC_APP_FILE_NAME               | The name of the IPA file that will be uploaded to the app store for submission.                                                                                                                                          |
| AC_APPLE_STORE_SUBMIT_API_TYPE | Specifies the type of API used for submitting apps to the Apple App Store, typically defining the submission process.                                                                                                    |

### Android Publish Reserved Variables

| Variable                      | Description                                                                                                                                                                                                                                |
|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AC_RELEASE_STATUS             | Used for the [Send to Google Play](/publish-integrations/android-publish-integrations/publish-to-google-play) step. Allows you to specify `draft` or `completed` app statuses on the Google Play Console.                                  |
| AC_STACK_TYPE                 | Used for the [Send to Google Play](/publish-integrations/android-publish-integrations/publish-to-google-play) step. Specifies the release track to send the binary. After the binary is uploaded, you can release it from the Google Play. |
| AC_TRACK_TO_CHECK             | Used for the [Get Approval from Google Play](/publish-integrations/android-publish-integrations/get-approval-from-google-play) step. It's recommended to check the track that you've sent the app in previous steps.                       |
| AC_ACCEPTED_STATUSES          | Used for the [Get Approval from Google Play](/publish-integrations/android-publish-integrations/get-approval-from-google-play) step. Statuses of `completed`,`inProgress`,`draft`,`halted` can be used.                                    |
| AC_HUAWEI_APP_ID              | Used for the [Send to Huawei AppGallery](/publish-integrations/android-publish-integrations/publish-to-huawei-appgallery) step. Huawei requires `Huawei App ID` to be sent app to Huawei App Gallery.                                      |
| AC_APP_FILE_URL               | The URL where the APK file for the Android app is hosted, used for distribution or submission purposes.                                                                                                                                    |
| AC_APP_FILE_NAME              | The name of the APK file that will be uploaded to the app store for submission.                                                                                                                                                            |
| AC_ICON_RESOURCE_REFERENCE_ID | The reference ID for the app's icon resource, used to associate the correct icon during the build and submission process.                                                                                                                  |
| AC_APP_ICON_URL               | The URL of the app icon that will be displayed in the app store and on devices.                                                                                                                                                            |
| AC_APP_ICON_FILE_NAME         | The name of the file containing the app icon, used during the app submission process.                                                                                                                                                      |

## FAQ

### How to change environment variable and exchange it between steps?

In the Appcircle Publish module, the steps within a Publish flow operate independently. This means that each step is executed in a separate, clean runner environment. This feature allows steps to run independently and individually. Therefore, to exchange environment variables between steps, the modified ENV value needs to be saved as an output variable.

Below is an example of how this can be done. Once an ENV variable is modified in a step and saved to the output direction, it will become accessible in another step.

- For the first step. Suppose we create a release note using the [**Publish Release Note Component**](/workflows/common-workflow-steps/publish-release-notes) during the build process. We then want to modify and use this release note during the Publish process.

:::caution

Predefined Publish Variables can also be modified using this method; however, once the flow is completed, they will revert to their originally defined default values.

:::

```bash

# Take AC_RELEASE_NOTES value
ac_build_release_notes="$AC_RELEASE_NOTES"

# Check the variable if it is null
if [ -z "$ac_build_release_notes" ]; then
  echo "Error: AC_RELEASE_NOTES variable was not determined or it is null."
  exit 1
else
  # Print current value
  echo "Before: $ac_build_release_notes"

  # Change release note value
  ac_build_release_notes="Release note changed\n New Release note prepared"

  # Print changed value
  echo -e "Changed: $ac_build_release_notes"

  # Write new env value AC_CHANGED_RELEASE_NOTES to .env file in output direction
  echo -e "AC_CHANGED_RELEASE_NOTES=\"${ac_build_release_notes}\"" >> $AC_OUTPUT_DIR/AC_OUTPUT.env
fi

```

- For the second step: We can now access this environment variable directly in another step.

```bash

echo "Print Changed Release Note Variable"
echo $AC_CHANGED_RELEASE_NOTES

```
