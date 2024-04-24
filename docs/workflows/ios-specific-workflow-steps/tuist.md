---
title: Tuist
description: Scale your Xcode projects with Tuist. Streamline project management and automate configurations for efficient iOS app development.
tags: [xcode automation, project management, ios development, code generation]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Tuist

[**Tuist**](https://docs.tuist.io/) is a command line tool that leverages project generation to abstract intricacies of Xcode projects, and uses it as a foundation to help teams maintain and optimize their large modular projects.

You can seamlessly integrate **Tuist** into your workflow with Appcircle, facilitating easy setup and utilization within your existing development processes.

### Prerequisites

Before running the **Tuist** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the CocoaPods installation process. After the clone, CocoaPods will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2829-tuistOrder.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2829-tuistInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_TUIST_PATH`              | The path to the directory that contains the definition of the project. This path will be automatically generated after [Git Clone](/workflows/common-workflow-steps/git-clone) step.  | Optional |
| `$AC_TUIST_PROJECT_ONLY`      | Only generate the local project (without generating its dependencies). | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-tuist-component