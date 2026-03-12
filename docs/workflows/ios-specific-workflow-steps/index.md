---
title: iOS Specific Workflow Steps
description: Dive into iOS-specific workflow steps for building profiles. Access our workflow marketplace for a comprehensive list.
slug: /build-integrations/ios-specific-integrations
tags: [ios, mobile, workflow, step]
---

# iOS Specific Integrations

The steps listed below are specific to the iOS build profiles.

You can find the full list of available integrations in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [App Center iOS Distribution](/build-integrations/ios-specific-integrations/appcenter-ios-distribution)

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

## [Appdome Build-2Secure for iOS](/build-integrations/ios-specific-integrations/appdome-build-to-secure-for-ios)

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

## [Audit Permission Changes](/build-integrations/ios-specific-integrations/audit-permission-change)

This component captures and compares permission changes in your iOS projects.

## [Azure Bot for SwiftLint](/build-integrations/ios-specific-integrations/azure-bot-for-swiftlint)

This step integrates Azure Bot with SwiftLint to provide feedback on code quality.

## [BrowserStack App Automate - XCUI](/build-integrations/ios-specific-integrations/browserstack-app-automation)

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files.

## [Carthage](/build-integrations/ios-specific-integrations/carthage)

Runs the Carthage bootstrap/update command for dependency management.

## [CocoaPods Deintegrate](/build-integrations/ios-specific-integrations/cocoapods-deintegrate)

This step runs the `pod deintegrate` command to remove CocoaPods from the project.

## [Cocoapods Install](/build-integrations/ios-specific-integrations/cocoapods-install)

Runs the Cocoapods install command for dependency management.

## [Convert Xcresult to HTML/XML](/build-integrations/ios-specific-integrations/convert-xcresult-to-xml-html)

This step converts Xcresult files to HTML or XML format.

## [Firebase Upload dSYM](/build-integrations/ios-specific-integrations/firebase-upload-dsym)

Upload your debug symbols to Firebase Crashlytics

## [Install Certificates and Profiles](/build-integrations/ios-specific-integrations/install-certificates-provisions)

This step installs the selected certificates and the provisioning profile for the build.

## [iOS Increment Build and Version](/build-integrations/ios-specific-integrations/ios-increment-build-and-version-number)

This step increments the build number and version number of the iOS project.

## [Slather](/build-integrations/ios-specific-integrations/slather)

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

## [SwiftLint](/build-integrations/ios-specific-integrations/swiftlint)

This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options.

## [Test Reports for iOS](/build-integrations/ios-specific-integrations/test-reports-for-ios)

This component provides detailed reports and insights on the results of iOS app tests conducted.

For detailed information on the usage of **Test Reports for iOS**, please refer to the documentation:
- [Generating Test Report](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests#generating-test-report)

## [Tuist Commands](/build-integrations/ios-specific-integrations/tuist-commands)

This step runs specific [Tuist Commands](https://docs.tuist.io/en/cli/auth) such as `tuist build` or `tuist test`.

## [Tuist Install](/build-integrations/ios-specific-integrations/tuist-install)

This step installs [Tuist](https://tuist.io/) and runs `tuist generate` with given options.

## [Xcode Select (Version)](/build-integrations/ios-specific-integrations/xcode-select)

This step is used to specify the Xcode version to be used during the build process.

:::info

### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools/#pool-based-xcode-version-selection).
:::

## [Xcodebuild for Devices (Archive & Export)](/build-integrations/ios-specific-integrations/xcodebuild-for-devices)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Share With Testers**](/testing-distribution/create-or-select-a-distribution-profile) feature or any other means of iOS distribution.

## [Xcodebuild for iOS Simulator](/build-integrations/ios-specific-integrations/xcodebuild-for-ios-simulator)

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

## [Xcodebuild for Testing](/build-integrations/ios-specific-integrations/xcodebuild-for-testing)

This step builds your application for testing.

## [Xcodebuild for Unit and UI Tests](/build-integrations/ios-specific-integrations/xcodebuild-for-unit-and-ui-test)

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.