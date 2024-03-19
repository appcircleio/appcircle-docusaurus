---
title: How to Share Files between Pipelines 
metaTitle: How to Share Files between Pipelines
metaDescription: How to Share Files between Pipelines
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# How to Share Files between Pipelines

With the build cache structure offered by Appcircle, you can share your cache files between pipelines in different branches. This file sharing will allow you to generate your packages faster in different branches and reduce your build time. Below is a simple example of how you can do this step by step. 

:::info
This simple example will use our CocoaPods files in a different branch. If you want to use a cache other than dependencies, please refer to the documentation for the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) component.
:::

:::caution
In order to share cache between pipelines, the [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) component must be added to the related pipeline.
:::

- First of all, we start by caching our CocoaPods files in the **development** branch. We will use these files in our master branch later. For this, the Cache Push step must be added to the workflow after the [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheDevelop.png' />

- After the build in the **development** branch is completed successfully, we are ready to use our cached CocoaPods files in the **master** branch.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheSuccess.png' />

- For the master branch, we first need to make our workflow steps suitable. For this, we add the Cache Pull step to the workflow before the CocoaPods Install step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheMaster.png' />

- When you enter the **Cache Pull** step, you will see the **Cache Label** parameter. This parameter comes as `$AC_BUILD_PROFILE_ID/$AC_GIT_BRANCH/cache` by default. Here, the `$AC_BUILD_PROFILE_ID` value will remain constant since we are in the same build profile, but we will change the `$AC_GIT_BRANCH` value with the **development** branch name. The parameter value should be `$AC_BUILD_PROFILE_ID/development/cache`

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheLabel.png' />

- After this parameter change, CocoaPods dependencies that we cached in the development branch pipeline will be automatically pulled to the master branch and used directly in the master branch pipeline.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullSuccess.png' />

:::warning
When sharing cache files between pipelines, please make sure that you spell your branch names correctly and use the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) and [**Cache Pull**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-pull) steps correctly. 
:::