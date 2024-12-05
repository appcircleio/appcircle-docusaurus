---
title: Flutter Build for Android
description: The Flutter Build for Android step builds your Flutter project with Flutter SDK.
tags: [flutter, build, android]
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Build for Android

The **Flutter Build for Android** step automates the generation of Android APK (Android Package) or AAB (Android App Bundle) files from [Flutter](https://flutter.dev) source code using the [Flutter SDK](https://docs.flutter.dev/tools/sdk). This simplifies the process of creating distributable packages for Flutter applications.

### Prerequisites

Before running the **Flutter Build for Android** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step | Description                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step fetches the repository that needs to be built from the specified branch. It is essential for initiating the Flutter Android build process. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_2.png'/>

| Variable Name                 | Description                                                                                           | Status    |
|-------------------------------|-------------------------------------------------------------------------------------------------------|-----------|
| `$AC_FLUTTER_PROJECT_DIR`     | Specifies the directory at the root of your Flutter project where the `pubspec.yaml` file is located. | Required  |
| `$AC_OUTPUT_TYPE`             | Defines the output type, such as `APK` or `AAB` (Android App Bundle).                                 | Required  |
| `$AC_FLUTTER_BUILD_MODE`      | Specifies the Flutter build mode. The default value is `release`.                                    | Optional  |
| `$AC_FLUTTER_BUILD_EXTRA_ARGS`| Additional custom build arguments. For instance: `--split-per-abi`.                                   | Optional  |

:::info

If the required variables are already defined in the **Configuration** section, there is no need to redefine them in the Workflow. For more details, see the [Build Profile Configuration Overview](/build/build-process-management/build-profile-configuration). The details you provide in the configuration will serve as input for the **Android Build** step. Kindly substitute the example information with your details:

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_3.png'/>

:::

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Output Variable           | Description                     |
|---------------------------|---------------------------------|
| `AC_APK_PATH`            | Path of the generated APK file. |        
| `AC_AAB_PATH`            | Path of the generated AAB file. |

:::info

The resulting files will be either APK or AAB, based on the `Output Type` selected in the project [Configuration](/build/build-process-management/build-profile-configuration).

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-flutter-build-component

---

## FAQ

### How can I solve the `Out of memory error: Java heap memory` or set the heap memory during the build?

To resolve this issue, please refer to the following document for detailed instructions:

- [Android Build FAQ](/workflows/android-specific-workflow-steps/android-build#how-can-i-solve-the-out-of-memory-error-java-heap-memory-or-set-the-heap-memory-during-the-build)