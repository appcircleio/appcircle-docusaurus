---
title: CocoaPods Deintegrate
description: Clean your Xcode projects with Cocoapods Deintegrate. Remove pods swiftly to maintain a streamlined, efficient development environment.
tags: [cocoapods, deintegrate, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# CocoaPods Deintegrate

The CocoaPods Deintegrate component removes all dependencies from your project using the `pod deintegrate` command, providing a clean environment for building.

You can easily integrate the Appcircle CocoaPods Deintegrate workflow step into your pipeline and utilize it in your projects.

### Prerequisites

Before running the **CocoaPods Deintegrate** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the CocoaPods Deintegrate process. After the clone, Fastlane will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created.|

:::caution

Please remember to use the [**CocoaPods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install) step after this component, as it clears all dependencies in the project.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3178-deintegrateOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3178-deintegrateInput1.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_XCODEPROJ_PATH`          | Specifies the project path. For example: `./appcircle.xcodeproj`. Empty value will look for an `.xcodeproj` file. | Optional |
| `$AC_REPOSITORY_DIR`    | Specifies the directory where the repository is cloned. This path is generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step.                                                                                         | Optional |
| `$AC_COCOAPODS_VERSION` | Specifies the CocoaPods version. If you need a specific version, provide it here as hardcoded, and the system will automatically install that version.                                                                                        | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cocoapods-deintegrate-component