---
title: Common Workflow Steps
description: Common workflow steps in Appcircle
tags: [workflow, steps, common]
---

import Screenshot from '@site/src/components/Screenshot';

# Common Workflow Steps

The steps listed below are common across all build profiles regardless of the target OS and platform.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Activate SSH Key

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

<ContentRef url="/workflows/common-workflow-steps/active-ssh-private-key">
    Active SSH Private Key
</ContentRef>

## Appium Server

This step installs [Appium Server](https://appium.io/) and starts it.

<ContentRef url="/workflows/common-workflow-steps/appium-server">
    Appium Server
</ContentRef>

## Authenticate with Netrc

The `.netrc` file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file. However, if you want to use the .netrc file with curl, you need to append the `-n` command line parameter. You may also use the `--netrc-optional` parameter if you don't always use the `.netrc` file with curl.

<ContentRef url="/workflows/common-workflow-steps/authenticate-with-netrc">
    Authenticate with Netrc
</ContentRef>

## Cache Pull

Cache push uploads cache archive file to remote location as we explained in detail above. On the other hand cache pull downloads and extracts that archive file in build pipeline. All files and folders are extracted to original locations that came from.

:::danger

Cache push and pull components should work in coordination on the same cache file. For this reason in order to download the pushed cache, cache pull must have the same cache label used in cache push.

:::

:::info

In the event that you need to utilize the cached folder in an alternate branch or a separate project, you have the capability to modify the values of `$AC_GIT_BRANCH` or `$AC_BUILD_PROFILE_ID`.

These variables can be adjusted within the **Cache Label** field, as indicated by the red highlight in the accompanying image. Simply replace them with the branch or project ID that corresponds to your intended usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/cache-01.png' />

:::

Also you can have more than one push and pull pairs in the same build pipeline according to your needs.

<ContentRef url="/workflows/common-workflow-steps/build-cache/cache-pull">
    Cache Pull
</ContentRef>

## Cache Push

Every single build at Appcircle runs in clean state. It means that all files and folders, that are not versioned in git repository, are lost when build pipeline is completed. For example, installed dependencies or build artifacts. If you need to keep those files and folders, you can use Appcircle cache push and pull components.

With cache you can persist any resource that are ignored from Git. So you can transfer files and folders between build pipelines. Sometimes it may speed up your build or it may help if you have reliability issues with the original download location for dependencies. But keep in mind that the cache is uploaded to or downloaded from remote location. It may help you in some cases, but it's not a guaranteed way of speeding up builds. You should try and see the actual results for your project.

:::info

Using **Cache Pull/Push** steps, particularly when employing repository management software like [Sonatype Nexus Repository](https://www.sonatype.com/products/sonatype-nexus-repository), may not always yield the desired efficiency in reducing build time.

:::

The cache is stored as a single archive file. Cache push and pull components work in coordination on the same cache file defined with a label. With custom labelling you can have different chunks of caches and you can share some caches between branches. Cache labelling helps you organize your caches.

When you drag and drop cache push component to your workflow, it comes with pre-defined values according to your project type. For example, for android projects it comes with pre-defined gradle cache paths which should be useful for most Android apps.

If you need more paths to cache or need to change paths according to your project, you can customize included and excluded paths as you wish. All path updates will be reflected to archived cache file on your next build.

Cache push uses a pattern in order to select files and folders. Although the pattern is not a regexp, it's closer to a shell glob. For example, `~/Library/Caches/CocoaPods` will select "Cocoapods" folder from home as a whole. Or for an android project you can cache home ".gradle" folder with `~/.gradle` include path and exclude all ".lock" files from there with `~/.gradle/**/*.lock` exclude path. Patterns, that can be used in included and excluded paths, is explained in detail [here](https://github.com/appcircleio/appcircle-cache-push-component#included--excluded-paths).

:::danger

Keep in mind that included paths and cache push step's workflow order are closely related with each other. For example, if you include a path from repository and you place cache push step before git clone step, cache push won't find that path since it's not git cloned yet. Although that's not a fatal error for cache push, it will inform you about unreachable paths on build logs. You can review and resolve those kinds of issues from build logs.

:::

You can not reach the cache archive file directly by yourself. But you can see cache file updates and track changes to cache at the end of build pipeline from "Download Artifacts > ac_cache.zip". Also build logs have some useful information about cache mechanism with how included and excluded paths are processed. You can see produced cache file size from build logs. (Size of cache file affects upload and download durations.)

:::danger

You can not delete specific cache file from UI but if you have a problem with cache file and need a fresh one, you can change your cache label to a new one to go on with clean cache.

:::

:::info

System automatically cleans unreachable and obsolete cache files periodically. For this reason, it's not guaranteed to reach a previously used cache file by using previous cache label in build. Also it’s a good idea to build your workflow in a way that your build won’t fail if the cache can’t be accessed.

:::

<ContentRef url="/workflows/common-workflow-steps/build-cache/cache-push">
    Cache Push
</ContentRef>

## Code Reviews with Danger

Danger runs during your CI process and gives teams the chance to automate common code review chores. This provides another logical step in your build, through this Danger can help lint your rote tasks in daily code review. You can use Danger to codify your team’s norms. Leaving humans to think about harder problems.

https://blog.appcircle.io/article/danger-in-ci-automate-your-mobile-code-reviews

<ContentRef url="/workflows/common-workflow-steps/danger">
    Code Reviews with Danger
</ContentRef>

## Custom Scripts

You can use custom scripts for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the build agent and you can use any functionality of the virtual machine as you need.

<ContentRef url="/workflows/common-workflow-steps/custom-script">
    Custom Scripts
</ContentRef>

## Data Theorem Mobile Secure

This component scans your app using Mobile Secure

<ContentRef url="/workflows/common-workflow-steps/data-theorem-mobile-secure">
    Data Theorem Mobile Secure
</ContentRef>

## Export Build Artifacts

Exports the specified build artifacts from the build agent to the Appcircle dashboard. The exported files will be available for download from the artifacts section of the completed build.

<ContentRef url="/workflows/common-workflow-steps/export-build-artifacts">
    Export Build Artifacts
</ContentRef>

## File Size Check

This component checks the file size and either warn or fail the workflow.

<ContentRef url="/workflows/common-workflow-steps/file-size-check">
    File Size Check
</ContentRef>

## Firebase App Distribution

Send your apps to be distributed via Firebase App Distribution

<ContentRef url="/workflows/common-workflow-steps/firebase-app-distribution">
    Firebase App Distribution
</ContentRef>

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component

## Fortify On Demand

This step installs [Fortify on Demand](https://www.microfocus.com/en-us/cyberres/application-security/fortify-on-demand/) and submits a Fortify on Demand Mobile Assessment

<ContentRef url="/workflows/common-workflow-steps/fod-mobile-assesment">
    Fortify On Demand
</ContentRef>

## FTP Upload

This component uploads file or folders to given FTP server.

<ContentRef url="/workflows/common-workflow-steps/ftp-upload">
    FTP Upload
</ContentRef>

## Git Clone

Clones the Git repository to the build agent with the given arguments.

<ContentRef url="/workflows/common-workflow-steps/git-clone">
    Git Clone
</ContentRef>

## Maestro Cloud Upload

This component uploasd both your app binary and flows to Maestro Cloud.

<ContentRef url="/workflows/common-workflow-steps/maestro-cloud-upload">
    Maestro Cloud Upload
</ContentRef>

## Repeato Mobile Test Automation

This component creates and automates UI tests for iOS and Android.

<ContentRef url="/workflows/common-workflow-steps/repeato-test-runner">
    Repeato Mobile Test Automation
</ContentRef>

## Release Notes

You can use Release Notes component to create release notes during your workflow.

<ContentRef url="/workflows/common-workflow-steps/publish-release-notes">
    Release Notes
</ContentRef>

## SonarQube

You can use SonarQube component to check your code quality.

<ContentRef url="/workflows/common-workflow-steps/sonarqube">
    SonarQube
</ContentRef>

## Snyk Scan Security

By utilizing this step, you will be able to test your project dependencies for vulnerabilities during builds and use Snyk to monitor your projects.

<ContentRef url="/workflows/common-workflow-steps/snyk-scan-security">
    Snyk Scan Security
</ContentRef>

## Testinium

This component runs your test plans with Testinium.

<ContentRef url="/workflows/common-workflow-steps/testinium">
    Testinium
</ContentRef>
