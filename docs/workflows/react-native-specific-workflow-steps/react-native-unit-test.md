---
title: React Native Unit Test
description: Learn how to run unit tests with Jest for your React Native projects easily with Appcircle, ensuring high-quality code and improved app performance.
tags: [react native, mobile, workflow, step, unit, test, jest, unit test]
---

import Screenshot from '@site/src/components/Screenshot';

# React Native Unit Test

This component runs all the unit tests in your project written with [Jest](https://jestjs.io/docs/tutorial-react-native) integration. When this step is completed, it generates a test report file in `JUnit.xml` format. You can view these test results in detail using Appcircle's **Test Report** component. To generate detailed Test Reports. Please visit our [Test Reports Component documentation](/workflows/react-native-specific-workflow-steps/test-reports-react-native).

For detailed information for continuous testing. Please visit our [React Native Continuous Testing documentation](/continuous-testing/react-native-testing/react-native-unit-testing).

### Prerequisites

The workflow steps that need to be executed before running the **React Native Unit Test** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                                                                 | Description                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps#git-clone)                                | Clone the selected repository to the build machine.                                                                                                                                    |
| [**Install Node**](/workflows/react-native-specific-workflow-steps#install-node)           | This step will install Node modules for your application.                                                                                                                              |
| [**NPM/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands) | This step install the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4443-rnUnitFlowOrder.png'/>

:::danger Step Rule

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. **If Test Report Component doesn't run, reports will not be generated.** You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail to **ON**
- Continue with the next step even if this step fails to **ON**

<Screenshot url="https://cdn.appcircle.io/docs/assets/ios-unit-test-report-steps-on.png" />

:::

### Input Variables

This step contains different variables. It needs these variables to work. The table below gives explanations of these variables.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4443-rnUnitFlowInputs.png' />

| Variable Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                       | Status   |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository directory. This path will be generated after the [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step.                                                                                                                                                                                                                                       | Required |
| `$AC_OUTPUT_DIR`           | This variable specifies the path of the artifacts that will be generated after the build is complete.                                                                                                                                                                                                                                                                                                             | Required |
| `$AC_RN_TEST_COMMAND_ARGS` | Specify additional command arguments for running Jest tests. An extra parameter will be added to the end of the command `jest --coverage --coverageDirectory=coverage --coverageReporters=lcov` which will be used by default. You can add extra arguments, such as `--debug --colors`, without affecting the default ones. For more information, see the Jest [CLI options](https://jestjs.io/docs/cli#options). | Optional |

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name             | Description                                                                                              |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| `AC_TEST_RESULT_PATH`     | The output path for the `JUnit.xml` file. This environment variable can be utilized in subsequent steps. |
| `AC_COVERAGE_RESULT_PATH` | The output path for the coverage files. This environment variable can be utilized in subsequent steps.   |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-react-native-unit-test-component
