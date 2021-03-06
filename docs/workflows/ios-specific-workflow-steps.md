---
title: iOS Specific Workflow Steps
metaTitle: iOS Specific Workflow Steps
metaDescription: iOS Specific Workflow Steps
sidebar_position: 3
---

# iOS Specific Workflow Steps

The steps listed below are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Xcode Select (Version)

This step is used to specify the Xcode version to be used during the build process.

https://github.com/appcircleio/appcircle-xcode-select-component

## Cocoapods Install

Runs the Cocoapods install command for dependency management.

https://github.com/appcircleio/appcircle-cocoapods-component

## Carthage

Runs the Carthage bootstrap/update command for dependency management.

https://github.com/appcircleio/appcircle-carthage-component

## Install Certificates and Profiles

This step installs the selected certificates and the provisioning profile for the build.

https://github.com/appcircleio/appcircle-ios-install-certificates-and-profiles-component

## Xcodebuild for Devices (Archive & Export)

This step builds your application for iOS devices in ARM architecture, which is required for the [**Share With Testers**](../distribute/create-or-select-a-distribution-profile.md) feature or any other means of iOS distribution.

https://github.com/appcircleio/appcircle-ios-build-sign-component

## Xcodebuild for iOS Simulator

This step builds your application for the iOS Simulator in x86 architecture which is required for the [**Preview on Device**](../distribute/preview-on-device.md) feature. This step creates an unsigned `xarchive` file.

https://github.com/appcircleio/appcircle-ios-build-simulator

## Xcodebuild for Testing

This step builds your application for testing.

https://github.com/appcircleio/appcircle-ios-build-for-testing

## Xcodebuild for Unit and UI Tests

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.

https://github.com/appcircleio/appcircle-ios-test-component/

## Slather

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

https://github.com/appcircleio/appcircle-slather-component

## Tuist

This step installs [Tuist](https://wwww.tuist.io/) and runs `tuist generate` with given options.

https://github.com/appcircleio/appcircle-tuist-component