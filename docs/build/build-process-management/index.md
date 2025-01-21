---
title: Build Profile
description: Learn how to manage your build processes effectively with Appcircle. Optimize your build configurations, manage branches, and automate your build pipeline for efficient app development.
tags:
  [
    build process management,
    build profiles,
    branch management,
    manual builds,
    automatic builds,
    app development,
    app deployment,
    appcircle build process,
  ]
---

New to Appcircle Build module? Follow our quick start guide to build your iOS and Android apps in the cloud.

The Build Module allows you to streamline and automate your mobile app build flows.

:::info

The Build Module is the first step to automate your CI/CD processes via Appcircle.

:::

## Creating a Profile

A Build profile can be created by following these steps: 

Click on the **Add New** button located at the middle of the screen. If you already have an existing profile displayed on the build profile list, this button will be at the top right corner.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build1.png' alt="Build Profile Creation" />

Provide a unique name for the build profile and choose a target Operating System (OS) which can be Android or iOS.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build2.png' alt="Build Profile Naming" />

After selecting the target OS, specify the corresponding target platform to set up a compatible build environment:

iOS Platforms:
* Objective-C / Swift
* React Native
* Flutter

Android Platforms:
* Java / Kotlin
* React Native
* Flutter

Click **Save** to proceed.

Choose from the available repository connection options to link your project source code:

* [GitHub](/build/manage-the-connections/adding-a-build-profile/connecting-to-github)
* [Azure](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure)
* [Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket)
* [GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab)
* [Connect via SSH](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh)
* Connect via URL
* [Connecting to Multiple Instances](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance)

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build3.png' alt="Repository connection" />

:::info
If you have not previously connected to a Git provider on Appcircle, i.e., created a profile and not connected a repository, you will not see any connection on this page.

For more information on creating repository connections, please refer to the [connections](/build/manage-the-connections) guide.
:::

To test drive Appcircle, you can find various sample projects in the [Appcircle GitHub page](https://github.com/appcircleio?q=sample) or you can just press on the **Quick start using the sample repository** button to populate the repository with a compatible project based on the selected framework.

For detailed instructions on connecting to each repository, refer to the [Connection Guides](/build/manage-the-connections/adding-a-build-profile#connect-your-repository).

Once the repository connection is established, the build profile will be created successfully. Appcircle will then pull your branches, commits, and other information from your repository. You can now use the build profile to manage and deploy your projects.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build4.png' alt="Build Profile"/>

### Profile Listing

Users can view their created build profiles by selecting the **Build Profiles** option in the left menu. They can also toggle between the profile card view and list view to easily locate profiles for different project types.

- Profile Card View:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-view2.png' alt="Build view"/>

- Profile List View:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-view1.png' alt="Build view alternate"/>

## Profile Configuration

Configuring a build profile has some basic steps that need to be completed before starting a build.

### Creating a configuration

You may create **Distribution** configuration to send your app to public stores or create **Testing** configuration to send your app to testers. Configurations allow you to set different certificates, distribution channels that can be used with different workflows.

- Click on **Configurations** to create configurations for different scenarios.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config1.png' alt="Build Config Creation"/>

- Click on **New** button to create your first configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config2.png' alt="Build Config New" />

- You may change the name of the configuration or delete the ones you don't need. To do that, click on the edit button shown and three dot on the configuration you want to edit/delete.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config5.png' alt="Build config edit" />

### Clone Configuration

If you have a configuration that you use constantly or want to quickly copy a configuration, you can use the "Configuration Clone" feature.

The configuration clone feature will speed up your projects where you use many configurations.

First of all, we open the configuration process by clicking the edit button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config5.png' alt="Build config edit" />

Then click on the three dots next to the configuration we want to copy, and click on the "Clone" button in the mini window that opens.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config3.png' alt="build config clone" />

And another one is created identical to the configuration we want to clone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config4.png' alt="created build config clone" />

:::info
The naming here is created by adding "\_copy_1" to the end of the main configuration name. For each configuration to be copied from now on, the name will be incremented to be unique.
:::

:::tip
Although the system gives a unique name for the copied configuration by default, you can give this configuration a new name using "Rename".
:::

### Download Configuration

You can download your **Configuration** in YAML format to perform actions like sharing the settings you've configured or creating a duplicate on another **Build Profile** page. Follow these steps to download your **Configuration**:

- Open the **Configuration** you've created.
- Locate the download button positioned at the bottom left of the Configuration interface. Click on the download button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-download.png' alt="Download Configuration" />

Your _configuration.yaml_ file will be downloaded to your local system.

:::tip
If you intend to copy the configuration to use on the same **Build Profile** page, consider using the [**Clone Configuration**](#clone-configuration) step as a quicker alternative.
:::

### Project details configuration

Every build profile needs to know project details regardless of the project being iOS or Android project. Project details can be entered manually or can be fetched from your project automatically by Appcircle if you click on **Autofill** button.

You can also select your self-hosted runner from the **SELECT A POOL** dropdown.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner">
  Self-hosted Runners
</ContentRef>

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-pool.png' alt="Pool Selection" />

#### Build Priority

The build priority configuration feature includes three levels: Low, Medium, and High.

These priority levels influence the starting order of queued builds, ensuring that higher-priority builds are initiated first.

For instance, if a high-priority build is added to the queue after a low-priority build, the high-priority build will commence before the low-priority one.

This functionality allows for better management of build processes, enabling teams to prioritize critical updates and enhancements efficiently.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-priority.png' alt="Build Priority" />

:::info
This feature is only available for organizations with Enterprise license.
:::

### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from Apple Developer account and uploaded to Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-ios-signing-configuration.png' />

You can either upload your iOS certificate and iOS provisioning profile or Android Keystore from here or within the [Signing Identities](/signing-identities) module.

### Distribution configuration

Distribution is a critical step when it comes to testing your app on real devices. You may need multiple testers and testing groups to download, install, test your app, and make sure it works on different devices and operating system versions.

Distribution configuration allows you to set which testing groups will receive your application after the build is complete. You can manually submit your binary to testers, or Appcircle can do it for you.

In this window, you can select one or more of the previously created distribution profiles or create a new one. You can use the "Manage Distribution Profiles" button above to quickly manage distribution profiles.

Finally, check "Automatically Distribute to Testers" if you want your build to be automatically distributed to the selected testers or testing groups.

<Screenshot url='https://cdn.appcircle.io/docs/assets/multiple-dist-build-1.png' />

You can also use other toggles on there to automatically distribute your app to the Enterprise App Store or Store Submit modules.

#### Send to Enterprise App Store

- Navigate to the configuration, then go to the Distribution tab, and ensure that **Automatically Distribute to Enterprise App Store** is enabled.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-build.png' />

- Whenever a new **signed** build is created, it will be sent to the Enterprise App Store.
- APK or IPA files can also be manually sent by clicking the **...** button and selecting Distribute Binary.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-binary.png' />

### Versioning configuration

You can set custom rules to manage the versioning of your app. You can increase both the build number and version number according to the rules you set.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-versioning.png' />

### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-env-variables.png' />

For more information regarding creating environment variables for build profiles, please refer to the related [documentation](/build/build-environment-variables).

## Workflows configuration

A workflow is a ladder of steps taken to build your applications.

Each step has a different purpose and the workflow can be customized by modifying step parameters and inputs, running custom scripts, or re-ordering steps.

Workflows allow you to have complete control on your build process and enhance it with third-party services and features.

:::caution

Please note that modifying workflow steps may cause your builds to fail, so utmost care is recommended when editing workflows.

:::

### Setting Up Workflows

To access the workflow editor for a build profile, click the Workflows button in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-workflow1.png' alt="workflow overview"/>

The workflow list will be displayed. To view the [Workflow Steps](#workflow-steps) of a workflow, click on it from the workflow list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-workflow2.png' />

To create a new workflow, press the "New" button at the top of the workflow list and select a template from the default workflows. Then edit the workflow name and press enter. You can also upload your workflow as a YAML file.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5278-workflow3.png" />

To rename/delete a current workflow, press the "Edit" button at the top of the workflow list and then click on the context menu that appears next to the workflow items.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-workflow4.png' />

You can use the "Clone" option to create a new workflow based on the currently available ones. You can [select different workflows for different build scenarios](/build/build-process-management/build-manually-or-with-triggers) (e.g. separate workflows for production and development).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-workflow5.png' />

### Workflow Steps

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE5278-workflow6.png" />

Appcircle will build your application with the steps defined in the workflow. Steps will be executed in order from the top to the bottom.

You can customize each step for specific configurations with your application structure. Step parameters can be modified, outputs of each step can be used in another step and step versions can be selected accordingly.

### Workflow Marketplace

Appcircle's powerful Workflow Editor has a built-in Workflow Marketplace that allows you to select and insert an unlimited amount of steps to your workflow.

You can find the full list of available workflow steps in our workflow marketplace at:;

[https://www.appcircle.io/integrations/](https://www.appcircle.io/integrations/)

You can add platform-specific workflow steps, custom scripts, and other steps into your workflow and re-order them as you like. You can also remove the steps you don't need. You can backup your current workflow by clicking the **Download YAML** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-workflow7.png' />

To access the Workflow Marketplace, click on the **Manage Workflow** button. You will see the Workflow Marketplace on the right and your Workflow steps on the left.

You can now drag and drop steps into your workflow. Any unwanted workflow steps can be removed by clicking on the delete button on the right side of each step.

You can also reorder steps so that they will be executed in the order you specify.

<Screenshot url='https://cdn.appcircle.io/docs/assets/08-08-WF_Reorder.gif' />

### Editing Workflow Settings

Each workflow step has its own set of configuration options, which can be set by clicking on the step in the workflow screen.

The first three items are common for all steps and they are set individually for each step:

- **Step Execution Active:** To enable/disable the step execution without removing it from the workflow

- **Continue with the next step even if this step fails:** If a step is optional or its result should not cause a build error, you can select this option to continue the workflow if this particular step fails. In default workflows, this option is `on` for specific steps. And since this step is active, the build status will appear as "Warning" when other steps in the build are successful. Detailed explanation about this state is given in the [Build Warning Status](#build-warning-status) section.

- **Workflow Step Version:** You can select a specific version of a step with which to execute your build. If you select a version with an asterisk (\*), you will receive the minor updates to the workflow step automatically. The major versions may include added or removed input fields and manual version selection is required for major version updates.;

The items in the "Inputs" section are specific to that step. The reserved environment variables are assigned to these fields by default and the values of these variables are set in the build configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (187).png' />

#### Build Warning Status

When we start a build, if we have activated the "Continue with the next step even if this step fails" setting for a component we use in the workflow and this step fails during the build, Appcircle will show the build status as "Warning" if the build is completed successfully for other steps.

In order to simulate the warning state and see its results on the pipeline, we can basically write a script that will fail in Custom Script.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-1.png' />

"Continue with the next step even if this step fails" must be `on` in this case.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-2.png' />

We are starting a build, and we see that it fails in the pipeline.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-3.png' />

And the build status will now appear as "Warning".

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-4.png' />

## Triggers configuration

To set up or manage the build triggers, click the Triggers button in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-trigger.png' />

The triggers are set up at the profile level and you can specify individual branch names or [utilize wildcards](/build/build-process-management/build-manually-or-with-triggers#wildcard-reference) for branch names to trigger builds.

You also need to select a workflow for each trigger and the build will be run with that trigger for the specified branch. You can build the same branch with different workflows (e.g. production or development) or you can use the same workflow for multiple branches (e.g. multiple feature branches built with the develop workflow).

For further information regarding triggers, please refer to the [Manual and Automatic Builds](/build/build-process-management/build-manually-or-with-triggers) documentation.

## Starting a Build

To initiate a build in Appcircle, follow these steps:

- Click on the Start Build button to begin the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start1.png' />

- Appcircle will prompt you to choose a configuration and workflow settings from the saved configurations. Select the appropriate settings that match your project requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start2.png' />

- Once the configurations are selected, click the Start button to start the build.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start3.png' />

- Users can monitor the progress, results, and logs of the workflow steps in real-time via the interface.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start4.png' />

- After the build is complete, you have the option to download the build logs for reference or troubleshooting purposes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start5.png' />

- Upon completion, the binary along with the artifacts will be displayed on the selected branch. These can be accessed for deployment or further use.

By following these steps, you can efficiently manage and monitor your builds in Appcircle.

For more detailed information on builds with different type of projects, please refer to the [Platform Build Guides](/build/platform-build-guides) documentation.

### Build Statuses

- **Success**: The build has finished successfully with no failures in the workflow steps.
- **Failed**: The build has failed due to one or more workflow steps failing.
- **Warning**: The build has finished with a failed workflow step that does not affect the final outcome.
- **Timeout**: The build exceeded the timeout limit and ended prematurely.
- **Canceled**: The build was canceled by the user.

## Binary Actions

With Appcircle's post-build actions, you can easily distribute your binary file manually, access artifacts and examine build logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-action.png' />

### Distribute Binary

The Distribute Binary feature sends the binary file to the relevant module based on the Distribution settings in the selected configuration.

:::caution

Please note that AAB files will not be distributed automatically since they cannot be installed on mobile devices directly.

:::

### View Build Logs

This feature allows the relevant build logs to be reviewed in the Appcircle log window. The logs can be examined step by step separately.

### Download Artifacts

Each time a build is completed by Appcircle, all artifacts produced after the build are stored for easy access. These files, which include artifacts such as IPA, APK, and AAB binary files, log files, and archive files, can be accessed by selecting Download Artifacts.

:::caution Output Artifacts

### For Android

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. On our [**testing portal**](/testing-distribution/testing-portal), your testers will be able to download each `.apk` file separately and test it on their devices.

### For iOS

iOS applications can be downloaded or distributed as IPA file format if you configure signing identities and sign the application during the build process.

If you disable signing or don't use any signing identities, iOS output will be an `.xarchive` file.

:::

### Download Build Logs

In addition to allowing the review of logs, Appcircle also permits the downloading of these logs in .txt file format, enabling the logs to be downloaded and used in a single file.

### Working with build logs

Build logs help you to observe and understand exactly what happened during a build. You can see build logs as they happen while a build is in process or you can view logs of a build after the build is completed.

:::info

In the build logs, the **Builds/Statuses** column is sorted by the latest completion build date. As a result, the start dates displayed in the list might not be in chronological order:

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-working-with-build-logs.png' />

:::

You can use build logs to debug your builds in case you get any errors. Additional parameters and flags can also be used in workflow steps to see more details in build logs.

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

You can also download build logs in plain text format in case you would like to investigate them on your own or share with your team.

### Delete Specific Builds

If you want to free up space from your Artifact Storage, you can delete older build profiles which are cluttering your space.

To do that, simply navigate to the Builds tab and select the builds, then click on the Delete icon

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-delete-specific.png' />

:::tip

Build Deletion feature is only available at Pro or above plans.

To get more info, see our Pricing: [https://appcircle.io/pricing/](https://appcircle.io/pricing/)

:::

## Connection Settings

After connecting build profile to a Git provider, we can see the **"Connection Settings"** button in the build profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-1.png' />

You can click on the "Connection Settings" button under the build profile name and URL to see the detailed information about the connection. (PAT, oAuth)

### OAuth

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-2.png' />

### Personal Access Token (PAT)

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-3.png' />

:::caution
If you added your repository via **multiple instances** using PAT (Personal Access Token), the "Connection Settings" will look different.

You can review the [**Connecting Multiple Instances**](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance#connection-settings-for-multiple-instances) page for using "Connection Settings" on multiple instances.
:::


## FAQ

### Artifact Storage is Full

Older builds and/or testing distributions will use almost all of your storage. If your artifact storage is full, you can free up some of the old artifacts.

#### [Refer here to delete a build profile](/build/manage-the-connections/adding-a-build-profile#delete-a-build-profile)

#### [Refer here to delete specific builds from your build profile](/build/build-process-management#delete-specific-builds)

#### [Refer here to delete testing distribution profiles and specific distribution artifacts](/testing-distribution/create-or-select-a-distribution-profile#delete-a-distribution-profile)

#### [Refer here to delete a Publish Profile](/publish-module/creating-publish-profiles/managing-publish-profiles#delete-publish-profile)

In order for storage to be freed up, you should also remove the other references pointing to the artifact. In example, if you have built an app, distributed it to testers, and submitted it to the Store Submit, you should delete that build from Testing Distribution, Store Submit, and Builds respectively.

:::caution

It may take a couple of minutes to see the change in your account after you have deleted some artifacts.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />