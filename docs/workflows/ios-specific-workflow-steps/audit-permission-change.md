---
title: Audit Permission Changes
description: Track and audit permission changes effectively. Ensure security and compliance with our guide on monitoring access rights alterations.
tags: [cocoapods, install, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Audit Permission Changes

This component captures and compares permission changes in your iOS projects.

The system conducts this check using a reference branch. First, run the pipeline containing this component on the branch you intend to use as a reference. Subsequently, when you run it on the branch you want to check, the system performs the control relative to this selected reference branch. When it detects a change in the project's permissions, Appcircle automatically stops the pipeline to ensure that no significant permission change goes unnoticed.

### Prerequisites

Before running the **Audit Permission Changes** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | You need to clone the repository to start the Audit Permission Changes process. After cloning, the system installs CocoaPods. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3179-permissionOrder.png' />

:::caution

The **Audit Permission Changes** component will automatically break the pipeline and halt operations if it detects a permission change. If you do not want this to occur, activate the **`'Continue with the next step even if this step fails'`** toggle within the step. This command will allow the pipeline to continue even if the step fails.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-steps-permissionWarning.png' />

:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3179-permissionInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_REFERENCE_BRANCH`        | Specifies the reference branch to check permissions. | Required |
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. This path will be generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Required |
| `$AC_PROJECT_PATH`            | Specifies the project path. For example: `./appcircle.xcodeproj` | Required |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-permission-check-component