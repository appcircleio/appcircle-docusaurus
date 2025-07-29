---
title: Auto Re-sign
description: Learn how to automatically re-sign your binary in the Publish module of Appcircle
tags: [publish, publish module, auto, re-sign, configuration]
sidebar_position: 3
---

# Auto Re-sign

The **Auto Re-sign** feature in Appcircle’s Publish module allows users to automatically re-sign their iOS (`.ipa`) and Android (`.apk`/`.aab`) applications with a different keystore, provisioning profile, or certificate before distribution.

## Enabling Auto Re-sign

To use the **Auto Re-sign** feature in the Appcircle Publish module, you need to enable the **Auto Re-sign** toggle within the Publish Settings section.

:::caution Business Rule for Auto Publish and Auto Re-sign

Appcircle supports both **Auto Publish** and **Auto Re-sign** features. If both toggles are **enabled** simultaneously, Appcircle, by business rule, will first initiate the automatic re-signing process. Once the re-signing is complete, the automatic publishing process will begin. For more detailed information about **Auto Publish**, please refer to the Auto Publish [documentation](/publish-module/publish-settings#auto-publish).

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-autoResignSettingss.png' />

## Auto Re-sign Configuration

To use Appcircle’s Auto Re-sign feature, you must first define a **configuration**. Appcircle will refer to this configuration for each automatic re-signing process and re-sign the incoming binary accordingly.

:::info Auto Re-sign

Please note that if Auto Re-sign is **enabled** and the configuration is **completed**, the re-signing process will automatically begin as soon as a binary is uploaded to the associated profile.

:::

:::caution Auto Re-sign configuration

If the configuration is **not defined correctly**, the re-signing flow **may fail**. Please make sure that your configuration is accurate and properly set up before uploading your binary.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-settings1.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-settings2.png' />


### Versioning

By utilizing the versioning capability of the Auto Re-sign feature, you can modify the version and build number of the incoming binary according to the defined strategy during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-versioning.png' />


#### Display Name(Only iOS)

With the **Display Name** parameter, you can change the visible name of the binary that will be re-signed. The re-signing process starts with the specified display name, and once completed, the `CFBundleDisplayName` value inside the binary is updated accordingly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-dipslayName.png' />

#### Update Build Number and Version Code

With the **Update Build Number(iOS)** and **Update Version Code(Android)** features, you can automatically increment the build number/version code of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new build number/version code will be generated based on the given offset before the re-signing begins, and the binary will be signed with this updated build number/version code.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-updateBuildNumber.png' />

- **Build Number/Version Code Source**: The defined base build number will be used for versioning during the re-signing process. **App Store**, **TestFlight**, **Google Play** and **Uploaded Binary** are available options
    - **App Store**: The build number will be calculated by referencing the latest live version available on the **Apple App Store**.
    - **TestFlight**: The build number will be determined by referencing the latest version available on **TestFlight**.
    - **Google Play(Android)**: The version code will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The build number or version code will be calculated from the **most recent binary** uploaded to Appcircle.
- **Build Number/Version Code Offset**: The offset value is a number to be added or subtracted from the **build number source**.

#### Update Version Number and Version Name

With the **Update Version Number(iOS)** and **Update Version Name(Android)** features, you can automatically increment the version number/version name of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version number/version name will be generated before the re-signing begins, based on the selected increment strategy and offset, and the binary will be signed with this updated version number/version name.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-updateVersionNumber.png' />

- **Version Number/Version Name Source**: The defined base version number will be used for versioning during the re-signing process. **App Store**, **TestFlight**, **Google Play** and **Uploaded Binary** are available options
    - **App Store**: The version number will be calculated by referencing the latest live version available on the **Apple App Store**.
    - **TestFlight**: The version number will be determined by referencing the latest version available on **TestFlight**.
    - **Google Play(Android)**: The version name will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The version number or version name will be calculated based on the most recently **uploaded binary** to Appcircle.
- **Version Number/Version Name Offset**: The offset value is a number to be added or subtracted from the **version number source**.
- **Increment Strategy**: You can increase the `major`, `minor`, or `patch` value of the version number.


:::caution Version Number/Name and Build Number/Version Code

Within the Auto Re-sign feature configuration, if any store-based option is selected for versioning, it is mandatory to select an appropriate API key to retrieve the version information. If you do not want to perform versioning using the store, please select the **Uploaded Binary** option instead.

For more information, please visit the **Credentials** [documentation.](/account/my-organization/security/credentials)

:::

## For iOS

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the iOS platform are explained step-by-step below.

### Bundle Identifier Management

Appcircle Publish profiles can accept binaries with different bundle identifiers. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different bundle identifier is uploaded, it is re-signed according to the bundle identifier of the profile. The bundle identifier of the resulting re-signed binary is updated to match the one associated with the profile. 

> ⚠️ Note: Release flows cannot be initiated with a binary whose bundle identifier differs from that of the profile. For more information, please visit the Binary Management [documentation.](/publish-module/binary-management).


:::caution Multiple Target Binary

If the binary to be re-signed has multiple targets, each target **must be registered** in your **Apple Developer** portal. Otherwise, you **may encounter errors** during the re-signing process.

:::


### Signing

Appcircle requires a valid keystore to successfully perform the auto re-sign process. The re-signing begins using the associated keystore.

:::caution Apple Certificates

In order for Appcircle to initiate the auto re-sign process, a selected certificate must be available. Therefore, ensure that the certificate you want to use for signing is uploaded under the Apple Certificate section in the Appcircle Signing Identity module. 

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Certificates](/signing-identities/apple-certificates) documentations.

:::


#### App Store Credential

Appcircle’s Auto Re-sign feature requires an **App Store Connect** credential. Therefore, selecting a credential is mandatory for both versioning and signing processes. This credential is used to download the necessary signing assets and, if versioning is configured to use App Store data, to retrieve version-related information directly from the store.

For more information, please visit the **App Store Connect API Key** [documentation](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-apiKeySelection.png' />

#### Signing Method

The **Signing Strategy** defines how Appcircle selects the provisioning profile during the re-signing process. This strategy determines whether Appcircle should use an existing provisioning profile. Selecting the appropriate signing strategy ensures compatibility with your target distribution method and proper signing of your binary.

For more information about these signing strategies, please visit the Apple Profiles [documentation](/signing-identities/apple-profiles).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-signingMethodNew.png' />

#### Re-create Provision Profile

If the **Re-create Provision Profile** option is enabled, Appcircle generates a valid provisioning profile for signing using the Apple API Key selected in the profile settings and your Apple Developer account. If this option is disabled, Appcircle matches an existing valid provisioning profile from your Apple Developer portal for the signing process.

:::caution Re-create Provision Profile

If you **do not** want to re-create the provisioning profile for signing, Appcircle will attempt to match a valid provisioning profile and use it for the signing process. Please note that if the matched provisioning profile is close to its expiration date, the re-signed binary may fail to function once the profile expires.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-recreateProv.png' />


#### Certificates

In addition to the selected signing strategy, Appcircle requires a corresponding certificate to perform the auto re-sign process. Therefore, make sure that your certificates are uploaded under the **Apple Certificate** section in the **Appcircle Signing Identity module**. The re-signing process will begin using the certificate you have selected.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Certificates](/signing-identities/apple-certificates) documentations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-certsNew.png' />




## For Android

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the Android platform are explained step-by-step below.

### Package Name Management

Appcircle Publish profiles can accept binaries with different package name. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different package name is uploaded, it is re-signed according to the package name of the profile. The package name of the resulting re-signed binary is updated to match the one associated with the profile. 

> ⚠️ Note: Release flows cannot be initiated with a binary whose package name differs from that of the profile. For more information, please visit the Binary Management [documentation.](/publish-module/binary-management).


### Signing

Appcircle requires a necessary Keystore to successfully perform the auto re-sign process. The re-signing begins using the associated keystore.

:::caution Keystore

In order for Appcircle to initiate the auto re-sign process, a selected keystore must be available. Therefore, ensure that the keystore you want to use for signing is uploaded under the **Android Keystores** section in the Appcircle Signing Identity module. 

For more information, please visit the [Signing Identity Module](/signing-identities) and [Android Keystores](/signing-identities/android-keystores) documentations.

:::


#### Google Play Console Credential

A **Google Play Console** credential is only required if versioning is configured to use store-based data. When versioning is set to retrieve version information from the Google Play Console, an API key must be provided to access live version details during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-androApiKey.png' />

#### Keystores

The **Keystores** section is where you manage the signing credentials required for Android re-signing. To successfully perform the auto re-sign process, Appcircle needs access to a valid keystore. You must upload the keystore file, provide the necessary alias, and enter the key and store passwords within the **Android Keystores** section of the **Signing Identity** module. The re-signing will be executed using the selected keystore credentials.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-keystore.png' />

#### Convert AAB To APK

The **Convert AAB to APK** option allows you to automatically convert an Android App Bundle (AAB) file into an APK during the re-signing process. This is especially useful when your distribution channel requires an `APK` instead of an `AAB`. When enabled, Appcircle will handle the conversion and signing of the resulting APK seamlessly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6679-convert.png' />