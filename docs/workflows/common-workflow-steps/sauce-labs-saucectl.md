---
title: Sauce Labs Saucectl
description: The `saucectl` command line interface orchestrates the relationship between your tests in your framework, and the rich parallelization, test history filtering, and analytics of Sauce Labs.
tags: [saucectl, saucectl run, sauce labs, test, android test, emulator, device test, automation, ios test, ui test, simulator]
---

import Screenshot from '@site/src/components/Screenshot';

# Sauce Labs Saucectl

The `saucectl` command line interface orchestrates the relationship between your tests in your framework, and the rich parallelization, test history filtering, and analytics of Sauce Labs. `saucectl` performs the underlying business logic to access the tests in your existing framework, runs them in the Sauce Labs Cloud, then securely transmits the test assets to the Sauce Labs platform, where you can review, share, and evaluate your test outcomes at scale.

For more information, please visit the [Saucectl documentation](https://docs.saucelabs.com/dev/cli/saucectl/). This document will guide you on how to use the `saucectl` command and [Sauce Labs](https://docs.saucelabs.com/sauce-basics/) through Appcircle.

### Prerequisites

Below are the workflow steps required before running the **Saucectl** step, listed with their reasons. Prerequisites vary by platform:

#### For Android

| Prerequisite Workflow Step  | Description                                                                   |
| --------------------------- | ----------------------------------------------------------------------------- |
| [Android Build for UI Testing](/workflows/android-specific-workflow-steps/android-build-for-ui-testing) | This step generates the required Android test application outputs needed for testing on Sauce Labs. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3930-androidSauce1.png' />

:::info Config.yaml

For this step to work, ensure that a `config.yml` file is available. You can set this file as an environment variable in Appcircle or include it directly in your repository.

Here’s a sample `config.yml` file for [Espresso](https://docs.saucelabs.com/mobile-apps/automated-testing/espresso-xcuitest/espresso/):

```yml title=".sauce/config.yml"
apiVersion: v1alpha
kind: espresso
defaults: {}
showConsoleLog: false
sauce:
  region: eu-central-1
  concurrency: 2
espresso:
  app: $AC_APK_PATH
  testApp: $AC_TEST_APK_PATH
suites:
- name: espresso - Google Pixel .* - Android GoogleAPI Emulator
  devices:
  - name: Google Pixel .*
  emulators:
  - name: Android GoogleAPI Emulator
    platformVersions:
    - "12.0"
artifacts:
  download:
    match:
    - '*'
    when: always
    directory: artifacts
```

:::

#### For iOS

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Testing**](/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) | After the [**Xcodebuild for Testing**](/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step runs, the test IPA and APP paths (`$AC_TEST_IPA_PATH` and `$AC_TEST_APP_PATH`) will be created automatically. So that the **Saucectl Run** component depends on these paths. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-saucectlRunFlow.png' />

:::info Config.yaml

For this step to work, ensure that a `config.yml` file is available. You can set this file as an environment variable in Appcircle or include it directly in your repository.

And sample `config.yml` file for [XCUITest](https://docs.saucelabs.com/mobile-apps/automated-testing/espresso-xcuitest/xcuitest/):

```yml title=".sauce/config.yml"
apiVersion: v1alpha
kind: xcuitest
sauce:
  region: us-west-1
  concurrency: 3
  metadata:
    tags:
      - e2e
      - release team
      - other tag
    build: Release $CI_COMMIT_SHORT_SHA

xcuitest:
  app: $AC_TEST_IPA_PATH
  testApp: $AC_UITESTS_RUNNER_PATH

suites:
  - name: "saucy xcuitest"
    devices:
      - name: "iPhone.*"
        options:
          carrierConnectivity: false
          deviceType: ANY
          private: false
artifacts:
  download:
    when: always
    match:
      - "junit.xml"
    directory: ./artifacts/

reporters:
  spotlight:
    enabled: true
```

:::

### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for the **Saucectl Run for Android** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-saucectl-2.0.png'/>


| Variable Name             | Description                                                                                                      | Status   |
|---------------------------|------------------------------------------------------------------------------------------------------------------|----------|
| AC_SL_CONFIG_PATH         | Path to the Sauce Labs configuration file. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--config) documentation for the option details. Default value is `.sauce/config.yml`. | Required |
| AC_SL_USERNAME            | Sauce Labs username. It must be set as a secret environment variable.                                            | Required |
| AC_SL_ACCESS_KEY          | Sauce Labs access key. It must be set as a secret environment variable.                                          | Required |
| AC_RUN_ONLY_VIA_CONFIG    | Whether to run only using the configuration file. If set to `true`, no need to fill in the other options. Default is `false`. Options: `true, false`. | Required |
| AC_SL_SELECT_SUITE        | Specifies a test suite to execute by name rather than all suites defined in the config file. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--select-suite) documentation for details. Default value is `$AC_SL_SELECT_SUITE`. | Optional |
| AC_SL_APP_PATH            | Path to the main application file that will be tested. This should be the location of the app (APK for Android or IPA for iOS) within the Sauce Labs environment or your build process. If not provided, app will be used as default in `config.yml`. If set to `AC_APK_PATH`, [Android Build for UI Testing](/workflows/android-specific-workflow-steps/android-build-for-ui-testing) step output will be loaded automatically. Or if set to `AC_TEST_APP_PATH` for iOS, [Xcodebuild for Testing](/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step output will be loaded automatically. | Optional |
| AC_SL_TEST_APP_PATH       | Path to the test application file, which contains the test code to be run against the main app. This is usually a separate test APK for Android or an additional test bundle for iOS. If not provided, app will be used as default in `config.yml`. If set to `AC_TEST_APK_PATH`, [Android Build for UI Testing](/workflows/android-specific-workflow-steps/android-build-for-ui-testing) step output will be loaded automatically. Or if set to `AC_TEST_IPA_PATH` for iOS, [Xcodebuild for Testing](/workflows/ios-specific-workflow-steps#xcodebuild-for-testing) step output will be loaded automatically. | Optional |
| AC_SL_ARTIFACT_CLEANUP    | Clear the artifacts directory before downloading new test data. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--artifactscleanup) documentation for details. Default is `false`. Options: `true, false`. | Optional |
| AC_SL_DOWNLOAD_DIR        | Specifies the path to the folder location in which to download artifacts. A separate subdirectory is generated in this location for each suite for which artifacts are downloaded. Must be set in conjunction with `Sauce Labs Download Match` and `Sauce Labs When to Download Artifacts`. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--artifactsdownloaddirectory) documentation for details. Default value is `$AC_SL_DOWNLOAD_DIR`. | Optional |
| AC_SL_DOWNLOAD_MATCH      | Specifies which artifacts to download based on whether they match the name or file type pattern provided. Supports the wildcard character *. Must be set in conjunction with `Sauce Labs Download Directory` and `Sauce Labs When to Download Artifacts`. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--artifactsdownloadwhen) documentation for details. Default value is `$AC_SL_DOWNLOAD_MATCH`. | Optional |
| AC_SL_WHEN_ARTIFACT_DOWNLOAD | Criteria for downloading assets. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--artifactsdownloadwhen) documentation for details. Default is `never`. Options: `always, never, pass, fail`. | Optional |
| AC_SL_ASYNC               | Launch tests without waiting for preceding test results. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--async) documentation for details. Default is `false`. Options: `true, false`. | Optional |
| AC_SL_BUILD               | Associates the tests with a build to support easy filtering of related test results in the Sauce Labs UI. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--build) documentation for details. Default value is `$AC_SL_BUILD`. | Optional |
| AC_SL_CCY                 | Maximum tests to run concurrently. If the config defines more suites than the max, excess suites are queued and run in order as each suite completes. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--ccy) documentation for details. Default value is `$AC_SL_CCY`. | Optional |
| AC_SL_ENV                 | An environment variable key value pair that may be referenced in the tests executed by this command. Expanded environment variables are supported. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--env) documentation for details. Default value is `$AC_SL_ENV`. | Optional |
| AC_SL_FAIL_FAST           | Stop suite execution after the first failure. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--fail-fast) documentation for details. Default is `false`. Options: `true, false`. | Optional |
| AC_SL_REGION              | Specifies the Sauce Labs data center through which tests will run. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--region) documentation for details. Default is `eu-central-1`. Options: `us-west-1, us-east-4, eu-central-1`. | Required |
| AC_SL_RETRIES             | Number of times to rerun a failed test suite. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--retries) documentation for details. Default value is `1`. | Optional |
| AC_SL_ROOT_DIR            | Specifies the project directory. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--root-dir) documentation for details. Default value is `$AC_REPOSITORY_DIR`. | Optional |
| AC_SL_SAUCEIGNORE         | Specifies the path to the `.sauceignore` file. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--sauceignore) documentation for details. Default value is `$AC_SL_SAUCEIGNORE`. | Optional |
| AC_SL_SHOW_CONSOLE_LOG    | Include the `console.log` contents in the output for all tests. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--show-console-log) documentation for details. Default is `true`. Options: `true, false`. | Optional |
| AC_SL_TAGS                | Keywords that may help you distinguish the test in Sauce Labs, and also help you apply filters to easily isolate tests based on metrics that are meaningful to you. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--tags) documentation for details. Default value is `$AC_SL_TAGS`. | Optional |
| AC_SL_TIMEOUT             | Global timeout that limits how long saucectl can run in total. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--timeout) documentation for details. Default is `10m`. | Optional |
| AC_SL_TUNNEL_NAME         | Use a running Sauce Connect tunnel to test. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--tunnel-name) documentation for details. Default value is `$AC_SL_TUNNEL_NAME`. | Optional |
| AC_SL_TUNNEL_OWNER        | The tunnel owner, if it is not the testing account. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--tunnel-owner) documentation for details. Default value is `$AC_SL_TUNNEL_OWNER`. | Optional |
| AC_SL_TUNNEL_TIMEOUT      | How long to wait for the specified tunnel to be ready. Check [saucectl](https://docs.saucelabs.com/dev/cli/saucectl/run/#--tunnel-timeout) documentation for details. Default value is `$AC_SL_TUNNEL_TIMEOUT`. | Optional | 

### Output Variables

The artifacts generated from the **Saucectl Run** step are saved in the directory specified.  (`AC_SL_DOWNLOAD_MATCH`) parameter and determine when they are downloaded using the **Sauce Labs When to Download Artifacts** (`AC_SL_WHEN_ARTIFACT_DOWNLOAD`) parameter.

| Variable Name                   | Description                                                                                       |
|---------------------------------|---------------------------------------------------------------------------------------------------|
| `$AC_SL_DOWNLOAD_MATCH`         | You can control the format of these outputs using the **Sauce Labs Download Match** parameter.    |
| `$AC_SL_WHEN_ARTIFACT_DOWNLOAD` | Determine when they are downloaded using the **Sauce Labs When to Download Artifacts** parameter. |


To access all saved artifacts, go to the [Download Artifacts](/build/post-build-operations/after-a-build#download-artifacts) section in Appcircle at the end of the build log.

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-saucectl-run-component