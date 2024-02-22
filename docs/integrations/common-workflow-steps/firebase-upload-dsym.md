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

This step should follow **Xcodebuild for Devices** step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsym_step_order.png' />

:::warning
If this step is not used after **Xcodebuild for devices**, the pipeline will error. Because the dSYM file is generated after the project is archived. 
:::

#### GoogleService-InfoPlist Path

In this path parameter the direction of the **GoogleService-InfoPlist** file must be defined. In the project, wherever your GoogleService-InfoPlist file is, type that path directly without any characters at the beginning. Appcircle will automatically fill the beginning of the path with the repository direction. For example, **`GoogleService-InfoPlist`** or **`services/GoogleService-InfoPlist`**. Appcircle will complete 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsym_google_path.png' />

#### Crashlitics Path

This path parameter specifies the path of the generated dSYM file. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2581-dsym_path.png' />

:::caution
For this, paths change depending on the platform. According to the mobile application platform you are working on, you need to give one of the following paths here.
:::

|Project Type|Crashlytics Paths for Platforms|
|------------|----|
|Native iOS CocoaPods|$AC_REPOSITORY_DIR/Pods/FirebaseCrashlytics/upload-symbols|
|Native iOS SPM|$HOME/Library/Developer/Xcode/DerivedData/**/SourcePackages/checkouts/firebase-ios-sdk/Crashlytics/upload-symbols|
|React Native iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|
|Flutter iOS|$AC_REPOSITORY_DIR/ios/Pods/FirebaseCrashlytics/upload-symbols|

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component