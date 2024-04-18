---
title: Cache Pull 
description: Enhance your development process with Cache Pull to quickly retrieve and reuse stored data, boosting efficiency and performance.
tags: [cache pull, efficiency, dependencies, cache structure]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Cache Pull

[**Cache Push**](./cache-push) uploads the cache archive file to a remote location, as we explained in detail in the **Cache Push** step. On the other hand, **Cache Pull** downloads and extracts that archive file in the build pipeline, restoring all files and folders to their original locations.

:::warning
[**Cache Push**](./cache-push) and **Cache Pull** components should work in coordination on the same cache file. Therefore, to download the pushed cache, the **Cache Pull** must have the same cache label as the **Cache Push**.
:::

:::info
If you need to use the cached folder in a different branch or a separate project, you have the capability to modify the values of `$AC_GIT_BRANCH` or `$AC_BUILD_PROFILE_ID`. For further information, please check out the following documentation:
- [How to Share Files Between Pipelines](./how-to-share-file-between-pipelines)
- [How to Share Files Between Build Profiles](./how-to-share-file-between-build-profiles)

These variables can be adjusted within the [cache label](#input-variables) field, as indicated by the red highlight in the accompanying image. Simply replace them with the branch or project ID that corresponds to your intended usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/cache-01.png' />
:::

### Prerequisites

:::caution
This component does not require any prerequisite steps for operation. The only thing necessary for the component to work as expected is to utilize the cached files before the step in which they will be used. Additionally, an important prerequisite for this step to function properly is that the files to be used must have been cached in previous builds. 

For example, in the screenshot, to use cached files for Cocoapods, the **Cache Pull** step should be used before the [**Cocoapods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullOrder.png' />
:::

:::warning
If there are no previously cached files and you attempt to use this step, the **Cache Pull** step will result in a **`not found error`** because it cannot locate the specified files at the remote location.
:::

### Input Variables

The parameters required for the operation of this step are given in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pullInput.png' />

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both [**Cache Push**](./cache-push) and **Cache Pull** steps should have the same value to match. | Required |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after running the [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step. | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-pull-component