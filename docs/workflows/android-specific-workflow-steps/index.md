---
title: Android Specific Workflow Steps
description: Android specific workflow steps in Appcircle
tags: [android, mobile]
---

# Android Specific Workflow Steps

The steps listed below are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [Android App Post-Processor](/workflows/android-specific-workflow-steps/app-post-processor)

This step performs necessary system operations to identify and process the Android output binary files.

## [Android Increment Build and Version Number](/workflows/android-specific-workflow-steps/increment-build-and-version-number)

This step increments the version code and version name in the Android project.

## [Android Build](/workflows/android-specific-workflow-steps/android-build)

This step builds your Android application for the architectures specified in your project.

:::tip

If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to [https://scans.gradle.com/](https://scans.gradle.com)

:::

## [Android Build for UI Testing](/workflows/android-specific-workflow-steps/android-build-for-ui-testing)

Builds your test applications with gradlew. Runs `./gradlew clean ${module}:assembleAndroidTest`.

## [Android Dependency Report](/workflows/android-specific-workflow-steps/android-dependency-report)

This step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) available in the project.

## [Android Lint](/workflows/android-specific-workflow-steps/lint)

This step runs lint Gradle tasks on the source files of the project.

## [Android Sign](/workflows/android-specific-workflow-steps/android-sign)

This step signs your APK or App Bundle with the given Android keystore and exports a binary file compatible with Android devices.

## [Android Unit Tests](/workflows/android-specific-workflow-steps/android-unit-tests)

This step runs the unit tests of the project.

## [App Center Android Distribution](/workflows/android-specific-workflow-steps/app-center-android-distribution)

Distribute APK, AAB, and mapping files to [App Center](https://appcenter.ms/). You need to enter your token, owner, app, and group names to distribute your binaries.

## [Appdome Build-2Secure for Android](/workflows/android-specific-workflow-steps/appdome-build-to-secure-for-android)

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:
[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

## [AppSweep Mobile Security Testing](/workflows/android-specific-workflow-steps/appsweep-mobile-security-testing)

Scan your Android app using [AppSweep](https://appsweep.guardsquare.com)

## [Azure DevOps Bot for Detekt Report](/workflows/android-specific-workflow-steps/azure-bot-for-detekt-report)

This step sends the Detekt report to Azure DevOps.

## [BrowserStack App Automate - Espresso](/workflows/android-specific-workflow-steps/browserstack-app-automate-espresso)

Run your Espresso tests on BrowserStack App Automate. You need to add **Android Build for UI Testing** before this step to create the required `$AC_APK_PATH` and `$AC_TEST_APK_PATH` files.

## [Bundle Universal Apk](/workflows/android-specific-workflow-steps/bundle-universal-apk)

This step generates a universal APK from an AAB.

## [Detekt](/workflows/android-specific-workflow-steps/detekt)

This step runs detekt gradle task.

## [Firebase Test Lab for Android](/workflows/android-specific-workflow-steps/firebase-test-lab)

This step runs your Android tests on Firebase Test Lab.

## [Gradle Runner](/workflows/android-specific-workflow-steps/gradle-runner)

This step runs given Gradle task.

## [Test Reports for Android](/workflows/android-specific-workflow-steps/test-reports-for-android)

This component provides detailed reports and insights on the results of Android app tests conducted.
For detailed information on the usage of **Test Reports for Android**, please refer to the documentation:

- [Generating Test Report](/continuous-testing/android-testing/running-android-unit-tests#generating-test-report)

## [Wait for Android Emulator](/workflows/android-specific-workflow-steps/wait-for-android-emulator)

This step waits for Android Emulator to boot. You must use this step before running any UI tests.