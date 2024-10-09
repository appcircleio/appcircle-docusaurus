---
title: Tuist Commands
description: Scale your Xcode projects with Tuist. Streamline project management and automate configurations for efficient iOS app development.
tags: [tuist, xcode automation, project management, ios development, code generation, tuist command]
---

import Screenshot from '@site/src/components/Screenshot';

# Tuist Commands

[**Tuist Commands**](https://docs.tuist.io/cli/auth) component is a component where you can run Tuist specific commands using the [**Tuist CLI**](https://docs.tuist.io/). 

You can seamlessly integrate Tuist Commands into your workflow with Appcircle, making setup and utilization within your existing development processes easy.

### Prerequisites

Before you run the **Tuist Commands** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                              | Description                                                                                                                                                                    |
|---------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | You need to clone the repository to start the Tuist Commands process. After cloning, it creates the `AC_REPOSITORY_DIR` variable, and the system is able to run the Tuist Commands. |
| [Tuist](/workflows/ios-specific-workflow-steps/tuist)   | You need to install the Tuist to start the Tuist Commands process.                                                                                                             |

:::caution Tuist Commands

Tuist must be installed in order to use the **Tuist Commands** component. Tuist is a tool that can execute many **Xcode commands** on its own. For this reason, when certain commands are used, Appcircle's other iOS specific components will not be needed. For example, Workflow will no longer need the [**Xcodebuild for devices**](/workflows/ios-specific-workflow-steps/xcodebuild-for-devices) step when using the `tuist build` command. 

The same applies to the `tuist test` command. For example, if you run your tests with `tuist test` command, you will not need [**Xcodebuild for Unit and UI Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test) and [**Xcodebuild for Testing**](/workflows/ios-specific-workflow-steps/xcodebuild-for-testing) steps in the workflow.   

For more information about Tuist CLI Commands, please visit the [**Tuist CLI**](https://docs.tuist.io/cli/auth) documentation.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4430New-tuistCommandsOrder.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4430New-tuistCommandInput.png' />

| Variable Name        | Description                                                                                                                                                                         | Status   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_TUIST_PATH`     | Specifies the path to the directory containing the project definition. This path is automatically generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Optional |
| `$AC_TUIST_COMMANDS` | Specifies the Tuist Commands to be able to run specific Tuist Commands. For example; `tuist test` or `tuist build`.                                                                     | Required |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-tuist-commands-component