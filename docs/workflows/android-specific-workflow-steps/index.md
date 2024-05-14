---
title: Android Specific Workflow Steps
description: Android specific workflow steps in Appcircle
tags: [android, mobile]
---

# Android Specific Workflow Steps

The steps listed below are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Android App Post-Processor

This step performs necessary system operations to identify and process the Android output binary files.

<ContentRef url="/workflows/android-specific-workflow-steps/post-processor">
    Android App Post-Processor
</ContentRef>

## Android Increment Build and Version Number

This step increments the version code and version name in the Android project.

<ContentRef url="/workflows/android-specific-workflow-steps/increment-build-and-version-number">
    Android Increment Build and Version Number
</ContentRef>

## Android Build

This step builds your Android application for the architectures specified in your project.

<ContentRef url="/workflows/android-specific-workflow-steps/android-build">
    Android Build
</ContentRef>

:::tip

If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to [https://scans.gradle.com/](https://scans.gradle.com)

:::

## Android Build for UI Testing

Builds your test applications with gradlew. Runs `./gradlew clean ${module}:assembleAndroidTest`.

<ContentRef url="/workflows/android-specific-workflow-steps/android-build-for-ui-testing">
    Android Build for UI Testing
</ContentRef>

## Android Dependency Report

This step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) available in the project.

<ContentRef url="/workflows/android-specific-workflow-steps/android-dependency-report">
    Android Dependency Report
</ContentRef>

## Android Lint

This step runs lint Gradle tasks on the source files of the project.

<ContentRef url="/workflows/android-specific-workflow-steps/lint">
    Android Lint
</ContentRef>

## Android Sign

This step signs your APK or App Bundle with the given Android keystore and exports a binary file compatible with Android devices.

<ContentRef url="/workflows/android-specific-workflow-steps/android-sign">
    Android Sign
</ContentRef>

## Android Unit Tests

This step runs the unit tests of the project.

<ContentRef url="/workflows/android-specific-workflow-steps/android-unit-tests">
    Android Unit Tests
</ContentRef>

## App Center Android Distribution

Distribute APK, AAB, and mapping files to [App Center](https://appcenter.ms/). You need to enter your token, owner, app, and group names to distribute your binaries.

<ContentRef url="/workflows/android-specific-workflow-steps/app-center-android-distribution">
    App Center Android Distribution
</ContentRef>

## Appdome Build-2Secure for Android

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:
[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

<ContentRef url="/workflows/android-specific-workflow-steps/appdome-build-to-secure-for-android">
    Appdome Build-2Secure for Android
</ContentRef>

## AppSweep Mobile Security Testing

Scan your Android app using [AppSweep](https://appsweep.guardsquare.com)

<ContentRef url="/workflows/android-specific-workflow-steps/appsweep-mobile-security-testing">
    AppSweep Mobile Security Testing
</ContentRef>

## Azure DevOps Bot for Detekt Report

This step sends the Detekt report to Azure DevOps.

<ContentRef url="/workflows/android-specific-workflow-steps/azure-bot-for-detekt-report">
    Azure DevOps Bot for Detekt Report
</ContentRef>

## BrowserStack App Automate - Espresso

Run your Espresso tests on BrowserStack App Automate. You need to add **Android Build for UI Testing** before this step to create the required `$AC_APK_PATH` and `$AC_TEST_APK_PATH` files.

<ContentRef url="/workflows/android-specific-workflow-steps/browserstack-app-automate-espresso">
    BrowserStack App Automate - Espresso
</ContentRef>

## Bundle Universal Apk

This step generates a universal APK from an AAB.

<ContentRef url="/workflows/android-specific-workflow-steps/bundle-universal-apk">
    Bundle Universal Apk
</ContentRef>

## Detekt

This step runs detekt gradle task.

<ContentRef url="/workflows/android-specific-workflow-steps/detekt">
    Detekt
</ContentRef>

## Firebase Test Lab for Android

This step runs your Android tests on Firebase Test Lab.

<ContentRef url="/workflows/android-specific-workflow-steps/firebase-test-lab">
    Firebase Test Lab for Android
</ContentRef>

## Gradle Runner

This step runs given Gradle task.

<ContentRef url="/workflows/android-specific-workflow-steps/gradle-runner">
    Gradle Runner
</ContentRef>

## Test Reports for Android

This component provides detailed reports and insights on the results of Android app tests conducted.
For detailed information on the usage of **Test Reports for Android**, please refer to the documentation:
[https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report](https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report)

<ContentRef url="/workflows/android-specific-workflow-steps/test-reports-for-android">
    Test Reports for Android
</ContentRef>

## Wait for Android Emulator

This step waits for Android Emulator to boot. You must use this step before running any UI tests.

<ContentRef url="/workflows/android-specific-workflow-steps/wait-for-android-emulator">
    Wait for Android Emulator
</ContentRef>
