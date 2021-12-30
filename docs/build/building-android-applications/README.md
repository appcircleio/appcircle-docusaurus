---
title: 'Building Android Applications'
metaTitle: 'Building Android Applications'
metaDescription: 'Building Android Applications'
---

import ContentRef from '@site/src/components/ContentRef';

# Building Android Applications

Before starting your first Android app build, please make sure you first create a build profile and connect your Git repository to your build profile. You can refer to the page below for this step:

<ContentRef url="../../build/adding-a-build-profile">Adding a Build Profile</ContentRef>

After connecting your repository, please add or create your Android Keystore. You can refer to the page below for this step:

<ContentRef url="../../signing-identities/android-keystores">Android Keystores</ContentRef>

When you are done with the steps above, you can now start building your Android application.

### Build Configuration

First, we need to set up the build configuration.

Click on the gear icon on the top right to access the build configuration. First step will be the build project details. You can enter details manually or click on the Fetch Details button to retrieve them from your project.

### Sending the Build Status to the Repository Providers

At the bottom of the config tab, you will the **Set Commit Build Status **option.

![](<https://cdn.appcircle.io/docs/assets/image (8).png>)

When this option is enabled, the build status for that commit is shared with the repository provider.&#x20;

![](<https://cdn.appcircle.io/docs/assets/image (213).png>)

![](https://cdn.appcircle.io/docs/assets/appcircle-github-commit-status-pass.png)

### Build Triggers

Appcircle allows you to trigger builds manually or automatically using build triggers.

- On push: Whenever code is pushed to a configured branch, the build is triggered.
- On a tagged push: Whenever a tagged commit is pushed, the build is triggered for that commit. Commits without any tags are ignored.
- On push with selective tags: Whenever a commit includes one of the typed in tags, the build is triggered. You can specify tags with Unix shell-style wildcards to trigger builds.

You can visit the following page for details on build triggers:

<ContentRef url="../build-manually-or-with-triggers">
  Build Manually or Automatically with Webhooks and Triggers
</ContentRef>

###

### Signing

The next step on build configuration is Signing. Here, please select the Android Keystore you added at [Android Keystores](../../signing-identities/android-keystores.md) page.

:::info

You can get both unsigned and signed build artifacts based on your configuration. Please note that unsigned builds will not be distributed by email.

:::

![](https://cdn.appcircle.io/docs/assets/android-config.png)

###

### Distribution

The next step on build configuration is Distribution. You can create a new distribution profile at this screen or select a previous profile you created earlier. You can also enable auto deployment features if you need to.

<ContentRef url="../../distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

:::info

Any previous build can be deployed to the Distribute module without the need for rebuilding.

:::

###

### Environment Variables

The final step on build configuration is Environment Variables.&#x20;

Appcircle Build module is simple and powerful. You can get your builds instantly just with a few clicks, advanced management of builds is also possible with the environment variables and workflows.

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

Please see the following page for more information about environment variables:

<ContentRef url="../../environment-variables/why-to-use-environment-variables-and-secrets">
  Why to Use Environment Variables and Secrets?
</ContentRef>

![](https://cdn.appcircle.io/docs/assets/android-env.png)

Please click on the Save button and close this modal.

###

### Workflow Editor

You can use the workflow editor for in-depth configuration of all build steps. Please click on the workflow icon to open and use workflow editor.

:::info

Any custom operation during the build can be executed through the Custom Script step in the workflow.

:::

For details on using Appcircle's workflow editor, please see the related page below:

<ContentRef url="../../workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>

###

### Start Build

You are now ready to start your first build.

At the build profile page, you can see your branches are listed on the left and commits on the right.&#x20;

![](https://cdn.appcircle.io/docs/assets/android-build.png)

You can start the build by clicking on Build Now to the right of each commit.

Appcircle will start building your application. Build log window will open and you can follow build process in realtime.

:::info

You can safely close the build log window, it won't affect the status of your build. You can come back and click on the build to track the status of your build.

:::

![](https://cdn.appcircle.io/docs/assets/04-18-Build-Building.jpg)

**Distribute Your Build**

Your build will be distributed automatically if you had set up Auto Distribute earlier. You can also manually distribute builds at any time you like.

<ContentRef url="../../build/after-a-build">After a Build</ContentRef>

![](https://cdn.appcircle.io/docs/assets/android-distribute.png)
