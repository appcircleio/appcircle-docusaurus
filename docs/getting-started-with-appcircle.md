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

<ContentRef url="/signing-identities">
  Apple Certificates &amp; Provisioning Profiles
</ContentRef>

For Android applications, you need to create a keystore file to sign your applications digitally.

<ContentRef url="/signing-identities/android-keystores">Android Keystores</ContentRef>

###

### Create Building Profiles

Building your mobile applications is very easy with Appcircle no matter what platform and language you are using. You can connect your repositories from GitHub, Bitbucket, or GitLab to Appcircle.

You can also connect to public repositories directly or use SSH for custom repository connections. If you want to try out Appcircle, you can find sample apps for different frameworks in [Appcircle GitHub](https://github.com/appcircleio?q=sample).

Appcircle will fetch all your branches and commits in your repository and lets you build any commit you want to test your application.

<ContentRef url="/build/manage-the-connections/connection-guides">Connection Guides</ContentRef>

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

<ContentRef url="/distribute/testing-groups">Testing Groups</ContentRef>

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

### Dashboard Overview

The Appcircle Dashboard provides a centralized view of your organization’s activity, usage, and resources. It is designed to give you a quick snapshot of your builds, distribution progress, store publishing status, and Enterprise App Store assets, along with fast access to your most frequently used modules.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE7498-1.png' />

:::info Organization Display
Please note that the displayed data belongs to the currently logged-in root organization. It does not include usage information or binary names from sub-organizations.
:::

#### Usage Summary

At the top of the Dashboard, you will find usage indicators summarizing the current limits and consumption of your plan:
- **Builds** – Total number of builds used within the current billing period.
- **Testing Distribution** – Number of downloaded distributed builds for testing.
- **Publishes** – Number of binaries published to external app stores.
- **Members** – The number of users currently active in the organization.
- **Concurrency** – The total number of concurrent build slots available to your plan.

#### Build Profiles

The Build Profiles section lists all configured profiles in the organization. Each profile displays:
- Platform badge (iOS or Android)
- Profile name
- Connected repository
- Quick navigation arrow to open the corresponding build profile

#### Last Builds

This section shows the most recent build activities across all profiles. Each row includes:
- Repository source (GitHub, GitLab, Bitbucket, SSH, Public, etc.)
- Build status (Running, Success, Failed, Canceled)
- The email of the user who triggered the build
- Quick access to build logs and details

#### Testing Distributions

All distributions created for internal testing are listed here. Each item displays:
- The distribution binary name
- The associated build artifact (IPA/APK file)
- A quick navigation link to open distribution details, testers, and installation access

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE7498-2.png' />

#### Publish to Stores

The Publish to Stores section displays binaries that are prepared or sent to app distribution services, such as:
- App Store Connect / TestFlight (iOS)
- Google Play Console (Android)
- Huawei AppGallery
- Microsoft Intune

:::tip 
Only RC (Release Candidate) marked binaries will be listed here.
:::

#### Enterprise App Store

If you use the Enterprise App Store module, this section lists your enterprise-distributed apps. Each enterprise app entry shows:
- The application name
- The binary version
- A link to the Enterprise App Store detail page