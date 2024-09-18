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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2829-tuistOrder.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4430-tuistInputs.png' />

| Variable Name            | Description                                                                                                                                                                         | Status   |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_TUIST_PATH`         | Specifies the path to the directory containing the project definition. This path is automatically generated after the [Git Clone](/workflows/common-workflow-steps/git-clone) step. | Optional |
| `$AC_TUIST_VERSION`      | Specifies the Tuist version. If not specified, the latest version of Tuist will be installed.                                                                                       | Optional |
| `$AC_TUIST_BUILD`        | Build your Tuist project. If it is true, it will run the `tuist build` command.                                                                                                     | Optional |
| `$AC_TUIST_TEST`         | Run tests in your project. If it is true, it will run the `tuist test` command.                                                                                                     | Optional |
| `$AC_TUIST_CLEAN`        | Clean all previous build files. It will provide clean build. If it is true, it will run the `tuist clean` command.                                                                  | Optional |
| `$AC_TUIST_PROJECT_ONLY` | Generates only the local project, without generating its dependencies.                                                                                                              | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-tuist-component