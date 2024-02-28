---
title: Flutter Install
metaTitle: Flutter Install
metaDescription: Flutter Install
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Install

This workflow step installs the specified [**Flutter SDK**](https://docs.flutter.dev/get-started/install) to run the [**Flutter CLI**](https://docs.flutter.dev/reference/flutter-cli) for subsequent analysis, build, and test operations. The Flutter version can be specified in [Configuration](https://docs.appcircle.io/build/building-flutter-applications/#build-configuration-for-flutter-applications).

:::info
All Flutter versions and detailed information can be found in the [Flutter repository](https://github.com/flutter/flutter).
:::

### Prerequisites

:::caution
These steps depend on Flutter installation and can only be used after the **Flutter Install** step:
- [**Flutter Build for iOS**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-build-for-ios)
- [**Flutter Build for Android**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-build-for-android)
- [**Flutter Analyze**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-analyze)
- [**Flutter Test**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-test)
- [**Flutter Build for Web**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-build-for-web)
:::


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2851-installOrder.png' />

:::warning
The steps specified in the table are steps dependent on the **Flutter Install** step. **If Flutter Install is not used before these steps**, these steps will give a **Flutter SDK not found error**.
:::


### Input Variables
You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2851-installInput.png' />

| Variable Name                 | Description                                    | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_SELECTED_FLUTTER_VERSION`| Specifies the Flutter version to install. Defaults to: stable. The version you set in the config section will override this setting. | Optional |  

:::caution
If no specific version is specified, this step will automatically install the latest [**stable**](https://docs.flutter.dev/release/archive?tab=macos) version released by Flutter.
:::

### Output Variables

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `PATH`| PATH variable that adds the Flutter tool to your workflow. | 

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-install-component


