---
title: Cache Push 
metaTitle: Cache Push
metaDescription: Cache Push
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Cache Push

Every single build at Appcircle runs in clean state. It means that all files and folders, that are not versioned in git repository, are lost when build pipeline is completed. For example, installed dependencies or build artifacts. If you need to keep those files and folders, you can use Appcircle cache push and pull components.

With cache you can persist any resource that are ignored from Git. So you can transfer files and folders between build pipelines. Sometimes it may speed up your build or it may help if you have reliability issues with the original download location for dependencies. But keep in mind that the cache is uploaded to or downloaded from remote location. It may help you in some cases, but it's not a guaranteed way of speeding up builds. You should try and see the actual results for your project.

The cache is stored as a single archive file. Cache push and pull components work in coordination on the same cache file defined with a label. With custom labelling you can have different chunks of caches and you can share some caches between branches. Cache labelling helps you organize your caches.

When you drag and drop cache push component to your workflow, it comes with pre-defined values according to your project type. For example, for android projects it comes with pre-defined gradle cache paths which should be useful for most Android apps.

If you need more paths to cache or need to change paths according to your project, you can customize included and excluded paths as you wish. All path updates will be reflected to archived cache file on your next build.

Cache push uses a pattern in order to select files and folders. Although the pattern is not a regexp, it's closer to a shell glob. For example, `~/Library/Caches/CocoaPods` and `./Pods` will select "Cocoapods" folder from home and repository direction as a whole. Or for an android project you can cache home ".gradle" folder with `~/.gradle` include path and exclude all ".lock" files from there with `~/.gradle/**/*.lock` exclude path. Patterns, that can be used in included and excluded paths, is explained in detail [here](https://github.com/appcircleio/appcircle-cache-push-component#included--excluded-paths).

:::warning

Keep in mind that included paths and cache push step's workflow order are closely related with each other. For example, if you include a path from repository and you place cache push step before git clone step, cache push won't find that path since it's not git cloned yet. Although that's not a fatal error for cache push, it will inform you about unreachable paths on build logs. You can review and resolve those kinds of issues from build logs.

:::

You can not reach the cache archive file directly by yourself. But you can see cache file updates and track changes to cache at the end of build pipeline from "Download Artifacts > ac_cache.zip". Also build logs have some useful information about cache mechanism with how included and excluded paths are processed. You can see produced cache file size from build logs. (Size of cache file affects upload and download durations.)

:::warning

You can not delete specific cache file from UI but if you have a problem with cache file and need a fresh one, you can change your cache label to a new one to go on with clean cache.

:::

:::info

System automatically cleans unreachable and obsolete cache files periodically. For this reason, it's not guaranteed to reach a previously used cache file by using previous cache label in build. Also it’s a good idea to build your workflow in a way that your build won’t fail if the cache can’t be accessed.

:::

### Prerequisites

:::caution
The prerequisite for this component to work is that it must be used after the step in which the generated artifact of the step is to be cached. For example in the screen shot, to cache dependencies, the **Cache Push** step is used after the [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/cocoapods-install) step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pushOrder.png' />

:::


### Input Variables

The parameters required for the operation of this step are given in the list below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2911-pushInput.png' />

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_CACHE_LABEL`          | User defined cache label to identify one cache from others. Both cache push and pull steps should have the same value to match. | Required |
| `$AC_CACHE_INCLUDED_PATHS`       | Specifies the files and folders which should be in cache. Multiple glob patterns can be provided as a colon-separated list. For example; `.gradle:app/build` or `./Pods` | Required |
| `$AC_CACHE_EXCLUDED_PATHS`       | Specifies the files and folders which should be ignored from cache. Multiple glob patterns can be provided as a colon-separated list. For example; `.gradle/*.lock:*.apk` | Optional |
| `$AC_REPOSITORY_DIR`       | Specifies the cloned repository path. This path will be generated after run [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step. | Optional |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-cache-push-component