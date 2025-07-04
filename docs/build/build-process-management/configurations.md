---
title: Configurations
description: Learn how to create and manage Build Profile configurations on Appcircle
tags: [build, build profile, configuration]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Build Configuration

Configuring a build profile requires completing some basic steps before starting a build.

### Creating a configuration

You may create a configuration profile that allows you to set different certificates and distribution channels that can be used with different workflows.

- Click on **Configurations** to create configurations for different scenarios.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config1.png' alt="Build Config Creation"/>

- Click on the **New** button to create your first configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config2.png' alt="Build Config New" />

You can also create a configuration profile by uploading a saved YAML file.

- You may change the name of the configuration or delete the ones you don't need. To do that, click on the edit button shown and the three dots on the configuration you want to edit/delete.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config5.png' alt="Build config edit" />

If you have a configuration that you use constantly or want to quickly copy a configuration, you can use the "Configuration Clone" feature.

The configuration clone feature will speed up your projects where you use many configurations.

First, open the configuration process by clicking the edit button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config5.png' alt="Build config edit" />

Then click on the three dots next to the configuration you want to copy and click the "Clone" button in the mini window that opens.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config3.png' alt="build config clone" />

Another one is created identical to the configuration you want to clone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-config4.png' alt="created build config clone" />

:::info
The name here is created by adding "\_copy_1" to the end of the main configuration name. For each configuration copied from now on, the name will be incremented to remain unique.
:::

:::tip
Although the system gives a unique name for the copied configuration by default, you can give this configuration a new name using "Rename".
:::

You can download your **Configuration** in YAML format to perform actions like sharing the settings you've configured or creating a duplicate on another **Build Profile** page. Follow these steps to download your **Configuration**:

- Open the **Configuration** you've created.
- Locate the download button positioned at the bottom left of the Configuration interface. Click on the download button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-download.png' alt="Download Configuration" />

Your _configuration.yaml_ file will be downloaded to your local system.

:::tip
If you intend to copy the configuration to use on the same **Build Profile** page, consider using the **Clone Configuration** step as a quicker alternative.
:::

:::caution
The downloaded YAML file is specific to the project type and can only be used for configuring the same type of project. For example, a YAML file generated for an iOS Swift project cannot be applied to an Android React Native project. Ensure that you use the correct YAML file for seamless configuration.
:::

### Config Details

Every build profile needs to know project details regardless of whether the project is an iOS or Android project. Project details can be entered manually or can be fetched from your project automatically by Appcircle if you click on **Autofill** button.

You can also select your self-hosted runner from the **SELECT A POOL** dropdown.

<ContentRef url="/self-hosted-appcircle/self-hosted-runner">
  Self-hosted Runners
</ContentRef>

<Tabs
defaultValue="ios"
values={[
{ label: 'iOS', value: 'ios' },
{ label: 'Android', value: 'android' },
]}
>
  <TabItem value="ios">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-pool.png' alt="Pool Selection" />
  </TabItem>
  <TabItem value="android">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-androidconfig.png' />
  </TabItem>
</Tabs>

#### Build Priority

The build priority configuration feature has three levels: Low, Medium, and High.

These priority levels determine the order in which queued builds start, ensuring that higher-priority builds are initiated first.

For example, if a high-priority build is added to the queue after a low-priority build, the high-priority build will start before the low-priority one.

This feature allows for better management of build processes, enabling teams to prioritize critical updates and improvements efficiently.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4818-priority.png' alt="Build Priority" />

:::info
This feature is only available for organizations with Enterprise license.
:::

#### ACRP - Auto Cancel Redundant Pipeline

When enabled, this feature automatically cancels any previously running build that matches the same configuration, workflow, branch, and trigger type, if a new run is triggered.
This helps prevent unnecessary resource usage and reduces queue time by skipping outdated pipeline runs.

For further details, see [Auto Cancel Redundant Pipeline](/build/build-process-management/build-manually-or-with-triggers).

### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle, or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from the Apple Developer account and uploaded to Appcircle.

<Tabs
defaultValue="ios"
values={[
{ label: 'iOS', value: 'ios' },
{ label: 'Android', value: 'android' },
]}
>
  <TabItem value="ios">
<Screenshot url='https://cdn.appcircle.io/docs/assets/build-profile-ios-signing-configuration.png' />
  </TabItem>
  <TabItem value="android">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-androidsign.png' />
  </TabItem>
</Tabs>

:::info
Please note that the [Automatic Code Signing](/signing-identities/apple-profiles#automatic-signing) option is only available for iOS projects.
:::

You can either upload your iOS [certificate](/signing-identities/apple-certificates) and iOS [provisioning profile](/signing-identities/apple-profiles) or [Android Keystore](/signing-identities/android-keystores) from here or within the [Signing Identities](/signing-identities) module.

### Distribution configuration

Set up automated distribution for your builds by configuring distribution settings in Appcircle. This feature allows you to automatically send completed builds to selected modules, including Testing Distribution, Publish, or the Enterprise Store, ensuring a seamless deployment process.

Simply enable the toggle of the module that you need and select the required profiles.

#### Send to Testing Distribution

Distribution configuration allows you to set which testing groups will receive your application after the build is complete. You can manually submit your binary to [Testing Distribution](/testing-distribution) profiles, or Appcircle can do it for you.

In this window, you can select one or more of the previously created distribution profiles. You can use the "Manage Distribution Profiles" button above to quickly manage distribution profiles.

Finally, check "Automatically Distribute to Testers" if you want your build to be automatically distributed to the selected testers or testing groups.

:::caution Binary comes from Build Module

If the `Bundle/Package` validation option is turned on in the **Testing Distribution** profile you want to automatic distribution and the bundle or package of the binary to be submitted does not match the one specified in this profile, you will get an error during submission. Appcircle does not prevent the profile from being selected. Please make sure that the bundle/package identifier of the binary you want to submit matches the one in the **Testing Distribution** profile.

For more detailed information about identifier validation, please visit the **Bundle/Package validation** [documentation](/testing-distribution/create-or-select-a-distribution-profile#bundlepackage-identifier-validation).

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/multiple-dist-build-1.png' />

#### Send to Publish

Enabling "Automatically Distribute to Publish" will display the available [Publish](/publish-module) profiles for distribution.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-publish.png' />

Simply select your relevant publish profiles, and Appcircle will automatically send your builds to the selected publish profiles.

Please note that the publish profiles should be created within the publish module prior to configuring the distribution settings in the build profile.

#### Send to Enterprise App Store

- Navigate to the configuration, then go to the Distribution tab, and ensure that **Automatically Distribute to Enterprise App Store** is enabled.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-build.png' />

- Whenever a new **signed** build is created, it will be sent to the [Enterprise App Store](/enterprise-app-store).

:::info
If you are building a binary for the first time or distributing it to the Enterprise App Store for the first time, a new Enterprise App Store profile will be created automatically. If there is an existing Enterprise App Store profile for your build, it will be directed to the existing profile.
:::

### Versioning configuration

You can set custom rules to manage the versioning of your app. You can increase both the build number and version number according to the rules you set.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-versioning.png' />

For more information please refer to the [Versioning](/versioning) documentation.

### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-configuration-env-variables.png' />

For more information regarding creating environment variables for build profiles, please refer to the related [Environment Variables](/build/build-environment-variables) documentation.