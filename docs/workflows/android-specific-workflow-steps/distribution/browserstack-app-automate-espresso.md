---
title: BrowserStack App Automate - Espresso
description: BrowserStack App Automate - Espresso is a testing solution provided by BrowserStack specifically designed for Android applications using the Espresso testing framework.
tags: [android, mobile, android, testing, browserstack]
sidebar_position: 14
---

import Screenshot from '@site/src/components/Screenshot';

# BrowserStack App Automate - Espresso

[BrowserStack App Automate - Espresso](https://www.browserstack.com/docs/app-automate/espresso/getting-started#4-execute-espresso-tests) is a testing solution provided by BrowserStack specifically designed for Android applications using the [Espresso](https://developer.android.com/training/testing/espresso) testing framework. It allows developers to run automated tests for their Android apps across a wide range of real devices hosted in the BrowserStack cloud infrastructure. This service enables efficient and comprehensive testing of Android applications, covering various scenarios and device configurations to ensure app quality and performance.

The Appcircle **BrowserStack App Automate - Espresso** step allows you to run automated tests on Android apps using the Espresso framework on real devices in the BrowserStack cloud.

### Prerequisites

The workflow steps that need to be executed before running the **BrowserStack App Automate - Espresso** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Android Build for UI Testing](https://docs.appcircle.io/workflows/android-specific-workflow-steps/#android-build-for-ui-testing) | The **Android Build for UI Testing** step must be executed to obtain the necessary Android app outputs for processing. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-browserstack-app-automate-espresso_1.png'/>

### Input Variables
For each component, specific input variables are required for its operation on your system. The input variables necessary for the **BrowserStack App Automate - Espresso** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-browserstack-app-automate-espresso_2.png'/>

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_BROWSERSTACK_USERNAME`   | Specifies the username of the BrowserStack account. Refer to [BrowserStack - Authenticate Test Runs](https://www.browserstack.com/docs/automate/cypress/authentication) for more details. | Required |
| `$AC_BROWSERSTACK_ACCESS_KEY` | Specifies the access key for the BrowserStack account. Refer to [BrowserStack - Authenticate Test Runs](https://www.browserstack.com/docs/automate/cypress/authentication) for more details. | Required |
| `$AC_APK_PATH`                | Specifies the path of the **APK** file produced in the Appcircle workflow to be sent to BrowserStack. This field is automatically populated if the **Android Build for UI Testing** step was executed in previous steps. | Required |
| `$AC_TEST_APK_PATH`           | Specifies the path of the **test APK** file produced in the Appcircle workflow to be sent to BrowserStack. This field is automatically populated if the **Android Build for UI Testing** step was executed in previous steps. | Required |
| `$AC_BROWSERSTACK_PAYLOAD`    | Specifies the payload to be sent to BrowserStack from your Appcircle workflow.`AC_BROWSERSTACK_APP_URL` and `AC_BROWSERSTACK_TEST_URL` will be auto generated. Please refer to the [documentation](https://www.browserstack.com/docs/app-automate/api-reference/espresso/builds#execute-a-build) for more details about the payload. | Optional |
| `$AC_BROWSERSTACK_TIMEOUT`    | Specifies the timeout in seconds for checking the BrowserStack plan. The default value is `600`. | Required |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-browserstack-espresso-component.git