---
title: Android Sign
description: This step signs your APK or AAB with the given Android keystore and exports a binary file compatible with Android devices.
tags: [android, mobile, sign]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Sign

**Android Sign** step signs your *APK* or *AAB* with the given Android *keystore* and exports a binary file compatible with Android devices.

:::info

This step follows the [**Android Build**](/workflows/android-specific-workflow-steps/android-build) step to sign the unsigned build output if the project doesn't include a *keystore*. If your project includes a *keystore*, the build application step will generate a signed artifact. If you do not disable this step, your artifact will be unsigned and then re-signed using the *keystore* selected in the **Configuration** or in this step.

:::

:::caution Debug Variant Signing  

As noted in the [**Android Developer documentation**](https://developer.android.com/build/build-for-release):

> If the build variant you've selected is a debug build type, then the APK is signed with a debug key and it's ready to install. If you've selected a release variant, then, by default, the APK is unsigned and you must manually [sign the APK](https://developer.android.com/studio/publish/app-signing).

When you build your app with the **debug** variant and select a keystore in [configurations](/build/platform-build-guides/building-android-applications#signing), the **Android Sign** step will replace the default debug signing files and re-sign the app using the specified keystore files.

:::

### Prerequisites

Before running the **Android Sign** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step relies on the **Android Build** step and the **Git Clone** step is necessary for the **Android Build** step to run successfully. |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | The app required for this step is generated by the **Android Build** (or alternative build steps). |

:::caution

If a step other than the **Android Build** step is used to build an app, then the **Android Sign** step depends on this step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-sign_0.png' alt="image1" />

:::danger

To share the signed apps created as an output of this step or to view them on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your workflow after this step.

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-sign_1.png' alt="image1" />

| Variable Name               | Description                                  | Status |
|-----------------------------|----------------------------------------------|--------|
| `$AC_APK_PATH` | The path of the *APK* file. This path is automatically generated in the **Android Build** step. You may need to modify this input variable to provide a different path. | Required |
| `$AC_AAB_PATH` | The path of the *AAB* file. This path is automatically generated in the **Android Build** step. You may need to modify this input variable to provide a different path. | Required |
| `$AC_ANDROID_KEYSTORE_PATH` | *Keystore* file can be selected in the **Configuration**. This value will be auto-generated depending on your *keystore* file selection in [signing configuration on Appcircle](/build/platform-build-guides/building-android-applications#signing). | Required |
| `$AC_ANDROID_KEYSTORE_PASSWORD` | Password for the selected *keystore* file. This value will be auto-generated based on your *keystore* file selection. | Required |
| `$AC_ANDROID_ALIAS` | Alias name for the selected *keystore* file. This value will be auto-generated depending on your **Configuration** |
| `$AC_ANDROID_ALIAS_PASSWORD` | Alias password for the selected *keystore* file. This value will be auto-generated depending on your **Configuration** |
| `$AC_V2_SIGN` | Defaults to false. Set true if the signature should be done using apksigner instead of jarsigner. For more information, [Apps targeting Android 11 require APK Signature Scheme v2](https://developer.android.com/about/versions/11/behavior-changes-11#minimum-signature-scheme). | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-sign_2.png' alt="image2" />

| Variable Name          | Description                                 |
|------------------------|---------------------------------------------|
| `AC_SIGNED_APK_PATH`  | Path for the signed *APK* file output. If an *APK* file is provided as input, the signed app will also be in *APK* format. |
| `AC_SIGNED_AAB_PATH`  | Path for the signed App Bundle file output. If an *AAB* file is provided as input, the signed app will also be in *AAB* format. |

:::tip

If both input value types (*AAB* and *APK*) are provided, the same type of signed app will be generated for both.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-sign-component.git
