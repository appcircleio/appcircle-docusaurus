---
title: Enterprise App Store Frequently Asked Questions (FAQ)
metaTitle: Enterprise App Store Frequently Asked Questions (FAQ)
metaDescription: Find answers to frequently asked questions about Appcircle's Enterprise App Store feature.
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';

# Enterprise App Store FAQ

## General Questions

### What is Enterprise App Store?

Enterprise App Store is Appcircle's new feature that lets you create your own mobile app store for your in-house apps (apps that are not meant to be distributed through Apple's App Store and Google Play Store).

### Can non-Enterprise companies use this feature?

Yes. From small teams to large enteprises, anybody can create their own app store.

### What kind of apps can I put to my App Store

As long as they are signed with an Ad Hoc or Enterprise Distribution Certificate, all apps with .ipa or .apk/.aab files can be uploaded.

### Can we customize our store and how?

Yes. You can customize your logo, primary and secondary color and the main text color.

### How will users enter my App Store?

Once you go to your store's settings in Appcircle, you can define a prefix and Appcircle will give you a URL with the given prefix. Alternatively, you can use your own domain. (Not eligable on Starter, Developer and Professional and AppSumo plans. Please contact sales@appcircle.io to request custom domains).

## Technical Questions

### Is my app store accessible from desktop web?

Yes. Desktop users can access your app store and view the available apps through your store's URL. To install and run an app, you need to open the store from a mobile device. Desktop website will display a QR code next to your store to pen the page from mobile devices easily.

### How can I create an Enterprise Distribution Certificate on iOS?

You have to be enrolled on Apple's Enterprise Developer Program ($299/year). You can alternatively use Ad Hoc certificates if you aren'a a member of the Enterprise Developer program (see question below).

### Can I distribute apps signed with Ad Hoc / App Store Provisioning Profile from my Store?

You can distribute apps that are signed with an Ad Hoc certificate (iOS). Please note that your users' device identifiers must be added to Apple Developer Portal and should be included in the provisioning profile used in signing the build. Apps signed with App Store certificates can't be distributed.

## Billing Questions

### What does downloads/month mean? How is the number calculated?

A download is calculated every time an app is downloaded from our servers. So a user downloading an app, updating to a new version and re-installing any version adds to the download count.

### Do you offer plans specific to Enterprise App Store (without CI/CD features)?

Not yet.

## Appsumo Deal

### **Why I can't redeem multiple coupons for the same account?**

We've disabled coupon stacking due to prevent licensing issues.

### **I'm already an Appcircle CI/CD customer. Can I apply AppSumo code?**

Unfortunately, no.