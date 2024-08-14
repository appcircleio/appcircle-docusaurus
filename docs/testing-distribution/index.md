---
title: Testing Distribution
description: Learn how to create a distribution profile and share your builds with testers in Appcircle
tags: [distribution, distribution profile, testing distribution, testers, faq]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';


In order to share your builds with testers, you can create distribution profiles and assign testing groups to the distribution profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/distribution-start.png' />

> Note that an empty Testing Distribution profile named **Send to Myself** will be created automatically for you.

:::info

A distribution profile corresponds to the multiple versions of the same application for iOS and Android. You do not need to create multiple Testing Distribution profiles for iOS and Android applications of the same application.
:::

<iframe width="600" height="315" src="https://www.youtube.com/embed/vZ3p5uZZcmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Distribution Profile

To share builds with testers, distribution profiles should be created and testing groups assigned to these profiles.

## Testing Groups

The testing group feature is used to manage and organize testers. Different versions of applications can be distributed to specific groups based on testing needs, such as OS versions, features, devices, and more.

## Apple Devices

When it comes to developing and testing iOS apps, one of the most important tasks is registering your devices with the Apple Developer portal. This is necessary so that you can install your app on those devices for testing purposes. However, this process can be a bit tedious, especially if you need to register a large number of devices. That's where Appcircle comes in.

## Re-sign Binaries

Re-signing is the process of modifying an existing binary with a new signing certificate or keystore, required when an application needs to be published under a different developer account or when updating an existing application. This process involves removing the original signature and replacing it with a new one.

## Testing Portal

Appcircle has a separate distribution screen designed to make it easy for test group developers and testers download the distributed applications easily.

## Reporting

Optimize your application management with detailed reports. Utilize the App Sharing Report and App Versions Report to gain insights and make informed decisions about your app's distribution and evolution.

## FAQ

### No files or multiple files were received from autodistribute;

A successful distribution depends on a correctly signed binary. Please check if the [signing configuration](/build/build-process-management/build-profile-configuration#signing-configuration) is correct.

You can also check the list of the [generated build artifacts](/build/post-build-operations/after-a-build) to confirm the output. In Android, you can also check the `ac_post_process_output.json` file in the build artifacts to see if the APKs are signed or not.

In Android, please also check if gradle sign is being used for the selected build variant. If gradle sign works alongside with Appcircle signing, you will receive multiple APKs.

### Deleted versions still occupy storage space

The master version of any artifact deployed from the Build to the Testing Distribution is stored within the build artifacts section. Once you delete such a version from the Testing Distribution, only the reference is removed and the binary is still available within the build artifacts of the related build. You also need to remove the binary from the build artifacts to save storage.

### Access Denied on builds

On some distributed apps, the **Access Denied** error can be bypassed by one of these steps:

- Launching the distribution link on a different browser and Incognito Mode
- Clearing the browser cache if the link is pasted to a browser instead of in-line browser on mail applications
- If there is an authorization configuration on Distribution, clearing the authorization temporarily
