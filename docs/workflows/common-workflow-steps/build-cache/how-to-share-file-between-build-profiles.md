---
title: How to Share Files Between Build Profiles 
description: Learn to share files between build profiles efficiently. Enhance collaboration and streamline your development process with our guide.
tags: [pipelines, data sharing, cache pull, cache push, efficiency]
---

import Screenshot from '@site/src/components/Screenshot';


# How to Share Files Between Build Profiles

With the build cache structure provided by Appcircle, cache files can be shared between different [**Build Profiles**](/build/manage-the-connections/adding-a-build-profile/). This sharing of files enables the faster generation of packages in different Build Profiles, reducing build time. Below is a simple, step-by-step example of how you can achieve this.

:::info

This simple example will use our [**CocoaPods**](https://cocoapods.org/) files in different build profiles. If you intend to use a cache other than dependencies, please refer to the documentation for the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) component.

:::

:::caution

To share cache between Build Profiles, the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) component must be added to the related pipeline.

:::

:::caution

As an example, **master** and **development** branches were used, but you can apply the same operations to different branches.

:::

:::danger

Please note that the organizational structure of Appcircle is designed in such a way as to prevent any **security vulnerabilities**. Consequently, exchanging files between organizations or sub-organizations **is not permitted**.

You can find detailed information about the Appcircle organizational structure in the documentation [**here**](/account/my-organization).

:::

1. Firstly, the caching of CocoaPods files is initiated in the **`Appcircle Team`** build profile. These files will subsequently be utilized in the **`Appcircle Team 2`** build profile. To accomplish this, the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) step should be incorporated into the workflow after the **CocoaPods Install** step in the initial build profile.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildCache.png' />

2. After the successful completion of the build in the **`Appcircle Team`** build profile, the cached CocoaPods files are now available for use in the **`Appcircle Team 2`** build profile.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheSuccess.png' />

3. For the **`Appcircle Team 2`** build profile, the workflow steps need to be adjusted accordingly. To do this, the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) step should be added to the workflow before the **CocoaPods Install** step for the relevant branch.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildPull.png' />

4. When the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) step is entered, the **cache label** parameter is encountered, which is set as `$AC_BUILD_PROFILE_ID/$AC_GIT_BRANCH/cache` by default. Here, the value of `$AC_BUILD_PROFILE_ID` needs to be updated because a different profile is being used. To accomplish this, the build profile ID of the **`Appcircle Team`** where the files were cached will be used. This ID can be found directly at the **Appcircle URL**. For example, in the URL `my.appcircle.io/build/detail/edc136b9-85fc-4e0a-aa7c-602375a84f64`, `edc136b9-85fc-4e0a-aa7c-602375a84f64` represents the build profile ID. After setting the profile ID, the `$AC_GIT_BRANCH` value that was cached in the previous profile, **`Appcircle Team`**, is specified, which is set to the **development** branch. Consequently, the **cache label** parameter will appear as `edc136b9-85fc-4e0a-aa7c-602375a84f64/development/cache`.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildPullLabel.png' />

5. After this parameter change, the CocoaPods dependencies that were cached in the **development** branch of the **`Appcircle Team`** build profile will be automatically pulled to the **master** branch of **`Appcircle Team 2`** and used directly in the pipeline.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildCacheSuccess.png' />

:::danger

When sharing cache files between **Build Profiles**, please make sure that you spell your build profile ID and branch names correctly and use the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) and [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) steps correctly in each profile. 

:::