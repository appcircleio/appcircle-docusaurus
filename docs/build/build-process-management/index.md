---
title: Build Profile
description: Learn how to manage your build processes effectively with Appcircle. Optimize your build configurations, manage branches, and automate your build pipeline for efficient app development.
tags:
  [
    build process management,
    build profiles,
    branch management,
    manual builds,
    automatic builds,
    app development,
    app deployment,
    appcircle build process,
  ]
---

New to Appcircle Build module? Follow our quick start guide to build your iOS and Android apps in the cloud.

The Build Module allows you to streamline and automate your mobile app build flows.

:::info

The Build Module is the first step to automate your CI/CD processes via Appcircle.

:::

## Starting a Build

To initiate a build in Appcircle, follow these steps:

- Click on the Start Build button to begin the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start1.png' />

- Appcircle will prompt you to choose a configuration and workflow settings from the saved configurations. Select the appropriate settings that match your project requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start2.png' />

- Once the configurations are selected, click the Start button to start the build.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start3.png' />

- Users can monitor the progress, results, and logs of the workflow steps in real-time via the interface.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start4.png' />

- After the build is complete, you have the option to download the build logs for reference or troubleshooting purposes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start5.png' />

- Upon completion, the binary along with the artifacts will be displayed on the selected branch. These can be accessed for deployment or further use.

By following these steps, you can efficiently manage and monitor your builds in Appcircle.

For more detailed information on builds with different type of projects, please refer to the [Platform Build Guides](/build/platform-build-guides) documentation.

### Build Statuses

- **Success**: The build has finished successfully with no failures in the workflow steps.
- **Failed**: The build has failed due to one or more workflow steps failing.
- **Warning**: The build has finished with a failed workflow step that does not affect the final outcome.
- **Timeout**: The build exceeded the timeout limit and ended prematurely.
- **Canceled**: The build was canceled by the user.

## Binary Actions

With Appcircle's post-build actions, you can easily distribute your binary file manually, access artifacts and examine build logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-action.png' />

### Distribute Binary

The Distribute Binary feature sends the binary file to the relevant module based on the Distribution settings in the selected configuration.

:::caution

Please note that AAB files will not be distributed automatically since they cannot be installed on mobile devices directly.

:::

### View Build Logs

This feature allows the relevant build logs to be reviewed in the Appcircle log window. The logs can be examined step by step separately.

### Download Artifacts

Each time a build is completed by Appcircle, all artifacts produced after the build are stored for easy access. These files, which include artifacts such as IPA, APK, and AAB binary files, log files, and archive files, can be accessed by selecting Download Artifacts.

:::caution Output Artifacts

### For Android

If your Android application has multiple product flavors, Appcircle will create a build for each flavor of your application and let you distribute them at once. A common usage to multi-flavor applications can be free and paid versions of the same application.

When you build and distribute an application with multiple flavors, and `.apk` file will be created for each flavor. On our [**testing portal**](/testing-distribution/testing-portal), your testers will be able to download each `.apk` file separately and test it on their devices.

### For iOS

iOS applications can be downloaded or distributed as IPA file format if you configure signing identities and sign the application during the build process.

If you disable signing or don't use any signing identities, iOS output will be an `.xarchive` file.

:::

### Download Build Logs

In addition to allowing the review of logs, Appcircle also permits the downloading of these logs in .txt file format, enabling the logs to be downloaded and used in a single file.

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

#### [Refer here to delete specific builds from your build profile](/build/build-process-management#delete-specific-builds)

#### [Refer here to delete testing distribution profiles and specific distribution artifacts](/testing-distribution/create-or-select-a-distribution-profile#delete-a-distribution-profile)

#### [Refer here to delete a Publish Profile](/publish-module/creating-publish-profiles/managing-publish-profiles#delete-publish-profile)

In order for storage to be freed up, you should also remove the other references pointing to the artifact. In example, if you have built an app, distributed it to testers, and submitted it to the Store Submit, you should delete that build from Testing Distribution, Store Submit, and Builds respectively.

:::caution

It may take a couple of minutes to see the change in your account after you have deleted some artifacts.

:::

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />