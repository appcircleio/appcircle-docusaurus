---
title: Xcode Select
description: Specify Xcode version for your build process with Xcode Select.
tags: [xcode, version, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Xcode Select (Version)

This step is used to specify the Xcode version to be used during the build process. All available versions of Xcode can be seen in the [Configuration](/build/build-process-management/build-profile-configuration) tab.

### Prerequisites

There are no prerequisites required before using the **Xcode Select** step.

:::danger

Always use this step **before** [**CocoaPods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install) and [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices). If you have other **Xcode related** steps, such as [**Xcodebuild for iOS Simulators**](/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator) and [**Xcodebuild for Unit and UI Tests**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test), **don't forget** to use before them.

:::

:::caution

Please **don't forget** to select the **Xcode version** from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration) first.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcodeOrder.png' />

### Version Change

- To select an Xcode version, open [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration) in the build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_config.png' />

- After opening the configuration, you will see the **Xcode Version** section. Now you can select a version for Xcode.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2585-xcode_select_list.png' />

:::info

Appcircle provides new versions of Xcode (including beta versions) within 24 hours after they are released.

:::

:::info Manually Xcode Version Change (Not Recommended)

In addition to the version change method described above, you can also change the Xcode version **manually**. For this, you can **hard-code** the desired Xcode version into the `$AC_XCODE_VERSION` parameter, which serves as the input for the **Xcode Select** step. For example: `15.1`.

Please note that, if the version you hard-coded is not available on the runner where the build will run, the build **will not** start. The [**Build Configuration**](/build/platform-build-guides/building-ios-applications#build-configuration) always lists the **available** Xcode versions.

For more information, please visit our [**iOS Build Stacks**](/infrastructure/ios-build-infrastructure#available-xcode-versions) documentation.

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5421-xcodeSelectInput.png' />

| Variable Name        | Description                                                                                                                                           | Status   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_XCODE_LIST_DIR` | Specifies the directory with the Xcode versions. Xcode versions are located under the `/Volumes` directory and selected according to the given version. | Required |
| `$AC_XCODE_VERSION`  | Specifies the xcode version. This variable comes from Configuration.                                                                                  | Required |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-xcode-select-component
