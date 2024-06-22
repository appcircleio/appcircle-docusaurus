---
title: Create a Distribution Profile and Sharing with Testers
description: Learn how to create a distribution profile and share your builds with testers in Appcircle
tags: [distribution, distribution profile, testing distribution, testers]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

## Testing Distribution

<iframe width="600" height="315" src="https://www.youtube.com/embed/vZ3p5uZZcmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In order to share your builds with testers, you can create distribution profiles and assign testing groups to the distribution profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/distribution-start.png' />

> Note that an empty Testing Distribution profile named **Send to Myself** will be created automatically for you.

:::info

A distribution profile corresponds to the multiple versions of the same application for iOS and Android. You do not need to create multiple Testing Distribution profiles for iOS and Android applications of the same application.
:::

## FAQ

### No files or multiple files were received from autodistribute;

A successful distribution depends on a correctly signed binary. Please check if the [signing configuration](/build/build-process-management/build-profile-configuration#signing-configuration) is correct.

You can also check the list of the [generated build artifacts](/build/post-build-operations/after-a-build) to confirm the output. In Android, you can also check the `ac_post_process_output.json` file in the build artifacts to see if the APKs are signed or not.

In Android, please also check if gradle sign is being used for the selected build variant. If gradle sign works alongside with Appcircle signing, you will receive multiple APKs.

### Deleted versions still occupy storage space

The master version of any artifact deployed from the Build to the Testing Distribution is stored within the build artifacts section. Once you delete such a version from the Testing Distribution, only the reference is removed and the binary is still available within the build artifacts of the related build. You also need to remove the binary from the build artifacts to save storage.

### Access Denied on builds

On some distributed apps, the **Access Denied** error can be bypassed by one of these steps:

- Launching the distribution link on a different browser and Incognito Mode
- Clearing the browser cache if the link is pasted to a browser instead of in-line browser on mail applications
- If there is an authorization configuration on Distribution, clearing the authorization temporarily

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

If you still can't solve your issues, ask on our Slack page. Our community and our support engineers will help you whenever they're available:

import NeedHelp from '@site/docs/\_need-help.mdx';

<NeedHelp />
