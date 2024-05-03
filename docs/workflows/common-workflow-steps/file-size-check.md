---
title: File Size Check
description: Use File Size Check to monitor your app's size. Break the pipeline or show warnings when the size limit is exceeded.
tags: [build, test, file, size, check, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# File Size Check

The **File Size Check** component checks the size of your generated **IPA**, **APK** or **AAB** file. It compares it against the size you have given and if the size is exceeded, it either breaks the pipeline or shows it as a warning.

### Prerequisites

The workflow steps that need to be executed before running the **File Size Check** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                                                                                                      | Description                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator)      | If your project is an **iOS** project using **Objective-C/Swift** or **React Native**, you should use this step to generate the file before checking the app file size. This step generates the **IPA** file.       |
| [**Flutter Build for iOS**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps/#flutter-build-for-ios)         | If your project is an **iOS** project using **Flutter**, you should use this step to generate the file before checking the app file size. This step generates an **IPA** file.                                      |
| [**Android Build**](https://docs.appcircle.io/workflows/android-specific-workflow-steps#android-build)                          | If your project is an **Android** project using **Java/Kotlin** or **React Native**, you should use this step to generate the file before checking the app file size. This step generates **APK** or **AAB** files. |
| [**Flutter Build for Android**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps/#flutter-build-for-android) | If your project is an **Android** project using **Flutter**, you should use this step to generate the file before checking the app file size. This step generates **APK** or **AAB** files.                         |

:::danger
If you use a different build step than the ones mentioned above to generate the app, then the **File Size Check** step depends on this particular step.
:::

#### For iOS

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_order.png' />

#### For Android

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_order_android.png' />

### Input Variables

When you enter this component detail, you need to specify the **File Size** and **Check Action**. The file size parameter here represents the **maximum allowable** size of the **IPA**, **APK** or **AAB** file. If the archived application size exceeds this size, the pipeline will be **broken** or **warned** according to the **fail** or **warn** option you specify in the check action parameter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_action.png' />

If you select **warn**, this is how it will appear in your build list:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2582-size_warn.png' />

You can find all the parameters required for this step in the table below, with their descriptions in detail.

| Variable Name                     | Description                                                                                                                                                           | Status   |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_ANALYZER_SOURCE_PATH`        | Full path of the **APK**, **AAB** or **IPA** file. Don't change it to use default artifacts. This path will be generated after the build steps.                       | Required |
| `$AC_ANALYZER_FILESIZE_THRESHOLD` | File size threshold of the artifacts in megabytes. Enter **0** to disable the check. The default variable is **200MB**.                                               | Required |
| `$AC_ANALYZER_FILESIZE_ACTION`    | Specifies whether to issue a warning or fail the workflow if the threshold limit is exceeded. The options are **warn** and **fail**, with the default being **fail**. | Optional |

:::caution
Note that this step only controls the size of the application generated according to the size variable you specify.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-filesize-component
