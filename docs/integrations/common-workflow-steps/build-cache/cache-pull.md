---
title: Cache Pull 
metaTitle: Cache Pull
metaDescription: Cache Pull
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Cache Pull

Cache push uploads cache archive file to remote location as we explained in detail in [**Cache Push**] step. On the other hand cache pull downloads and extracts that archive file in build pipeline. All files and folders are extracted to original locations that came from.

:::warning

Cache push and pull components should work in coordination on the same cache file. For this reason in order to download the pushed cache, cache pull must have the same cache label used in cache push.

:::

:::info

In the event that you need to utilize the cached folder in an alternate branch or a separate project, you have the capability to modify the values of `$AC_GIT_BRANCH` or `$AC_BUILD_PROFILE_ID`.

These variables can be adjusted within the **Cache Label** field, as indicated by the red highlight in the accompanying image. Simply replace them with the branch or project ID that corresponds to your intended usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/cache-01.png' />

:::

### Prerequisites

:::caution
This component does not require any prerequisites for operation. The only thing necessary for the component to work as expected is to use the cached files before the step in which they will be used. For example in the screen shot, to use cached files for **Cocoapods**, **Cache Pull** step should be used before [**Cocoapods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullOrder.png' />
:::

### Input Variables

The parameters required for the operation of this step are given in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullInput.png' />

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both cache push and pull steps should have the same value to match. | Required |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after run [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step. | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-pull-component