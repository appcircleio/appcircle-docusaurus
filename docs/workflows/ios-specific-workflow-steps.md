---
title: iOS Specific Workflow Steps
metaTitle: iOS Specific Workflow Steps
metaDescription: iOS Specific Workflow Steps
sidebar_position: 3
---

import ExternalUrlRef from '@site/src/components/ExternalUrlRef';


# iOS Specific Workflow Steps

The steps listed below are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Xcode Select (Version)

This step is used to specify the Xcode version to be used during the build process.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-xcode-select-component" title="Appcircle XCode Select Component"/>

:::info
### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](../self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools.md/#pool-based-xcode-version-selection).
:::

## Cocoapods Install

Runs the Cocoapods install command for dependency management.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-cocoapods-component" title="Appcircle Cocoapods Component"/>

## Carthage

Runs the Carthage bootstrap/update command for dependency management.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-carthage-component" title="Appcircle Carthage Component"/>

## Install Certificates and Profiles

This step installs the selected certificates and the provisioning profile for the build.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-install-certificates-and-profiles-component" title="Appcircle iOS Install Certificates and Profiles Component"/>

## Xcodebuild for Devices (Archive & Export)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Share With Testers**](../distribute/create-or-select-a-distribution-profile.md) feature or any other means of iOS distribution.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-build-sign-component" title="Appcircle iOS Build Sign Component"/>

## Xcodebuild for iOS Simulator

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-build-simulator" title="Appcircle iOS Build Simulator"/>

## Xcodebuild for Testing

This step builds your application for testing.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-build-for-testing" title="Appcircle iOS Build for Testing"/>

## Xcodebuild for Unit and UI Tests

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-test-component/" title="Appcircle iOS Test Component"/>

## Slather

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-slather-component" title="Appcircle Slather Component"/>

## Tuist

This step installs [Tuist](https://wwww.tuist.io/) and runs `tuist generate` with given options.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-tuist-component" title="Appcircle Tuist Component"/>

## SwiftLint

This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-swiftlint-component" title="appcircle-swiftlint-component"/>

## BrowserStack App Automate - XCUI

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-browserstack-xcui-component" title="Appcircle Browserstack xcui Component"/>

## App Center iOS Distribution

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

<ExternalUrlRef url="https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component" title="Appcircle iOS Appcenter Distribute Component"/>