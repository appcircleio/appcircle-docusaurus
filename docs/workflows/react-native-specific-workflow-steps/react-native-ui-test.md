---
title: React Native UI Test
description: Learn how to run UI tests with Detox for your React Native projects easily with Appcircle, ensuring high-quality code and improved app performance.
tags: [react native, mobile, workflow, step, test, ui test, detox]
---

import Screenshot from '@site/src/components/Screenshot';

# React Native UI Test

This component runs all the UI tests in your project written with [Detox](https://wix.github.io/Detox/docs/introduction/getting-started) integration. When this step is completed, it generates a test report file in `e2e-report.xml` format. You can view these test results in detail using Appcircle's [**Test Report**](/workflows/react-native-specific-workflow-steps/test-reports-react-native) component.

For detailed information for continuous testing, please visit our [React Native Continuous Testing documentation](/continuous-testing/react-native-testing/react-native-ui-test-with-detox).

To generate detailed Test Reports. Please visit our [Test Reports Component documentation](/workflows/react-native-specific-workflow-steps/test-reports-react-native).

:::info Java Version

The default Java version in Appcircle's build stacks is **Java 17**. If your project requires a **higher** or **lower** Java version, please use the [**Select Java Version**](/workflows/common-workflow-steps/select-java-version) component. On the other hand, you can see all details for build stacks both iOS and Android with this [documentation](/infrastructure).

:::

### Prerequisites

Before running the **React Native UI Test** step, you must complete certain prerequisites, as detailed in the table below:

#### For iOS

| Prerequisite Workflow Step                                                                 | Description                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone)                                | Clone the selected repository to the build machine.                                                                                                                                    |
| [**Install Node**](/workflows/react-native-specific-workflow-steps#install-node)           | This step will install Node modules for your application.                                                                                                                              |
| [**NPM/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands) | This step installs the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications. |
| [**Cocoapods Install**](/workflows/ios-specific-workflow-steps#cocoapods-install)          | This step installs all the dependencies of the pod file.                                                                                                                               |

:::info

If your **CocoaPods** dependencies are **embedded** in the project, you do not need to use the **CocoaPods Install** step to run UI tests.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/uiOrderNew.png' />

#### For Android

| Prerequisite Workflow Step                                                                            | Description                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone)                                           | Clone the selected repository to the build machine.                                                                                                                                    |
| [**Install Node**](/workflows/react-native-specific-workflow-steps#install-node)                      | This step will install Node modules for your application.                                                                                                                              |
| [**NPM/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands)            | This step installs the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications. |
| [**Wait for Android Emulator**](/workflows/android-specific-workflow-steps/wait-for-android-emulator) | This step waits for the Android Emulator to boot. You must use this step before running any UI tests.                                                                                  |

:::danger React Native UI Test for Android

For Appcircle **Cloud**, you need to use **Appcircle Linux Pool (x86_64)** to run your UI tests on the Android platform. Since **Appcircle Standard macOS Pool (arm64)** is based on **Apple Silicon's virtualization** technology, it does not support running Android emulators. If your organization has **self-hosted pools**, you can choose and use any pool that has bare-metal machines or VMs that support nested virtualization. For more information, please follow the [**Build Configuration**](/build/build-process-management/build-profile-configuration) and [**Android Build Infrastructure**](/infrastructure/android-build-infrastructure) documentations.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-androidFlow.png' />

:::caution Android Emulator

React Native UI Test component works according to the device given in the project configurations. To change the emulator device or install a new device, please follow the [**Emulator**](/infrastructure/android-build-infrastructure#emulator) documentation.

:::

:::danger Step Rule

If any workflow steps fail, Appcircle automatically skips the next steps. However, it is possible that some of your tests may fail. If you have a failing test, Appcircle will break the pipeline. If you want your pipeline not to break even if an error occurs in this step (especially for exporting test reports), you should activate the following option:

- Continue with the next step even if this step fails to **ON**

<Screenshot url='https://cdn.appcircle.io/docs/assets/uiStepRule.png' />

:::


### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/uiInputNew.png' />

| Variable Name                | Description                                                                                                                                                                                                                                                                                                                                 | Status   |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`         | Specifies the cloned repository directory. This path will be generated after the [**Git Clone**](/workflows/common-workflow-steps#git-clone) step.                                                                                                                                                                 | Required |
| `$AC_OUTPUT_DIR`             | This variable specifies the path of the artifacts that will be generated after the build is complete.                                                                                                                                                                                                                                       | Required |
| `$AC_RN_DETOX_CONFIGURATION` | Specify the detox configuration name to used when building and running the tests.                                                                                                                                                                                                                                                           | Required |
| `$AC_RN_DETOX_TEST_ARGS`     | Specify the Detox extra arguments to add the test command. The arguments will be executed by appending `detox test --configuration<configname>` to the end of the command. The default value is `--take-screenshots all` For more information, see the Detox test [CLI options](https://wix.github.io/Detox/docs/19.x/api/detox-cli/#test). | Optional |

:::danger Detox Configuration

To able to run your test successfully, you must specify the **Detox Configuration** in the `$AC_RN_DETOX_CONFIGURATION`. If you do not specify a specific configuration, UI tests will throw an error because of the configuration not found.

**Example Configuration**

```
  configurations: {
    'ios.sim.debug': {
      device: 'simulator',
      app: 'ios.debug',
    },
    'ios.sim.release': {
      device: 'simulator',
      app: 'ios.release',
    },
    'android.emu.debug': {
      device: 'emulator',
      app: 'android.debug',
    },
    'android.emu.release': {
      device: 'emulator',
      app: 'android.release',
    },
  },
```

For more information, please visit [**Continuous Testing**](/continuous-testing/react-native-testing/react-native-ui-test-with-detox) documentation.

:::

:::info How to Download Screen Shots

The Appcircle interface does **not** support displaying screenshots generated from UI tests in React Native projects. All screenshots created as a result of these tests are exported to [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) as `test_attachments.zip`. You can access the relevant screenshots in **Download Artifact** and download them directly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/downloadAttachments.png' />

:::

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name         | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| `AC_TEST_RESULT_PATH` | The output path for the `e2e-report.xml` file. This environment variable can be utilized in subsequent steps. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-react-native-ui-test-component
