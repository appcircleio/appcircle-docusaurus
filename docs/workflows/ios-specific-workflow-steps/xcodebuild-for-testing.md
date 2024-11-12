---
title: Xcodebuild for Testing
description: Build your app with Xcodebuild for Testing. Generate an IPA for use in test automation frameworks like BrowserStack or Testinium."
tags: [build, test, ios, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Xcodebuild for Testing

This step builds your application and generates an IPA for testing so that it can be used in test automation frameworks like [**BrowserStack**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#browserstack-app-automate---xcui) or [**Testinium**](/workflows/common-workflow-steps/testinium).

### Prerequisites

In order for this step to work correctly, it must be used after the two steps listed below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcode Select**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcode-select-version)     | This step selects the Xcode version that is specified. |
| [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#cocoapods-install)   | This step installs all the dependencies of the pod file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2827-testingOrder.png' />

:::caution
If you use SPM (Swift Package Manager), Xcode will manage itself when a project build. The **CocoaPods Install** step is not necessary.
:::

### Input Variables

You can find the parameters required for this step to work and detailed explanations in the list below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2827-testingInputs.png' />

| Variable Name                 | Description                                    | Status               |
|-------------------------------|------------------------------------------------|----------------------|
| `$AC_REPOSITORY_DIR`         | Specifies the cloned repository directory. This path will be generated after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step. | Required |
| `$AC_SCHEME`                 | Specifies the project scheme for build. If you filled in `Config => Build Schema` in the Configuration, this variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration). | Required |
| `$AC_ARCHIVE_FLAGS`             | Specifies the extra xcodebuild flag. For example: **`-quiet`** | Optional |
| `$AC_PROJECT_PATH`               | Specifies the project path. For example: **`./appcircle.xcodeproj`**. This variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration). | Required |
| `$AC_CONFIGURATION_NAME`             | You can build your project with any configuration you want. Specify the configuration as hard-coded. Appcircle will automatically add this configuration to the xcodebuild command. For example; **`Debug`** | Optional |
| `$AC_COMPILER_INDEX_STORE_ENABLE` | You can disable indexing during the build for a faster build. The default value is **`No`**. | Optional |
| `$AC_DESTINATION` | This parameter determines for which destination the application will be built and IPA will be generated. The default value is **`generic/platform=iOS`**, which means that it will be built for all iOS devices. | Required |

### Output Variables

This component outputs some important parameters after running.

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `AC_TEST_APP_PATH`           | This parameter is the path of the application after the build is complete. If you are using a test automation tool, you can use this path as the app path. |
| `AC_UITESTS_RUNNER_PATH`     | This path is the UI Runner Path for running UI tests after the build is complete. This variable is sent to test automation tools to run the tests. |
| `AC_XCTEST_PATH`             | This variable is the path containing the tests. |
| `AC_UITESTS_RUNNER_IPA_PATH` | This variable is the path that the IPA generated for the test creates for the UI tests to run. This can be sent directly to test automation tools. |
| `AC_XCTEST_ZIP_PATH`         | Path to the IPA version of the Xctests. You can access it directly via this path. |
| `AC_TEST_IPA_PATH`           | This path holds the IPA file created for running tests and sending the IPA file to test automation tools. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-build-for-testing