---
title: Android Keystores
metaTitle: Android Keystores
metaDescription: Android Keystores
sidebar_position: 2
---

# Android Keystores

You need to sign your Android applications with a keystore in order to install and test your application on virtual or real devices and submit your application to Google Play store.

Android keystores can be generated in Appcircle or pre-obtained keystores can be uploaded to use for signing Android applications. If you want to generate keystore in your machine, you can use [KeyStore Explorer](https://keystore-explorer.org).

![](https://cdn.appcircle.io/docs/assets/02-04-Android-Keystores.png)

### 1. Generate Android Keystores

You can create a keystore just by entering the necessary information. No additional software is needed.

![](https://cdn.appcircle.io/docs/assets/02-05-Generate-Android-Keystores.png)

### 2. Upload Android Keystore File

Upload your readily available keystore file along with the password(s).

:::info

Only files with .keystore extension can be uploaded.

:::

![](https://cdn.appcircle.io/docs/assets/02-06-Upload-Android-Keystores.png)

Builds with debug type will be signed with a default keystore and don't need a keystore file to be uploaded to Appcircle. If you are building your app for distribution, you need to upload your keystore file in order to have your application signed.

### In-Project Keystore Usage

You can alternatively have your signing details stored in your Gradle file and use your in-project keystore to sign your app.;

Go to build workflow editor and disable Sign Application step to use your keystore in your Gradle file.

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::
