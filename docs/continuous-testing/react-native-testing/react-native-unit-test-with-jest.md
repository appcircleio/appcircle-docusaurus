---
title: Unit Test with Jest
description: Learn effectively run unit tests with Jest to ensure quality of React Native projects.
tags: [unit test, jest, testing strategy, quality assurance, react native testing]
---

# React Native Unit Test on Appcircle

Introduction to **React Native Unit Test** on Appcircle focuses on enhancing code quality and reliability by automating the testing of individual components and functionalities, ensuring seamless performance across different devices and environments.

## Configure Jest for Test Reports

Default Jest generates test result as JSON but the **React Native Unit Test** requires Junit style for parsing the test results.

Follow below steps to get Junit style test results:

1. First add **jest-junit** to your project as a dev dependency simply running below command:

```bash
  yarn add -D jest-junit
```

2. Add custom reporter configuration to your jest configuration file like below:

```bash
  reporters: [
    'default',
    [
      'jest-junit',
      {
        outputDirectory: './test-reports',
        outputName: 'junit-report.xml',
      },
    ],
  ],
```

When **React Native Unit Test** step will run the tests with parameter below to get test results.

```bash
yarn run jest --reporters=jest-junit
```

:::caution Output Directory

The **outputDirectory** must be set to **test-reports** at the root of the project, as the step will search for test results in that directory.

:::

:::caution Output Name

The **outputName** must be set to `\*-report.xml` at the end of the file name, as the step will search for test results for these files.

:::

## Performing React Native Unit tests in Appcircle

To run your tests during the build process, you can simply add the **React Native Unit Test** step in your workflows.

Make sure the step is placed after the following:

- [**Node Install**](/workflows/react-native-specific-workflow-steps/node-install)
- [**Npm/Yarn Commands**](/workflows/react-native-specific-workflow-steps/npm-yarn-commands)

and  make sure the step is placed before the following: 

- [**Test Reports for React Native**](/workflows/react-native-specific-workflow-steps/test-reports-react-native)
- [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts)

For detailed information on Workflow structure, please visit the [**Workflows documentation**](/workflows).

For more information, please visit the **React Native Unit Test** workflow step [documentation](/workflows/react-native-specific-workflow-steps/react-native-unit-test#prerequisites).


## Generating Test Report

If you add [Test Report Component](/workflows/react-native-specific-workflow-steps/test-reports-react-native) to your workflow, Appcircle will show the result of your tests and code coverage with a clean UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/test-reports.png' />

You must add this step **after** the `React Native Unit Test` so that it can parse test results. Your workflow should look like the below.

:::danger Step Rule

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. **If Test Report Component doesn't run, reports will not be generated.** You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail to **ON**
- Continue with the next step even if this step fails to **ON**

<Screenshot url="https://cdn.appcircle.io/docs/assets/ios-unit-test-report-steps-on.png" />

:::


## Showing Test Reports

Appcircle can show passing and failing tests in compact UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/test-reports-detail.png' />

:::caution Test Suites

The name for Test Suites appears as **undefined** because the tests are not wrapped inside a describe block, which is required for the suite name to be properly displayed in the report.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/test-reports-suite-detail.png' />