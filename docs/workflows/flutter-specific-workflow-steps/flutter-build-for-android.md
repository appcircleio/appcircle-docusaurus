---
title: Flutter Build for Android
description: The Flutter Build for Android step builds your Flutter project with Flutter SDK.
tags: [flutter, build, android]
---

import Screenshot from '@site/src/components/Screenshot';

# Flutter Build for Android

The **Flutter Build for Android** step automates the generation of Android APK (Android Package) or AAB (Android App Bundle) files from [Flutter](https://flutter.dev) source code using the [Flutter SDK](https://docs.flutter.dev/tools/sdk). This simplifies the process of creating distributable packages for Flutter applications.

### Prerequisites

Before running the **Flutter Build for Android** step, certain prerequisites must be completed. These prerequisites are detailed in the table below:

| Prerequisite Workflow Step | Description                                                                                   |
| -------------------------- | --------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/#git-clone) | This step fetches the repository that needs to be built from the specified branch. It is essential for initiating the Flutter Android build process. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_1.png'/>

### Input Variables

Each component requires specific input variables for its operation. The input variables necessary for the **Flutter Build for Android** step are:

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_2.png'/>

| Variable Name                 | Description                                                                                           | Status    |
|-------------------------------|-------------------------------------------------------------------------------------------------------|-----------|
| `$AC_FLUTTER_PROJECT_DIR`     | Specifies the directory at the root of your Flutter project where the `pubspec.yaml` file is located. | Required  |
| `$AC_OUTPUT_TYPE`             | Defines the output type, such as `APK` or `AAB` (Android App Bundle).                                 | Required  |
| `$AC_FLUTTER_BUILD_MODE`      | Specifies the Flutter build mode. The default value is `release`.                                    | Optional  |
| `$AC_FLUTTER_BUILD_EXTRA_ARGS`| Additional custom build arguments. For instance: `--split-per-abi`.                                   | Optional  |

:::info

If the required variables are already defined in the **Configuration** section, there is no need to redefine them in the Workflow. For more details, see the [Build Profile Configuration Overview](/build/build-process-management/build-profile-configuration). The details you provide in the configuration will serve as input for the Android Build step. Kindly substitute the example information with your details:

<Screenshot url='https://cdn.appcircle.io/docs/assets/flutter-workflow-components-build_3.png'/>

:::

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Output Variable           | Description                     |
|---------------------------|---------------------------------|
| `$AC_APK_PATH`            | Path of the generated APK file. |        
| `$AC_AAB_PATH`            | Path of the generated AAB file. |

:::info

The resulting files will be either APK or AAB, based on the `Output Type` selected in the project [Configuration](/build/build-process-management/build-profile-configuration).

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-flutter-build-component