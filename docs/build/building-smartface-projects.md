---
title: Building Smartface Projects
metaTitle: Building Smartface Projects
metaDescription: Building Smartface Projects
sidebar_position: 9
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Building Smartface Projects

Once your build is complete, you can now download the binary file or deploy it to distribute module manually (if autodistribute is enabled, it will be sent automatically after a successful build).

You can also view or download your build logs anytime.Smartface builds work very similar to any iOS or Android builds. Appcircle can build mobile applications developed with Smartface Cloud IDE flawlessly.

Smartface projects are single-code based and can be built into both iOS and Android applications using Appcircle.

:::caution

Please note that you need to create separate build profiles for iOS and Android outputs for the same Smartface project.

:::

### Build Configuration

The overall workflow for Smartface builds is almost the same as the iOS and Android build steps explained earlier.


### Signing

In the Signing page, select the proper signing certificates for iOS or Android applications.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (170).png' />

###

### Distribution

On the Distribution page, create a new distribution profile or select a previous profile you created earlier. You can also enable auto distribution feature if you need to.

<ContentRef url="/distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

:::info

Any previous build can be deployed to the Distribute module without the need for rebuilding

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (171).png' />

###

### Environment Variables

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

Please see the following page for more information about environment variables:

<ContentRef url="/environment-variables/why-to-use-environment-variables-and-secrets">
  Why to Use Environment Variables and Secrets?
</ContentRef>

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (172).png' />

Please click on the Save button and close this modal.

###

### Workflow Editor

You can use the workflow editor for in-depth configuration of all build steps. Please click on the workflow icon to open and use workflow editor.

:::info

Any custom operation during the build can be executed through the Custom Script step in the workflow.

:::

![](https://cdn.appcircle.io/docs/assets/03-05a-Smf-Build-Workflow.png)

For details on using Appcircle's workflow editor, please see the related page below:

<ContentRef url="/workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>

### Start Build

You are now ready to start your first build. Select the branach from the left side and click on the **Start Build** button.


![](https://cdn.appcircle.io/docs/assets/start-build.png)

Select a configuration, workflow, commit id and click on **Start Build button**

![](https://cdn.appcircle.io/docs/assets/start-build-configuration.png)

:::info

You can safely close the build log window, it won't affect the status of your build. You can come back and click on the build to track the status of your build.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/03-06b-iOS-Build-Building.png' />

Your build will be distributed automatically if you had set up auto build earlier. You can also manually distribute builds at any time you like.

<ContentRef url="/build/after-a-build">After a Build</ContentRef>

![](https://cdn.appcircle.io/docs/assets/03-06-iOS-Build-AfterBuild.png)

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
