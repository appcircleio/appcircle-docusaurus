---
title: Flutter Build for iOS
description: Learn to build iOS apps with the Flutter Build for iOS component. Ensure Flutter Install and Git Clone steps are completed first.
tags: [flutter, build, test, workflow, step]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Build for iOS

This step makes your Flutter project suitable for the iOS environment and builds it using the [Flutter SDK](https://github.com/flutter/flutter).

### Prerequisites

:::caution
Once you have compiled your app for Flutter iOS, the native environment will be built. For this reason, this step should be used before the [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export) step.
:::

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | This step will clone your project through the connected Git provider and create the `$AC_REPOSITORY_DIR` variable. |
| [**Flutter Install**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-install) | This step will install the Flutter SDK. If a version is not specified, it will install the latest **stable** version. The **Flutter SDK** package must be installed on the system. For this reason, make sure that **Flutter Build for iOS** is used after the **Flutter Install**. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2854-flutterOrder1.png' />

:::warning
**Keep in mind** that this step is dependent on the Flutter Install step. If Flutter is not installed on the system, it will give a Flutter SDK not found error.
:::

### Input Variables

The parameters required for this step to work are given in the table below with explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2854-flutterInput.png' />

| Variable Name                 | Description                                    | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FLUTTER_PROJECT_PATH`    | This parameter is used as the repository path. This path is created immediately after the Git Clone step. If the Git Clone step is not used, this path cannot be found. | Required|
| `$AC_FLUTTER_BUILD_MODE`      | With this variable, you can add the mode you want to build in the build command. For example: `release`. | Required |
| `$AC_FLUTTER_BUILD_EXTRA_ARGS`| You can use this parameter if you want to add an extra parameter to the build command line. | Optional |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-flutter-build-component
