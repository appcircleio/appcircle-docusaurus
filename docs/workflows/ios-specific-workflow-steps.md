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

:::info
This step is the archive and export step. When the step is completed, the .ipa file of the application is generated.
:::
:::caution
This step should always follow steps that may affect Archive and Export, such as Xcode Select and Cocoapods.
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2580-xcodebuild_order.png' />
:::

#### Adding Addtional parameter
This step builds, archives and exports your application using the **xcodebuild** command. You can write the extra command parameters you use when archiving in your local environment in the **Archive Flag** variable. 

You can write the custom parameters by leaving a space between them. Parameters written to **Archive Flag** will be added directly to the **xcodebuild** command.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2580-xcodebuild_details_flag.png' />

:::warning
**Remember**. The extra parameters you add in this step must be **known by the xcodebuild command**. This means that if you give a parameter other than the xcodebuild command parameter, the step will **fail**. For example, if you give a **Linux command** parameter, **xcodebuild command will not recognize that parameter**.
:::

#### Adding Configuration Parameter
You can specify the current build configuration of your project with the **Configuration** tab. For this, it will be enough to type your **configuration type correctly**. For example **Debug** or **Release**. This step will add the configuration parameter directly to the **xcodebuild command** as **`-configuration "Your Configuration"`**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2580-xcodebuild_details_config.png' />

:::warning
**Remember**, if you do not specify this parameter according to the configuration type in your project or if you make a **spelling mistake**, Xcode will fail the step because it cannot find this configuration.
:::



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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_order.png' />

:::info
After **Xcodebuild Build for Testing** step runs, `$AC_TEST_IPA_PATH` and `$AC_UITESTS_RUNNER_PATH` paths will be created automatically. The BrowserStack component depends on these paths.
:::

:::warning
When the build step order is not like this, **BrowserStack** will throw an **error** and **break the pipeline** because it cannot find the paths that your step depends on. 
- **Note that this step is dependent on Xcodebuild Build for Testing**
:::

#### Configuration of BrowserStack

You need to enter your BrowserStack **Username** and **Access Key** to use this step. This step will send the ipa created for the test to the BrowserStack dashboard with the credentials you provide. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_name.png' />

:::warning
**Do not specify the Access Key directly in a hard coded format in steps. Please use Environment Variables when using potentially sensitive variables like this.**
:::

At the same time, if you have custom configuration when you use BrowserStack, you can send a payload. If you have not a custom payload, this step comes with a default payload.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2587-bs_payload.png' />

In addition, you can specify a timeout period for the running time of the step. The duration is in seconds.

[https://github.com/appcircleio/appcircle-browserstack-xcui-component](https://github.com/appcircleio/appcircle-browserstack-xcui-component)

## App Center iOS Distribution

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

[https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component](https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component)

## Appdome Build-2Secure for iOS

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

[https://github.com/appcircleio/appcircle-ios-appdome-component](https://github.com/appcircleio/appcircle-ios-appdome-component)

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)
