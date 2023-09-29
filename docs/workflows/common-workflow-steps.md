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

:::info

In the event that you need to utilize the cached folder in an alternate branch or a separate project, you have the capability to modify the values of `$AC_GIT_BRANCH` or `$AC_BUILD_PROFILE_ID`. These variables can be adjusted within the `Cache Label` field, as indicated by the red highlight in the accompanying image. Simply replace them with the branch or project ID that corresponds to your intended usage.

![](<https://cdn.appcircle.io/docs/assets/cache-01.png>)

:::

Also you can have more than one push and pull pairs in the same build pipeline according to your needs.

[https://github.com/appcircleio/appcircle-cache-pull-component](https://github.com/appcircleio/appcircle-cache-pull-component)

## Release Notes

You can use Release Notes component to create release notes during your workflow.

[https://github.com/appcircleio/appcircle-release-notes-component](https://github.com/appcircleio/appcircle-release-notes-component)

## SonarQube

You can use SonarQube component to check your code quality.

[https://github.com/appcircleio/appcircle-sonarqube-component](https://github.com/appcircleio/appcircle-sonarqube-component)

## Appium Server

This step installs [Appium Server](https://appium.io/) and starts it.

https://github.com/appcircleio/appcircle-appium-component

## Firebase App Distribution

Send your apps to be distributed via Firebase App Distribution

[https://github.com/appcircleio/appcircle-firebase-distribution-component](https://github.com/appcircleio/appcircle-firebase-distribution-component)

## Firebase Deployment

Deploy your web applications to Firebase Hosting

https://github.com/appcircleio/appcircle-firebase-deploy-component


## Firebase Upload dSYM

Upload your debug symbols to Firebase Crashlytics

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component

## Fortify On Demand

This step installs [Fortify on Demand](https://www.microfocus.com/en-us/cyberres/application-security/fortify-on-demand/) and submits a Fortify on Demand Mobile Assessment

https://github.com/appcircleio/appcircle-fod-mobile-assessment

## Code Reviews with Danger

Danger runs during your CI process and gives teams the chance to automate common code review chores. This provides another logical step in your build, through this Danger can help lint your rote tasks in daily code review. You can use Danger to codify your team’s norms. Leaving humans to think about harder problems.

https://github.com/appcircleio/appcircle-danger-component

https://blog.appcircle.io/article/danger-in-ci-automate-your-mobile-code-reviews

## Authenticate with netrc

The `.netrc` file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file. However, if you want to use the .netrc file with curl, you need to append the `-n` command line parameter. You may also use the `--netrc-optional` parameter if you don't always use the `.netrc` file with curl.

https://github.com/appcircleio/appcircle-netrc-component

## File size check

This component checks the file size and either warn or fail the workflow.

https://github.com/appcircleio/appcircle-filesize-component

## FTP Upload

This component uploads file or folders to given FTP server.

https://github.com/appcircleio/appcircle-ftp-upload-component


## Testinium

This component runs your test plans with Testinium.

https://github.com/appcircleio/appcircle-testinium-component

## Maestro Cloud Upload

This component uploasd both your app binary and flows to Maestro Cloud.

https://github.com/appcircleio/appcircle-maestro-cloud-upload-component

## Data Theorem Mobile Secure

This component scans your app using Mobile Secure

https://github.com/appcircleio/appcircle-datatheorem-component

## Repeato Mobile Test Automation

This component creates and automates UI tests for iOS and Android. 

https://github.com/appcircleio/appcircle-repeato-component

## Snyk Scan Security

By utilizing this step, you will be able to test your project dependencies for vulnerabilities during builds and use Snyk to monitor your projects.

https://github.com/appcircleio/appcircle-snyk-scan-secure-component