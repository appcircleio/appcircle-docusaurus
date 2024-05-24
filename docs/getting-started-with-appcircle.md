---
title: Getting Started With Appcircle
description: Appcircle is a mobile CI/CD platform which makes it easy for you to manage the lifecycle of your mobile applications.
tags: [getting started, mobile, ci/cd, platform]
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';

# Getting Started With Appcircle

Appcircle is a mobile CI/CD platform which makes it easy for you to manage the lifecycle of your mobile applications.

:::tip

Appcircle supports mobile applications developed in Swift/Objective-C, Java/Kotlin, React Native and Flutter for both iOS and Android.

:::

Before going through with the documentation, you can also view the following introductory video about Appcircle:

<iframe width="560" height="315" src="https://www.youtube.com/embed/OUoZFGqJFdM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

A basic lifecycle of a mobile application can be broken down into 4 steps:

### Create or Add Signing Identities

Your mobile applications must be digitally signed to be able to distributed, tested and, submitted to app stores.

For iOS applications, you must have a signing certificate and provisioning profiles to be able to run your application on real devices and submit them to Apple Appstore.

<ContentRef url="/signing-identities/ios-certificates-and-provisioning-profiles">
  iOS Certificates &amp; Provisioning Profiles
</ContentRef>

For Android applications, you need to create a keystore file to sign your applications digitally.

<ContentRef url="/signing-identities/android-keystores">Android Keystores</ContentRef>

###

### Create Building Profiles

Building your mobile applications is very easy with Appcircle no matter what platform and language you are using. You can connect your repositories from GitHub, Bitbucket, or GitLab to Appcircle.

You can also connect to public repositories directly or use SSH for custom repository connections. If you want to try out Appcircle, you can find sample apps for different frameworks in [Appcircle GitHub](https://github.com/appcircleio?q=sample).

Appcircle will fetch all your branches and commits in your repository and lets you build any commit you want to test your application.

<ContentRef url="/build/manage-the-connections/adding-a-build-profile">Adding a Build Profile</ContentRef>

Configure your build profile and select project parameters, signing options, distribution profiles and environment variables. Your project will be built using these settings and options.

<ContentRef url="/build/build-process-management/build-profile-configuration">Build Profile Configuration Overview</ContentRef>

You can customize your build flow using our workflow editor. Workflow editor allows you to be in control of the build process. You can add or remove build steps, add your custom scripts for advanced build processes.

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

You can also automate your build process by telling Appcircle to automatically build your code with every push to your repository. There are also options including tagged pushes for more advanced cases.

<ContentRef url="/build/build-process-management/build-manually-or-with-triggers">
  Build Manually or Automatically with Webhooks and Triggers
</ContentRef>

###

### Distribute Your Applications

Distribution is a very major and important step for testing and deploying a mobile application.

Create testing groups, add testers to testing groups and assign these groups to distribution profiles to distribute your build to testers so that they can download and install applications on their devices.

<ContentRef url="/distribute/testing-management/testing-groups">Testing Groups</ContentRef>

If you have a team of testers, you can create testing groups and distribute builds to your testers manually or automatically after each build and let them run the application on their mobile devices.

<ContentRef url="/distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

### Submit to the Public App Stores

You can manually or automatically send your binaries to respective app stores.

Send a binary to Apple Testflight or App Store.

<ContentRef url="/publish-integrations/ios-publish-integrations/send-to-app-store">Send Apps to App Store Connect and TestFlight</ContentRef>

Send a binary to Google Play.

<ContentRef url="/publish-integrations/android-publish-integrations/publish-to-google-play">Send Apps to Google Play Console</ContentRef>

Send a binary to Huawei AppGallery.

<ContentRef url="/publish-integrations/android-publish-integrations/publish-to-huawei-appgallery">Send Apps to Huawei AppGallery</ContentRef>
