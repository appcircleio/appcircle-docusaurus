---
title: Testinium
description: Testinium step allows users to run automated tests on their mobile applications using Testinium directly from the Appcircle.
tags: [testinium, test]
---

import Screenshot from '@site/src/components/Screenshot';

# Testinium

The **Testinium** step integrates the [Testinium](https://testinium.com/) testing platform into Appcircle's CI/CD workflow, allowing for automated testing of mobile applications directly within the Appcircle environment. This step enables developers to execute test scripts, analyze test outcomes, and verify the quality of their mobile apps before deployment

### Prerequisites

Before running the **Testinium** step, you must complete certain prerequisites, as detailed in the table below:

#### For Android (Java / Kotlin and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | Generates the app required for the **Testinium** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_1.png'/>

#### For iOS (Objective-C / Swift and React Native) 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_2.png'/>

#### For Android Flutter 

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Flutter Build for Android**](/workflows/flutter-specific-workflow-steps#flutter-build-for-android) | Generates the app required for the **Testinium** step.                                                                           |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign)   | This step is required for signing the app. It processes the output for signing but can be skipped if the app is already signed. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_3.png'/>

#### For iOS Flutter

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) | Builds the application in ARM architecture and generates an `IPA` file. |
| [**Flutter Build for iOS**](/workflows/flutter-specific-workflow-steps#flutter-build-for-ios) | Prepares the Flutter project for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_4.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_5.png'/>

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name               | Description                                                                                                 | Status   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_TESTINIUM_APP_PATH`    | Specifies the full file path of the build output, such as `$AC_EXPORT_DIR/Myapp.ipa` for iOS or `$AC_APK_PATH` for Android.           | Required |
| `$AC_TESTINIUM_USERNAME`    | Specifies the Testinium username used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PASSWORD`    | Specifies the Testinium password used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PROJECT_ID`  | Specifies the Testinium project ID. This ID must be obtained from the Testinium platform.                   | Required |
| `$AC_TESTINIUM_PLAN_ID`     | Specifies the Testinium plan ID. This ID must be obtained from the Testinium platform.                      | Required |
| `$AC_TESTINIUM_COMPANY_ID`  | Specifies the Testinium company ID. This ID must be obtained from the Testinium platform.                   | Required |
| `$AC_TESTINIUM_MAX_FAIL_PERCENTAGE` | Specifies the maximum failure percentage limit to interrupt the workflow. It must be in the range 1-100.   | Optional |
| `$AC_TESTINIUM_TIMEOUT`     | Specifies the Testinium plan timeout in minutes.                                                            | Required |
| `$AC_TESTINIUM_MAX_API_RETRY_COUNT` | Specifies the maximum repetition in case of Testinium platform congestion or API errors.            | Required |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_6.png'/>

| Variable Name                          | Description                                             |
| -------------------------------------- | ------------------------------------------------------- | 
| `AC_TESTINIUM_RESULT_FAILURE_SUMMARY` | Total number of failures in the test.                   |
| `AC_TESTINIUM_RESULT_ERROR_SUMMARY`   | Total number of errors in the test.                     |
| `AC_TESTINIUM_RESULT_SUCCESS_SUMMARY` | Total number of successes in the test results.          |


---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-testinium-component