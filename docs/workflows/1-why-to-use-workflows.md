---
title: 'What are Workflows and How to Use Workflows?'
metaTitle: 'What are Workflows and How to Use Workflows?'
metaDescription: 'What are Workflows and How to Use Workflows?'
---

# What are Workflows and How to Use Them?

A workflow is a ladder of steps taken to build your applications.

Each step has a different purpose and the workflow can be customized by modifying step parameters and inputs, running custom scripts, or re-ordering steps.

Workflows allow you to have complete control on your build process and enhance it with third-party services and features.

:::caution

Please note that modifying workflow steps may cause your builds to fail, so utmost care is recommended when editing workflows.

:::

### Setting Up Workflows

To access the workflow editor for a build profile, click the Workflows button in the context menu of the build profile, accessible from the top of the profile details.

![](<https://cdn.appcircle.io/docs/assets/image (181).png>)

The workflow list will be displayed. To view the [Workflow Steps](why-to-use-workflows#worfklow-steps) of a workflow, click on it from the workflow list.

![](<https://cdn.appcircle.io/docs/assets/image (197).png>)

To create a new workflow, press the "New" button at the top of the workflow list and select a template from the default workflows. Then edit the workflow name and press enter.

![](<https://cdn.appcircle.io/docs/assets/image (198).png>)

To rename/delete a current workflow, press the "Edit" button at the top of the workflow list and then click on the context menu that appears next to the workflow items.

![](<https://cdn.appcircle.io/docs/assets/image (183).png>)

You can use the "Clone" option to create a new workflow based on the currently available ones. You can [select different workflows for different build scenarios](../build/build-manually-or-with-triggers#setting-and-managing-autobuild-triggers) (e.g. separate workflows for production and development).

![](<https://cdn.appcircle.io/docs/assets/image (184).png>)

### Worfklow Steps

![](<https://cdn.appcircle.io/docs/assets/image (185).png>)

Appcircle will build your application with the steps defined in the workflow. Steps will be executed in order from the top to the bottom.

You can customize each step for specific configurations with your application structure. Step parameters can be modified, outputs of each step can be used in another step and step versions can be selected accordingly.

### Workflow Marketplace

Appcircle's powerful Workflow Editor has a built-in Workflow Marketplace that allows you to select and insert an unlimited amount of steps to your workflow.

You can find the full list of available workflow steps in our workflow marketplace at:&#x20;

[https://appcircle.io/workflow-marketplace/](https://appcircle.io/workflow-marketplace/)

You can add platform-specific workflow steps, custom scripts, and other steps into your workflow and re-order them as you like. You can also remove the steps you don't need.

To access the Workflow Marketplace, go to the Workflow Editor and click on the Edit button:

![](<https://cdn.appcircle.io/docs/assets/image (186).png>)

You will see the Workflow Marketplace on the right and your Workflow steps on the left. You can now drag and drop steps into your workflow. Any unwanted workflow steps can be removed by clicking on the delete button on the right side of each step.

You can also reorder steps so that they will be executed in the order you specify.

![](https://cdn.appcircle.io/docs/assets/08-08-WF_Reorder.gif)

###

### Workflow Settings

Each workflow step has its own set of configuration options, which can be set by clicking on the step in the workflow screen.

The first three items are common for all steps and they are set individually for each step:

- **Step Execution Active:** To enable/disable the step execution without removing it from the workflow
- **Continue with the next step even if this step fails:** If a step is optional or if its result should not cause a build failure, you can select this option to continue the workflow in case of the failure of this specific step. In the default workflows, this option is turned on for certain steps.
- **Workflow Step Version: **You can select a specific version of a step with which to execute your build. If you select a version with an asterisk (\*), you will receive the minor updates to the workflow step automatically. The major versions may include added or removed input fields and manual version selection is required for major version updates.&#x20;

The items in the "Inputs" section are specific to that step. The reserved environment variables are assigned to these fields by default and the values of these variables are set in the build configuration.

![](<https://cdn.appcircle.io/docs/assets/image (187).png>)
