---
title: Data Theorem Mobile Secure
description: Data Theorem Mobile Secure, enables users to automatically scan their mobile applications for security vulnerabilities and compliance issues directly from the Appcircle.
tags: [data theorem, secure, mobile]
---

import Screenshot from '@site/src/components/Screenshot';

# Data Theorem Mobile Secure

The **Data Theorem Mobile Secure** step integrates the [Data Theorem Mobile Secure](https://www.datatheorem.com/products/mobile-secure/) service into the CI/CD workflow on Appcircle. This step allows users to automatically scan their mobile applications for security vulnerabilities and compliance issues, facilitating proactive security testing. Developers can identify and resolve potential security threats before deploying their mobile applications.

### Prerequisites

The workflow steps that need to be executed before running the **Data Theorem Mobile Secure** step vary depending on the platform and are listed below:

#### For Android (Java / Kotlin and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | Generates the app required for the **Data Theorem Mobile Secure** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | Required if using a signed app. Processes the output for signing. If already signed, this step can be skipped. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-datatheorem_1.png'/>

#### For iOS (Objective-C / Swift and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-datatheorem_2.png'/>

#### For Android Flutter 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Flutter Build for Android**](/workflows/flutter-specific-workflow-steps#flutter-build-for-android) | Generates the app required for the **Data Theorem Mobile Secure** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | Required if using a signed app. Processes the output for signing. If already signed, this step can be skipped. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-datatheorem_3.png'/>

#### For iOS Flutter

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |
| [**Flutter Build for iOS**](/workflows/flutter-specific-workflow-steps#flutter-build-for-ios) | Prepares the Flutter project for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-datatheorem_4.png'/>

### Input Variables

Specific input variables are required for the operation of each component in your system. The following are the input variables necessary for the **Data Theorem Mobile Secure** step:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-datatheorem_5.png'/>

:::danger

Confidential information should be entered as a [secret environment variable](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [environment variable group](/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](/build/build-process-management/build-profile-configuration/).

:::

| Variable Name           | Description                                                                                    | Status   |
| ----------------------- | ---------------------------------------------------------------------------------------------- | -------- |
| `$AC_DT_FILE_PATH`      | Specifies the file path to the IPA or APK to upload. For Android, use `$AC_APK_PATH` or `$AC_SIGNED_APK_PATH`. For iOS, use `$AC_EXPORT_DIR/Myapp.ipa`. | Required |
| `$AC_DT_UPLOAD_API_KEY` | Specifies the Data Theorem Mobile Secure Upload API Key.  You need to obtain your organization's Upload API key from the portal. For more details, refer to [this document](https://docs.securetheorem.com/mobile_security_devops/uploading_mobile_apps.html). | Required |


### Output Variables

The **Data Theorem Mobile Secure** step does not produce any output variables. The results are shown in the build log.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-datatheorem-component