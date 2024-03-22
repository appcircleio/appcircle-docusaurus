---
title: How to Share Files Between Pipelines 
metaTitle: How to Share Files Between Pipelines
metaDescription: How to Share Files Between Pipelines
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# How to Share Files Between Pipelines

With the build cache structure provided by Appcircle, you can share cache files between pipelines in different branches. This sharing enables faster package generation across various branches, reducing overall build time. Below is a simple step-by-step example of how you can achieve this.

:::info
This simple example will use our [**CocoaPods**](https://cocoapods.org/) files in a different branch. If you want to use a cache other than dependencies, please refer to the documentation for the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) component.
:::

:::caution
In order to share cache between pipelines, the [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) component must be added to the related pipeline.
:::

:::caution
As an example, **master** and **development** branches were used, but you can apply the same operations to different branches.
:::

:::warning
Please note that the organizational structure of Appcircle is designed in such a way as to prevent any **security vulnerabilities**. Consequently, exchanging files between organizations or sub-organizations **is not permitted**.

You can find detailed information about the Appcircle organizational structure in the documentation [**here**](https://docs.appcircle.io/account/my-organization).
:::

- First of all, we start by caching our CocoaPods files in the **development** branch. We will use these files in our master branch later. For this, the Cache Push step must be added to the workflow after the [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheDevelop.png' />

- After the build in the **development** branch is completed successfully, we are ready to use our cached CocoaPods files in the **master** branch.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheSuccess.png' />

- For the master branch, we first need to make our workflow steps suitable. For this, we add the Cache Pull step to the workflow before the CocoaPods Install step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheMaster.png' />

- When you enter the **Cache Pull** step, you will see the **Cache Label** parameter. This parameter comes as `$AC_BUILD_PROFILE_ID/$AC_GIT_BRANCH/cache` by default. Here, the `$AC_BUILD_PROFILE_ID` value will remain constant since we are in the same build profile, but we will change the `$AC_GIT_BRANCH` value with the **development** branch name. The parameter value should be `$AC_BUILD_PROFILE_ID/development/cache`.

:::caution
If you use more than one cache for the same branch, you can edit your cache label accordingly (both Cache Pull and Cache Push). For example, `$AC_BUILD_PROFILE_ID/development/cache-1` or `$AC_BUILD_PROFILE_ID/development/cache-cocoapods`.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheLabel.png' />

- After this parameter change, CocoaPods dependencies that we cached in the development branch pipeline will be automatically pulled to the master branch and used directly in the master branch pipeline.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullSuccess.png' />

:::warning
When sharing cache files between pipelines, please make sure that you spell your branch names correctly and use the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) and [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) steps correctly. 
:::