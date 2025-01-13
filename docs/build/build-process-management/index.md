---
title: Build Profile
description: Learn how to manage your build processes effectively with Appcircle. Optimize your build configurations, manage branches, and automate your build pipeline for efficient app development.
tags:
  [
    build process management,
    build profiles,
    branch management,
    manual builds,
    automatic builds,
    app development,
    app deployment,
    appcircle build process,
  ]
---

This documentation provides step-by-step guidance for creating a new build profile in the Build module.

## Creating a Profile

A Build profile can be created by following these steps: 

- Click on the **Create New** button located at the top-right corner of the screen.

--ss--

- Provide a unique name for the build profile and choose a target Operating System (OS) which can be Android or iOS.

--ss--

- After selecting the target OS, specify the corresponding target platform to set up a compatible build environment:

iOS Platforms:
* Objective-C / Swift
* React Native
* Flutter

Android Platforms:
* Java / Kotlin
* React Native
* Flutter

--ss--

- Click **Save** to proceed.

- Choose from the available repository connection options to link your project source code:

* GitHub
* Azure
* Bitbucket
* GitLab
* Connect via SSH
* Connect via URL

--ss--

Alternatively, select Quick Start using the Sample Repository to explore the module using a pre-configured sample repository.

For detailed instructions on connecting to each repository, refer to the Connection Guides.

Once the repository connection is established, the build profile will be created successfully. You can now use the build profile to manage and deploy your projects.

## Configurations










<!-- Master the management of your build profiles in Appcircle with the following features: -->

<!-- - [**Profile Configuration**](/build/build-process-management/build-profile-configuration): Set up and manage the configurations for your build profiles. This involves specifying the settings that control the build process for each app version. -->

<!-- - [**Branch Management**](/build/build-process-management/build-profile-branch-operations): Organize and handle different code branches within your repository. This section allows you to manage which branches are built and when. -->

<!-- - [**Manual and Automatic Builds**](/build/build-process-management/build-manually-or-with-triggers): Control how and when your builds are triggered. Opt for manual builds for greater control, or set up automatic builds to streamline your development pipeline whenever changes are pushed to your branches. -->