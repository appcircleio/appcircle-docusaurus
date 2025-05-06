---
title: CodePush Release Management
description: Learn how to create Appcircle CodePush profile
tags: [appcircle codepush, profile, codepush]
sidebar_position: 3
---

# CodePush Release Management

This section describes how to manage and distribute CodePush updates through Appcircle, covering versioning, release strategies, and common practices for efficient update delivery.


## Deployment Keys

Deployment keys are used to link your deployment channels with the CodePush SDK, ensuring that updates are delivered to the correct target environment. For each newly created deployment channel, Appcircle will automatically generate a unique deployment key.

//deployment key ss

## Upload New Release

With the Appcircle CodePush **Upload New Release** feature, you can manually release a bundle file that you have generated in your local environment.

// upload new release ss

To use this feature, you need to upload the bundle file you created as a `.zip` archive. Below you can find a detailed explanation of the required inputs for the Upload Release feature.

//upload new release detail ss

- **App Version:** This field specifies which app version the update is targeted for. Make sure it matches the version defined in your project settings.
- **Release Note:** A description of the changes or improvements included in this release. This helps users and team members understand what the update contains.
- **Mandatory Update:** If enabled, users will be forced to install the update immediately upon launch.
- **Disable:** Disables the current release, making it unavailable to users even if it was previously deployed.
- **Rollout Percentage:** Defines what percentage of users will receive the update initially, allowing for gradual rollout and safer deployments.

## Managing Versions

The version management section allows you to view, compare previous CodePush releases for better control and organization of your update history. All fiels are being explained below in version list.

//version listesi ss

- **Release Version:** Indicates the version of the CodePush update you have uploaded.
- **Target Version:** Shows which app version this release is intended to run on.
- **Status:** Displays the current status of the release (e.g., Enabled, Disabled).
- **Mandatory:** Specifies whether the update is mandatory for users or optional.
- **Active Devices:** The number of devices currently running this release version.
- **Rollout%:** The percentage of users to whom the release has been deployed.
- **Date:** The timestamp of when the release was uploaded.


## Version Actions

In this section, you can perform actions such as details, disabling, or enabling a specific CodePush version to manage your release lifecycle more effectively.

//action list ss

### Version Details
This option allows you to view the all informations and configuration details of a specific CodePush release.

### Promote
Use this action to promote a release from one deployment channel to another, such as from Staging to Production.

### Rollback
This action reverts your app to the previous stable CodePush version in case of issues with the latest update. It also allows you to rollback to any specific version if desired.

### Settings
Allows you to modify release configurations such as rollout percentage or mark the release as mandatory.

- **Description:** A brief note summarizing what this specific version includes. Useful for internal tracking and user communication.
- **Mandatory:** Indicates whether this version must be installed immediately by users or can be deferred.
- **Enable or Disable Version:** Allows you to control the availability of a version by toggling it on or off.
- **Rollout Percentage:** Lets you define what proportion of users will receive the update, enabling staged rollouts to monitor stability.

:::caution Setting Fields

The **Mandatory**, **Disable**, and **Rollout Percentage** parameters in the Settings section are applied in real time. This means that any changes you make will be immediately reflected across all user devices.

For example, when a version is released, some users may download it. If you later disable the version, users who haven't updated yet will no longer see this release.

Similarly, if an update was initially published as optional but later marked as **Mandatory**, all users who haven't updated yet will be forced to install the new version.

:::

:::info Rollout Percentage

The rollout percentage distributes updates randomly across devices based on the specified percentage. It is not possible to determine exactly which devices will receive the update.

For example, if you release an update with a 70% rollout percentage, 7 out of 10 devices with the app installed will receive the update at random. The remaining 3 devices will not see the update.

:::

### Download Bundle
Use this option to download the `.zip` bundle file associated with a specific CodePush release.


