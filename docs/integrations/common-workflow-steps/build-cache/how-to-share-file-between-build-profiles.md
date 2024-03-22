---
title: How to Share Files Between Build Profiles 
metaTitle: How to Share Files Between Build Profiles
metaDescription: How to Share Files Between Build Profiles
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';



# How to Share Files Between Build Profiles

With the build cache structure provided by Appcircle, cache files can be shared between different [**Build Profiles**](https://docs.appcircle.io/build/adding-a-build-profile/). This sharing of files enables the faster generation of packages in different Build Profiles, reducing build time. Below is a simple step-by-step example of how you can achieve this.

:::info
This simple example will use our [**CocoaPods**](https://cocoapods.org/) files in a different build profiles. If you want to use a cache other than dependencies, please refer to the documentation for the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) component.
:::

:::caution
In order to share cache between Build Profiles, the [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) component must be added to the related pipeline.
:::

:::caution
As an example, **master** and **development** branches were used, but you can apply the same operations to different branches.
:::

:::warning
Please note that the organizational structure of Appcircle is designed in such a way as to prevent any **security vulnerabilities**. Consequently, exchanging files between organizations or sub-organizations **is not permitted**.

You can find detailed information about the Appcircle organizational structure in the documentation [**here**](https://docs.appcircle.io/account/my-organization).
:::

- First of all, we start by caching our CocoaPods files in the **`Appcircle Team`** build profile. We will use these files in our **`Appcircle Team 2`** build profile later. For this, the Cache Push step must be added to the workflow after the CocoaPods Install step in the first build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildCache.png' />

- After the build in the **`Appcircle Team`** build profile is completed successfully, we are ready to use our cached CocoaPods files in the **`Appcircle Team 2`** build profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheSuccess.png' />

- For the **`Appcircle Team 2`** build profile, we first need to make our workflow steps suitable. For this, we add the Cache Pull step to the workflow before the CocoaPods Install step for related branch.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildPull.png' />

- When you enter the **Cache Pull** step, you will see the **Cache Label** parameter. This parameter comes as `$AC_BUILD_PROFILE_ID/$AC_GIT_BRANCH/cache` by default. Here, we need to change the `$AC_BUILD_PROFILE_ID` value because we are in a **different profile**. For this, we will use the **`Appcircle Team`** build profile ID where we cache our files. You can get this ID directly from the **Appcircle URL**. For example, `my.appcircle.io/build/detail/edc136b9-85fc-4e0a-aa7c-602375a84f64` in this URL,  the `edc136b9-85fc-4e0a-aa7c-602375a84f64` is your build profile ID. After setting the profile ID, we need to give the `$AC_GIT_BRANCH` value that we cached in the previous profile, **Appcircle Team**. Entering the **development** branch for this. The **cache label** parameter will appear like `edc136b9-85fc-4e0a-aa7c-602375a84f64/development/cache`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildPullLabel.png' />

- After this parameter change, CocoaPods dependencies that we cached in the **development branch** of **Appcircle Team** build profile will be automatically pulled to the master branch of **Appcircle Team 2** and used directly in pipeline.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-buildCacheSuccess.png' />

:::warning
When sharing cache files between **Build Profiles**, please make sure that you spell your build profile ID and branch names correctly and use the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) and [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) steps correctly in each profile. 
:::