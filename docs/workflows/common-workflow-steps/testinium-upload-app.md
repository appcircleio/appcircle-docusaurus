---
title: Testinium Upload App
description: The Testinium Upload App step enables uploading mobile applications to the Testinium platform for automated testing directly from Appcircle.
tags: [testinium, app, upload, test, mobile, app automate, automation]
---

import Screenshot from '@site/src/components/Screenshot';
import SensitiveVariablesDanger from '@site/docs/workflows/\_sensitive-variables-danger.mdx';

# Testinium Upload App

The **Testinium Upload App** step integrates the [Testinium](https://testinium.com/) testing platform into Appcircle's CI/CD workflow, allowing developers to upload mobile applications seamlessly to Testinium. This step serves as a prerequisite for executing test plans, enabling efficient and automated testing directly within the Appcircle environment.

### Prerequisites

Before running the **Testinium Upload App** step, you must complete certain prerequisites, as detailed in the table below:

:::info

After uploading the application, you should use the [**Testinium Run Test Plan**](/workflows/common-workflow-steps/testinium-run-test-plan) step to run the test plan and view the test report. If you prefer to perform both operations within the same step, use the [**Testinium**](/workflows/common-workflow-steps/testinium) step instead.

:::

#### For Android (Java / Kotlin and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | Generates the app required for the **Testinium Upload App** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium-upload-app_1.png'/>

#### For iOS (Objective-C / Swift and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium-upload-app_2.png'/>

#### For Android Flutter 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Flutter Build for Android**](/workflows/flutter-specific-workflow-steps#flutter-build-for-android) | Generates the app required for the **Testinium Upload App** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium-upload-app_3.png'/>

#### For iOS Flutter

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |
| [**Flutter Build for iOS**](/workflows/flutter-specific-workflow-steps#flutter-build-for-ios) | Prepares the Flutter project for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium-upload-app_4.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium-upload-app_5.png'/>

<SensitiveVariablesDanger />

| Variable Name               | Description                                                                                                 | Status   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_TESTINIUM_APP_PATH`    | Specifies the full file path of the build output, such as `$AC_OUTPUT_DIR/MyApp.ipa` for iOS or `$AC_APK_PATH` for Android.           | Required |
| `$AC_TESTINIUM_USERNAME`    | Specifies the Testinium username used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PASSWORD`    | Specifies the Testinium password used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PROJECT_ID`  | Specifies the Testinium project ID. This ID must be obtained from the Testinium platform.                   | Required |
| `$AC_TESTINIUM_COMPANY_ID`  | Specifies the Testinium company ID. This ID must be obtained from the Testinium platform.                   | Required |
| `$AC_TESTINIUM_TIMEOUT`     | Specifies the Testinium plan timeout in minutes.                                                            | Required |
| `$AC_TESTINIUM_MAX_API_RETRY_COUNT` | Specifies the maximum repetition in case of Testinium platform congestion or API errors.            | Required |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-testinium-upload-app-component