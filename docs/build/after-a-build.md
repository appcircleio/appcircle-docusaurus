---
title: After a Build
metaTitle: After a Build
metaDescription: After a Build
sidebar_position: 13
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# After a Build

### Android outputs

Appcircle will build your Android applications into APK files to download and run on Android devices or AAB format that you can upload to Google Play to support Dynamic Delivery.

:::caution

Please note that AAB files will not be distributed automatically since they cannot be installed on mobile devices directly.

:::

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. On our [**testing portal**](../distribute/downloading-binaries.md), your testers will be able to download each `.apk` file separately and test it on their devices.

### iOS outputs

iOS applications can be downloaded or distributed as IPA file format if you configure signing identities and sign the application during the build process.

If you disable signing or don't use any signing identities, iOS output will be an `.xarchive` file.

To download or manually distribute your builds, go to your distribution profile and click on the builds tab to see your past builds. Click on the actions icon of the build you want to download or distribute.

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-ios-distribute-artifacts.png' />

You can now download the binary file or send it to distribute the module manually.

If you click on Distribute Binary option, your build file will be sent to the related test group automatically.

### Working with build logs

Build logs help you to observe and understand exactly what happened during a build. You can see build logs as they happen while a build is in process or you can view logs of a build after the build is completed.

You can use build logs to debug your builds in case you get any errors. Additional parameters and flags can also be used in workflow steps to see more details in build logs.

<ContentRef url="/workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>

You can also download build logs in plain text format in case you would like to investigate them on your own or share with your team.

### Delete Specific Builds

If you want to free up space from your Artifact Storage, you can delete older build profiles which are cluttering your space.

To do that, simply navigate to the Builds tab and select the builds, then click on the Delete icon

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-delete-specific.png' />

:::tip

Build Deletion feature is only available at Pro or above plans.

To get more info, see our Pricing: [https://appcircle.io/pricing/](https://appcircle.io/pricing/)

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
