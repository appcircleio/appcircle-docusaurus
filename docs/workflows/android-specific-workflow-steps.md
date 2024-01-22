---
title: Android Specific Workflow Steps
metaTitle: Android Specific Workflow Steps
metaDescription: Android Specific Workflow Steps
sidebar_position: 4
---
# Android Specific Workflow Steps

The steps listed below are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Android Build

This step builds your Android application for the architectures specified in your project.

[https://github.com/appcircleio/appcircle-android-build-component](https://github.com/appcircleio/appcircle-android-build-component)

:::info


**Tip: **If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to [https://scans.gradle.com/](https://scans.gradle.com)

:::

## Gradle Runner

This step runs given Gradle task.

[https://github.com/appcircleio/appcircle-android-gradle-task-component](https://github.com/appcircleio/appcircle-android-gradle-task-component)

## Android Sign

This step signs your APK or App Bundle with the given Android keystore and exports a binary file compatible with Android devices.

[https://github.com/appcircleio/appcircle-android-sign-component](https://github.com/appcircleio/appcircle-android-sign-component)


## Android App Post-Processor

This step performs necessary system operations to identify and process the Android output binary files.

[https://github.com/appcircleio/appcircle-android-post-process-component](https://github.com/appcircleio/appcircle-android-post-process-component)

## Android Lint

This step runs lint Gradle tasks on the source files of the project.

[https://github.com/appcircleio/appcircle-android-lint-component](https://github.com/appcircleio/appcircle-android-lint-component)

## Android Build for UI Testing

Builds your test applications with gradlew. Runs `./gradlew clean ${module}:assembleAndroidTest`.

[https://github.com/appcircleio/appcircle-android-build-ui-test-component](https://github.com/appcircleio/appcircle-android-build-ui-test-component)

## Android Unit Tests

This step runs the unit tests of the project.;

[https://github.com/appcircleio/appcircle-android-unit-test-component](https://github.com/appcircleio/appcircle-android-unit-test-component)

## Android Dependency Report

This step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring\_dependencies.html#sec:what-are-dependency-configurations) available in the project.

[https://github.com/appcircleio/appcircle-dependency-report](https://github.com/appcircleio/appcircle-dependency-report)

## Wait for Android Emulator

This step waits for Android Emulator to boot. You must use this step before running any UI tests.

[https://github.com/appcircleio/appcircle-android-wait-emulator](https://github.com/appcircleio/appcircle-android-wait-emulator)

## Bundle Universal Apk

This step generates an universal APK from an AAB.

[https://github.com/appcircleio/appcircle-bundletool-component](https://github.com/appcircleio/appcircle-bundletool-component)

## Detekt

This step runs detekt gradle task.

[https://github.com/appcircleio/appcircle-detekt-component](https://github.com/appcircleio/appcircle-detekt-component)

## BrowserStack App Automate - Espresso

Run your Espresso tests on BrowserStack App Automate. You need to add **Android Build for UI Testing** before this step to create the required `$AC_APK_PATH` and `$AC_TEST_APK_PATH` files.

[https://github.com/appcircleio/appcircle-browserstack-espresso-component](https://github.com/appcircleio/appcircle-browserstack-espresso-component)

## AppSweep Mobile Security Testing

Scan your Android app using [AppSweep](https://appsweep.guardsquare.com)

[https://github.com/appcircleio/appcircle-appsweep-component](https://github.com/appcircleio/appcircle-appsweep-component)

## App Center Android Distribution

Distribute APK,AAB and mapping files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

[https://github.com/appcircleio/appcircle-android-appcenter-distribute-component](https://github.com/appcircleio/appcircle-android-appcenter-distribute-component)

## Appdome Build-2Secure for Android

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

[https://github.com/appcircleio/appcircle-android-appdome-component](https://github.com/appcircleio/appcircle-android-appdome-component)

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)
