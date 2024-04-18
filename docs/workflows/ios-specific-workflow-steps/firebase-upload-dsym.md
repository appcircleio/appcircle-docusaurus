---
title: Firebase Upload dSYM 
description: Upload your debug symbols to Firebase Crashlytics with Appcircle. Streamline your iOS app development and debugging processes.
tags: [build, test, distribute, firebase, crashlytics, ios, workflow, step]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase Upload dSYM

This step allows to upload your debug symbols to [**Firebase Crashlytics**](https://firebase.google.com/docs/crashlytics/get-deobfuscated-reports?hl=tr&platform=ios). 

### Prerequisites

The workflow steps that need to be executed before running the `Firebase Upload dSYM` workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/#xcodebuild-for-devices-archive--export) | This step will build your application, create an Archive file, and generate `.ipa`. The Archive file contains the `.dSYM` file. Please use **Firebase Upload dSYM** step after this step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsym_step_order.png' />

:::warning
If this step is not used after **Xcodebuild for Devices**, the pipeline will give error. Because the dSYM file is generated after the project is archived. 
:::

### Input Variables

You can find all the parameters required for this step in the table below with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsymInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FIREBASE_PLIST_PATH`         | The path of the **GoogleService-InfoPlist** file must be defined. In the project, wherever your GoogleService-InfoPlist file is, type that path directly without any characters at the beginning. Appcircle will automatically fill the beginning of the path with the repository path. For example, **`GoogleService-InfoPlist`** or **`services/GoogleService-InfoPlist`**.  | Required |
| `$AC_FIREBASE_CRASHLYTICS_PATH`               | This path parameter specifies the path of the generated dSYM file.  | Required |

:::info
Crashlytics paths change depending on the platform. According to the mobile application platform you are working on, you need to provide one of the following paths here.

|Project Type|Crashlytics Paths for Platforms|
|------------|----|
|Native iOS CocoaPods|$AC_REPOSITORY_DIR/Pods/FirebaseCrashlytics/upload-symbols|
|Native iOS SPM|$HOME/Library/Developer/Xcode/DerivedData/**/SourcePackages/checkouts/firebase-ios-sdk/Crashlytics/upload-symbols|
|React Native iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|
|Flutter iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component