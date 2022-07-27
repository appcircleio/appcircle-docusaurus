---
title: Common Workflow Steps
metaTitle: Common Workflow Steps
metaDescription: Common Workflow Steps
sidebar_position: 2
---
# Common Workflow Steps

The steps listed below are common across all build profiles regardless of the target OS and platform.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Component Downloader

This is a built-in step present within the build agent and executed before every step in the workflow. It is responsible for downloading the sources of the next step/component in the workflow.

## Activate SSH Key

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

[https://github.com/appcircleio/appcircle-activate-ssh-key-component](https://github.com/appcircleio/appcircle-activate-ssh-key-component)

## Custom Scripts

You can use custom scripts for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the build agent and you can use any functionality of the virtual machine as you need.

[https://github.com/appcircleio/appcircle-custom-script-component/](https://github.com/appcircleio/appcircle-custom-script-component/)

## Git Clone

Clones the Git repository to the build agent with the given arguments.

[https://github.com/appcircleio/appcircle-git-clone-component](https://github.com/appcircleio/appcircle-git-clone-component)

## Export Build Artifacts

Exports the specified build artifacts from the build agent to the Appcircle dashboard. The exported files will be available for download from the artifacts section of the completed build.

[https://github.com/appcircleio/appcircle-export-build-artifacts](https://github.com/appcircleio/appcircle-export-build-artifacts)

## Cache Push

Every single build at Appcircle runs in clean state. It means that all files and folders, that are not versioned in git repository, are lost when build pipeline is completed. For example, installed dependencies or build artifacts. If you need to keep those files and folders, you can use Appcircle cache push and pull components.

With cache you can persist any resource that are ignored from Git. So you can transfer files and folders between build pipelines. Sometimes it may speed up your build or it may help if you have reliability issues with the original download location for dependencies. But keep in mind that the cache is uploaded to or downloaded from remote location. It may help you in some cases, but it's not a guaranteed way of speeding up builds. You should try and see the actual results for your project.

The cache is stored as a single archive file. Cache push and pull components work in coordination on the same cache file defined with a label. With custom labelling you can have different chunks of caches and you can share some caches between branches. Cache labelling helps you organize your caches.

When you drag and drop cache push component to your workflow, it comes with pre-defined values according to your project type. For example, for android projects it comes with pre-defined gradle cache paths which should be useful for most Android apps.

If you need more paths to cache or need to change paths according to your project, you can customize included and excluded paths as you wish. All path updates will be reflected to archived cache file on your next build.

Cache push uses a pattern in order to select files and folders. Although the pattern is not a regexp, it's closer to a shell glob. For example, `~/Library/Caches/CocoaPods` will select "Cocoapods" folder from home as a whole. Or for an android project you can cache home ".gradle" folder with `~/.gradle` include path and exclude all ".lock" files from there with `~/.gradle/**/*.lock` exclude path. Patterns, that can be used in included and excluded paths, is explained in detail [here](https://github.com/appcircleio/appcircle-cache-push-component#included--excluded-paths).

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

[https://github.com/appcircleio/appcircle-cache-push-component](https://github.com/appcircleio/appcircle-cache-push-component)

## Cache Pull

Cache push uploads cache archive file to remote location as we explained in detail above. On the other hand cache pull downloads and extracts that archive file in build pipeline. All files and folders are extracted to original locations that came from.

:::warning

Cache push and pull components should work in coordination on the same cache file. For this reason in order to download the pushed cache, cache pull must have the same cache label used in cache push.

:::

Also you can have more than one push and pull pairs in the same build pipeline according to your needs.

[https://github.com/appcircleio/appcircle-cache-pull-component](https://github.com/appcircleio/appcircle-cache-pull-component)

## Release Notes

You can use Release Notes component to create release notes during your workflow.

[https://github.com/appcircleio/appcircle-release-notes-component](https://github.com/appcircleio/appcircle-release-notes-component)

## SonarQube

You can use SonarQube component to check your code quality.

[https://github.com/appcircleio/appcircle-sonarqube-component](https://github.com/appcircleio/appcircle-sonarqube-component)