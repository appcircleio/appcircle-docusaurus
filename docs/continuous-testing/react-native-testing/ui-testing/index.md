---
title: UI Testing with Detox
description: Learn effectively run detox tests to ensure quality of react native projects
tags: [unit tests, ui tests, testing strategy, quality assurance]
---

# Introduction to React Native UI Test on Appcircle

UI Testing with Detox for React Native ensures the reliability and performance of mobile apps by automating interactions and validating the user experience on real devices and simulators across platforms.

## Configuring Detox for Execution on Appcircle

When you configure Detox using the `detox init` command, it generates an **e2e** folder and a `jest.config.js` file. Since Detox runs on Jest, you’ll need to set up Jest properly to generate test reports.

Default jest generates test result as json but the **React Native UI Test** requires junit style for parsing the test results.

1. First add **jest-junit** to your project as a dev dependency simply running below command

```bash
  yarn add -D jest-junit
```

2. Open `e2e/jest.config.js` file and add below report configuration to get reports junit style:

```
  reporters: [
    'detox/runners/jest/reporter',
    [
      'jest-junit',
      {
        outputDirectory: './test-reports',
        outputName: 'e2e-report.xml',
      },
    ],
  ],
```

3. Ensure that your `.detoxrc.js, file contains a valid configuration, as the workflow step requires which configuration to build and run. An example configuration might look like this:

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

:::caution
The React Native project must be built with Detox in release mode, as debug builds trigger Metro to start, which can interfere with testing. For more details, [refer to the official Detox documentation](https://wix.github.io/Detox/docs/introduction/preparing-for-ci)
:::

:::caution
The **outputDirectory** must be set to **test-reports** at the root of the project, as the step will search for test results in that directory.
:::

:::caution
The **outputName** must be set to **\*-report.xml** at the end of the file name, as the step will search for test results for these files.
:::

## Performing React Native UI tests in Appcircle

To run your tests during the build process, you can simply add the **React Native UI Test** step in your workflows.

Make sure the step is after the **Node Install**, **Npm&Yarn**, **Cocoapods Install** and before **Export Build Artifacts**.

See the following page on our documentation to learn more about adding new workflow steps:

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

To learn more about **React Native UI Test** step, visit its source on Github:

https://github.com/appcircleio/appcircle-react-native-UI-test-component

## Generating Test Report

If you add [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) to your workflow, Appcircle will show the result of your tests and code coverage with a clean UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-report-overview.png' />

You must add this step **after** the `React Native UI Test` so that it can parse test results. Your workflow should look like the below.

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
