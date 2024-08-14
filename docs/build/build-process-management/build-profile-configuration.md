---
title: Profile Configuration
description: Configuring a build profile has some basic steps that need to be completed before starting a build.
tags: [build profile, configuration, build configuration, build profile configuration]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Build Profile Configuration Overview

Configuring a build profile has some basic steps that need to be completed before starting a build.

### Creating a configuration

You may create **Distribution** configuration to send your app to public stores or create **Testing** configuration to send your app to testers. Configurations allow you to set different certificates, distribution channels that can be used with different workflows.

- Click on **Configurations** to create configurations for different scenarios.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-configuration-showcase.png' />

- Click on **New** button to create your first configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-another-configuration.png' />

- You may change the name of the configuration or delete the ones you don't need. To do that, click on the edit button shown and three dot on the configuration you want to edit/delete.

<Screenshot url='https://cdn.appcircle.io/docs/assets/clone-1.png' />

### Clone Configuration

If you have a configuration that you use constantly or want to quickly copy a configuration, you can use the "Configuration Clone" feature.

The configuration clone feature will speed up your projects where you use many configurations.

First of all, we open the configuration process by clicking the edit button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/clone-1.png' />

Then click on the three dots next to the configuration we want to copy, and click on the "Clone" button in the mini window that opens.

<Screenshot url='https://cdn.appcircle.io/docs/assets/clone-2.png' />

And another one is created identical to the configuration we want to clone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/clone-3.png' />

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
  <Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-download-component.png' />

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

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-ios-fetch.png' />

### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from Apple Developer account and uploaded to Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-ios-signing-configuration.png' />

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

### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-env-variables.png' />

### Versioning configuration

You can set custom rules to manage the versioning of your app. You can increase both the build number and version number according to the rules you set.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-versioning.png' />

### Workflows and Triggers

For advanced configuration, you can utilize [workflows](/workflows) and for automatic builds, you can utilize [triggers](build-manually-or-with-triggers#automatic-build).

These options are available at the profile level in the profile context menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-workflow-trigger-showcase.png' />

### Connection Settings

After connecting build profile to a Git provider, we can see the **"Connection Settings"** button in the build profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-1.png' />

You can click on the "Connection Settings" button under the build profile name and URL to see the detailed information about the connection. (PAT, oAuth)

#### OAuth

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-2.png' />

#### Personal Access Token (PAT)

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-3.png' />

:::caution
If you added your repository via **multiple instances** using PAT (Personal Access Token), the "Connection Settings" will look different.

You can review the [**Connecting Multiple Instances**](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance#connection-settings-for-multiple-instances) page for using "Connection Settings" on multiple instances.
:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
