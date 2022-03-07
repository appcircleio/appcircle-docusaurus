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

With cache you can persist any resource that are ignored from Git. So you can transfer files and folders between build pipelines. Sometimes it may speed up your build or it may help if you have reliability issues with the original download location for dependencies. But keep in mind that the cache is uploaded to or downloaded from remote location. It may help you in some cases, but it's not a guaranteed way of speeding up buils. You should try and see the actual results for your project.

The cache is stored as a single archive file. Cache push and pull components work in coordination on the same cache file defined with a label. With custom labelling you can have different chunks of caches and you can share some caches between branches. Cache labelling helps you organize your caches.

When you drag and drop cache push component to your workflow, it comes with pre-defined values according to your project type. For example, for android projects it comes with pre-defined gradle cache paths which should be useful for most Android apps.

If you need more paths to cache or need to change paths according to your project, you can customize included and excluded paths. All path updates will be reflected to archived cache file on your next build. For patterns that can be used in included and excluded paths is explained in detail, see following component link for more information.

You can not reach the cache archive file directly by yourself. But you can see cache file updates and track changes to cache at the end of build pipeline from "Download Artifacts". Also build logs has some information about cache mechanism with how included and excluded paths are processed.

You can not delete specific cache file from UI but if you have a problem with cache file, you can change your cache label to a new one to go on with clean cache. System will automatically clean up unreachable cache files periodically.

[https://github.com/appcircleio/appcircle-cache-push-component](https://github.com/appcircleio/appcircle-cache-push-component)

## Cache Pull

Cache push uploads cache archive file to remote location as we explained in detail above. On the other hand cache pull downloads and extracts that archive file in build pipeline. All files and folders are extracted to original locations that came from.

Cache push and pull components work in coordination on the same cache file. For this reason in order to download the pushed cache, cache pull must have the same cache label used in cache push. Also you can have more than one push and pull pairs in the same build pipeline according to your needs.

[https://github.com/appcircleio/appcircle-cache-pull-component](https://github.com/appcircleio/appcircle-cache-pull-component)
