---
title: iOS Specific Workflow Steps
description: Dive into iOS-specific workflow steps for building profiles. Access our workflow marketplace for a comprehensive list.
tags: [ios, mobile, workflow, step]
---

# iOS Specific Workflow Steps

The steps listed below are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [App Center iOS Distribution](/workflows/ios-specific-workflow-steps/appcenter-ios-distribution)

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

## [Audit Permission Changes](/workflows/ios-specific-workflow-steps/audit-permission-change)

This component captures and compares permission changes in your iOS projects.

## [Appdome Build-2Secure for iOS](/workflows/ios-specific-workflow-steps/appdome-build-to-secure-for-ios)

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

## [BrowserStack App Automate - XCUI](/workflows/ios-specific-workflow-steps/browserstack-app-automation)

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files.

## [Carthage](/workflows/ios-specific-workflow-steps/carthage)

Runs the Carthage bootstrap/update command for dependency management.

## [Cocoapods Install](/workflows/ios-specific-workflow-steps/cocoapods-install)

Runs the Cocoapods install command for dependency management.

## [Install Certificates and Profiles](/workflows/ios-specific-workflow-steps/install-certificates-provisions)

This step installs the selected certificates and the provisioning profile for the build.

## [iOS Increment Build and Version](/workflows/ios-specific-workflow-steps/ios-increment-build-and-version-number)

This step increments the build number and version number of the iOS project.

## [CocoaPods Deintegrate](/workflows/ios-specific-workflow-steps/cocoapods-deintegrate)

This step runs the `pod deintegrate` command to remove CocoaPods from the project.

## [Convert Xcresult to HTML/XML](/workflows/ios-specific-workflow-steps/convert-xcresult-to-xml-html)

This step converts Xcresult files to HTML or XML format.

## [Slather](/workflows/ios-specific-workflow-steps/slather)

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

## [Azure Bot for SwiftLint](/workflows/ios-specific-workflow-steps/azure-bot-for-swiftlint)

This step integrates Azure Bot with SwiftLint to provide feedback on code quality.

## [SwiftLint](/workflows/ios-specific-workflow-steps/swiftlint)

This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options.

## [Test Reports for iOS](/workflows/ios-specific-workflow-steps/test-reports-for-ios)

This component provides detailed reports and insights on the results of iOS app tests conducted.

For detailed information on the usage of **Test Reports for iOS**, please refer to the documentation:

[https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests#generating-test-report](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests#generating-test-report)

## [Tuist Install](/workflows/ios-specific-workflow-steps/tuist-install)

This step installs [Tuist](https://tuist.io/) and runs `tuist generate` with given options.

## [Tuist Commands](/workflows/ios-specific-workflow-steps/tuist-commands)

This step runs specific [Tuist Commands](https://docs.tuist.io/en/cli/auth) such as `tuist build` or `tuist test`.

## [Xcode Select (Version)](/workflows/ios-specific-workflow-steps/xcode-select)

This step is used to specify the Xcode version to be used during the build process.

:::info

### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools/#pool-based-xcode-version-selection).
:::

## [Firebase Upload dSYM](/workflows/ios-specific-workflow-steps/firebase-upload-dsym)

Upload your debug symbols to Firebase Crashlytics

## [Xcodebuild for Devices (Archive & Export)](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Share With Testers**](/testing-distribution/create-or-select-a-distribution-profile) feature or any other means of iOS distribution.

## [Xcodebuild for iOS Simulator](/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator)

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

## [Xcodebuild for Testing](/workflows/ios-specific-workflow-steps/xcodebuild-for-testing)

This step builds your application for testing.

## [Xcodebuild for Unit and UI Tests](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test)

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.