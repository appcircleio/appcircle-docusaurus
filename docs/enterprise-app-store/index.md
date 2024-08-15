---
title: Enterprise App Store
description: Distribute your in-house applications to your users with the Enterprise App Store in Appcircle
tags: [enterprise app store, in-house distribution, enterprise distribution, faq]
---

import ContentRef from '@site/src/components/ContentRef';

# Enterprise App Store

If you want to distribute your in-house applications to your users, you can use the **Enterprise App Store**.

Appcircle's Enterprise App Store helps you to set up your own store and have full control over deployment and access management.

### Prerequisites

In order for your users to download IPA or APK files, those files must be signed with proper certificates or Keystore files.

Android apps can be signed with any Keystore if the user's device allows installing apps from other sources.

Although iOS apps can be signed with Ad-Hoc provisioning profiles for in-house distribution, this type of distribution is limited to 100 devices per year. Once you hit that limit, you need to wait a year to reset your device limit. You also need to add the UUID of your users' device to Apple's Developer website. Therefore, Ad-Hoc distribution is intended for internal developer team members.

If you have more than 100 users and don't want to deal with device enrollment, you need to use sign your apps with Enterprise Certificate. Please check the Apple's Enterprise program for more information.

https://developer.apple.com/programs/enterprise/

## Enterprise App Store Profile

There are several ways to create an Enterprise App Store Profile. You can either manually upload your IPA or APK files or send them through Appcircle's Distribution, Build, or Publish modules.

## Store Customization

The Enterprise App Store module allows for tailoring the login page to reflect your organization's branding. You can customize the colors, update the title, and replace the logo to create a seamless and professional experience for your users.

## Store Settings

The Enterprise App Store Settings allows you to configure your store's authentication and domain settings.

## Enterprise Store

Enterprise Store allows you to share your applications via Beta and Live channels.

## Store Reports

You can access reports for your Enterprise App Store from this screen. The reports screen provides the following data through a clear and concise user interface.

## Enterprise App Store FAQ

### General Questions

#### What is Enterprise App Store?

Enterprise App Store is Appcircle's new feature that lets you create your own mobile app store for your in-house apps (apps that are not meant to be distributed through Apple's App Store and Google Play Store).

#### Can non-Enterprise companies use this feature?

Yes. From small teams to large enteprises, anybody can create their own app store.

#### What kind of apps can I put to my App Store

As long as they are signed with an Ad Hoc or Enterprise Distribution Certificate, all apps with .ipa or .apk/.aab files can be uploaded.

#### Can we customize our store and how?

Yes. You can customize your logo, primary and secondary color and the main text color.

#### How will users enter my App Store?

Once you go to your store's settings in Appcircle, you can define a prefix and Appcircle will give you a URL with the given prefix. Alternatively, you can use your own domain. (Not eligible on Starter, Developer, and Professional plans. Please [contact us](https://appcircle.io/contact) to request custom domains).

### Technical Questions

#### Is my app store accessible from desktop web?

Yes. Desktop users can access your app store and view the available apps through your store's URL. To install and run an app, you need to open the store from a mobile device. Desktop website will display a QR code next to your store to pen the page from mobile devices easily.

#### How can I create an Enterprise Distribution Certificate on iOS?

You have to be enrolled on [Apple Enterprise Developer Program](https://developer.apple.com/programs/enterprise/) ($299/year). You can alternatively use Ad Hoc certificates if you aren'a a member of the Enterprise Developer program (see question below).

#### Can I distribute apps signed with Ad Hoc / App Store Provisioning Profile from my Store?

You can distribute apps that are signed with an Ad Hoc certificate (iOS). Please note that your users' device identifiers must be added to Apple Developer Portal and should be included in the provisioning profile used in signing the build. Apps signed with App Store certificates can't be distributed.

### Billing Questions

#### What does downloads/month mean? How is the number calculated?

A download is calculated every time an app is downloaded from our servers. So a user downloading an app, updating to a new version and re-installing any version adds to the download count.

#### Do you offer plans specific to Enterprise App Store (without CI/CD features)?

Thanks to the modular structure of Appcircle, all modules can be used independently. Accordingly, you can also request a special plan only for Enterprise App Store. Please [contact us](https://appcircle.io/contact) for detailed information.