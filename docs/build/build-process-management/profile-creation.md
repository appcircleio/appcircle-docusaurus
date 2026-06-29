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

Click on the **Add New** button located in the middle of the screen. If you already have an existing profile displayed on the build profile list, this button will be in the top right corner.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build1.png' alt="Build Profile Creation" />

Provide a unique name for the build profile and choose a target operating system (OS), which can be Android or iOS.

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

* [GitHub](/build/manage-the-connections/connection-guides/connecting-to-github)
* [Azure](/build/manage-the-connections/connection-guides/connecting-to-azure)
* [Bitbucket](/build/manage-the-connections/connection-guides/connecting-to-bitbucket)
* [GitLab](/build/manage-the-connections/connection-guides/connecting-to-gitlab)
* [Connect via SSH](/build/manage-the-connections/connection-guides/connecting-to-private-repository-via-ssh)
* Connect via URL
* [Connecting to Multiple Instances](/build/manage-the-connections/connection-guides/connecting-multiple-instance)

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build3.png' alt="Repository connection" />

:::info
If you have not previously connected to a Git provider on Appcircle, i.e., created a profile but have not connected a repository, you will not see any connection on this page.

For more information on creating repository connections, please refer to the [connections](/build/manage-the-connections) guide.
:::

To test drive Appcircle, you can find various sample projects on the [Appcircle GitHub page](https://github.com/appcircleio?q=sample) or you can just press the **Quick Start Using the Sample Repository** button to populate the repository with a compatible project based on the selected framework.

For detailed instructions on connecting to each repository, refer to the [Connection Guides](/build/manage-the-connections/connection-guides).

Once the repository connection is established, the build profile will be created successfully. Appcircle will then pull your branches, commits, and other information from your repository. You can now use the build profile to manage and deploy your projects.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-build4.png' alt="Build Profile"/>

### Profile Listing

You can switch between **Board View** and **List View** using the view selector located at the top right of the page. Both views display the same build profiles, allowing you to choose the layout that best fits their workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build2.png' />

<Tabs
defaultValue="board"
values={[
{ label: 'Profile Board View', value: 'board' },
{ label: 'Profile List View', value: 'list' },
]}
>
  <TabItem value="board">
<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build6.png' />
  </TabItem>
  <TabItem value="list">
<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build5.png' />  </TabItem>
</Tabs>

In addition to view options, the profile list provides search, filtering, and ordering capabilities to help users quickly locate specific build profiles.

#### Search Profiles

Click the **Search** icon in the top right corner to open the profile search dialog. You can search for build profiles by name and quickly navigate to the desired profile from the search results. It will also bring your recent search results.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build4.png' />

:::info
The search feature looks for matches in both Build Profile names and the associated full repository URLs. Any profile matching the entered keyword in either field will appear in the search results.
:::

#### Filter Profiles

Use the **Filter** button to narrow down the profile list based on available criteria. Profiles can be filtered by:

- Platform
- Last Build Status
- Repository Source

Applied filters are displayed at the top of the page and can be removed individually when no longer needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build1.png' />

#### Sort and Order Profiles

The profile list can also be organized using the available ordering options. Users can change the sorting direction and select different ordering criteria, such as **Last Build Date**, to customize how profiles are displayed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA45-build5.png' />

## Connection Settings

After connecting a build profile to a Git provider, we can see the **"Connection Settings"** button in the build profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-connection1.png' />

You can click on the "Connection Settings" button under the build profile name and URL to see detailed information about the connection. (PAT, OAuth)

### OAuth

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-connection2.png' />

### Personal Access Token (PAT)

<Screenshot url='https://cdn.appcircle.io/docs/assets/connection-settings-main-3.png' />

:::caution
If you added your repository via **multiple instances** using PAT (Personal Access Token), the "Connection Settings" will look different.

You can review the [**Connecting Multiple Instances**](/build/manage-the-connections/connection-guides/connecting-multiple-instance#connection-settings-for-multiple-instances) page to learn how to use "Connection Settings" for multiple instances.
:::