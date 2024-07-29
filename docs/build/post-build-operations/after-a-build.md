---
title: Build Artifacts
description: Learn how to manage build artifacts in Appcircle
tags: [build, build artifacts, build outputs, build logs, faq]
sidebar_position: 13
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Managing Build Artifacts

### Android outputs

Appcircle will build your Android applications into APK files to download and run on Android devices or AAB format that you can upload to Google Play to support Dynamic Delivery.

:::caution

Please note that AAB files will not be distributed automatically since they cannot be installed on mobile devices directly.

:::

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. On our [**testing portal**](/distribute/downloading-binaries), your testers will be able to download each `.apk` file separately and test it on their devices.

### iOS outputs

iOS applications can be downloaded or distributed as IPA file format if you configure signing identities and sign the application during the build process.

If you disable signing or don't use any signing identities, iOS output will be an `.xarchive` file.

To download or manually distribute your builds, go to your distribution profile and click on the builds tab to see your past builds. Click on the actions icon of the build you want to download or distribute.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-ios-distribute-artifacts.png' />

You can now download the binary file or send it to distribute the module manually.

If you click on Distribute Binary option, your build file will be sent to the related test group automatically.

### Working with build logs

Build logs help you to observe and understand exactly what happened during a build. You can see build logs as they happen while a build is in process or you can view logs of a build after the build is completed.

:::info

In the build logs, the **Builds/Statuses** column is sorted by the latest completion build date. As a result, the start dates displayed in the list might not be in chronological order:

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-working-with-build-logs.png' />

:::

You can use build logs to debug your builds in case you get any errors. Additional parameters and flags can also be used in workflow steps to see more details in build logs.

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

You can also download build logs in plain text format in case you would like to investigate them on your own or share with your team.

### Delete Specific Builds

If you want to free up space from your Artifact Storage, you can delete older build profiles which are cluttering your space.

To do that, simply navigate to the Builds tab and select the builds, then click on the Delete icon

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-delete-specific.png' />

:::tip

Build Deletion feature is only available at Pro or above plans.

To get more info, see our Pricing: [https://appcircle.io/pricing/](https://appcircle.io/pricing/)

:::

## FAQ

### Artifact Storage is Full

Older builds and/or testing distributions will use almost all of your storage. If your artifact storage is full, you can free up some of the old artifacts.

#### [Refer here to delete a build profile](/build/manage-the-connections/adding-a-build-profile#delete-a-build-profile)

#### [Refer here to delete specific builds from your build profile](/build/post-build-operations/after-a-build#delete-specific-builds)

#### [Refer here to delete testing distribution profiles and specific distribution artifacts](/distribute/create-or-select-a-distribution-profile#delete-a-distribution-profile)

#### [Refer here to delete a Publish Profile](/publish-module/creating-publish-profiles/managing-publish-profiles#delete-publish-profile)

In order for storage to be freed up, you should also remove the other references pointing to the artifact. In example, if you have built an app, distributed it to testers, and submitted it to the Store Submit, you should delete that build from Testing Distribution, Store Submit, and Builds respectively.

:::caution

It may take a couple of minutes to see the change in your account after you have deleted some artifacts.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
