---
title: Android Specific Integrations
description: Android specific workflow steps in Appcircle
slug: /build-integrations/android-specific-integrations
tags: [android, mobile]
---

# Android Specific Integrations

The steps listed below are specific to the Android build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [Android Build for UI Testing](/build-integrations/android-specific-integrations/android-build-for-ui-testing)

Builds your test applications with gradlew. Runs `./gradlew clean ${module}:assembleAndroidTest`.

## [Android Build](/build-integrations/android-specific-integrations/android-build)

This step builds your Android application for the architectures specified in your project.

:::tip

If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to [https://scans.gradle.com/](https://scans.gradle.com)

:::

## [Android Dependency Report](/build-integrations/android-specific-integrations/android-dependency-report)

This step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) available in the project.

## [Android Sign](/build-integrations/android-specific-integrations/android-sign)

This step signs your APK or App Bundle with the given Android keystore and exports a binary file compatible with Android devices.

## [Android Unit Tests](/build-integrations/android-specific-integrations/android-unit-tests)

This step runs the unit tests of the project.

## [App Center Android Distribution](/build-integrations/android-specific-integrations/app-center-android-distribution)

Distribute APK, AAB, and mapping files to [App Center](https://appcenter.ms/). You need to enter your token, owner, app, and group names to distribute your binaries.

## [Android App Post-Processor](/build-integrations/android-specific-integrations/app-post-processor)

This step performs necessary system operations to identify and process the Android output binary files.

## [Appdome Build-2Secure for Android](/build-integrations/android-specific-integrations/appdome-build-to-secure-for-android)

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:
[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

## [AppSweep Mobile Security Testing](/build-integrations/android-specific-integrations/appsweep-mobile-security-testing)

Scan your Android app using [AppSweep](https://appsweep.guardsquare.com)

## [Azure DevOps Bot for Detekt Report](/build-integrations/android-specific-integrations/azure-bot-for-detekt-report)

This step sends the Detekt report to Azure DevOps.

## [BrowserStack App Automate - Espresso](/build-integrations/android-specific-integrations/browserstack-app-automate-espresso)

Run your Espresso tests on BrowserStack App Automate. You need to add **Android Build for UI Testing** before this step to create the required `$AC_APK_PATH` and `$AC_TEST_APK_PATH` files.

## [Bundle Universal Apk](/build-integrations/android-specific-integrations/bundle-universal-apk)

This step generates a universal APK from an AAB.

## [Detekt](/build-integrations/android-specific-integrations/detekt)

This step runs detekt gradle task.

## [Firebase Test Lab for Android](/build-integrations/android-specific-integrations/firebase-test-lab)

This step runs your Android tests on Firebase Test Lab.

## [Gradle Runner](/build-integrations/android-specific-integrations/gradle-runner)

This step runs given Gradle task.

## [LambdaTest App Automate - Espresso](/build-integrations/android-specific-integrations/lambdatest-app-automate-espresso)

[LambdaTest App Automate - Espresso](https://www.lambdatest.com/support/docs/getting-started-with-espresso-testing/) is a cloud-based testing solution designed for Android applications using the [Espresso](https://developer.android.com/training/testing/espresso) testing framework. It enables developers to run automated tests for Android apps across a wide range of real devices hosted in the LambdaTest cloud infrastructure. This solution allows efficient, scalable, and reliable testing of Android applications to ensure app quality and compatibility.

## [Android Increment Build and Version Number](/build-integrations/android-specific-integrations/increment-build-and-version-number)

This step increments the version code and version name in the Android project.

## [Android Lint](/build-integrations/android-specific-integrations/lint)

This step runs lint Gradle tasks on the source files of the project.

## [Test Reports for Android](/build-integrations/android-specific-integrations/test-reports-for-android)

This component provides detailed reports and insights on the results of Android app tests conducted.
For detailed information on the usage of **Test Reports for Android**, please refer to the documentation:

- [Generating Test Report](/continuous-testing/android-testing/running-android-unit-tests#generating-test-report)

## [Wait for Android Emulator](/build-integrations/android-specific-integrations/wait-for-android-emulator)

This step waits for Android Emulator to boot. You must use this step before running any UI tests.