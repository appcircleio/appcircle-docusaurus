---
title: Profile Creation
description: Learn how to create Build Profiles on Appcircle
tags: [build, build profile]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

A Build profile can be created by following these steps:

## Creating a Profile

A Build profile can be created by following these steps:

Click on the **Add New** button located at the middle of the screen. If you already have an existing profile displayed on the build profile list, this button will be at the top right corner.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build1.png' alt="Build Profile Creation" />

Provide a unique name for the build profile and choose a target Operating System (OS) which can be Android or iOS.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build2.png' alt="Build Profile Naming" />

After selecting the target OS, specify the corresponding target platform to set up a compatible build environment:

iOS Platforms:
* [Objective-C / Swift](/build/platform-build-guides/building-ios-applications)
* [React Native](/build/platform-build-guides/building-react-native-applications)
* [Flutter](/build/platform-build-guides/building-flutter-applications)

Android Platforms:
* [Java / Kotlin](/build/platform-build-guides/building-android-applications)
* [React Native](/build/platform-build-guides/building-react-native-applications)
* [Flutter](/build/platform-build-guides/building-flutter-applications)

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

<Tabs
defaultValue="card"
values={[
{ label: 'Profile Card View', value: 'card' },
{ label: 'Profile List View', value: 'list' },
]}
>
  <TabItem value="card">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-view2.png' alt="Build view" />
  </TabItem>
  <TabItem value="list">
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-view1.png' alt="Build view alternate" />
  </TabItem>
</Tabs>

## Connection Settings

After connecting build profile to a Git provider, we can see the **"Connection Settings"** button in the build profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-connection1.png' />

You can click on the "Connection Settings" button under the build profile name and URL to see the detailed information about the connection. (PAT, oAuth)

### OAuth

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-connection2.png' />

### Personal Access Token (PAT)

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-3.png' />

:::caution
If you added your repository via **multiple instances** using PAT (Personal Access Token), the "Connection Settings" will look different.

You can review the [**Connecting Multiple Instances**](/build/manage-the-connections/adding-a-build-profile/connecting-multiple-instance#connection-settings-for-multiple-instances) page for using "Connection Settings" on multiple instances.
:::