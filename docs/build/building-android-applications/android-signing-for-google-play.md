---
title: Android 11+ Signing for Google Play
metaTitle: Android 11+ Signing for Google Play
metaDescription: Android 11+ Signing for Google Play
sidebar_position: 11
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NarrowImage from '@site/src/components/NarrowImage';
import ExternalUrlRef from '@site/src/components/ExternalUrlRef';

# Android 11+ Signing for Google Play

As per Google's update on Android 11 behavior changes, there is an important (breaking) change regarding app signing

<ExternalUrlRef url="https://developer.android.com/about/versions/11/behavior-changes-11#minimum-signature-scheme" title="Minimum Signature Scheme Changes on Android 11"/>

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

<NarrowImage src="https://cdn.appcircle.io/docs/assets/image%20(247).png" />

Alternatively, you can accomplish the same within environment variables. The environment variable for this action is `AC_V2_SIGN` . More information is found at the document below:

<ContentRef url="../environment-variables/why-to-use-environment-variables-and-secrets">
  Why to Use Environment Variables and Secrets?
</ContentRef>

### Enable V2 Sign Through the Android Project (build.gradle)

Alternatively, you can use `build.gradle` instead to specify the signing you will use.

The current Android Sign step in Appcircle utilizes [jarsigner to sign apps](https://developer.android.com/studio/build/building-cmdline#bundle_build_gradle) with the APK Signature Scheme v1 and the alternative _apksigner_ cannot be used to sign app bundles (AAB).

The solution for this is to utilize signing in gradle within the app. A sample build.gradle file that utilizes APK Signature Scheme v2 can be found at [https://github.com/appcircleio/appcircle-sample-android/blob/v2-sign/app/build.gradle](https://github.com/appcircleio/appcircle-sample-android/blob/v2-sign/app/build.gradle) and the sample code can be seen below:


<Tabs>
  <TabItem value="groovy" label="build.gradle" default>

```groovy
signingConfigs {
    release {
      if (System.getenv('AC_APPCIRCLE')) { // new configuration for Appcircle
          println 'Running on Appcircle'
          keyAlias "${System.getenv("AC_ANDROID_ALIAS")}"
          keyPassword "${System.getenv("AC_ANDROID_ALIAS_PASSWORD")}"
          storeFile file("${System.getenv("AC_ANDROID_KEYSTORE_PATH")}")
          storePassword "${System.getenv("AC_ANDROID_KEYSTORE_PASSWORD")}"
      } else {
          println 'Running on local' // Your old configuration
          keyAlias keystoreProperties['keyAlias']
          keyPassword keystoreProperties['keyPassword']
          storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
          storePassword keystoreProperties['storePassword']
      }
    }
}
// Rest of your build.gradle

```


  </TabItem>
  <TabItem value="kotlin" label="build.gradle.kts">

```kotlin
signingConfigs {
    create("release") {
        if (System.getenv()["AC_APPCIRCLE"].toBoolean()) { // new configuration for Appcircle
            println("Running on Appcircle")
            storeFile = file(System.getenv()["AC_ANDROID_KEYSTORE_PATH"])
            storePassword = System.getenv()["AC_ANDROID_KEYSTORE_PASSWORD"]
            keyAlias = System.getenv()["AC_ANDROID_ALIAS"]
            keyPassword = System.getenv()["AC_ANDROID_ALIAS_PASSWORD"]
        } else {
            println("Running on local") // Your old configuration
            storeFile = file(keystoreProperties.getProperty("storeFile"))
            storePassword = keystoreProperties.getProperty("storePassword")
            keyAlias = keystoreProperties.getProperty("keyAlias")
            keyPassword = keystoreProperties.getProperty("keyPassword")
        }
    }
}
// Rest of your build.gradle.kts

```

  </TabItem>
</Tabs>

:::warning

You need to either sign with Appcircle Android Sign Step or via Gradle. If you're using Appcircle's Android sign step, remove `signingConfig signingConfigs.release` block from your `build.gradle`.

:::


:::info

If you're using **Gradle** to sign your APK file, you may need to add `v1SigningEnabled` and `v2SigningEnabled` to your signing configurations to install your APK file to both old and new Android versions.


<Tabs>
  <TabItem value="groovy" label="build.gradle" default>

```groovy
signingConfigs {
    release {
      if (System.getenv('AC_APPCIRCLE')) { // new configuration for Appcircle
          println 'Running on Appcircle'
          keyAlias "${System.getenv("AC_ANDROID_ALIAS")}"
          keyPassword "${System.getenv("AC_ANDROID_ALIAS_PASSWORD")}"
          storeFile file("${System.getenv("AC_ANDROID_KEYSTORE_PATH")}")
          storePassword "${System.getenv("AC_ANDROID_KEYSTORE_PASSWORD")}"
          v2SigningEnabled true
          v1SigningEnabled true

      } else {
          println 'Running on local' // Your old configuration
          keyAlias keystoreProperties['keyAlias']
          keyPassword keystoreProperties['keyPassword']
          storeFile keystoreProperties['storeFile'] ? file(keystoreProperties['storeFile']) : null
          storePassword keystoreProperties['storePassword']
      }
    }
}
// Rest of your build.gradle

```


  </TabItem>
  <TabItem value="kotlin" label="build.gradle.kts">

```kotlin
signingConfigs {
    create("release") {
        if (System.getenv()["AC_APPCIRCLE"].toBoolean()) { // new configuration for Appcircle
            println("Running on Appcircle")
            storeFile = file(System.getenv()["AC_ANDROID_KEYSTORE_PATH"])
            storePassword = System.getenv()["AC_ANDROID_KEYSTORE_PASSWORD"]
            keyAlias = System.getenv()["AC_ANDROID_ALIAS"]
            keyPassword = System.getenv()["AC_ANDROID_ALIAS_PASSWORD"]
            isV1SigningEnabled = true
            isV2SigningEnabled = true

        } else {
            println("Running on local") // Your old configuration
            storeFile = file(keystoreProperties.getProperty("storeFile"))
            storePassword = keystoreProperties.getProperty("storePassword")
            keyAlias = keystoreProperties.getProperty("keyAlias")
            keyPassword = keystoreProperties.getProperty("keyPassword")
        }
    }
}
// Rest of your build.gradle.kts
```

  </TabItem>
</Tabs>


:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
