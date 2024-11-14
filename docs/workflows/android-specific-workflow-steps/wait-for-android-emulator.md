---
title: Wait for Android Emulator
description: The Wait for Android Emulator step waits for the Android Emulator to boot. You must use this step before running any UI tests.
tags: [android, mobile, emulator]
---

import Screenshot from '@site/src/components/Screenshot';

# Wait for Android Emulator

The **Wait for Android Emulator** step waits for the Android Emulator to boot. You must use this step before running any UI tests.

For additional details, please refer to the [**Emulator**](https://docs.appcircle.io/infrastructure/android-build-infrastructure/#emulator) documentation.

:::danger

Ensure that you select the **Intel Pool** in the Configuration tab, as the **Wait for Android Emulator** step will not function in the **M1 Pool**. Please refer to [this documentation](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/#project-details-configuration) for selecting a pool in Configuration.

:::

### Prerequisites

Before running the **Wait for Android Emulator** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                                         | Description                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Android Build**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/android-build) | This step is necessary to obtain the Android outputs required for processing. Without adding this step beforehand, the **Wait for Android Emulator** step will still function, but the app will not be installed.                                                                                                                      |
| [**Android Sign**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/android-sign)   | If you intend to use a signed app, this step must be executed beforehand to process the output. Failure to add this step beforehand will result in the **Wait for Android Emulator** step still functioning, but since the app is not signed, there may be installation issues. If your app is already signed, you can skip this step. |

:::caution

If a step other than the **Android Build** or **Android Sign** step is used to build or sign the app, then the **Wait for Android Emulator** step depends on this step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-wait-for-android-emulator_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-wait-for-android-emulator_2.png'/>

| Variable Name               | Description                                                                                                                                                                                                                                                                                                                                                                  | Status   |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_TEST_DEVICE`           | Specifies the device for the test. The default value is `Pixel_3a`. If you use an emulator other than `Pixel_3a`, you need to create it manually. To install a different device, please follow [this document](https://docs.appcircle.io/infrastructure/android-build-infrastructure/#emulator).                                                                             | Required |
| `$AC_TEST_ADB_WAIT_SECONDS` | Specifies the number of seconds the component must wait for the emulator to boot. The default value is `300`.                                                                                                                                                                                                                                                                | Optional |
| `$AC_TEST_ADB_ARGUMENTS`    | ADB arguments for the device. For additional details about ADB arguments, please refer to the [Android Debug Bridge](https://developer.android.com/tools/adb) documentation. The default value is: `-no-window -no-audio -no-boot-anim -netdelay none -no-snapshot -wipe-data -gpu auto`. You may add new arguments, but don't change the default ones, such as `no-window`. | Required |
| `$AC_SIGNED_APK_PATH`       | The optional full path of the signed APK file to install after the emulator boots. If this step runs after the **Android Sign** step, the variable will be automatically populated. If the signing takes place in the build step and you want to directly enter the APK you received from the **Android Build** step here, you can change the variable to `$AC_APK_PATH`.    | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-wait-emulator.git
