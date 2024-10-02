---
title: Unit Testing
description: Learn effectively run unit tests to ensure quality of react native projects
tags: [unit tests, testing strategy, quality assurance]
---

# Introduction to React Native Unit Testing on Appcircle

Introduction to React Native Unit Testing on Appcircle focuses on enhancing code quality and reliability by automating the testing of individual components and functionalities, ensuring seamless performance across different devices and environments.

## Configure Jest for Test Reports

Default jest generates test result as json but the **React Native Unit Test** requires junit style for parsing the test results.

Follow below steps to get junit style test results:

1. First add **jest-junit** to your project as a dev dependency simply running below command

```bash
  yarn add -D jest-junit
```

2. add custom reporter configuration to your jest configuration file like below

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

When **React Native Unit Test** step will run the tests with parameter below to get test results

```bash
yarn run jest --reporters=jest-junit
```

:::caution
The **outputDirectory** must be set to **test-reports** at the root of the project, as the step will search for test results in that directory.
:::

:::caution
The **outputName** must be set to **\*-report.xml** at the end of the file name, as the step will search for test results for these files.
:::

## Performing React Native Unit tests in Appcircle

To run your tests during the build process, you can simply add the **React Native Unit Test** step in your workflows.

Make sure the step is after the **Node Install**, **Npm&Yarn** and before **Export Build Artifacts**.

See the following page on our documentation to learn more about adding new workflow steps:

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

To learn more about **React Native Unit Test** step, visit its source on Github:

https://github.com/appcircleio/appcircle-react-native-unit-test-component

## Generating Test Report

If you add [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) to your workflow, Appcircle will show the result of your tests and code coverage with a clean UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-report-overview.png' />

You must add this step **after** the `React Native Unit Test` so that it can parse test results. Your workflow should look like the below.

--- TODO: Add a workflow sample screenshot ----

:::caution
The name for Test Suites appears as undefined because the tests are not wrapped inside a describe block, which is required for the suite name to be properly displayed in the report.
:::

:::danger
There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. **If Test Report Component doesn't run, reports will not be generated.** You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail to **ON**
- Continue with the next step even if this step fails to **ON**
  :::

  <Screenshot url="https://cdn.appcircle.io/docs/assets/ios-unit-test-report-steps-on.png" />

## Showing Test Reports

Appcircle can show passing and failing tests in compact UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-result-overview.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-ui-detail.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-coverage.png' />

---- TODO: Update above Screenshots ----
