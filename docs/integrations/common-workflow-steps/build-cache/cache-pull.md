---
title: Cache Pull 
metaTitle: Cache Pull
metaDescription: Cache Pull
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Cache Pull

Cache push uploads the cache archive file to a remote location, as we explained in detail in the [**Cache Push**](https://docs.appcircle.io/workflows/common-workflow-steps/#cache-push) step. On the other hand, cache pull downloads and extracts that archive file in the build pipeline. All files and folders are extracted to the original locations they came from.

:::warning

Cache push and pull components should work in coordination on the same cache file. For this reason, in order to download the pushed cache, the cache pull must have the same cache label as the cache push.

:::

:::info

In the event that you need to utilize the cached folder in an alternate branch or a separate project, you have the capability to modify the values of `$AC_GIT_BRANCH` or `$AC_BUILD_PROFILE_ID`.

These variables can be adjusted within the **Cache Label** field, as indicated by the red highlight in the accompanying image. Simply replace them with the branch or project ID that corresponds to your intended usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/cache-01.png' />

:::

### Prerequisites

:::caution
This component does not require any prerequisites step for operation. The only thing necessary for the component to work as expected is to use the cached files before the step in which they will be used. At the same time, another important point for this step to work is that the files to be used must have been cached in previous builds. 

For example in the screen shot, to use cached files for **Cocoapods**, **Cache Pull** step should be used before [**Cocoapods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullOrder.png' />
:::

:::warning
If there are no previously cached files and you want to use this step, the **Cache Pull** step will give a **`not found error`** because it cannot find the specified files at the remote location.
:::

### Input Variables

The parameters required for the operation of this step are given in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullInput.png' />

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both Cache Push and Cache Pull steps should have the same value to match. | Required |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after run [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step. | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-pull-component