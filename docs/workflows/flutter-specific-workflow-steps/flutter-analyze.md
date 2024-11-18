---
title: Flutter Analyze
description: This component runs the `flutter analyze` command in your Flutter project.
tags: [flutter, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Analyze

This component runs the `flutter analyze` command in your Flutter project. Please note that it requires the [**Flutter SDK**](https://docs.flutter.dev/get-started/install).

### Prerequisites

Before running the **Flutter Analyze** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step will clone your project through the connected Git provider and create the `$AC_REPOSITORY_DIR` variable. |
| [**Flutter Install**](/workflows/flutter-specific-workflow-steps/flutter-install) | This step will install the [Flutter SDK](https://flutter-ko.dev/development/tools/sdk/releases) release. If the version is not specified, it will install the latest **stable** version.|

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2852-flutterAnalayzeOrder.png' />

:::danger

This step is particularly dependent on the Flutter Install step. If the Flutter SDK is not installed, the step will give an error that the required command was not found.

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2852-flutterAnalyzeInput.png' />

| Variable Name                 	       | Description                         | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FLUTTER_PROJECT_DIR`         | This parameter is used as the repository path. This path is created immediately after the Git Clone step. If the Git Clone step is not used, this path cannot be found. | Required|
| `$AC_FLUTTER_ANALYZE_EXTRA_ARGS`               | You can use this parameter if you want to add an extra parameter to the build command line. | Optional |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-analyze-component
