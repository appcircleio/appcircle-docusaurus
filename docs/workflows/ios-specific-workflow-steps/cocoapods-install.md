---
title: Cocoapods Install
description: Master Cocoapods Install for managing dependencies in your project. Learn how to use the 'pod install' command effectively.
tags: [cocoapods, install, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Cocoapods Install

Runs the [CocoaPods](https://cocoapods.org) install command for dependency management. This step installs all pod dependencies. Appcircle uses the `pod install` command to install pods in the project. This command comes from the CocoaPods tool installed on the system. If a version is not specified for CocoaPods, this step will use the version of [**CocoaPods installed**](/infrastructure/ios-build-infrastructure#ios-build-agent-stacks) on the system.

### Prerequisites

Before running the **Cocoapods Install** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                        | Description                                                                                                                                                                                              |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the CocoaPods installation process. After the clone, CocoaPods will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_order.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_version.png' />

| Variable Name           | Description                                                                                                                                                                                                                                                     | Status   |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_PROJECT_PATH`      | Specifies the project path. For example: `./appcircle.xcodeproj`. If you filled in **`Configuration => Project or Workspace`**, this variable comes from [Configuration](/build/build-process-management/build-profile-configuration). | Required |
| `$AC_REPOSITORY_DIR`    | Specifies the cloned repository directory. This path will be generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step.                                                                                         | Required |
| `$AC_COCOAPODS_VERSION` | Specifies the CocoaPods version. If there is a specific version you want to use, give it here as hardcoded, and the system will automatically install the given version.                                                                                        | Optional |

:::info

Please note that the CocoaPods Install step uses the default system [**CocoaPods version**](/infrastructure/ios-build-infrastructure#ios-build-agent-stacks). If you want to use a specific version, please enter it hardcoded in the CocoaPods Version parameter in the step.

:::

:::danger

Remember, if the project extension is not **.xcworkpace**, the pod install step will not work as expected. In the Configuration tab, make sure that the extension in the project path is **.xcworkspace**.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cocoapods-component
