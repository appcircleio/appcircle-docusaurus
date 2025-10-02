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

<Screenshot url='https://cdn.appcircle.io/docs/assets/7140-30.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6562-autoResignSettingss.png' />

## Auto Re-sign Configuration

To use Appcircle’s Auto Re-sign feature, you must first define a **configuration**. Appcircle will refer to this configuration for each automatic re-signing process and re-sign the incoming binary accordingly.

:::info Auto Re-sign

Please note that if Auto Re-sign is **enabled** and the configuration is **completed**, the re-signing process will automatically begin as soon as a binary is uploaded to the associated profile.

:::

:::caution Auto Re-sign configuration

If the configuration is **not defined correctly**, the re-signing flow **may fail**. Please make sure that your configuration is accurate and properly set up before uploading your binary.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/7140-28.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/7140-29.png' />


## For iOS

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the iOS platform are explained step-by-step below.

### Information

From the **Information** tab under Auto Re-sign configuration, you can manage the application's bundle identifier and display name values.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-infoNew.png' />

#### Bundle Identifier

Appcircle Publish profiles can accept binaries with different bundle identifiers. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different bundle identifier is uploaded, it is re-signed according to the bundle identifier of the profile. The bundle identifier of the resulting re-signed binary is updated to match the one associated with the profile. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-informationBundle.png' />

> ⚠️ Note: Release flows cannot be initiated with a binary whose bundle identifier differs from that of the profile. For more information, please visit the Binary Management [documentation](/publish-module/binary-management).


:::caution Multiple Target Binary

If the binary to be re-signed has multiple targets, each target bundle identifiers **must be registered** in your **Apple Developer** portal. Otherwise, you **may encounter errors** during the re-signing process.

:::

#### Display Name

With the **Display Name** parameter, you can change the visible name of the binary that will be re-signed. The re-signing process starts with the specified display name, and once completed, the `CFBundleDisplayName` value inside the binary is updated accordingly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-displayNameNew.png' />

### Versioning

By utilizing the versioning capability of the Auto Re-sign feature, you can modify the version and build number of the incoming binary according to the defined strategy during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-versioningNew.png' />

#### Update Build Number

With the **Update Build Number** feature, you can automatically increment the build number of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new build number will be generated based on the given offset before the re-signing begins, and the binary will be signed with this updated build number.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-updateBuildNumberNeww.png' />


- **Build Number Source**: The defined base build number will be used for versioning during the re-signing process. **App Store**, **TestFlight**, and **Uploaded Binary** are available options.
    - **App Store**: The build number will be calculated based on the latest live version available on the **Apple App Store**.
    - **TestFlight**: The build number will be determined by referencing the latest version available on **TestFlight**.
    - **Uploaded Binary**: The build number or version code will be calculated from the **most recent binary** uploaded to Appcircle.
- **Build Number**: The offset value is a number to be added or subtracted from the **build number source**.


#### Update Version Number

With the **Update Version Number** feature, you can automatically increment the version number  of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version number will be generated before the re-signing begins, based on the selected increment strategy and offset, and the binary will be signed with this updated version number.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-updateVersionNumberNew.png' />

- **Version Number**: The defined base version number will be used for versioning during the re-signing process. **App Store**, **TestFlight**, and **Uploaded Binary** are available options
    - **App Store**: The version number will be calculated by referencing the latest live version available on the **Apple App Store**.
    - **TestFlight**: The version number will be determined based on the latest version available on **TestFlight**.
    - **Uploaded Binary**: The version number or version name will be calculated based on the most recently **uploaded binary** to Appcircle.
- **Version Number**: The offset value is a number to be added or subtracted from the **version number source**.
- **Increment Strategy**: You can increase the `major`, `minor`, or `patch` value of the version number.

:::caution Update Versioning

Within the Auto Re-sign feature configuration, if any store-based option is selected for versioning, it is mandatory to select an appropriate API key to retrieve the version information. If you do not want to perform versioning using the store, please select the **Uploaded Binary** option instead.

For more information, please visit the **Credentials** [documentation.](/account/my-organization/security/credentials)

:::

### Signing

Appcircle requires valid certificate and provisioning profile to successfully perform the auto re-sign process. The re-signing begins using the associated certificates and provisioning profile..

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-signingNew.png' />


#### App Store Credential

Appcircle’s Auto Re-sign feature requires an **App Store Connect** credential. Therefore, selecting a credential is mandatory for both versioning and signing processes. This credential is used to download the necessary signing assets and retrieve version-related information when versioning is configured to use App Store data.

For more information, please visit the **App Store Connect API Key** [documentation](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key).

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-credentialNew.png' />

#### Signing Method

The **Signing Method** defines how Appcircle selects the provisioning profile during the re-signing process. This strategy determines whether Appcircle should use an existing provisioning profile. Selecting the appropriate signing strategy ensures compatibility with your target distribution method and proper signing of your binary.

For more information about these signing strategies, please visit the Apple Profiles [documentation](/signing-identities/apple-profiles).

:::caution Enterprise API Key and In-house Signing

The Auto Re-sign feature also supports **In-house** signing. You can perform this by selecting an **Enterprise API Key**. However, please note that only In-house signing is allowed with an Enterprise Key—attempting to use it with any other signing method will result in an error.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-signingMethodNeww.png' />

#### Create a New Provision Profile

If the **Create a New Provision Profile** option is enabled, Appcircle generates a valid provisioning profile for signing using the Apple API Key selected in the profile settings and your Apple Developer account. If this option is disabled, Appcircle matches an existing valid provisioning profile from your Apple Developer portal for the signing process.

:::caution Create a New Provision Profile

If you **do not** want to create the provisioning profile for signing, Appcircle will attempt to match a valid provisioning profile and use it for the signing process. When this option is disabled and a matching provisioning profile cannot be found, a new provisioning profile will be automatically created.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-createNew.png' />

#### Using Existing Provisioning Profile

When using the Auto Re-sign feature, Appcircle also provides the option to select an existing provisioning profile. If the **Create a New Provision Profile** option is not enabled, the user can manually select a provisioning profile. To be selectable, the relevant profile must already be uploaded under **Apple Profiles** in the **Signing Identity** module.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Profiles](/signing-identities/apple-profiles) documentations.

:::caution Existing Provision Profile

If no provisioning profile is selected, Appcircle will still **attempt to match** a provisioning profile using the selected **App Store Credential**. If the provisioning profile **cannot be found** in the **Apple Developer portal**, a new one **will be generated**. 

For example, if the binary being signed has multiple targets and only one provisioning profile has been selected, Appcircle **will try to find** the related provisioning profiles for the other targets in the **Apple Developer portal**, and if they are not found, **it will generate them**.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-useExistingNew.png' />


#### Certificates

In addition to the selected signing strategy, Appcircle requires a corresponding certificate to perform the auto re-sign process. Therefore, make sure that your certificates are uploaded under the **Apple Certificate** section in the **Appcircle Signing Identity module**. The re-signing process will begin using the certificate you have selected.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Certificates](/signing-identities/apple-certificates) documentations.

:::caution Enterprise API Key and In-house signing

If you want to perform **In-house** signing using an **Enterprise API** Key, make sure that a compatible signing certificate is selected. Otherwise, Appcircle will not be able to verify the certificate and the signing process will fail.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-certNew.png' />


## For Android

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the Android platform are explained step-by-step below.

### Information

From the Information tab under Auto Re-sign configuration, you can manage the application's package identifier value.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-androidInfo.png' />

#### Package Identifier

Appcircle Publish profiles can accept binaries with different package name. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different package name is uploaded, it is re-signed according to the package name of the profile. The package name of the resulting re-signed binary is updated to match the one associated with the profile. 

> ⚠️ Note: Release flows cannot be initiated with a binary whose package name differs from that of the profile. For more information, please visit the Binary Management [documentation](/publish-module/binary-management).

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-packageIdNew.png' />

### Versioning

By utilizing the versioning capability of the Auto Re-sign feature, you can modify the version code and version name of the incoming binary according to the defined strategy during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-androVersioningNew.png' />

#### Update Version Code

With the **Update Version Code** feature, you can automatically increment the version code of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version code will be generated based on the given offset before the re-signing begins, and the binary will be signed with this updated version code.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-updateVersionCodeNew.png' />

- **Version Code Source**: The defined base version code will be used for versioning during the re-signing process. **Google Play**, and **Uploaded Binary** are available options.
    - **Google Play**: The version code will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The version code will be calculated from the **most recent binary** uploaded to Appcircle.
- **Version Code Offset**: The offset value is a number to be added or subtracted from the **version code source**.

#### Update Version Name

With the **Update Version Name** features, you can automatically increment the version name of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version name will be generated before the re-signing begins, based on the selected increment strategy and offset, and the binary will be signed with this updated version name.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-updateVersionNameNew.png' />

- **Version Number/Version Name Source**: The defined base version name will be used for versioning during the re-signing process. **Google Play** and **Uploaded Binary** are available options
    - **Google Play(Android)**: The version name will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The version name will be calculated based on the most recently **uploaded binary** to Appcircle.
- **Version Name Offset**: The offset value is a number to be added or subtracted from the **version name source**.
- **Increment Strategy**: You can increase the `major`, `minor`, or `patch` value of the version name.


:::caution Update Versioning

Within the Auto Re-sign feature configuration, if any store-based option is selected for versioning, it is mandatory to select an appropriate API key to retrieve the version information. If you do not want to perform versioning using the store, please select the **Uploaded Binary** option instead.

For more information, please visit the **Credentials** [documentation.](/account/my-organization/security/credentials)

:::

### Signing

Appcircle requires a necessary Keystore to successfully perform the auto re-sign process. The re-signing begins using the associated keystore.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-signingNewAndro.png' />

#### Google Play Console Credential

A **Google Play Console** credential is only required if versioning is configured to use store-based data. When versioning is set to retrieve version information from the Google Play Console, an API key must be provided to access live version details during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-androCredNew.png' />

#### Keystores

The **Keystores** section is where you manage the signing credentials required for Android re-signing. To successfully perform the auto re-sign process, Appcircle needs access to a valid keystore. You must upload the keystore file, provide the necessary alias, and enter the key and store passwords within the **Android Keystores** section of the **Signing Identity** module. The re-signing will be executed using the selected keystore credentials.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Android Keystores](/signing-identities/android-keystores) documentations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-androKeystoreNew.png' />

#### Convert AAB To APK

The **Convert AAB to APK** option allows you to automatically convert an Android App Bundle (AAB) file into an APK during the re-signing process. This is especially useful when your distribution channel requires an `APK` instead of an `AAB`. When enabled, Appcircle will handle the conversion and signing of the resulting APK seamlessly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/CSM125-androConvertNew.png' />