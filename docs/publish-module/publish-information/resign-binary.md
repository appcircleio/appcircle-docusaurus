---
title: Resign Binary
description: Learn how to resign your iOS application binaries within Appcircle to change provisioning profiles or app entitlements.
tags: [iOS, resigning, provisioning profiles, entitlements]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Resign Binary

The **Resign Binary** feature in Appcircle allows you to resign both iOS and Android application binaries. For iOS applications, you can use new provisioning profiles or modify the app's entitlements, which is useful for adjusting the app’s capabilities or updating its distribution settings without requiring a new build. For Android applications, you can resign your binaries with a new keystore, allowing you to update the app's signing credentials crucial for app distribution and updates.

This feature streamlines the process of updating app distribution and security settings, ensuring that your applications can be quickly adapted to meet changing requirements or distribution strategies.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub8.png' />

## Resign iOS Binary

When you need to distribute an iOS application to different environments (like QA, staging, or production) or need to change the app’s entitlements, the **Resign Binary** feature simplifies this process. You can resign an app binary with a new provisioning profile that matches the intended distribution certificate.

### Fields and Options

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-resignUI.png' />

#### Display Name

- **Field**: [`CFBundleDisplayName`](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundledisplayname)
- **Description**: The user-visible name for the bundle, used by Siri and visible on the iOS Home screen.

#### Version

- **Field**: [`CFBundleShortVersionString`](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring)
- **Description**: The release or version number of the bundle.

#### Build Number

- **Field**: [`CFBundleVersion`](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleversion)
- **Description**: The version of the build that identifies an iteration of the bundle.

#### Entitlements

- **Options**:
  - **Entitlements from provisioning profiles**: Existing entitlements in the signed provision profile.
  - **Edit**: Edit exist entitlements, or add or remove.


#### Targets

- **Description**: Select a new provisioning profile for new targets.

#### Bundle ID

- **Field**: [`CFBundleIdentifier`](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleidentifier)
- **Description**: Original Bundle ID.

:::caution BundleID
Please note that changing the **BundleID** is allowed while the related version is being resigned in the **Publish module**. However, you **cannot start** a publish operation unless it matches the Bundle ID defined for the [Publish Profile](/publish-module/creating-publish-profiles#create-profile-manually).
:::

#### Provisioning Profiles

- **Description**: Select a new provisioning profile for the Bundle ID.

### Edit Entitlements

With the entitlement editing feature of the Resign Binary feature in the Publish module of Appcircle. If you want, you can change your existing entitlements or add or remove them.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-entitlementEdit.png' />

#### Changing Existing Entitlement or Add/Remove Option

When you click the Edit button on the Resign Binary screen, a new page will open for Entitlement editing. In this page, you can update, delete or add a new entitlement to your existing entitlements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-editDetails.png' />

:::danger Entitlement Change

If you want to change, add or remove Entitlement. The **Provision Profile** and **Bundle Identifier** you will resign **must contain** the **entitlements** you want to change. If the **Bundle ID** or **Provision Profile** does not contain or support these changes, the resign operation may **fail**.

:::

### Resigning Process

To resign a binary, follow these steps:

1. **Select the Version**: Choose the version of your app you wish to resign from the **Version List** in the Publish module.
2. **Configure Resigning Options**: Navigate to the **Resign Binary** action and configure the necessary fields such as the provisioning profile, entitlements, and other settings.
3. **Sign the Binary**: After configuring, click the **Sign** button to resign the binary. This process will create a new package with the updated provisioning profile and entitlements.

### Post-Resignation

Once the binary is resigned, a new package is automatically created to reflect the changes. This ensures that any distribution or testing utilizes the most current setup without requiring a complete rebuild.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3161-publish-resigned.png' />

The newly created package can then be distributed or tested according to your publish flow requirements. This update ensures that your application conforms to the necessary provisioning and entitlement specifications for different environments, such as development, staging, or production, without additional build steps.

This feature streamlines the application update process by allowing for quick adjustments to the app's configurations, significantly reducing the time and resources needed for separate build cycles.

## Resign Android Binary

Resigning an Android binary allows you to apply a new keystore to your application after the initial build. This is useful for updating the signing configuration or switching to a different keystore as needed without needing to rebuild the app.

### Fields and Options

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3161-publish-resign-android-option.png' />

- **Package ID**: This is the unique identifier for your Android application, also known as the application ID. It usually follows the format `com.example.myapp` and should not be changed during the resigning process.

:::caution Package ID
Please note that changing the **Package ID** is not allowed while the related version is being resigned in the **Publish module**. If you need to change the **Package ID value** of your package, please use the **Resign Binary** feature in [Testing Distribution](/distribute/platform-specific-guidance/android/resigning-android-binaries).
:::

- **Version Name**: This field represents the human-readable version of your app, such as `1.2.3`. It is used for display purposes and can be adjusted if necessary during the resigning process.

- **Version Code**: The version code is a numerical value that represents the version of your app. Unlike the version name, this is used by the Android system to prevent or allow installations over existing ones. This should be incremented or adjusted according to your versioning strategy.

- **Keystores**: This dropdown allows you to select a keystore to resign your binary. A keystore contains one or more keys. You must select the keystore that contains the appropriate key for signing your application. The keystore used for resigning must match the requirements of the platform where the app will be distributed.

### Resigning Process

When you opt to resign an Android binary:

1. **Package ID**: This is your Android application's unique identifier and cannot be changed during the resigning process.
2. **Version Name & Code**: Adjust the version name and code if necessary. This helps in maintaining versioning integrity across different release channels.
3. **Keystores**: Select the keystore you wish to use for resigning the binary. This could be a newly added keystore or one previously used in other projects.

After configuring the necessary options, click the **Sign** button to start the resigning process.

### Post-Resignation

Once the binary has been resigned, it will create a new package with the updated signing configurations. The newly resigned binary will appear in your version list marked with the new version code if updated during the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3161-publish-android-after-resign.png' />
