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

This step is used to specify the Xcode version to be used during the build process. All available versions of Xcode can be seen from configuration tab. 

- For this, open configurations in build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_config.png' />

- Create a new configuration set or use existing one

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_config_details.png' />

- After open configuration set, you will see **Xcode Version** section. Now you can select a version for Xcode.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_list.png' />

:::info
Appcircle provides new versions of Xcode (including Beta versions) within 24 hours after they released. 
:::
:::caution
### Pool-Based Xcode Version Selection

A version other than the Xcode versions on the configuration page should not be entered manually as the Xcode select workflow argument.
Because the Xcode versions on the configuration page are the versions installed on runners.
Entering an unavailable Xcode version may cause the build to fail.

You can review the documentation for detailed information about the Xcode version selection [here](../self-hosted-appcircle/self-hosted-runner/configure-runner/manage-pools.md/#pool-based-xcode-version-selection).
:::

https://github.com/appcircleio/appcircle-xcode-select-component

## Cocoapods Install

Runs the Cocoapods install command for dependency management. This step install your all pod dependencies. And it should be used after **Git Clone** step

- For this, open workflow and check **Cocoapods Install** step

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_order.png' />

- You can specify the Cocoapods version. Default is empty. If you leave empty this parameter, Appcircle will read **Podfile.lock** and install related version of Cocoapods.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_version.png' />

:::warning
Remember, if the project extension is not **.xcworkpace**, the pod install step will not work as expected. In the Configuration tab, make sure that the extension in the project path is **.xcworkspace**.
:::



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

[https://github.com/appcircleio/appcircle-browserstack-xcui-component](https://github.com/appcircleio/appcircle-browserstack-xcui-component)

## App Center iOS Distribution

Distribute IPA and dSYM files to [App Center](https://appcenter.ms/). You need enter your token, owner, app and group names to distribute your binaries.

[https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component](https://github.com/appcircleio/appcircle-ios-appcenter-distribute-component)

## Appdome Build-2Secure for iOS

Appdome Build-2Secure is a comprehensive automated solution that seamlessly integrates advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

[https://github.com/appcircleio/appcircle-ios-appdome-component](https://github.com/appcircleio/appcircle-ios-appdome-component)

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

[https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration](https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-integration)
