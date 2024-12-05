---
title: iOS Specific Workflow Steps
description: Dive into iOS-specific workflow steps for building profiles. Access our workflow marketplace for a comprehensive list.
tags: [ios, mobile, workflow, step]
---

# iOS Specific Workflow Steps

The steps listed below are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## App Center iOS Distribution

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

<ContentRef url="/workflows/ios-specific-workflow-steps/appcenter-ios-distribution">
    App Center iOS Distribution
</ContentRef>

## Audit Permission Changes

This component captures and compares permission changes in your iOS projects.

<ContentRef url="/workflows/ios-specific-workflow-steps/audit-permission-change">
    Audit Permission Changes
</ContentRef>

## Appdome Build-2Secure for iOS

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

<ContentRef url="/workflows/ios-specific-workflow-steps/appdome-build-to-secure-for-ios">
    Appdome Build-2Secure for iOS
</ContentRef>

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)

## BrowserStack App Automate - XCUI

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files.

<ContentRef url="/workflows/ios-specific-workflow-steps/browserstack-app-automation">
    BrowserStack App Automate - XCUI
</ContentRef>

## Carthage

Runs the Carthage bootstrap/update command for dependency management.

<ContentRef url="/workflows/ios-specific-workflow-steps/carthage">
    Carthage
</ContentRef>

## Cocoapods Install

Runs the Cocoapods install command for dependency management.

<ContentRef url="/workflows/ios-specific-workflow-steps/cocoapods-install">
    Cocoapods Install
</ContentRef>

## Install Certificates and Profiles

This step installs the selected certificates and the provisioning profile for the build.

<ContentRef url="/workflows/ios-specific-workflow-steps/install-certificates-provisions">
    Install Certificates and Profiles
</ContentRef>

## iOS Increment Build and Version

This step increments the build number and version number of the iOS project.

<ContentRef url="/workflows/ios-specific-workflow-steps/ios-increment-build-and-version-number">
    iOS Increment Build and Version
</ContentRef>

## CocoaPods Deintegrate

This step runs the `pod deintegrate` command to remove CocoaPods from the project.

<ContentRef url="/workflows/ios-specific-workflow-steps/cocoapods-deintegrate">
    CocoaPods Deintegrate
</ContentRef>

## Convert Xcresult to HTML/XML

This step converts Xcresult files to HTML or XML format.

<ContentRef url="/workflows/ios-specific-workflow-steps/convert-xcresult-to-xml-html">
    Convert Xcresult to HTML/XML
</ContentRef>

## Slather

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

<ContentRef url="/workflows/ios-specific-workflow-steps/slather">
    Slather
</ContentRef>

## Azure Bot for SwiftLint

This step integrates Azure Bot with SwiftLint to provide feedback on code quality.

<ContentRef url="/workflows/ios-specific-workflow-steps/azure-bot-for-swiftlint">
    Azure Bot for SwiftLint
</ContentRef>

## SwiftLint

This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options.

<ContentRef url="/workflows/ios-specific-workflow-steps/swiftlint">
    SwiftLint
</ContentRef>

## Test Reports for iOS

This component provides detailed reports and insights on the results of iOS app tests conducted.

For detailed information on the usage of **Test Reports for iOS**, please refer to the documentation:
- [Generating Test Report](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests#generating-test-report)

<ContentRef url="/workflows/ios-specific-workflow-steps/test-reports-for-ios">
    Test Reports for iOS
</ContentRef>

## Tuist Install

This step installs [Tuist](https://tuist.io/) and runs `tuist generate` with given options.

<ContentRef url="/workflows/ios-specific-workflow-steps/tuist-install">
    Tuist Install
</ContentRef>

## Tuist Commands

This step runs specific [Tuist Commands](https://docs.tuist.io/en/cli/auth) such as `tuist build` or `tuist test`.

<ContentRef url="/workflows/ios-specific-workflow-steps/tuist-commands">
    Tuist Commands
</ContentRef>

## Xcode Select (Version)

This step is used to specify the Xcode version to be used during the build process.

<ContentRef url="/workflows/ios-specific-workflow-steps/xcode-select">
Xcode Select (Version)
</ContentRef>

:::info

### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](/self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools/#pool-based-xcode-version-selection).
:::

## Firebase Upload dSYM

Upload your debug symbols to Firebase Crashlytics

<ContentRef url="/workflows/ios-specific-workflow-steps/firebase-upload-dsym">
    Firebase Upload dSYM
</ContentRef>

## Xcodebuild for Devices (Archive & Export)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Share With Testers**](/testing-distribution/create-or-select-a-distribution-profile) feature or any other means of iOS distribution.

<ContentRef url="/workflows/ios-specific-workflow-steps/xcodebuild-for-devices">
    Xcodebuild for Devices (Archive & Export)
</ContentRef>

## Xcodebuild for iOS Simulator

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

<ContentRef url="/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator">
    Xcodebuild for iOS Simulator
</ContentRef>

## Xcodebuild for Testing

This step builds your application for testing.

<ContentRef url="/workflows/ios-specific-workflow-steps/xcodebuild-for-testing">
    Xcodebuild for Testing
</ContentRef>

## Xcodebuild for Unit and UI Tests

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.

<ContentRef url="/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test">
    Xcodebuild for Unit and UI Tests
</ContentRef>
