---
title: Android Keystores
description: Learn how to manage Android keystores in Appcircle
tags: [android, android keystores, keystore, signing, signing identities]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Android Keystores

You need to sign your Android applications with a keystore in order to install and test your application on virtual or real devices and submit your application to Google Play store.

Android keystores can be generated in Appcircle or pre-obtained keystores can be uploaded to use for signing Android applications. If you want to generate keystore in your machine, you can use [KeyStore Explorer](https://keystore-explorer.org).

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-04-Android-Keystores.png' />

### 1. Generate Android Keystores

You can create a keystore just by entering the necessary information. No additional software is needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-05-Generate-Android-Keystores.png' />

### 2. Upload Android Keystore File

Upload your readily available keystore file along with the password(s).

:::info

Only files with .keystore extension can be uploaded.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8651-keystorenewpage.png' />

Builds with debug type will be signed with a default keystore and don't need a keystore file to be uploaded to Appcircle. If you are building your app for distribution, you need to upload your keystore file in order to have your application signed.

:::info Android Keystore Expiration Notifications

You will be notified when an Android Keystore is about to expire. You can see the expiration notification in the [in-app notification window](/account/my-account/in-app-notifications) and optionally enable expiration [notifications](/account/my-organization/notifications) for Email, Slack, Microsoft Teams, etc.

**Standard Schedule**: Keystores already in the system 30+ days before expiration receive notifications at 30, 15, 7, 3, 1 days before expiration, plus expiring today.

**Late Upload**: Keystores uploaded with less than 30 days remaining before expiration get notifications starting from upload day, then continuing with the next applicable intervals from the standard schedule.

:::

### Uploading a Multi-Alias Keystore

Appcircle supports uploading multi-alias Android keystores. If your keystore contains more than one alias, you can upload the same keystore multiple times by using a different alias for each entry.

:::info

Make sure that the alias and password you enter belong to the same key entry. Different aliases from the same keystore can be uploaded separately, but each one must be added with its correct alias and password.

:::

### Sharing Android Keystores

Root Organization users have the ability to share their Android Keystores with Sub-Organizations. 

Shared keystores can be used in Sub-Organizations just like locally created or uploaded keystores.

#### How to Share Android Keystores

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8525-15.png' />

1. Navigate to the Android Keystores Section  
   Go to the Signing Identity module and open the **Android Keystores** section.

2. Open Keystore List  
   Locate the keystore you want to share.

3. Select the Keystore  
   Click the **Share** icon under the Actions column.

4. Configure Sharing Settings  
   In the Share panel:

- Enable **Share with all sub-organizations** to automatically share the keystore with all existing and newly created sub-organizations.
- Alternatively, manually select specific sub-organizations.

5. Save Sharing Configuration  
   Click **Share** to complete the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8525-16.png' />

#### Behavior in Sub-Organizations

- Shared keystores will be visible and selectable in Sub-Organizations.
- These keystores will be marked with a **Shared** on Root Organizations and **Inherited** tag on Sub Organizations.
- Sub-Organization users **cannot edit, rename, or delete** shared keystores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8525-18.png' />

:::tip
- If **Share with all sub-organizations** is enabled, the keystore will also be automatically available in newly created sub-organizations.
:::

:::caution
- Any changes or deletions made in the Root Organization will affect all Sub-Organizations using the shared keystore.
:::

### In-Project Keystore Usage

You can alternatively have your signing details stored in your Gradle file and use your in-project keystore to sign your app.;

Go to build workflow editor and disable Sign Application step to use your keystore in your Gradle file.

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::

## FAQ

### What to Do if I Lost My Keystore (Signing File)

First, the keystore is essential for verifying app ownership and enabling updates on platforms like [Google Play](https://play.google.com/store/) or [Huawei AppGallery](https://consumer.huawei.com/tr/mobileservices/appgallery/). 

If you have lost your keystore, here are the steps you can take:

#### Google Play:

The [Google Play Console](https://play.google.com/console/) can't restore a lost signing file, but it does let you reset it. To reset your signing file, follow these steps:

:::info

Only the account owner on Google Play Console can reset the signing file.

:::

1. Go to [Google Play Console](https://play.google.com/console/).
2. Select the app for which you want to reset the signing file.
3. Click the `App signing` under the `⚙️ Setup` section.
4. Scroll down and click the `Request upload key reset` button.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/02-07-Upload-Android-Keystores.png'/>

5. Choose `I lost my upload key`.

  <Screenshot url='https://cdn.appcircle.io/docs/assets/02-08-Upload-Android-Keystores.png' />

6. Generate a new upload key via [Appcircle](#1-generate-android-keystores) or [follow these instructions.](https://support.google.com/googleplay/android-developer/answer/9842756#create).
7. Export the upload key certificate as a PEM file using the provided command.
8. Upload the PEM file.
9. Click the `Request` button.
3. You’ll receive an email within a few days if your request is approved by the Google Play Console team.

:::tip

To cancel the reset request, click `Cancel Request` under the `Request upload key reset` header after step **9**.

:::

:::warning

> Resetting your upload key doesn’t affect the app signing key that Google Play uses to re-sign APKs before delivering them to users.

For more details, please check Google Play's documentation:
- [Lost or compromised upload key?](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en-GB#lost)

:::

#### Huawei AppGallery:

Whether you can release the same app after losing the keystore on Huawei AppGallery depends on if you have previously used [Huawei App Signing Service](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-appsigning-newapp-0000001052418290).

- **Without App Signing Service:** You cannot update the app. You'll need either a new package name or a key change, which will require all users to reinstall the app.
  
- **With App Signing Service:** Your key is protected on the server. You only need to manage your upload key, and even if it's lost, you can still update the app without user impact.