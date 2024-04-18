---
title: Xcodebuild for iOS Simulator
description: Build your iOS app for the Simulator with Xcodebuild. Creates an unsigned xarchive file. 
tags: [ios, simulator, xcodebuild, workflow, step]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Xcodebuild for iOS Simulator

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for the given simulator.

### Prerequisites

Use this step after the **Xcode Select**  and **CocoaPods Install** (if you use **CocoaPods** in your project) steps.  

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcode Select**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcode-select-version)     | This step selects the Xcode version that is specified. |
| [**Cocoapods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#cocoapods-install)   | This step installs all the dependencies of the pod file. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_order.png' />

:::caution
If you use SPM (Swift Package Manager), Xcode will manage itself when a project is built. The **CocoaPods Install** step is not necessary.
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-simInput.png' />


| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_REPOSITORY_DIR`         | Specifies the cloned repository directory. This path will be generated after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step. | Required |
| `$AC_OUTPUT_DIR_PATH`        | Specifies the path for outputs for generated artifacts. | Required |
| `$AC_SCHEME`                 | Specifies the project scheme for build. If you filled in `Config => Build Schema` in the Configuration, this variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration). | Required |
| `$AC_SIMULATOR_ARCH`          | Specifies the CPU architecture for the simulator build. The default variable is **`arm64`**. | Optional |
| `$AC_SIMULATOR_NAME`         | Destination name of the simulator. Ex. `iPhone 14`. If you set a simulator name, the build will be installed into the given simulator. Please be aware that setting the simulator name invalidates the `AC_SIMULATOR_ARCH` option. | Required |
| `$AC_ARCHIVE_FLAGS`             | Specifies the extra xcodebuild flag. For example: -quiet | Optional |
| `$AC_PROJECT_PATH`               | Specifies the project path. If you filled in `Config => Xcode Project or Workspace Path` in the Configuration, this variable comes from [Configuration](https://docs.appcircle.io/build/building-ios-applications#build-configuration). For example: `./appcircle.xcodeproj`. | Required |
| `$AC_CONFIGURATION_NAME`             | You can build your project with any configuration you want. Specify the configuration as hard coded. Appcircle will automatically add this configuration to the xcodebuild command. For example; **`Debug`**. | Optional |
| `$AC_COMPILER_INDEX_STORE_ENABLE` | You can disable indexing during the build for a faster build. The default value is **`No`**. | Required |

:::caution
Be aware of which OS version you used; the simulator type should match that OS version. For example, if you use the [**latest OS version**](https://developer.apple.com/documentation/ios-ipados-release-notes), you can not use the **iPhone 14** simulator.
:::
 
### Output Variables

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `$AC_SIMULATOR_APP_PATH`      | Simulator app path. You can reach the Simulator app from this path, and it will be exported, it can be downloaded from the download artifacts. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-build-simulator