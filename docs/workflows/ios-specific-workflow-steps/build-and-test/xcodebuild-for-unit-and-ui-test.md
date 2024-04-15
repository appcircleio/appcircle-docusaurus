---
title: Xcodebuild for Unit and UI Testing
description: This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests.
tags: [build, test, ios, workflow, step]
sidebar_position: 8
---

import Screenshot from '@site/src/components/Screenshot';

# Xcodebuild for Unit and UI Testing

This step allows you to run unit and UI tests in your project. When this step runs, all your tests are run, and an `.xcresult` file is created as a result. This step does not `build` your app, but uses the `xcodebuild` command to run tests.

:::caution

This step does not generate **IPA**, it only runs tests within the project.

:::

### Prerequisites
| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/build-and-test/git-clone) | The repo needs to be cloned in order to start the running unit and UI test process. After the clone, unit and UI tests will be run. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |
| [**Xcode Select**](/workflows/ios-specific-workflow-steps/build-and-test/xcode-select)     | This step selects the Xcode version that is specified. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-unitOrder.png' />

:::warning

When this step runs, if there is a failed test or tests in the project, it will automatically give an error. This is actually not an error of the Appcircle workflow, but an error caused by the tests in the project finding a failure. In order not to disrupt the workflow flow 
The option **`"Continue with the next step even if this step fails"`** should be enabled.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-continueEnable.png' />

:::


### Input Variables

You can find the parameters required for this step to work and detailed explanations in the list below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-unitInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. This path will be generated after the [Git Clone](/workflows/common-workflow-steps/build-and-test/git-clone) step. | Required |
| `$AC_OUTPUT_DIR_PATH`         | Specifies the path for outputs for generated artifacts. | Required |
| `$AC_SCHEME`                  | Specifies the project scheme for build. If you filled in `Config => Build Schema` in the Configuration, this variable comes from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration). | Required |
| `$AC_ARCHIVE_FLAGS`           | Specifies the extra xcodebuild flag. For example: **`-quiet`** | Optional |
| `$AC_PROJECT_PATH`            | Specifies the project path. For example: **`./appcircle.xcodeproj`**. This variable comes from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration). | Optional |
| `$AC_CONFIGURATION_NAME`      | You can build your project with any configuration you want. Specify the configuration as hard-coded. Appcircle will automatically add this configuration to the xcodebuild command. For example; **`Debug`** | Optional |
| `$AC_COMPILER_INDEX_STORE_ENABLE`| You can disable indexing during the build for a faster build. The default value is **`No`**. | Required |
| `$AC_TEST_OS_VERSION`         | Specify the test OS version. The default value is `latest`. User can use different OS version. For example: `16.3` | Required |
| `$AC_TEST_DEVICE`             | Destination name of the test simulator device. Ex. `iPhone 14`. If you set a simulator name, the build will be installed into the given simulator. The default value is `iPhone 8 Plus`.  | Required |
| `$AC_TEST_PLATFORM`           | Specify the test platform. The default value is `iOS Simulator`. | Required |

:::caution

Be aware of which OS version you used; the simulator type should match that OS version. For example, if you use the [**latest OS version**](https://developer.apple.com/documentation/ios-ipados-release-notes), you can not use the **iPhone 14** simulator.

:::

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/build-and-test/export-build-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/build-and-test/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables
| Variable Name                 | Description                         |
|-------------------------------|-------------------------------------|
| `$AC_TEST_RESULT_PATH`        | The output path of `.xcresult` file. User can use this enviroment variable for other steps. |