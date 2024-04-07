---
title: Fastlane
description: Appcircle supports Fastlane for build automation as a supplementary feature to Appcircle's own build automation.
tags: [fastlane, build, automation, workflow, step]
sidebar_position: 9
---

import Screenshot from '@site/src/components/Screenshot';

# Fastlane

Appcircle supports [**Fastlane**](https://fastlane.tools/) for build automation as a supplementary feature to Appcircle's own build automation.

With Appcircle, you can automate your build and signing processes with the flexible workflow structure, and you can also use Fastlane as a workflow step within the build workflows.

### Prerequisites

The workflow steps that need to be executed before running the Fastlane workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/build-and-test/git-clone) | The repo needs to be cloned in order to start the Fastlane process. After the clone, Fastlane will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-fastlaneOrder.png' />

:::caution
Fastlane needs project files to work. If there is no **Git Clone** step in your workflow, it will give an error because it cannot find the relevant files of the project.
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3049-fastlaneInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FASTLANE_DIR`            | This path is Fastlane's path in the project. By default, it is AC_REPOSITORY_DIR. If your Fastlane file is in a different location in the repo, please change it. | Required |
| `$AC_FASTLANE_LANE`           | Fastlane lane. For example: `android deploy` or `ios release` | Required |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-fastlane-component

