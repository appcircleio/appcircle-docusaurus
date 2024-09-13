---
title: Android Keystores
description: Learn how to manage Android keystores in Appcircle
tags: [android, android keystores, keystore, signing, signing identities]
sidebar_position: 4
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

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-06-Upload-Android-Keystores.png' />

Builds with debug type will be signed with a default keystore and don't need a keystore file to be uploaded to Appcircle. If you are building your app for distribution, you need to upload your keystore file in order to have your application signed.

### In-Project Keystore Usage

You can alternatively have your signing details stored in your Gradle file and use your in-project keystore to sign your app.;

Go to build workflow editor and disable Sign Application step to use your keystore in your Gradle file.

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::

## FAQ

### What to Do if I Lost My Keystore (Signing File)

First, the keystore is essential for verifying app ownership and enabling updates on platforms like [Google Play](https://play.google.com/store/) or [Huawei AppGallery](https://consumer.huawei.com/tr/mobileservices/appgallery/). 

If you've lost your keystore, here's what you can do:

#### Google Play:

The [Google Play Console](https://play.google.com/console/) can't restore a lost signing file, but it does let you reset it. To reset your signing file, follow these steps:

:::INFO

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

For more detail please check Google Play's documantion:
- [Lost or compromised upload key?](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en-GB#lost)

:::

#### Huawei AppGallery:

Whether you can release the same app after losing the keystore on Huawei AppGallery depends on if you have previously used [Huawei App Signing Service](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-appsigning-newapp-0000001052418290).

- **Without App Signing Service:** You cannot update the app; you'll need a new package name or a key change, requiring all users to reinstall the app.
  
- **With App Signing Service:** Your key is protected on the server. You only need to manage your upload key, and even if it's lost, you can still update the app without user impact.