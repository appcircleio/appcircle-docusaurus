---
title: Build Profile Configuration Overview
metaTitle: Build Profile Configuration Overview
metaDescription: Build Profile Configuration Overview
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Build Profile Configuration Overview

Configuring a build profile has some basic steps that need to be completed before starting a build.

### Creating a configuration

You may create **Distribution** configuration to send your app to public stores or create **Testing** configuration to send your app to testers. Configurations allow you to set different certificates, distribution channels that can be used with different workflows.

- Click on **Configurations** to create configurations for different scenarios. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (168).png' />

- Click on **New** button to create your first configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/create-build-configuration1.png' />

- You may change the name of the configuration or delete the ones you don't need.

<Screenshot url='https://cdn.appcircle.io/docs/assets/create-build-configuration2.png' />

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
The naming here is created by adding "_copy_1" to the end of the main configuration name. For each configuration to be copied from now on, the name will be incremented to be unique.
:::

:::tip
Although the system gives a unique name for the copied configuration by default, you can give this configuration a new name using "Rename".
:::

### Project details configuration

Every build profile needs to know project details regardless of the project being iOS or Android project. Project details can be entered manually or can be fetched from your project automatically by Appcircle if you click on **Autofill** button.

You can also select your self-hosted runner from the **SELECT A POOL** dropdown.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner">
  Self-hosted Runners
</ContentRef>

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-fetch.png' />

### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from Apple Developer account and uploaded to Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (170).png' />

### Distribution configuration

Distribution is a critical step when it comes to testing your app on real devices. You may need multiple testers and testing groups to download, install, test your app, and make sure it works on different devices and operating system versions.

Distribution configuration allows you to set which testing groups will receive your application after the build is complete. You can manually submit your binary to testers, or Appcircle can do it for you.

In this window, you can select one or more of the previously created distribution profiles or create a new one. You can use the "Manage Distribution Profiles" button above to quickly manage distribution profiles.

Finally, check "Automatically Distribute to Testers" if you want your build to be automatically distributed to the selected testers or testing groups.

<Screenshot url='https://cdn.appcircle.io/docs/assets/multiple-dist-build-1.png' />

You can also use other toggles on there to automatically distribute your app to the Enterprise App Store or Store Submit modules.

### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (172).png' />

### Versioning configuration

You can set custom rules to manage the versioning of your app. You can increase both the build number and version number according to the rules you set.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (173).png' />

### Workflows and Triggers

For advanced configuration, you can utilize [workflows](../workflows/why-to-use-workflows.md) and for automatic builds, you can utilize [triggers](build-manually-or-with-triggers.md#automatic-build).

These options are available at the profile level in the profile context menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (188).png' />

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
