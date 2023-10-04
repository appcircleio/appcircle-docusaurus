---
title: Build Profile Configuration Overview
metaTitle: Build Profile Configuration Overview
metaDescription: Build Profile Configuration Overview
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';

# Build Profile Configuration Overview

Configuring a build profile has some basic steps that need to be completed before starting a build.

### Creating a configuration

You may create **Distribution** configuration to send your app to public stores or create **Testing** configuration to send your app to testers. Configurations allow you to set different certificates, distribution channels that can be used with different workflows.

- Click on **Configurations** to create configurations for different scenarios. 

![](<https://cdn.appcircle.io/docs/assets/image (168).png>)

- Click on **New** button to create your first configuration.

![](<https://cdn.appcircle.io/docs/assets/create-build-configuration1.png>)

- You may change the name of the configuration or delete the ones you don't need.

![](<https://cdn.appcircle.io/docs/assets/create-build-configuration2.png>)

### Clone Configuration

If you have a configuration that you use constantly or want to quickly copy a configuration, you can use the "Configuration Clone" feature.

The configuration clone feature will speed up your projects where you use many configurations.

First of all, we open the configuration process by clicking the edit button.

![](<https://cdn.appcircle.io/docs/assets/clone-1.png>)

Then click on the three dots next to the configuration we want to copy, and click on the "Clone" button in the mini window that opens.

![](<https://cdn.appcircle.io/docs/assets/clone-2.png>)

And another one is created identical to the configuration we want to clone. 

![](<https://cdn.appcircle.io/docs/assets/clone-3.png>)

:::info
The naming here is created by adding "_copy_1" to the end of the main configuration name. For each configuration to be copied from now on, the name will be incremented to be unique.
:::

:::tip
Although the system gives a unique name for the copied configuration by default, you can give this configuration a new name using "Rename".
:::

### Project details configuration

Every build profile needs to know project details regardless of the project being iOS or Android project. Project details can be entered manually or can be fetched from your project automatically by Appcircle if you click on **Autofill** button.

You can also select your self-hosted runner from the **SELECT A POOL** dropdown.


<ContentRef url="/self-hosted-runner/overview">
  Self-Hosted Runners
</ContentRef>

![](<https://cdn.appcircle.io/docs/assets/ios-fetch.png>)

### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from Apple Developer account and uploaded to Appcircle.

![](<https://cdn.appcircle.io/docs/assets/image (170).png>)

### Distribution configuration

Distribution is a critical step when it comes to test your application on real devices. You may need multiple testers and test groups to download, install and test your application and make sure it works on different devices and operating system versions.

Distribution configuration allows you to set up which testing groups will receive your application after the build is complete. You can manually send your binary file to testers or Appcircle can do this for you.

You can select a previously created distribution profile or create a new one on this window. Use the top input box to enter a name for the new distribution profile you want to create. Press enter or click on the green + icon on the right to create the distribution profile.

Finally, check Auto Distribute if you want your build to be deployed to the Testing Distribution automatically and Auto Deployment if you want the build to be deployed to Store Submission automatically.

![](<https://cdn.appcircle.io/docs/assets/image (171).png>)

### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

![](<https://cdn.appcircle.io/docs/assets/image (172).png>)

### Versioning configuration

You can set custom rules to manage the versioning of your app. You can increase both the build number and version number according to the rules you set.

![](<https://cdn.appcircle.io/docs/assets/image (173).png>)

### Workflows and Triggers

For advanced configuration, you can utilize [workflows](../workflows/why-to-use-workflows.md) and for automatic builds, you can utilize [triggers](build-manually-or-with-triggers.md#automatic-build).

These options are available at the profile level in the profile context menu.

![](<https://cdn.appcircle.io/docs/assets/image (188).png>)

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
