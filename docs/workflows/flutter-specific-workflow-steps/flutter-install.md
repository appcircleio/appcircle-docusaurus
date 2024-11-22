---
title: Flutter Install
description: This workflow step installs the specified Flutter SDK to run the Flutter CLI for subsequent analysis, build, and test operations.
tags: [flutter, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Install

This workflow step installs the specified [**Flutter SDK**](https://docs.flutter.dev/get-started/install) to run the [**Flutter CLI**](https://docs.flutter.dev/reference/flutter-cli) for subsequent analysis, build, and test operations. The Flutter version can be specified in [Configuration](/build/platform-build-guides/building-flutter-applications#build-configuration-for-flutter-ios-applications)

:::info

All Flutter versions and detailed information can be found in the [Flutter repository](https://github.com/flutter/flutter).

:::

### Prerequisites

There are no prerequisites required before using the **Flutter Install** step.

:::caution

These steps depend on Flutter installation and can only be used after the **Flutter Install** step:
- [**Flutter Build for iOS**](/workflows/flutter-specific-workflow-steps/flutter-build-for-ios)
- [**Flutter Build for Android**](/workflows/flutter-specific-workflow-steps/flutter-build-for-android)
- [**Flutter Analyze**](/workflows/flutter-specific-workflow-steps/flutter-analyze)
- [**Flutter Test**](/workflows/flutter-specific-workflow-steps/flutter-test)
- [**Flutter Build for Web**](/workflows/flutter-specific-workflow-steps/flutter-build-for-web)

:::


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2851-installOrder.png' />

:::danger

The steps specified in the table are steps dependent on the **Flutter Install** step. **If Flutter Install is not used before these steps**, these steps will give a **Flutter SDK not found error**.

:::


### Input Variables
This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2851-installInput.png' />

| Variable Name                 | Description                                    | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_SELECTED_FLUTTER_VERSION`| Specifies the Flutter version to install. Defaults to: `stable`. The version you set in the [Configuration](/build/platform-build-guides/building-flutter-applications#build-configuration-for-flutter-ios-applications) section will override this setting. | Optional |  

:::caution

If no specific version is specified, this step will automatically install the latest [**stable**](https://docs.flutter.dev/release/archive?tab=macos) version released by Flutter.

:::

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `PATH`| PATH variable that adds the Flutter tool to your workflow. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-install-component
