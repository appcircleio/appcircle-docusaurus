---
title: Binary Actions
description: Learn how to use binary actions on Appcircle
tags: [build, binary actions]
sidebar_position: 7
---

# Binary Actions

With Appcircle's post-build actions, you can easily distribute your binary file manually, access artifacts, and examine build logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-action.png' />

## Distribute Binary

The Distribute Binary feature sends the binary file to the relevant module based on the distribution settings in the selected configuration.

:::caution

Please note that AAB files will not be distributed automatically since they cannot be installed on mobile devices directly.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-dist.png' />

## View Build Logs

This feature allows the relevant build logs to be reviewed in the Appcircle log window. The logs can be examined step by step separately.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-log.png' />

## Download Artifacts

Each time a build is completed by Appcircle, all artifacts produced after the build are stored for easy access. These files, which include artifacts such as IPA, APK, and AAB binary files, log files, and archive files, can be accessed by selecting Download Artifacts.

:::caution Output Artifacts

#### For Android

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage of multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. On our [**testing portal**](/testing-distribution/testing-portal), your testers will be able to download each `.apk` file separately and test it on their devices.

#### For iOS

iOS applications can be downloaded or distributed as IPA file format if you configure signing identities and sign the application during the build process.

If you disable signing or don't use any signing identities, iOS output will be a `.xarchive` file.

:::

## Download Build Logs

In addition to allowing the review of logs, Appcircle also permits the downloading of these logs in .txt file format, enabling the logs to be downloaded and used in a single file.

#### Working with build logs

Build logs help you to observe and understand exactly what happened during a build. You can see build logs as they happen while a build is in process, or you can view logs of a build after the build is completed.

:::info

In the build logs, the **Builds/Statuses** column is sorted by the latest completion build date. As a result, the start dates displayed in the list might not be in chronological order:

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-working-with-build-logs.png' />

:::

You can use build logs to debug your builds in case you get any errors. Additional parameters and flags can also be used in workflow steps to see more details in build logs.

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

You can also download build logs in plain text format in case you would like to investigate them on your own or share with your team.

#### Delete Specific Builds

If you want to free up space from your Artifact Storage, you can delete older build profiles that are cluttering your space.

To do that, simply navigate to the Builds tab and select the builds, then click on the Delete icon.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-delete5.png' />

:::info

The build deletion feature is only available for organizations with an enterprise license.

:::

## FAQ

### Artifact Storage is Full

Older builds and/or testing distributions will use almost all of your storage. If your artifact storage is full, you can free up some of the old artifacts.

#### [Refer here to delete specific builds from your build profile](/build/build-process-management/binary-actions#delete-specific-builds)

#### [Refer here to delete testing distribution profiles and specific distribution artifacts](/testing-distribution/create-or-select-a-distribution-profile#delete-a-distribution-profile)

#### [Refer here to delete a Publish Profile](/publish-module/creating-publish-profiles/managing-publish-profiles#delete-publish-profile)

In order for storage to be freed up, you should also remove the other references pointing to the artifact. For example, if you have built an app, distributed it to testers, and submitted it to the Store Submit, you should delete that build from Testing Distribution, Store Submit, and Builds, respectively.

:::caution

It may take a couple of minutes to see the change in your account after you have deleted some artifacts.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />