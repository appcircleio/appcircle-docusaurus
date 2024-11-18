---
title: Flutter Test
description: This component allows you to run Flutter unit tests.
tags: [flutter, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Test

This component allows you to run [**Flutter Unit Tests**](https://docs.flutter.dev/cookbook/testing/unit/introduction#run-tests-in-a-terminal). Please note that it requires the [**Flutter SDK**](https://flutter-ko.dev/development/tools/sdk/releases).

### Prerequisites

Before running the **Flutter Test** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step will clone your project through the connected Git provider and create the `$AC_REPOSITORY_DIR` variable. |
| [**Flutter Install**](/workflows/flutter-specific-workflow-steps/flutter-install) | This step will install the [Flutter SDK](https://flutter-ko.dev/development/tools/sdk/releases) release. If the version is not specified, it will install the latest **stable** version.|

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2853-testOrder1.png' />

:::danger

This step is particularly dependent on the Flutter Install step. If the Flutter SDK is not installed, the step will give an error that the required command was not found.

:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2853-testInput.png' />

| Variable Name                 	       | Description                         | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FLUTTER_PROJECT_DIR`     | This parameter is used as the repository path. This path is created immediately after the Git Clone step. If the Git Clone step is not used, this path cannot be found. | Required|
| `$AC_FLUTTER_JUNIT_REPORTS`       | If this is set to `YES`, [JUnit](https://junit.org/junit5/) test report will be created at the `AC_TEST_RESULT_PATH`. | Optional |
| `$AC_FLUTTER_TEST_EXTRA_ARGS`     | You can use this parameter if you want to add an extra parameter to the build command line. | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name                 	       | Description                         |
|-------------------------------|------------------------------------------------|
| `AC_TEST_RESULT_PATH`        | This path is created after the test results are reported. If you are using the [**Export Build Artifact**](/workflows/common-workflow-steps/export-build-artifacts) step, it can be accessed directly from [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts). | 

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-test-component