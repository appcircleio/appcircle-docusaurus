---
title: BrowserStack App Automate
description: Run your XCUI tests on BrowserStack App Automate. This step allows you to send test IPA's to the BrowserStack dashboard and run your test on it.
tags: [build, test, browserstack, app automate, xcui, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';


# BrowserStack App Automate (XCUI)

Run your [**XCUI**](https://developer.apple.com/documentation/xctest/user_interface_tests) tests on [**BrowserStack**](https://www.browserstack.com) App Automate. This step allows you to send test IPA's to the **BrowserStack** dashboard and run your test on it.

### Prerequisites

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Testing**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) | After the [**Xcodebuild for Testing**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step runs, the test IPA paths (`$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH`) will be created automatically. So that the **BrowserStack** component depends on these paths. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_order.png' />

:::danger
In the build step, if there is no **Xcodebuild Build for Testing** step before **BrowserStack**, **BrowserStack** will throw an **error** and **break the pipeline** because it cannot find the paths that your step depends on. 
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bsInput.png' />

:::danger
Do not specify the **Access Key** directly in a hard coded format in steps. Please use [**Environment Variables**](https://docs.appcircle.io/environment-variables/) when using potentially *sensitive variables* like this.
:::

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_BROWSERSTACK_USERNAME`         | Username of the **BrowserStack** account. It should come from the **BrowserStack** account. | Required |
| `$AC_BROWSERSTACK_ACCESS_KEY`       | Access key for the **BrowserStack** account. It should come from the **BrowserStack** account. For more information, please follow [this document](https://www.browserstack.com/docs/iaam/security/manage-access-keys). | Required |
| `$AC_TEST_IPA_PATH`              | Full path of the IPA file. This path will automatically generate in [**Xcodebuild for Testing**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step.| Required |
| `$AC_UITESTS_RUNNER_PATH`             | Full path of the *-Runner.app. This path will automatically generate in [**Xcodebuild for Testing**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step. | Required |
| `$AC_BROWSERSTACK_PAYLOAD`    | `$AC_BROWSERSTACK_APP_URL` and `$AC_BROWSERSTACK_TEST_URL` will be auto generated. Please check the [documentation](https://www.browserstack.com/docs/app-automate/api-reference/xcuitest/builds#execute-a-build) for more details about the payload. | Optional |
| `$AC_BROWSERSTACK_TIMEOUT` | **BrowserStack** plans a timeout in seconds. If there is any problem in BrowserStack, these variables will break the pipeline after a certain time. The default variable is **600 seconds**. | Required |

To access the source code of this component, please use the following link:

[https://github.com/appcircleio/appcircle-browserstack-xcui-component](https://github.com/appcircleio/appcircle-browserstack-xcui-component)