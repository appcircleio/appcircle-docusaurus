---
title: Building iOS Applications
metaTitle: Building iOS Applications
metaDescription: Building iOS Applications
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Building iOS Applications

Building iOS applications may be complex and confusing. Appcircle will help you smooth the process and doesn't require any additional configuration files from you.

Before starting your first iOS app build, please make sure you first create a build profile and connect your Git repository to your build profile. You can refer to the page below for this step:

<ContentRef url="/build/adding-a-build-profile">Adding a Build Profile</ContentRef>

After connecting your repository, please add or create your iOS certificate and provisioning profile. You can refer to the page below for this step:

<ContentRef url="/signing-identities/ios-certificates-and-provisioning-profiles">
  iOS Certificates and Provisioning Profiles
</ContentRef>

When you are done with the steps above, you can now start building your iOS application.

### Build Configuration

First, we need to set up a build configuration. Select the configuration from the **Configuration** section. The first step will be to enter project details. You can enter details manually or click on the "Autofill" button to retrieve them from your project.

Your iOS project needs to have an **Xcode project** or an **Xcode workspace** and a **shared scheme** to complete the build configuration successfully. Appcircle can fetch these workspaces and shared schemes from your branch automatically.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-fetch.png' />

**Share your iOS schemes**

iOS schemes must be marked as shared in order to build your application outside of Xcode. If your application doesn't have a shared scheme, it can only be built using Xcode.

You can check the shared option in your Xcode's scheme manager to mark your application's scheme as shared.

:::caution

Please don't forget to add additional scheme files to your version control.

:::

### Private Modules

If your project uses private modules, don't forget the add necessary SSH keys to your workflow steps. You can use `Activate SSH Private Key` step to add your private SSH keys.

<ContentRef url="/build/adding-a-build-profile/connecting-to-private-repository-via-ssh">Connecting to Private Repository via SSH</ContentRef>

You may also use `Authenticate with netrc` step to access your private modules.

https://github.com/appcircleio/appcircle-netrc-component

#### Selecting the Xcode Version and Switching to the Xcode Beta

Major Xcode versions are available for building in Appcircle. You can select the preferred Xcode version in Build Configuration window.

The list of currently available Xcode versions can be found in the following document: [iOS Build Infrastructure](../infrastructure/ios-build-infrastructure.md)

By default, the most recent stable version of Xcode is selected. If available, you can also switch to the most recent Xcode beta at the top of the list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-fetch.png' />

### Sending the Build Status to the Repository Providers

At the bottom of the config tab, you will see the **Set Commit Build Status** option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (8).png' />

When this option is enabled, the build status for that commit is shared with the repository provider.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (213).png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/appcircle-github-commit-status-pass.png' />

### Build Triggers

Appcircle allows you to trigger builds manually or automatically using build triggers.

- On push: Whenever code is pushed to a configured branch, the build is triggered.
- On a tagged push: Whenever a tagged commit is pushed, the build is triggered for that commit. Commits without any tags are ignored.
- On push with selective tags: Whenever a commit includes one of the typed in tags, the build is triggered. You can specify tags with Unix shell-style wildcards to trigger builds.

You can visit the following page for details on build triggers:

<ContentRef url="/build/build-manually-or-with-triggers">
  Build Manually or Automatically with Webhooks and Triggers
</ContentRef>

###

### Signing

The next step on build configuration is Signing. Here, please select the provisioning profile you added at [iOS Certificates & Provisioning Profiles](../signing-identities/ios-certificates-and-provisioning-profiles.md) page.

:::info

You can get both unsigned and signed build artifacts based on your configuration.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (170).png' />

### Distribution

The next step on build configuration is Distribution. You can create a new distribution profile at this screen or select a previous profile you created earlier. You can also enable auto deployment features if you need to.

<ContentRef url="/distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

:::info

Any previous build can be deployed to the Distribute module without the need for rebuilding.

:::

### Versioning

The versioning tab will allow you to change the build or version number during the build. You can increase the build number or version number by using different sources and strategies. 

<ContentRef url="/versioning/ios-version">
  Managing iOS Build and Version Numbers
</ContentRef>


### Environment Variables

The final step on build configuration is Environment Variables.

Appcircle Build module is simple and powerful. You can get your builds instantly just with a few clicks, advanced management of builds is also possible with the environment variables and workflows.

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

Please see the following page for more information about environment variables:

<ContentRef url="/environment-variables">
  Why to Use Environment Variables and Secrets?
</ContentRef>

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (172).png' />

Please click on the Save button and close this modal.

### Workflow Editor

You can use the workflow editor for in-depth configuration of all build steps. Please click on the workflow icon to open and use workflow editor.

:::info

Any custom operation during the build can be executed through the Custom Script step in the workflow

:::

For details on using Appcircle's workflow editor, please see the related page below:

<ContentRef url="/workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>


### Start Build

You are now ready to start your first build. Select the branach from the left side and click on the **Start Build** button.


<Screenshot url='https://cdn.appcircle.io/docs/assets/start-build.png' />

Select a configuration, workflow, commit id and click on **Start Build button**

<Screenshot url='https://cdn.appcircle.io/docs/assets/start-build-configuration.png' />


Appcircle will start building your application. Build log window will open and you can follow build process in realtime.

:::info

You can safely close the build log window, it won't affect the status of your build. You can come back and click on the build to track the status of your build.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/03-06b-iOS-Build-Building.png' />

---

**Distribute your build**

Your build will be distributed automatically if you had set up auto build earlier. You can also manually distribute builds at any time you like.

<ContentRef url="/build/after-a-build">After a Build</ContentRef>

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-distribute.png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
