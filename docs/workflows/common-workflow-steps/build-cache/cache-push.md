---
title: Cache Push
description: Optimize your workflow by utilizing Cache Push to save and streamline data access, improving speed and reliability in your projects.
tags: [cache push, optimization, storage, dependencies, cache structure]
---

import Screenshot from '@site/src/components/Screenshot';

# Cache Push

Every single build at Appcircle runs in a clean state. It means that all files and folders that are not versioned in the Git repository are lost when the build pipeline is completed. For example, install dependencies or build artifacts. If you need to keep those files and folders, you can use the Appcircle **Cache Push** and [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) components.

With cache, you can persist any resource that is ignored by Git. So you can transfer files and folders between build pipelines. Sometimes it may speed up your build, or it may help if you have reliability issues with the original download location for dependencies. But keep in mind that the cache is uploaded to or downloaded from a remote location. It may help you in some cases, but **it's not a guaranteed way to speed up builds**. You should try and see the actual results of your project.

The cache is stored as a single archive file. **Cache Push** and [**Cache Pull**](/workflows/common-workflow-steps/build-cache/cache-pull) components work in coordination on the same cache file defined with a label. Cache labeling helps you organize your caches. With custom labeling, you can have different chunks of caches, and you can share some caches between branches or build profiles. For further information, please check out the following documentation:

- [How to Share Files Between Pipelines](/workflows/common-workflow-steps/build-cache/how-to-share-file-between-pipelines)
- [How to Share Files Between Build Profiles](/workflows/common-workflow-steps/build-cache/how-to-share-file-between-build-profiles)

When you drag and drop the **Cache Push** component into your [workflow](/workflows), it comes with pre-defined values according to your project type. For example, in the case of Android projects, it comes with pre-defined [Gradle cache](https://docs.gradle.org/current/userguide/build_cache.html) paths, which should prove useful for most Android apps.

If you need more paths to cache or need to change paths according to your project, you can customize [included](#input-variables) and [excluded](#input-variables) paths as you wish. All path updates will be reflected in the archived cache file on your next build.

:::danger
You cannot delete a specific cache file from the UI, but if you have a problem with a cache file and need a fresh one, you can change your [cache label](#input-variables) to a new one to go on with a clean cache.
:::

:::info
The system automatically cleans unreachable and obsolete cache files periodically. For this reason, **it's not guaranteed to reach a previously used cache file by using the previous cache label in build**. Also, it’s a good idea to build your workflow in such a way that your **build won’t fail if the cache can’t be accessed**.
:::

### Prerequisites

| Prerequisite Workflow Step                                                           | Description                                                                                                                                                                  |
| ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) | If the folders to be cached are in the repo directory, the **Git Clone** step must be used before. This step will generate the [`AC_REPOSITORY_DIR`](#input-variables) path. |

:::danger
Keep in mind that included paths and the **Cache Push** step's workflow order are closely related to each other. For example, if you include a path from a repository and you place the **Cache Push** step before the **Git Clone** step, **Cache Push** won't find that path since it's not Git cloned yet. Although that's not a fatal error for **Cache Push**, it will inform you about unreachable paths on build logs. You can review and resolve those kinds of issues from build logs.
:::

:::caution
The other important prerequisite for this component to work is that it must be used after the step in which the generated artifact of the step is to be cached. For example, in the screen shot, to cache dependencies, the **Cache Push** step is used after the [**CocoaPods Install**](/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pushOrder.png' />
:::

### Input Variables

The parameters required for the operation of this step are given in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pushInput.png' />

| Variable Name              | Description                                                                                                                                                                             | Status   |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both **Cache Push** and **Cache Pull** steps should have the same value to match.                                           | Required |
| `$AC_CACHE_INCLUDED_PATHS` | Specifies the files and folders that should be in the cache. Multiple glob patterns can be provided as a colon-separated list. For example; `.gradle:app/build` or `Pods:Podfile.lock`. | Required |
| `$AC_CACHE_EXCLUDED_PATHS` | Specifies the files and folders that should be ignored from the cache. Multiple glob patterns can be provided as a colon-separated list. For example, `.gradle/*.lock:*.apk`.           | Optional |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after running the [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step.          | Optional |

:::tip
**Cache Push** uses a pattern in order to select files and folders. Although the pattern is not a RegExp, it's closer to a shell glob. For example, `~/Library/Caches/CocoaPods` and `Pods` will select the `CocoaPods` folder from home and the repository direction as a whole. Or for an Android project, you can cache the `.gradle ` folder with `~/.gradle` include path and exclude all `.lock` files from there with `~/.gradle/**/*.lock` exclude path. Patterns that can be used in both included and excluded paths are explained in detail [here](https://github.com/appcircleio/appcircle-cache-push-component#included--excluded-paths).
:::

### Output Variables

You cannot reach the cache archive file directly by yourself. But you can see cache file updates and track changes to cache at the end of the build pipeline from '[Download Artifacts](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) > `ac_cache.zip`'. Also, build logs have some useful information about the cache mechanism and how included and excluded paths are processed. You can see the produced cache file size from the build logs. (The size of the cache file affects upload and download durations.)

:::caution
To view the generated artifacts on the [**Download Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) page, please ensure that the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts) step is included in the [workflow](/workflows) after this step.
:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-push-component
