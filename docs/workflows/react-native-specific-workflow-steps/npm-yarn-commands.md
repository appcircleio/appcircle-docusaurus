---
title: NPM/Yarn Commands
description: Learn to use NPM/Yarn commands for managing dependencies in your React Native applications. Enhance your app's functionality.
tags: [react-native, mobile, workflow, step]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# NPM/Yarn Commands

You may want to use the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your [React Native](https://reactnative.dev/) applications. The package manager commands you enter are executed in this workflow step.

### Prerequisites

The workflow steps that need to be executed before running the **NPM/Yarn Commands** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Install Node**](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps#install-node) | This step will install Node modules for your application. Please note that the **NPM/Yarn Commands** step should be used after this step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2797-npmOrder.png' />

### Input Variables

This step contains different variables. It needs these variables to work. The table below gives explanations of these variables.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2797-nmpDetails.png' />

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_REPOSITORY_DIR`          | Specifies the cloned repository directory. This path will be generated after the [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps#git-clone) step. | Required |
| `$AC_NPM_COMMAND_ARGS`        | The NPM command to run. You can add different command parameters directly. The default is: `npm/yarn install` | Optional |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-npm-yarn-component
