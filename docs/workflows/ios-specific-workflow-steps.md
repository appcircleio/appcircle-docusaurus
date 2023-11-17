---
title: iOS Specific Workflow Steps
metaTitle: iOS Specific Workflow Steps
metaDescription: iOS Specific Workflow Steps
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# iOS Specific Workflow Steps

The steps listed below are specific to the iOS build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Xcode Select (Version)

This step is used to specify the Xcode version to be used during the build process.

https://github.com/appcircleio/appcircle-xcode-select-component

:::info
### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](../self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools.md/#pool-based-xcode-version-selection).
:::

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

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

https://github.com/appcircleio/appcircle-ios-build-simulator

## Xcodebuild for Testing

This step builds your application for testing.

https://github.com/appcircleio/appcircle-ios-build-for-testing

## Xcodebuild for Unit and UI Tests

This step performs unit and UI tests for your iOS applications. This does not "build" your app, but uses the "xcodebuild" command to run tests. To build your app for testing, please refer to the previous workflow step.

https://github.com/appcircleio/appcircle-ios-test-component/

## Audit Permission Changes

With this component, you can check the permissions defined for your application in your project and see them directly if there is a change.

If an added or removed permission is detected, Appcircle will alert you about this change.

This component takes a reference branch, writes its permissions to a text file, and caches this file. When used on a branch for which a comparison is desired, it compares the permissions of the reference branch with those of the branch in question and detects any changes.

:::info
Keep in mind that, for the comparison to be made based on the reference branch, this component needs to be run once in the workflow of the branch from which you're taking the reference. This is only required for the initial run.
:::

A reference branch variable should be entered for permissions that will be referenced. If a component reference branch build is being performed, it will cache the permissions. If a build from another branch is being performed, it will attempt to determine the differences between the reference branch permissions and the current branch permissions by pulling the cached permissions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-steps-permissionReferance.png' />

If a component is run in a branch different from the one specified as a reference, and a permission change is detected, the workflow will automatically be aborted, and the build will fail. If you don't want this to happen, you need to enable the `Continue with the next step even if this step fails` toggle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-steps-permissionWarning.png' />

If this toggle is turned on, the workflow will continue without being aborted, and it will appear as a `Warning` when the build is completed.

:::info
If the component does not detect a permission change relative to the referenced branch, it will continue with the normal flow of the workflow without breaking it.
:::
:::caution
This component operates in a way that breaks the workflow when it detects a permission difference. Please note that if you do not enable the `Continue with the next step even if this step fails` toggle, the build will automatically fail.
:::
:::warning
This component works by identifying the differences based on the permissions of the branch provided as a reference. If it is not run at least once in the reference branch, it will throw an error and will not be able to detect permission differences.
:::

[https://github.com/appcircleio/appcircle-ios-permission-check-component](https://github.com/appcircleio/appcircle-ios-permission-check-component)

## Slather

This step converts Xcode's test results to different formats by using [Slather](https://github.com/SlatherOrg/slather/). This workflow must be run **after** [Xcodebuild for Unit and UI Tests](#xcodebuild-for-unit-and-ui-tests) step.

https://github.com/appcircleio/appcircle-slather-component

## Tuist

This step installs [Tuist](https://wwww.tuist.io/) and runs `tuist generate` with given options.

https://github.com/appcircleio/appcircle-tuist-component

## SwiftLint

This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs swiftlint with given options.

https://github.com/appcircleio/appcircle-swiftlint-component

## BrowserStack App Automate - XCUI

Run your XCUI tests on BrowserStack App Automate. You need to add **Xcodebuild Build for Testing** before this step to create the required `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` files.

[https://github.com/appcircleio/appcircle-browserstack-xcui-component](https://github.com/appcircleio/appcircle-browserstack-xcui-component)

## App Center iOS Distribution

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

[https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component](https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component)