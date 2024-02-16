---
title: iOS Workflow Steps
metaTitle: iOS Workflow Steps
metaDescription: iOS Workflow Steps
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

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