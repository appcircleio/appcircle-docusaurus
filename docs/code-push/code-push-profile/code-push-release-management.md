---
title: CodePush Release
description: Learn how to manage a release with Appcircle CodePush
tags: [appcircle codepush, profile, codepush]
sidebar_position: 3
---

# CodePush Release

This section describes how to manage and distribute CodePush updates through Appcircle, including versioning, release strategies, and common practices for efficient update delivery.

## Deployment Keys

Deployment keys are used to link your deployment channels with the CodePush SDK, ensuring that updates are delivered to the correct target environment. For each newly created deployment channel, Appcircle will automatically generate a unique deployment key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-deploymentKeys.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-deploymentKeysDetails.png' />

## Upload New Release

With the Appcircle CodePush **Upload New Release** feature, you can manually release a bundle file that you have generated in your local environment.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-newRelease.png' />

To use this feature, you need to upload the bundle file you created as a `.zip` archive. Below you can find a detailed explanation of the required inputs for the Upload Release feature.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-newReleaseDetails.png' />

- **App Version:** Specifies which app version the update is targeted for. Make sure it matches the version defined in your project settings.
- **Release Note:** A description of the changes or improvements included in this release. This helps users and team members understand what the update contains.
- **Mandatory Update:** When enabled, users are required to install the update immediately upon app launch.
- **Disable:** Disables the current release, making it unavailable to users, even if it was previously deployed.
- **Rollout Percentage:** Defines what percentage of users who will receive the update initially. This allows for a gradual rollout and safer deployments.

## Managing Versions

The version management section allows you to view and compare previous CodePush releases for better control and organization of your update history. All fields in the version list are explained below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-versionList.png' />

- **Release Version:** Indicates the version of the CodePush update you have uploaded.
- **Target Version:** Shows which app version this release is intended to run on.
- **Status:** Displays the current status of the release (e.g., Enabled, Disabled).
- **Mandatory:** Specifies whether the update is mandatory for users or optional.
- **Active Devices:** The number of devices currently running this release version.
- **Rollout%:** The percentage of users to whom the release has been deployed.
- **Date:** The timestamp of when the release was uploaded.

## Version Actions

In this section, you can perform actions such as viewing details, disabling, or enabling a specific CodePush version to manage your release lifecycle more effectively.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-versionActions.png' />

All version actions are detailed below.

### Details
This option allows you to view all the information and configuration details of a specific CodePush release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-versionDetails.png' />

  - **Released on:** Displays the exact date and time when this release was created.
  - **Channel:** Indicates the deployment channel (e.g., Staging or Production) to which this release belongs.
  - **Release Method:** Shows whether the release was uploaded manually, promoted from another channel, or generated automatically by the Build Module.
  - **Target Version:** Specifies the binary version of the app that this release is compatible with.
  - **Size:** The file size of the update bundle, giving users an idea of the download footprint.
  - **Mandatory:** States whether this update must be installed immediately by users or can be skipped.
  - **Status:** Reflects the current state of the release (Enabled or Disabled).
  - **Rollout:** Indicates the percentage of devices that will receive this release based on rollout settings.
  - **Description:** A short summary of the changes or improvements included in this release.

### Promote
Use this action to promote a release from one deployment channel to another, such as from Staging to Production.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-promote.png' />

  - **Released Version:** Displays the exact version identifier of the release you are promoting.
  - **Released on:** Shows the original date and time when this release was first created.
  - **Promote To:** Specifies the target deployment channel (e.g., Production) where the release will be promoted.
  - **Description:** A brief note explaining the purpose of this promotion or summarizing the changes included in the release.

### Rollback
This action reverts your app to the previous stable CodePush version in case of issues with the latest update. You can also roll back to any specific version if needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-rollback.png' />

### Settings
Allows you to modify release configurations such as rollout percentage or mark the release as mandatory.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-settingsNew.png' />

- **Description:** A brief note summarizing what this specific version includes. Useful for internal tracking and user communication.
- **Mandatory:** Indicates whether this version must be installed immediately by users or can be deferred.
- **Enable or Disable Version:** Allows you to control the availability of a version by toggling it on or off.
- **Rollout Percentage:** Lets you define what proportion of users will receive the update, enabling staged rollouts to monitor stability.

:::caution Setting Fields

The **Mandatory**, **Disable**, and **Rollout Percentage** parameters in the Settings section are applied in real time. This means that any changes you make will be immediately reflected across all user devices.

For example, when a version is released, some users may download it. If you disable the version later, users who haven't received the update yet will no longer see this release.

Similarly, if an update was initially published as optional but later marked as **Mandatory**, all users who haven't received the update yet will be required to install the new version.

:::

:::info Rollout Percentage

The rollout percentage distributes updates randomly across devices based on the specified percentage. It is not possible to determine exactly which devices will receive the update.

For example, if you release an update with a 70% rollout percentage, 7 out of 10 devices with the app installed will receive the update at random. The remaining 3 devices will not get the update.

:::

### Download Bundle
Use this option to download the `.zip` bundle file associated with a specific CodePush release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-downloadBundle.png' />