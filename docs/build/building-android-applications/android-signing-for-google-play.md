---
title: Android 11+ Signing for Google Play
metaTitle: Android 11+ Signing for Google Play
metaDescription: Android 11+ Signing for Google Play
sidebar_position: 11
---

# Android 11+ Signing for Google Play

As per Google's update on Android 11 behavior changes, there is an important (breaking) change regarding app signing

https://developer.android.com/about/versions/11/behavior-changes-11#minimum-signature-scheme

> Apps that target Android 11 (API level 30) that are currently only signed using APK Signature Scheme v1 must now also be signed using [APK Signature Scheme v2](https://source.android.com/security/apksigning/v2) or higher. Users can't install or update apps that are only signed with APK Signature Scheme v1 on devices that run Android 11.

In order to adapt your Application, you need to enable V2 Signing through either:

- Appcircle (Recommended)
- In your Project

### Enable V2 Sign in Appcircle

In order to keep your config in Appcircle, you need to Navigate through:

1. Your workflows
2. Select a workflow
3. Edit the **Android Sign** workflow
4. Set V2 Sign to either **true **or **false.**

![](<https://cdn.appcircle.io/docs/assets/image (247).png>)

Alternatively, you can accomplish the same within environment variables. The environment variable for this action is `AC_V2_SIGN` . More information is found at the document below:

<ContentRef url="../environment-variables/why-to-use-environment-variables-and-secrets">
  Why to Use Environment Variables and Secrets?
</ContentRef>

### Enable V2 Sign Through the Android Project (build.gradle)

Alternatively, you can use `build.gradle` instead to specify the signing you will use.

The current Android Sign step in Appcircle utilizes [jarsigner to sign apps](https://developer.android.com/studio/build/building-cmdline#bundle_build_gradle) with the APK Signature Scheme v1 and the alternative \_apksigner \_cannot be used to sign app bundles (AAB).

The solution for this is to utilize signing in gradle within the app. A sample build.gradle file that utilizes APK Signature Scheme v2 can be found at [https://github.com/appcircleio/appcircle-sample-android/blob/v2-sign/app/build.gradle](https://github.com/appcircleio/appcircle-sample-android/blob/v2-sign/app/build.gradle) and the sample code can be seen below:

```groovy
signingConfigs {
    release {
        storeFile file("${System.getenv("AC_ANDROID_KEYSTORE_PATH")}")
        storePassword "${System.getenv("AC_ANDROID_KEYSTORE_PASSWORD")}"
        keyAlias "${System.getenv("AC_ANDROID_ALIAS")}"
        keyPassword "${System.getenv("AC_ANDROID_ALIAS_PASSWORD")}"
        v2SigningEnabled true
        v1SigningEnabled true
    }
}

buildTypes {
    release {
        minifyEnabled false
        proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        signingConfig signingConfigs.release
    }
}
```
