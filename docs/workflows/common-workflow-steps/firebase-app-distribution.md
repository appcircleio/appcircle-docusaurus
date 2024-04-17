---
title: Firebase App Distribution
description: Firebase App Distribution, enables developers to distribute their applications to testers and stakeholders for testing purposes.
tags: [firebase, mobile, distribution]
sidebar_position: 8
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase App Distribution

[**Firebase App Distribution**](https://firebase.google.com/docs/app-distribution) is a platform provided by [Google Firebase](https://firebase.google.com/) that enables developers to distribute pre-release versions of mobile apps to testers and stakeholders. This platform streamlines the distribution of Android and iOS apps and offers features such as targeted distribution, release notes, and feedback collection.
The Appcircle **Firebase App Distribution** step enables you to efficiently distribute your mobile applications to testers and relevant parties directly from your Appcircle workflow. With this integration, you can optimize the distribution process and gather valuable feedback to iterate on your app before its public release.

:::caution

Please note that you can also distribute your app via Appcircle. Utilizing Appcircle's distribution modules enhances manageability within the platform.

For more details, please refer to the following links:

- [Appcircle Testing Distribution](https://docs.appcircle.io/distribute/)
- [Appcircle Enterprise App Store](https://docs.appcircle.io/enterprise-appstore/)
- [Appcircle Publish](https://docs.appcircle.io/publish-module/)

:::

### Prerequisites

Below are the workflow steps required before running the **Firebase App Distribution** step, listed with their reasons. Prerequisites vary by platform:

#### For Android (Java / Kotlin and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Android Build**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/android-build) | Generates the app required for the **Firebase App Distribution** step.                                                                           |
| [**Android Sign**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/android-sign)   | Required for signing the app; processes the app for signing. This step can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-firebase-app-distribution_1.png'/>

#### For iOS (Objective-C / Swift and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-firebase-app-distribution_2.png'/>

#### For Android Flutter 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Flutter Build for Android**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-build-for-android) | Generates the app required for the **Firebase App Distribution** step.                                                                           |
| [**Android Sign**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/android-sign)   | Required for signing the app; processes the app for signing. This step can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-firebase-app-distribution_3.png'/>

#### For iOS Flutter

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |
| [**Flutter Build for iOS**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-build-for-ios) | Prepares the Flutter project for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-firebase-app-distribution_4.png'/>

### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for **Firebase App Distribution** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-firebase-app-distribution_5.png'/>

:::warning

Confidential information should be entered as a [secret environment variable](https://docs.appcircle.io/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [environment variable group](https://docs.appcircle.io/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/).

:::

| Variable Name                   | Description                                                                                                                                                           | Status   |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_FIREBASE_VERSION`         | Specifies the Firebase version to be used. Enter your Firebase version, such as `v11.11.0`, for a specific version. The default value is `latest`.                                                  | Required |
| `$AC_FIREBASE_APP_PATH`        | Specifies the full path of the build. For example, `$AC_EXPORT_DIR/Myapp.ipa` or `$AC_APK_PATH`.                                                             | Required |
| `$AC_FIREBASE_APP_ID`          | Specifies your app's Firebase App ID. You can find the app ID in the [Firebase console](https://console.firebase.google.com/u/0/).                                                                      | Required |
| `$AC_FIREBASE_TOKEN`           | Specifies a refresh token that's printed when you authenticate with the `firebase login:ci` command. **Select either a Firebase token or a Google Service account**.  | Optional |
| `$GOOGLE_APPLICATION_CREDENTIALS` | Specifies the path of the Google Service Account JSON. Upload the service account as a file to your environment group and name it `GOOGLE_APPLICATION_CREDENTIALS`. **Select either a Firebase token or a Google Service account**. | Optional |
| `$AC_FIREBASE_RELEASE_NOTES`   | Specifies the release notes for this build. If you want to use a file for release notes, leave this field empty and configure the next section.                     | Optional |
| `$AC_FIREBASE_RELEASE_NOTES_PATH` | If you use the Publish Release Notes component before this step, `release-notes.txt` will be used as release notes.                                                  | Optional |
| `$AC_FIREBASE_GROUPS`          | Specifies the Firebase tester groups you want to invite.                                                                                               | Optional |
| `$AC_FIREBASE_EXTRA_PARAMETERS` | Specifies extra command line parameters. Enter `--debug` for debug mode.                                                                                              | Optional |

### Output Variables

The **Firebase App Distribution** step generates no output variables. The step succeeds if the app is distributed successfully; otherwise, it fails.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-firebase-distribution-component
