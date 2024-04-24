---
title: CocoaPods Deintegrate
description: Clean your Xcode projects with Cocoapods Deintegrate. Remove pods swiftly to maintain a streamlined, efficient development environment.
tags: [cocoapods, deintegrate, workflow, step]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# CocoaPods Deintegrate

The CocoaPods Deintegrate component cleanses your project of all dependencies with `pod deintegrate` command, providing a clean environment for building.

You can easily integrate Appcircle's CocoaPods Deintegrate workflow step into your pipeline and utilize them in your projects.

### Prerequisites

Before running the **CocoaPods Deintegrate** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the CocoaPods Deintegrate process. After the clone, Fastlane will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created.|

:::caution

Please note that after using this component since it will clear all dependencies in the project, you should not forget to use the [**CocoaPods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install) step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3178-deintegrateOrder.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3178-deintegrateInput1.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_XCODEPROJ_PATH`          | Specifies the project path. For example: `./appcircle.xcodeproj`. Empty value will look for an `.xcodeproj` file. | Optional |
| `$AC_REPOSITORY_DIR`    | Specifies the cloned repository directory. This path will be generated after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step.                                                                                         | Optional |
| `$AC_COCOAPODS_VERSION` | Specifies the CocoaPods version. If there is a specific version you want to use, give it here as hardcoded, and the system will automatically install the given version.                                                                                        | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cocoapods-deintegrate-component