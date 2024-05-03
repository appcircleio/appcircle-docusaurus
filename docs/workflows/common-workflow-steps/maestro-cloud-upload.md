---
title: Maestro Cloud Upload
description: Facilitate the execution of automated tests for mobile applications directly within Appcircle using Maestro Cloud Upload.
tags: [maestro, maestro-cloud, mobile, testing]
---

import Screenshot from '@site/src/components/Screenshot';

# Maestro Cloud Upload

[Maestro Cloud](https://cloud.mobile.dev) is a cloud-based mobile device farm for testing and debugging mobile applications, offering developers and QA teams access to a wide range of real devices for comprehensive testing across various platforms, operating systems, and device configurations.

The Appcircle **Maestro Cloud Upload** step enables users to upload their mobile applications directly to Maestro, a cloud-based mobile device farm for testing and debugging applications. This integration simplifies the process of distributing apps for testing purposes across various devices and platforms supported by Maestro. Users can configure this step within their CI/CD workflows to deploy their apps to Maestro's cloud infrastructure, facilitating efficient and comprehensive testing procedures.

## Prerequisites

Before running the **Maestro Cloud Upload** step, certain prerequisites must be completed. These prerequisites, detailed in the table below, vary depending on the platform:

### For All Platforms

| Prerequisite Workflow Step                                   | Description                                                                                                                                                                                  |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/#git-clone) | Fetches the repository to be built from the specified branch, ensuring that the [Maestro CLI](https://maestro.mobile.dev/getting-started/installing-maestro) can run on the repository path. |

### For Android (Java / Kotlin and React Native)

| Prerequisite Workflow Step                                                    | Description                                                                                                                     |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | Generates the app required for the **Maestro Cloud Upload** step.                                                               |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-maestro-cloud-upload_1.png'/>

### For iOS (Objective-C / Swift and React Native)

| Prerequisite Workflow Step                                                                                  | Description                                                             |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-maestro-cloud-upload_2.png'/>

### For Android Flutter

| Prerequisite Workflow Step                                                                            | Description                                                                                                                     |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [**Flutter Build for Android**](/workflows/flutter-specific-workflow-steps#flutter-build-for-android) | Generates the app required for the **Maestro Cloud Upload** step.                                                               |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)                           | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-maestro-cloud-upload_3.png'/>

### For iOS Flutter

| Prerequisite Workflow Step                                                                                  | Description                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file.                                                         |
| [**Flutter Build for iOS**](/workflows/flutter-specific-workflow-steps#flutter-build-for-ios)               | Prepares the Flutter project for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-maestro-cloud-upload_4.png'/>

## Input Variables

The **Maestro Cloud Upload** step requires specific input variables:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-maestro-cloud-upload_5.png'/>

:::danger

Enter confidential information as a [secret environment variable](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, select the appropriate [environment variable group](/environment-variables/managing-variables#using-environment-variable-groups-in-builds) in the [Configuration](/build/build-process-management/build-profile-configuration/).

:::

| Variable Name                    | Description                                                                                                                                                                           | Status   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_MAESTRO_API_KEY`            | The API key is required for accessing Maestro Cloud services.                                                                                                                         | Required |
| `$AC_MAESTRO_APP_FILE`           | **Android**: Specify the path to an x86 compatible APK file. **iOS**: Provide a zip archive containing an x86 compatible simulator build.                                             | Required |
| `$AC_MAESTRO_WORKSPACE`          | Specifies the directory or file path where Maestro flows are located. By default, it looks for a `.maestro` folder in the project root. Override with a workspace argument if needed. | Required |
| `$AC_MAESTRO_UPLOAD_NAME`        | Specifies the custom name for the upload.                                                                                                                                             | Optional |
| `$AC_MAESTRO_ASYNC`              | Toggle to enable asynchronous mode for running flows.                                                                                                                                 | Optional |
| `$AC_MAESTRO_ENV`                | Pass environment variables to the flows. Separate variables using a new line, or `\n`.                                                                                                | Optional |
| `$AC_MAESTRO_ANDROID_API_LEVEL`  | Set the Android API level for devices to run. The default value is `30`.                                                                                                              | Optional |
| `$AC_MAESTRO_INCLUDE_TAGS`       | Run only flows containing the specified tags (comma-separated).                                                                                                                       | Optional |
| `$AC_MAESTRO_EXCLUDE_TAGS`       | Exclude flows with the specified tags (comma-separated).                                                                                                                              | Optional |
| `$AC_MAESTRO_EXPORT_TEST_REPORT` | Toggle to export the test suite report (JUnit).                                                                                                                                       | Optional |
| `$AC_MAESTRO_EXPORT_OUTPUT`      | Specify the output file for the test file output. The default is `report.xml`.                                                                                                        | Optional |
| `$AC_MAESTRO_MAPPING_FILE`       | **Android**: Include the Proguard mapping file. **iOS**: Include the generated .dSYM file.                                                                                            | Optional |
| `$AC_MAESTRO_BRANCH`             | The branch from which the upload originated.                                                                                                                                          | Optional |
| `$AC_MAESTRO_REPO_NAME`          | The name of the repository (e.g., GitHub repo slug).                                                                                                                                  | Optional |
| `$AC_MAESTRO_REPO_OWNER`         | The owner of the repository (e.g., GitHub organization or user slug).                                                                                                                 | Optional |
| `$AC_MAESTRO_PULL_ID`            | The ID of the pull request from which the upload originated.                                                                                                                          | Optional |
| `$AC_MAESTRO_CLI_VERSION`        | The version of the Maestro CLI is to be downloaded in your CI environment. The default value is the `latest` version.                                                                 | Optional |

## Output Variables

The **Maestro Cloud Upload** step does not produce any output variables. The results are shown in the build log.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-maestro-cloud-upload-component.git
