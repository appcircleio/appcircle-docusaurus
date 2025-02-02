---
title: Tuist Install
description: Scale your Xcode projects by installing Tuist. Streamline project management and automate configurations for efficient iOS app development.
tags: [tuist, xcode automation, project management, ios development, code generation, tuist install]
---

import Screenshot from '@site/src/components/Screenshot';

# Tuist Install

[**Tuist**](https://docs.tuist.io/) is a command-line tool that abstracts the intricacies of Xcode projects through project generation. It serves as a foundation to help teams maintain and optimize their large modular projects.

You can seamlessly integrate Tuist Install into your workflow with Appcircle, making setup and utilization within your existing development processes easy.

:::info

Tuist CLI tool is a tool that enables different actions to be performed in the project with different commands. The **Tuist Install** step only installs Tuist and runs the `tuist generate` command to generate the project. On the other hand, if you want to run other commands that Tuist has, please visit the [**Tuist Commands**](/workflows/ios-specific-workflow-steps/tuist-commands) step document.

:::

### Prerequisites

Before running the **Tuist Install** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | You need to clone the repository to start the Tuist process. After cloning, the system installs Tuist and creates the `$AC_REPOSITORY_DIR` variable.  |

:::caution Tuist Usage

Appcircle's Tuist Install component generates your project using only the `tuist generate` command. This means that it will automatically generate the `.xcworkspace` and `.xcodeproj` files in the project after the tuist generate command runs. Note that if you use **Tuist Install** in the Appcircle pipeline and want to generate an **IPA** file, you need the other build steps, such as

- [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices)
- [**Xcodebuild for iOS Simulator**](/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator)
- [**Xcodebuild for Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-testing)
- [**Xcodebuild for Unit and UI Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test)
- [**Cocoapods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install)

For more iOS specific workflow steps, please visit the [**iOS Integration**](/workflows/ios-specific-workflow-steps) documentation.

:::

:::danger

In Tuist integrated projects, there will be cases where `.xcworkspace` and `.xcodeproj` files will be created after the `tuist generate` command. For this reason, the **auto fill** feature in the **build configuration** may not work as expected. For more information about build configurations, please visit the [**Build Configurations**](/build/build-process-management/configurations) documentation.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/tuistInstallStepOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/tuistIntallStepInput.png' />

:::tip Tuist Version

In some projects, the version of Tuist that needs to be installed and used can be integrated **into the project** with the `.tuist-version` file. If you have a project with **Tuist** version integrated in this way, Appcircle will **not detect** the Tuist version in the project, so if there is a **specific** Tuist version you want to install, you **must** enter this version in the **Tuist Version** input field in the step.

:::

:::caution Tuist Install

Appcircle uses homebrew as [installation method](https://docs.tuist.io/en/guides/quick-start/install-tuist) in **Tuist Install** step, therefore only compatible versions are supported. For more information, please check this [list](https://github.com/tuist/homebrew-tuist/tree/main/Formula) for compatible versions of Tuist.

For this reason, iOS apps using Tuist versions `1.x` or `2.x` are not supported with Appcircle's Tuist Components.

:::

| Variable Name            | Description                                                                                                                                                                         | Status   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_TUIST_PATH`         | Specifies the path to the directory containing the project definition. This path is automatically generated after the [**Git Clone**](/workflows/common-workflow-steps/git-clone) step. | Required |
| `$AC_TUIST_VERSION`      | Specifies the Tuist version. If not specified, the latest version of Tuist will be installed.                                                                                       | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-tuist-component