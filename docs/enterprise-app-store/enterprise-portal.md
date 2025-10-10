---
title: Enterprise Portal 
description: Learn how to use Enterprise Portal in Appcircle
tags: [enterprise app store, enterprise portal setup, enterprise portal]
sidebar_position: 4
---

Appcircle features a separate distribution screen designed to facilitate easy downloading of shared applications.

For iOS and Android, users can log in via the shared link and view all the versions shared with them. Downloading iOS and Android binaries is managed through the specific flows for each operating system.

## Prerequisites

In order for your users to download IPA or APK files, those files must be signed with proper certificates or Keystore files.

Android apps can be signed with any Keystore if the user's device allows installing apps from other sources.

Although iOS apps can be signed with Ad-Hoc provisioning profiles for in-house distribution, this type of distribution is limited to 100 devices per year. Once you hit that limit, you need to wait a year to reset your device limit. You also need to add the UUID of your users' device to Apple's Developer website. Therefore, Ad-Hoc distribution is intended for internal developer team members.

If you have more than 100 users and don't want to deal with device enrollment, you need to use sign your apps with Enterprise Certificate. Please check the Apple's Enterprise program for more information.

:::caution Signing Binary

Appcircle's Enterprise App Store module allows you to distribute your application without the need for any external tools. However, the way your app is signed remains your responsibility and depends on your own workflows; therefore, if you are not enrolled in the Apple Enterprise Program, Appcircle will not provide an enterprise signing service.

:::

https://developer.apple.com/programs/enterprise/

## Login

When a binary is shared with users through the share action for Live and Beta channels, they will receive a link for access.

Upon clicking the link, users will be redirected to the Enterprise Portal.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-store1.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-mobile1.png" />

:::info

Authentication method can be configured from the [store settings](/enterprise-app-store/portal-settings#store-authentication).

:::

:::warning

Please note that to login to the Enterprise Portal, you must enable cookies in your browser. Cookies help maintain your session and ensure secure access.

Refer to your browser's settings to enable cookies:

**Chrome**: Settings > Privacy and security > Cookies.
**Safari**: Preferences > Privacy.

:::

## Listing and Downloading App version

Once logged in, users will be able to see the app version shared from the Enterprise App Store profile. Files can be downloaded with a single click.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-newmobile.png" />

You can also navigate back to the app version list, where the shared binaries for the Live or Beta channels can be viewed. Each channel will display different app versions based on what was uploaded to the Enterprise App Store profile in Appcircle.

:::info

Beta channel users have access to both Live and Beta applications, while Live users can only view Beta versions.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-store3.png" />


:::info

Please note that to download and install an .IPA file, you must log in from an iOS device. 

Similarly, .APK files must be downloaded and installed from an Android device.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-mobile2.png" />

#### Log Out

Users can logout by selecting the profile icon in the top right corner of the screen.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-newlogout.png" />
