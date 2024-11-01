---
title: Fastlane
description: Appcircle supports Fastlane for build automation as a supplementary feature to Appcircle's own build automation.
tags: [fastlane, build, automation, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Fastlane

Appcircle supports [**Fastlane**](https://fastlane.tools/) for build automation as a supplementary feature to Appcircle's own build automation.

With Appcircle, you can automate your build and signing processes with the flexible workflow structure, and you can also use Fastlane as a workflow step within the build workflows.

### Prerequisites

The workflow steps that need to be executed before running the Fastlane workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](/workflows/common-workflow-steps/git-clone) | The repo needs to be cloned in order to start the Fastlane process. After the clone, Fastlane will be installed. After this step works, the variable `AC_REPOSITORY_DIR` will be created. |


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


## Fastlane FAQ

### How to run a Fastlane plug-in directly? 

With Appcircle's Fastlane integration, you can easily run the lane you want with the Fastfile in your project. 

You can easily add the [Fastlane plugins](https://rubygems.org/search?query=fastlane-plugin-) you want to run, which are not included in your Fastfile and are available on the Fastlane plugins, to the pipeline via a [**Custom Script**](/workflows/common-workflow-steps/custom-script) and run them easily. For all available plugins, please visit the [**Fastlane plugins**](https://docs.fastlane.tools/plugins/available-plugins/) documentations.

The example script below shows how to run the Fastlane plugin with a gem file. Add a Custom Script to your workflow and run the following script. For detailed information, please visit the [**Workflows**](/workflows) documentation. 


```bash

gem install fastlane-plugin-json
echo "gem 'fastlane-plugin-json'" >> Gemfile
fastlane run read_json json_path:'./example.json'

```

Once a plugin is installed, it is run with the `fastlane run` command. The necessary actions must be completed for the plugin to work correctly. The command used for this is as follows.

```bash

fastlane run [action] parameter:value

```

- `Action`: Plugin will be run.
- `Parameter`: Input parameter expected by the plugin.
- `Value`: Input value to be entered.

If the plugin you are using contains more than one parameter, you can use the parameters side by side as below.

```bash

fastlane run [action] parameter1:value1 parameter2:value2

```

For plugin details and the actions they contain, visit the repository of the [**Fastlane plugins**](https://docs.fastlane.tools/plugins/available-plugins/).


In this example, `fastlane-plugin-json` is used as Fastlane plugin.