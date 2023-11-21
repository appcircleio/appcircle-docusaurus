---
title: Android Specific Workflow Steps
metaTitle: Android Specific Workflow Steps
metaDescription: Android Specific Workflow Steps
sidebar_position: 4
---

import ExternalUrlRef from '@site/src/components/ExternalUrlRef';

# Android Specific Workflow Steps

The steps listed below are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Android Build

This step builds your Android application for the architectures specified in your project.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-build-component" title="Appcircle Android Build Component"/>

:::info


**Tip: **If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to [https://scans.gradle.com/](https://scans.gradle.com)

:::

## Gradle Runner

This step runs given Gradle task.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-gradle-task-component" title="Appcircle Android Gradle Task Component"/>

## Android Sign

This step signs your APK or App Bundle with the given Android keystore and exports a binary file compatible with Android devices.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-sign-component" title="Appcircle Android Sign Component"/>


## Android App Post-Processor

This step performs necessary system operations to identify and process the Android output binary files.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-post-process-component" title="Appcircle Android Post Process Component"/>

## Android Lint

This step runs lint Gradle tasks on the source files of the project.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-lint-component" title="Appcircle Android Lint Component"/>

## Android Build for UI Testing

Builds your test applications with gradlew. Runs `./gradlew clean ${module}:assembleAndroidTest`.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-build-ui-test-component" title="Appcircle Android UI Test Component"/>

## Android Unit Tests

This step runs the unit tests of the project.;

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-unit-test-component" title="Appcircle Android Unity Test Component"/>

## Android Dependency Report

This step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring\_dependencies.html#sec:what-are-dependency-configurations) available in the project.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-dependency-report" title="Appcircle Dependency Report Component"/>

## Wait for Android Emulator

This step waits for Android Emulator to boot. You must use this step before running any UI tests.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-wait-emulator" title="Appcircle Android Wait Emulator Component"/>

## Bundle Universal Apk

This step generates an universal APK from an AAB.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-bundletool-component" title="Appcircle Android BundleTool Component"/>

## Detekt

This step runs detekt gradle task.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-detekt-component" title="Appcircle Android Detekt Component"/>

## BrowserStack App Automate - Espresso

Run your Espresso tests on BrowserStack App Automate. You need to add **Android Build for UI Testing** before this step to create the required `$AC_APK_PATH` and `$AC_TEST_APK_PATH` files.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-browserstack-espresso-component" title="Appcircle Browserstack Espresso Component"/>

## AppSweep Mobile Security Testing

Scan your Android app using [AppSweep](https://appsweep.guardsquare.com)

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-appsweep-component" title="Appcircle Appsweep Component"/>

## App Center Android Distribution

Distribute APK,AAB and mapping files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-android-appcenter-distribute-component" title="Appcirlce AppCenter Distribute Component"/>