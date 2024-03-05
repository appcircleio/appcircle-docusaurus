---
title: Firebase Upload dSYM 
metaTitle: Firebase Upload dSYM
metaDescription: Firebase Upload dSYM
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Firebase Upload dSYM

This step allows to to upload your debug symbols to Firebase Crashlytics. 

### Prerequisites

This step depends on the **Xcodebuild for Devices** step to upload the .dSYM file.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/#xcodebuild-for-devices-archive--export) | This step will build your application, create an Archive file, and generate .ipa. The Archive file contains the .dSYM file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsym_step_order.png' />

:::warning
If this step is not used after **Xcodebuild for devices**, the pipeline will error. Because the dSYM file is generated after the project is archived. 
:::

### Input Variables

You can find all the parameters required for this step in the table below with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsymInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FIREBASE_PLIST_PATH`*         | In this path parameter, the direction of the **GoogleService-InfoPlist** file must be defined. In the project, wherever your GoogleService-InfoPlist file is, type that path directly without any characters at the beginning. Appcircle will automatically fill the beginning of the path with the repository direction. For example, **`GoogleService-InfoPlist`** or **`services/GoogleService-InfoPlist`**. Appcircle will complete  | Required |
| `$AC_FIREBASE_CRASHLYTICS_PATH`               | This path parameter specifies the path of the generated dSYM file.  | Required |

:::caution
For this, paths change depending on the platform. According to the mobile application platform you are working on, you need to provide one of the following paths here.
:::

|Project Type|Crashlytics Paths for Platforms|
|------------|----|
|Native iOS CocoaPods|$AC_REPOSITORY_DIR/Pods/FirebaseCrashlytics/upload-symbols|
|Native iOS SPM|$HOME/Library/Developer/Xcode/DerivedData/**/SourcePackages/checkouts/firebase-ios-sdk/Crashlytics/upload-symbols|
|React Native iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|
|Flutter iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component