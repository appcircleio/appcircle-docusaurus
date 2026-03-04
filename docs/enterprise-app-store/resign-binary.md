---
title: Re-sign Binary
description: Learn how to resign your iOS and Android application binaries within Appcircle Enterprise App Store to change provisioning profiles or app entitlements.
tags: [ios, android, resigning, provisioning profiles, keystore, entitlements, faq]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import RunnerUsage from '@site/docs/\_publish-steps-runner-usage-caution.mdx';

# Re-sign Binary

Enterprise App Store Re-Sign & Auto-Resign enables re-signing and automatic re-signing of iOS and Android applications distributed via the Enterprise App Store.

This feature allows controlled updates to build and version numbers, signing identities, and store credentials, while providing a unified re-sign flow for both manual and automated scenarios.

<RunnerUsage />

## iOS Re-sign

Manual iOS re-sign allows you to re-sign an existing IPA using a different signing configuration without rebuilding the application.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-r2.png' />

You can use manual re-sign to:
- Change the signing certificate or provisioning profile
- Update the bundle identifier to match the profile
- Modify the app display name
- Adjust version and build numbers before distribution

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an2.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an4.png' />

Manual re-sign operations are performed per app version and the resulting output is stored as a new re-signed artifact.

:::info iOS Re-sign Configurations 
For detailed information about Manual iOS Re-sign configurations, please refer to the [configuration](/enterprise-app-store/resign-binary#ios-auto-re-sign) section. The configuration structure for Manual and Auto Re-sign is the same. However, unlike Auto Re-sign, Manual Re-sign configurations must be reconfigured for each re-sign action.
:::

## Android Re-sign

Manual Android re-sign enables re-signing APK or AAB files using a different keystore configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an1.png' />

You can use manual re-sign to:
- Replace the signing keystore
- Update the package name to match the profile
- Modify version code and version name values
- Convert AAB files to APK if required for distribution

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a2.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a4.png' />

:::info Android Re-sign Configurations
For detailed information about Manual Android Re-sign configurations, please refer to the [configuration](/enterprise-app-store/resign-binary#android-auto-re-sign) section. The configuration structure for Manual and Auto Re-sign is the same. However, unlike Auto Re-sign, Manual Re-sign configurations must be reconfigured for each re-sign action.
:::

## Auto Re-sign Configurations

Auto Re-sign enables Appcircle to automatically re-sign newly uploaded binaries based on predefined signing and versioning rules.

Before using this feature, you must first configure the Auto Re-sign settings for the relevant platform (iOS or Android), including identifier management, versioning strategy, and signing credentials.

After completing the configuration, make sure to enable the Auto Re-sign option from the Enterprise App Store profile settings. Otherwise, newly uploaded binaries will not be re-signed automatically.

### iOS Auto Re-sign

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the iOS platform are explained step-by-step below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i1.png' />

#### Information

From the **Information** tab under Auto Re-sign configuration, you can manage the application's bundle identifier and display name values.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i2.png' />

_**Bundle Identifier**_

Appcircle Publish profiles can accept binaries with different bundle identifiers. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different bundle identifier is uploaded, it is re-signed according to the bundle identifier of the profile. The bundle identifier of the resulting re-signed binary is updated to match the one associated with the profile.

> ⚠️ Note: Release flows cannot be initiated with a binary whose bundle identifier differs from that of the profile. For more information, please visit the Binary Management [documentation](/publish-to-stores-module/binary-management).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i6.png' />

:::caution Multiple Target Binary

If the binary to be re-signed has multiple targets, each target bundle identifiers **must be registered** in your **Apple Developer** portal. Otherwise, you **may encounter errors** during the re-signing process.

:::

_**Select a Pool**_

The Pool Selection field defines which organization pool will be used to execute the Auto Re-sign process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i7.png' />

:::caution Pool Selection Is Mandatory
Auto Re-sign will not work if a pool is not selected.

If no pool is defined:
- The Auto Re-sign process will not start.
- Uploaded binaries will remain unsigned.
- No re-signed output will be generated for Publish profile.

Always ensure that a valid macOS pool is selected before saving the Auto Re-sign configuration.
:::

_**Display Name**_

With the **Display Name** parameter, you can change the visible name of the binary that will be re-signed. The re-signing process starts with the specified display name, and once completed, the `CFBundleDisplayName` value inside the binary is updated accordingly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i8.png' />

#### Versioning

By utilizing the versioning capability of the Auto Re-sign feature, you can modify the version and build number of the incoming binary according to the defined strategy during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i3.png' />

_**Update Build Number**_

With the **Update Build Number** feature, you can automatically increment the build number of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new build number will be generated based on the given offset before the re-signing begins, and the binary will be signed with this updated build number.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i9.png' />

- **Build Number Source**: The defined base build number will be used for versioning during the re-signing process. **App Store**, **TestFlight**, and **Uploaded Binary** are available options.
    - **App Store**: The build number will be calculated based on the latest live version available on the **Apple App Store**.
    - **TestFlight**: The build number will be determined by referencing the latest version available on **TestFlight**.
    - **Uploaded Binary**: The build number or version code will be calculated from the **most recent binary** uploaded to Appcircle.
- **Build Number**: The offset value is a number to be added or subtracted from the **build number source**.


_**Update Version Number**_

With the **Update Version Number** feature, you can automatically increment the version number  of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version number will be generated before the re-signing begins, based on the selected increment strategy and offset, and the binary will be signed with this updated version number.

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

#### Signing

Appcircle requires valid certificate and provisioning profile to successfully perform the auto re-sign process. The re-signing begins using the associated certificates and provisioning profile..

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i4.png' />


_**App Store Credential**_

Appcircle’s Auto Re-sign feature requires an **App Store Connect** credential. Therefore, selecting a credential is mandatory for both versioning and signing processes. This credential is used to download the necessary signing assets and retrieve version-related information when versioning is configured to use App Store data.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i11.png' />

For more information, please visit the **App Store Connect API Key** [documentation](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key).

_**Signing Method**_

The **Signing Method** defines how Appcircle selects the provisioning profile during the re-signing process. This strategy determines whether Appcircle should use an existing provisioning profile. Selecting the appropriate signing strategy ensures compatibility with your target distribution method and proper signing of your binary.

For more information about these signing strategies, please visit the Apple Profiles [documentation](/signing-identities/apple-profiles).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i13.png' />

:::caution Enterprise API Key and In-house Signing

The Auto Re-sign feature also supports **In-house** signing. You can perform this by selecting an **Enterprise API Key**. However, please note that only In-house signing is allowed with an Enterprise Key—attempting to use it with any other signing method will result in an error.

:::

_**Create a New Provision Profile**_

If the **Create a New Provision Profile** option is enabled, Appcircle generates a valid provisioning profile for signing using the Apple API Key selected in the profile settings and your Apple Developer account. If this option is disabled, Appcircle matches an existing valid provisioning profile from your Apple Developer portal for the signing process.

:::caution Create a New Provision Profile

If you **do not** want to create the provisioning profile for signing, Appcircle will attempt to match a valid provisioning profile and use it for the signing process. When this option is disabled and a matching provisioning profile cannot be found, a new provisioning profile will be automatically created.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i5.png' />

_**Using Existing Provisioning Profile**_

When using the Auto Re-sign feature, Appcircle also provides the option to select an existing provisioning profile. If the **Create a New Provision Profile** option is not enabled, the user can manually select a provisioning profile. To be selectable, the relevant profile must already be uploaded under **Apple Profiles** in the **Signing Identity** module.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Profiles](/signing-identities/apple-profiles) documentations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i10.png' />

:::caution Existing Provision Profile

If no provisioning profile is selected, Appcircle will still **attempt to match** a provisioning profile using the selected **App Store Credential**. If the provisioning profile **cannot be found** in the **Apple Developer portal**, a new one **will be generated**.

For example, if the binary being signed has multiple targets and only one provisioning profile has been selected, Appcircle **will try to find** the related provisioning profiles for the other targets in the **Apple Developer portal**, and if they are not found, **it will generate them**.

:::

_**Certificates**_

In addition to the selected signing strategy, Appcircle requires a corresponding certificate to perform the auto re-sign process. Therefore, make sure that your certificates are uploaded under the **Apple Certificate** section in the **Appcircle Signing Identity module**. The re-signing process will begin using the certificate you have selected.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Apple Certificates](/signing-identities/apple-certificates) documentations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-i12.png' />

:::caution Enterprise API Key and In-house signing

If you want to perform **In-house** signing using an **Enterprise API** Key, make sure that a compatible signing certificate is selected. Otherwise, Appcircle will not be able to verify the certificate and the signing process will fail.

:::

:::info Enabling Auto Re-sign
Once you configure the Auto Re-sign settings, you must enable the Auto Re-sign feature from the Enterprise App Store profile settings. Otherwise, newly uploaded binaries will not be re-signed automatically.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an7.png' />

### Android Auto Re-sign

The functionality and configuration steps of **Appcircle’s Auto Re-sign** feature for the Android platform are explained step-by-step below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a1.png' />

#### Information

From the Information tab under Auto Re-sign configuration, you can manage the application's package identifier value.

_**Package Identifier**_

Appcircle Publish profiles can accept binaries with different package name. The binary defined for the profile serves as the reference for Auto Re-sign. When a binary with a different package name is uploaded, it is re-signed according to the package name of the profile. The package name of the resulting re-signed binary is updated to match the one associated with the profile.

> ⚠️ Note: Release flows cannot be initiated with a binary whose package name differs from that of the profile. For more information, please visit the Binary Management [documentation](/publish-to-stores-module/binary-management).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a6.png' />

_**Select a Pool**_

The Pool Selection field defines which organization pool will be used to execute the Auto Re-sign process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a7.png' />

:::caution Pool Selection Is Mandatory
Auto Re-sign will not work if a pool is not selected.

If no pool is defined:
- The Auto Re-sign process will not start.
- Uploaded binaries will remain unsigned.
- No re-signed output will be generated for Publish profile.

Always ensure that a valid macOS pool is selected before saving the Auto Re-sign configuration.
:::

#### Versioning

By utilizing the versioning capability of the Auto Re-sign feature, you can modify the version code and version name of the incoming binary according to the defined strategy during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a9.png' />

_**Update Version Code**_

With the **Update Version Code** feature, you can automatically increment the version code of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version code will be generated based on the given offset before the re-signing begins, and the binary will be signed with this updated version code.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a8.png' />

- **Version Code Source**: The defined base version code will be used for versioning during the re-signing process. **Google Play**, and **Uploaded Binary** are available options.
    - **Google Play**: The version code will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The version code will be calculated from the **most recent binary** uploaded to Appcircle.
- **Version Code Offset**: The offset value is a number to be added or subtracted from the **version code source**.

_**Update Version Name**_

With the **Update Version Name** features, you can automatically increment the version name of the uploaded binary during the auto re-sign process using the specified offset value. When this feature is enabled, a new version name will be generated before the re-signing begins, based on the selected increment strategy and offset, and the binary will be signed with this updated version name.

- **Version Number/Version Name Source**: The defined base version name will be used for versioning during the re-signing process. **Google Play** and **Uploaded Binary** are available options
    - **Google Play(Android)**: The version name will be set by referencing the latest live version on **Google Play Console**.
    - **Uploaded Binary**: The version name will be calculated based on the most recently **uploaded binary** to Appcircle.
- **Version Name Offset**: The offset value is a number to be added or subtracted from the **version name source**.
- **Increment Strategy**: You can increase the `major`, `minor`, or `patch` value of the version name.


:::caution Update Versioning

Within the Auto Re-sign feature configuration, if any store-based option is selected for versioning, it is mandatory to select an appropriate API key to retrieve the version information. If you do not want to perform versioning using the store, please select the **Uploaded Binary** option instead.

For more information, please visit the **Credentials** [documentation.](/account/my-organization/security/credentials)

:::

#### Signing

Appcircle requires a necessary Keystore to successfully perform the auto re-sign process. The re-signing begins using the associated keystore.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a10.png' />

_**Google Play Console Credential**_

A **Google Play Console** credential is only required if versioning is configured to use store-based data. When versioning is set to retrieve version information from the Google Play Console, an API key must be provided to access live version details during the re-signing process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a11.png' />

_**Keystores**_

The **Keystores** section is where you manage the signing credentials required for Android re-signing. To successfully perform the auto re-sign process, Appcircle needs access to a valid keystore. You must upload the keystore file, provide the necessary alias, and enter the key and store passwords within the **Android Keystores** section of the **Signing Identity** module. The re-signing will be executed using the selected keystore credentials.

For more information, please visit the [Signing Identity Module](/signing-identities) and [Android Keystores](/signing-identities/android-keystores) documentations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a12.png' />

_**Convert AAB To APK**_

The **Convert AAB to APK** option allows you to automatically convert an Android App Bundle (AAB) file into an APK during the re-signing process. This is especially useful when your distribution channel requires an `APK` instead of an `AAB`. When enabled, Appcircle will handle the conversion and signing of the resulting APK seamlessly.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-a13.png' />

:::info Enabling Auto Re-sign
Once you configure the Auto Re-sign settings, you must enable the Auto Re-sign feature from the Enterprise App Store profile settings. Otherwise, newly uploaded binaries will not be re-signed automatically.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8261-an8.png' />