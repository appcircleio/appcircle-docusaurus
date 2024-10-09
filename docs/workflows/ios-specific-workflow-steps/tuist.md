---
title: Tuist
description: Scale your Xcode projects with Tuist. Streamline project management and automate configurations for efficient iOS app development.
tags: [xcode automation, project management, ios development, code generation]
---

import Screenshot from '@site/src/components/Screenshot';

# Tuist

[**Tuist**](https://docs.tuist.io/) is a command-line tool that abstracts the intricacies of Xcode projects through project generation. It serves as a foundation to help teams maintain and optimize their large modular projects.

You can seamlessly integrate Tuist into your workflow with Appcircle, making setup and utilization within your existing development processes easy.


### Prerequisites

Before you run the **Tuist** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | You need to clone the repository to start the Tuist process. After cloning, the system installs Tuist and creates the `AC_REPOSITORY_DIR` variable.  |

:::caution Tuist Usage

Appcircle's Tuist component generates your project using only the `tuist generate` command. This means that it will automatically generate the `.xcworkspace` and `.xcodeproj` files in the project after the tuist generate command runs. Note that if you use Tuist in the Appcircle pipeline and want to generate an **IPA** file, you need the other build steps, such as

- [**Xcodebuild for Devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices)
- [**Xcodebuild for iOS Simulator**](/workflows/ios-specific-workflow-steps/xcodebuild-for-ios-simulator)
- [**Xcodebuild for Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-testing)
- [**Xcodebuild for Unit and UI Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test)
- [**Cocoapods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install)

For more iOS specific workflow steps, please visit the [**iOS Integration**](/workflows/ios-specific-workflow-steps) documentation.

:::

:::danger

In Tuist integrated projects, there will be cases where `.xcworkspace` and `.xcodeproj` files will be created after the `tuist generate` command. For this reason, the **auto fill** feature in the **build configuration** may not work as expected. For more information about build configurations, please visit the [**Build Configurations**](/build/build-process-management/build-profile-configuration) documentation.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2829-tuistOrder.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4430New-tuistInput.png' />

| Variable Name            | Description                                                                                                                                                                         | Status   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_TUIST_PATH`         | Specifies the path to the directory containing the project definition. This path is automatically generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Optional |
| `$AC_TUIST_VERSION`      | Specifies the Tuist version. If not specified, the latest version of Tuist will be installed.                                                                                       | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-tuist-component