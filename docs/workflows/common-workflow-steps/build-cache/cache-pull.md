---
title: Cache Pull 
description: Enhance your development process with Cache Pull to quickly retrieve and reuse stored data, boosting efficiency and performance.
tags: [cache pull, efficiency, dependencies, cache structure]
---

import Screenshot from '@site/src/components/Screenshot';
import CacheTokenIdCaution from '@site/docs/workflows/common-workflow-steps/build-cache/\_cache-token-id-expiration-time-caution.mdx';

# Cache Pull

[**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) uploads the cache archive file to a remote location, as we explained in detail in the **Cache Push** step. On the other hand, **Cache Pull** downloads and extracts that archive file in the build pipeline, restoring all files and folders to their original locations.

:::danger

[**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) and **Cache Pull** components should work in coordination on the same cache file. Therefore, to download the pushed cache, the **Cache Pull** must have the same cache label as the **Cache Push**.

:::

:::warning Deprecation of Branch-Based Caching

Previously, the Cache Pull step used branch-based caching by default. This behavior has been deprecated, and branches now share the same cache by default.
If you prefer to continue using branch-based caching, you can manually add branch information to your cache label. Check out the details on [how to enable branch-based caching](/workflows/common-workflow-steps/build-cache/cache-push#how-to-configure-branch-based-caching).

:::

:::info

If you need to use the cached folder in a separate project, you have the capability to modify the value of `$AC_BUILD_PROFILE_ID`. For further information, please check out the following documentation:
- [How to Share Files Between Build Profiles](/workflows/common-workflow-steps/build-cache/how-to-share-file-between-build-profiles)

This variables can be adjusted within the [cache label](#input-variables) field, as indicated by the red highlight in the accompanying image. Simply replace them with the project ID that corresponds to your intended usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM-197-cache-pull-1.png' />

If you are using [branch-based caching](/workflows/common-workflow-steps/build-cache/cache-push#how-to-configure-branch-based-caching), you might need to use share cached build files between workflows. For this, you can modify the value of `$AC_GIT_BRANCH`. For further information, please check out the following documentation:
- [How to Share Files Between Workflows](/workflows/common-workflow-steps/build-cache/how-to-share-file-between-pipelines)
:::

### Prerequisites

There are no prerequisites required before using the **Cache Pull** step.

:::caution

This component does not require any prerequisite steps for operation. The only thing necessary for the component to work as expected is to utilize the cached files before the step in which they will be used. Additionally, an important prerequisite for this step to function properly is that the files to be used must have been cached in previous builds. 

For example, in the screenshot, to use cached files for Cocoapods, the **Cache Pull** step should be used before the [**Cocoapods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM-197-cache-pull-2.png' />

:::

:::danger

If there are no previously cached files and you attempt to use this step, the **Cache Pull** step will result in a **`not found error`** because it cannot locate the specified files at the remote location.

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM-197-cache-pull-3.png' />

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both [**Cache Push**](/workflows/common-workflow-steps/build-cache/cache-push) and **Cache Pull** steps should have the same value to match. | Required |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after running the [**Git Clone**](/workflows/common-workflow-steps/git-clone) step. | Optional |

<CacheTokenIdCaution />

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-pull-component