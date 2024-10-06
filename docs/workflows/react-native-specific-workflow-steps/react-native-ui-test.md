---
title: React Native UI Test
description: Learn how to run UI tests for your React Native projects easily with Appcircle, ensuring high-quality code and improved app performance.
tags: [react native, mobile, workflow, step, ui, tests, ui test]
---

import Screenshot from '@site/src/components/Screenshot';

# React Native UI Test

This component runs all the UI tests in your project written with [Detox](https://wix.github.io/Detox/docs/introduction/getting-started) integration. When this step is completed, it generates a test report file in `e2e-report.xml` format. You can view these test results in detail using Appcircle's Test Report component.

For detailed information for Continuous Testing. Please visit our [React Native Continuous Testing documentation](/continuous-testing/react-native-testing/react-native-ui-testing-with-detox).

To generate detailed Test Reports. Please visit our [Test Reports Component documentation](/workflows/react-native-specific-workflow-steps/test-reports-react-native).

:::info Java Version

The default Java version in Appcircle's build stacks is **Java 11**. If your project requires a **higher** Java version, please see the [**How to Change Java Version**](/workflows/common-workflow-steps/custom-script#how-to-change-java-version) document. On the other hand, you can see all details for build stacks both iOS and Android with this [documentation](/infrastructure).

:::

### Prerequisites

The workflow steps that need to be executed before running the **React Native UI Test** workflow step in both iOS and Android platforms, along with their respective reasons, are listed in the table below.

#### For iOS

| Prerequisite Workflow Step                                                                 | Description                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone)                                | Clone the selected repository to the build machine. Please use the [**Install Node**](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) step after this step. |
| [**Install Node**](/workflows/react-native-specific-workflow-steps#install-node)           | This step will install Node modules for your application. Please note that the **NPM/Yarn Commands** step should be used after this step.                                                          |
| [**NPM/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands) | This step install the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications.             |
| [**Cocoapods Install**](/workflows/ios-specific-workflow-steps#cocoapods-install)          | This step installs all the dependencies of the pod file.                                                                                                                                           |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4443-rnUiFlow.png' />

#### For Android

| Prerequisite Workflow Step                                                                            | Description                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone)                                           | Clone the selected repository to the build machine. Please use the [**Install Node**](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) step after this step. |
| [**Install Node**](/workflows/react-native-specific-workflow-steps#install-node)                      | This step will install Node modules for your application. Please note that the **NPM/Yarn Commands** step should be used after this step.                                                          |
| [**NPM/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands)            | This step install the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications.             |
| [**Wait for Android Emulator**](/workflows/android-specific-workflow-steps/wait-for-android-emulator) | This step waits for the Android Emulator to boot. You must use this step before running any UI tests.                                                                                              |

:::danger React Native UI Test for Android

You need to use **Intel pool** to run your UI tests on the Android platform. For more information, please follow the [**Build Configuration**](/build/build-process-management/build-profile-configuration) and [**Android Build Infrastructure**](/infrastructure/android-build-infrastructure) documentations.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-androidFlow.png' />

:::caution Android Emulator

React Native UI Test component works according to the device given in the project configurations. To change the emulator device or install a new device, please follow the [**Emulator**](/infrastructure/android-build-infrastructure#emulator) documentation.

:::


### Input Variables

This step contains different variables. It needs these variables to work. The table below gives explanations of these variables.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4443-rnuiTestInput1.png' />

| Variable Name                | Description                                                                                                                                                                 | Status   |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR`         | Specifies the cloned repository directory. This path will be generated after the [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step. | Required |
| `$AC_OUTPUT_DIR`             | This variable specifies the path of the artifacts that will be generated after the build is complete.                                                                       | Required |
| `$AC_RN_DETOX_CONFIGURATION` | Specify the detox configuration name to used when building and running the tests.                                                                                           | Required |

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

For more information, plese visit [**Continuous Testing**](/continuous-testing/react-native-testing/react-native-ui-testing-with-detox) documentation.

:::

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name         | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| `AC_TEST_RESULT_PATH` | The output path for the `e2e-report.xml` file. This environment variable can be utilized in subsequent steps. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-react-native-ui-test-component
