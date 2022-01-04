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
