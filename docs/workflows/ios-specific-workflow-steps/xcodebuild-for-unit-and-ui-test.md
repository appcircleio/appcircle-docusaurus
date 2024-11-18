---
title: Xcodebuild for Unit and UI Testing
description: This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests.
tags: [build, test, ios, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Xcodebuild for Unit and UI Testing

This step allows you to run unit and UI tests in your project. When this step runs, all your tests are run, and an `.xcresult` file is created as a result. This step does not `build` your app, but uses the `xcodebuild` command to run tests.

:::caution

This step does not generate **IPA**, it only runs tests within the project.

:::

### Prerequisites

Before running the **Xcodebuild for Unit and UI Testing** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                                | Description                                     |
|-------------------------------------------------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone)                | The repository must be cloned to initiate the unit and UI testing process. Following the clone, this step will run the tests and create the `AC_REPOSITORY_DIR` variable. |
| [**Xcode Select**](/workflows/ios-specific-workflow-steps/xcode-select)    | This step selects the specified Xcode version. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-unitOrder.png' />

:::danger

If any tests fail during this step, an error will be automatically reported, which reflects issues within the project's tests, not the Appcircle workflow. To prevent disruption in the workflow, enable the **`"Continue with the next step even if this step fails"`** option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-continueEnable.png' />

:::


### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3098-unitInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. This path will be generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Required |
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

Ensure the simulator type matches the OS version used. For example, if you use the [**latest OS version**](https://developer.apple.com/documentation/ios-ipados-release-notes), the iPhone 14 simulator cannot be used.

:::

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name                 | Description                                                                                              |
|-------------------------------|----------------------------------------------------------------------------------------------------------|
| `AC_TEST_RESULT_PATH`        | The output path for the `.xcresult` file. This environment variable can be utilized in subsequent steps. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-test-component