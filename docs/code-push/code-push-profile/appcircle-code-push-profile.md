---
title: CodePush Profile Management
description: Learn how to create Appcircle CodePush profile
tags: [appcircle codepush, profile, codepush]
sidebar_position: 1
---

# Apcircle CodePush Profile

This section explains how to create and manage a CodePush profile in Appcircle to enable over-the-air (OTA) updates for your React Native projects. A properly configured profile allows you to connect your CodePush deployments with your Appcircle workflows, manage versioning, and control release behaviors through a user-friendly interface. Follow the steps below to get started.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-codePushEmptyState.png' />

## Creating CodePush Profile

To use CodePush in your project, you must first create a CodePush profile in Appcircle, which links your application to the update delivery system. In Appcircle, click the `Add New` button to create a new CodePush profile and assign a name to it.

:::info CodePush Profile Name

The name you assign to your profile will be used as the `App Name` for your over-the-air updates.

:::

:::caution CodePush Profiles

To ensure better manageability of your updates, we recommend creating two separate profiles for iOS and Android platforms. For example: `MyApp-iOS` and `MyApp-Android`.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-codePushAddNew.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-profileCard.png' />

## Profile Actions

By clicking the three dots on the profile card, you can:

- Rename the profile
- Pin the profile
- Delete the existing profile

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-profileActions.png' />

:::caution Changing Profile Name

Remember, the name given to the profile is used as the **App Name** parameter during the CodePush update process. If you change the profile name, you must also **update** this parameter when delivering updates.

:::


## Profile Management

This section provides an overview of how to manage your existing CodePush profiles in Appcircle.

### Deployment Channels

Deployment channels allow you to categorize and manage your CodePush releases, enabling different update strategies such as `Staging` and `Production` deployments.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-deploymentChannels.png' />

### Adding new Deployment Channel

- To add a new deployment channel, click on the `+` button 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-addNewDeploy.png' />

- Provide a unique channel name in the opened modal, and save your configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-channelName.png' />
