---
title: How to Share Files Between Pipelines 
description: Master the art of sharing files between pipelines to optimize workflow continuity and efficiency in your development projects.
tags: [pipelines, data sharing, cache push, cache pull, efficiency]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# How to Share Files Between Pipelines

With the build cache structure provided by Appcircle, you can share cache files between pipelines in different branches. This sharing enables faster package generation across various branches, reducing overall build time. Below is a simple, step-by-step example of how you can achieve this.

:::info
This simple example will use our [**CocoaPods**](https://cocoapods.org/) files in a different branch. If you want to use a cache other than dependencies, please refer to the documentation for the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) component.
:::

:::info
As an example, **master** and **development** branches were used, but you can apply the same operations to different branches.
:::

:::warning
Please note that the organizational structure of Appcircle is designed in such a way as to prevent any **security vulnerabilities**. Consequently, exchanging files between organizations or sub-organizations **is not permitted**.

You can find detailed information about the Appcircle organizational structure in the documentation [**here**](https://docs.appcircle.io/account/my-organization).
:::

:::caution
In order to share cache between pipelines, the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) component must be added to the related pipeline.
:::

1. To start, cache the CocoaPods files in the **development** branch, which will later be utilized in the **master** branch. For this purpose, add the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) step to the workflow after the [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheDevelop.png' />

2. After the successful completion of the build in the **development** branch, cached CocoaPods files are ready to be used in the **master** branch.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheSuccess.png' />

3. For the **master** branch, the [workflow](/workflows) steps need to be made suitable first. To achieve this, the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) step is added to the workflow before the **CocoaPods Install** step.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheMaster.png' />

4. When you enter the [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) step, the **Cache Label** will be visible. By default, this parameter is set as `$AC_BUILD_PROFILE_ID/$AC_GIT_BRANCH/cache`. In this case, the value of `$AC_BUILD_PROFILE_ID` will remain constant as it is within the same build profile, while the value of `$AC_GIT_BRANCH` will be changed to the **development** branch name. The parameter value should be set as `$AC_BUILD_PROFILE_ID/development/cache`.

	<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-cacheLabel.png' />

	:::caution
	If you use more than one cache for the same branch, you can edit the [cache label](/workflows/common-workflow-steps/build-cache/cache-push#input-variables) accordingly in both [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) and [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) steps. For example:
	- `$AC_BUILD_PROFILE_ID/development/cache-1`
	- `$AC_BUILD_PROFILE_ID/development/cache-cocoapods`
	:::

5. After this parameter change, the CocoaPods dependencies that were cached in the **development** branch pipeline will be automatically pulled to the **master** branch and used directly in the **master** branch pipeline.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullSuccess.png' />

:::warning
When sharing cache files between pipelines, please make sure that you spell your branch names correctly and use the [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) and [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) steps correctly. 
:::