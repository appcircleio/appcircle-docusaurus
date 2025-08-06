---
title: LambdaTest App Automate - Espresso
description: LambdaTest App Automate - Espresso is a cloud-based testing solution tailored for Android applications using the Espresso testing framework.
tags: [android, mobile, testing, espresso, lambdatest]
---

import Screenshot from '@site/src/components/Screenshot';
import SensitiveVariablesDanger from '@site/docs/\_sensitive-variables-danger.mdx';

# LambdaTest App Automate - Espresso

[LambdaTest App Automate - Espresso](https://www.lambdatest.com/support/docs/getting-started-with-espresso-testing/) is a cloud-based testing solution designed for Android applications using the [Espresso](https://developer.android.com/training/testing/espresso) testing framework. It enables developers to run automated tests for Android apps across a wide range of real devices hosted in the LambdaTest cloud infrastructure. This solution allows efficient, scalable, and reliable testing of Android applications to ensure app quality and compatibility.

The Appcircle **LambdaTest App Automate - Espresso** step allows you to run automated tests on Android apps using the Espresso framework on real devices in the LambdaTest cloud.

### Prerequisites

Before running the **LambdaTest App Automate - Espresso** step, ensure you have completed the following prerequisite:

| Prerequisite Workflow Step                                                                                  | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| [**Android Build for UI Testing**](/workflows/android-specific-workflow-steps/android-build-for-ui-testing) | The **Android Build for UI Testing** step must be executed to obtain the required app and test APK outputs. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lambdatest-app-automate-espresso_0.png'/>

### Input Variables

This step includes several input variable(s) required for proper execution. See the table below for a detailed description:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lambdatest-app-automate-espresso_1.png'/>

<SensitiveVariablesDanger />

| Variable Name             | Description                                                                                                                                                                                                                | Status   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_LT_USERNAME`         | LambdaTest account username. Required to authenticate API requests.                                                                                                                                                        | Required |
| `$AC_LT_ACCESS_KEY`       | LambdaTest account access key. Required to authenticate API requests.                                                                                                                                                      | Required |
| `$AC_LT_APK_PATH`            | Path to the `APK` file to upload to LambdaTest. Auto-filled by prior Android build step.                                                                                                                                 | Required |
| `$AC_LT_TEST_APK_PATH`       | Path to the test `APK` file to upload to LambdaTest. Auto-filled by prior **Android Build** step.                                                                                                                            | Required |
| `$AC_LT_PAYLOAD`          | JSON string that defines test configuration. App/Test `APK` URLs are auto-inserted. Refer to [LambdaTest API](https://www.lambdatest.com/support/docs/espresso-testing/#execute-your-first-test) documantation for payload structure. | Optional |
| `$AC_LT_TIMEOUT`          | Timeout value in seconds for test execution. Default is `600`.                                                                                                                                                             | Required |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name             | Description                           |
| ------------------------- | ------------------------------------- |
| `$AC_LT_TEST_RESULT_PATH` | Path to save test results. Must be writable. Defaults to a directory under `$AC_OUTPUT_DIR`.                    |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-lambdatest-espresso-app-automate-component.git
