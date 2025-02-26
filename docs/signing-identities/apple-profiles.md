---
title: Apple Profiles
description: Learn how to manage iOS profiles in Appcircle
tags: [signing identities, ios certificates, provisioning profiles]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Apple Profiles Overview

Provisioning profiles can be in `.mobileprovision` file format. There are 4 main types of iOS certificates:

**1. Apple App Development:** Used to install development applications on test devices. This provisioning profile type is matched with a development certificate to enable app deployment during development. This is used mainly for debugging or functional testing.

**2. Ad Hoc:** Used for installing an application on a limited number of registered devices.

Ad Hoc profiles enable the installation of the binary on a specified device pool. This allows application testing on actual devices while limiting the app distribution to external parties by requiring all devices to be registered in the Apple Developer Portal to run any app signed by the Ad Hoc certificate of the same developer account.

There is a limit on the number of devices registered for Ad Hoc distribution and for the deployments with a development profile. This limit resets yearly.

For this purpose, you need to get the UDID information of your test devices, register them in the Apple Developer Portal, and then generate an Ad Hoc provisioning profile. You can then upload this file to the Appcircle Signing Identities module to be used in builds.

Please note that every time you add a new device, you have to regenerate the provisioning profile and reupload it to Appcircle. (Regeneration of the associated certificate is not necessary as long as it is valid.)

For more information on getting the UDID and registering it, please refer to the following Apple Developer guide. This guide walks you through all the steps necessary to get a device assigned to your Apple Developer account: [https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices](https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices)

You can use the Appcircle Testing Distribution to deploy apps built with an ad hoc profile. (If the receiving device is registered, of course.)

**3. App Store:** Used for submitting applications to the Apple App Store.

App Store profiles allow you to build store-ready versions of your app to be submitted to the App Store or to TestFlight. You can use the Appcircle Store Submit module to upload apps signed with an App Store profile to App Store Connect.

You cannot use the Appcircle Testing Distribution to deploy apps built with an App Store profile. (You can still share the binary but it cannot be installed on the target device.) The only valid target is for the apps signed with this profile is App Store Connect.

**4. Enterprise (In-House):** Used for in-house application distribution for the enterprises enrolled in the Apple Developer Enterprise Program.

This profile type is only available with the Apple Developer Enterprise program with strict requirements for registration. The apps signed with an enterprise profile can be installed freely on any device without going through the App Store or the Ad Hoc device registration.

The user will only be displayed a trust warning for the first time they are running an app signed with a specific enterprise certificate and then the app can be run just like an app downloaded from the App Store.

There are certain limitations that are mandated by the Apple Developer Enterprise program agreement such as the apps can only be used for work purposes by the actual employees of the enterprise, so it's not a free-for-all certificate to bypass the App Store processes. Apple reserves the right to revoke your certificate at any time in case of a violation.

You can use the Appcircle Testing Distribution or the Enterprise App Store module to deploy apps built with an enterprise profile to any device.

There is no need for device registration, but Apple requires the binary to be protected and not open for public download, so you can use the enrollment feature of the Appcircle Testing Distribution to protect the app distribution.

:::info

For app builds, signing identities are not mandatory. For example, you can use unsigned apps to run on the simulator or on third-party platforms that resign your app, such as AWS Device Farm.

However, unsigned binaries cannot be installed on actual devices; therefore they cannot be used in the Appcircle Testing Distribution.

:::

You can obtain your developer certificates and provisioning profiles from the Apple Developer Portal:

[https://developer.apple.com/support/code-signing/](https://developer.apple.com/support/code-signing/)


## Using Appcircle Signing Identity module for Apple Profiles

To register, upload or fetch your Apple Profiles, select **Apple Profiles** from the signing module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-appleProfiles.png' />

### Register a New Provisioning Profile

**Prerequisite**: To register a new provision profile in your Apple Developer Account, you need to add an App Store Connect API Key. Visit the link below for instructions.

<ContentRef url="/account/my-organization/security/credentials/adding-an-app-store-connect-api-key">Adding an App Store Connect API Key</ContentRef>

With Appcircle's register provisionn feature, you can easily create a new provision profile on the Apple Developer portal using the App ID of your choice. 

:::info Registering Provision Profile

The provision profile you register via Appcircle is simultaneously registered on the Apple Developer portal.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-registerProfile.png' />

In order to register a profile, some parameters are needed. 

After selecting the distribution method, the relevant App ID is selected for which Bundle ID will be created. Then you need to select which certificate you want to create with.

:::info

The certificates that need to be selected when registering a profile are listed by retrieving certificates from your **Apple Developer** account. The certificates listed here are **not** related to the ones uploaded to **Appcircle**.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-registerProfileDetails.png' />

#### Device Registration

If you have selected Ad-hoc or Development as distribution method, you need to select a device to be added to the provision profile in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-deviceSelection.png' />

### Get Provisioning Profiles from Apple Developer

**Prerequisite**: To list all the signing identities saved in your Apple Developer Account, you need to add an App Store Connect API Key. Visit the link below for instructions.

<ContentRef url="/account/my-organization/security/credentials/adding-an-app-store-connect-api-key">Adding an App Store Connect API Key</ContentRef>

When you go to add a new Provisioning Profile, you'll see the option **Get Provisioning Profiles from App Store Connect**. Select it to see the list of identities fetched from Apple.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-getProfiles.png' />

You can select to download the provisioning profile from the list. **If you don't want Appcircle to keep the provisioning profile**, you can make our build agents to keep a reference. This way, our agents will fetch the profiles **before every build and dismiss them** when the build is finalized.

<Screenshot url="https://cdn.appcircle.io/docs/assets/signing-ios-provision-profile-allow-download.png" />

You can select the profiles you want to download from the list and fetch them to your Appcircle environment with the download button.

### Upload a Provisioning Profiles

Simply upload your provisioning profiles obtained from the Apple Developer portal.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-uploadProfiles.png' />

:::info

Provisioning profile and certificate matching will be done automatically. You can also have multiple provisioning profiles to use in different applications with different Apple developer accounts.

:::

:::tip

You can upload multiple Provisioning Profile files at once.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4060-upload.png' />

You can list and manage your provisioning profiles here. Newly uploaded files will display with a blue-colored background. If there is a matching certificate, the profile will show a green check mark. If not, you will see a red cross mark indicating there is no certificate matching the provisioning profile.

You can also see the matching application ID and expiration date of the profiles here.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4060-upload2.png' />

### Deleting Provisioning Profiles

You can delete a single Provisioning Profile or multiple ones by selecting the checkboxes next to the provisioning profiles. You can also select the checkbox at the top of the list to select all available ones. Once you select the checkboxes for the files you need, a delete button will appear at the top right corner.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4060-delete1.png' />

If you attempt to delete a Provisioning Profile that is saved in a build configuration of an active Build Profile, a warning message will appear. This message will allow you to view the affected build profiles and navigate to their configuration screens to make necessary changes.

You also have the option to force delete it without changing the configurations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4060-delete2.png' />

:::caution

Affected build profiles will not be displayed within the warning message if you delete multiple Provisioning Profiles.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4060-delete3.png' />

### Profile Actions

You can access different Actions for existing provisions within 3 points in the area where the provisions are listed on the Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-renewOption.png' />

- **Renew**: Renews provisioning that has expired or become out of date
- **Apple Devices**: Lists the device UDIDs registered in the provision
- **Download**: Downloads the selected provisioning

:::danger Renew

The Renew function only applies to provisions that have been **registered** with Appcircle or **fetched** via the Apple Developer portal.

You **cannot** renew **manually uploaded provisioning**.

:::

:::info Renewed Profiles

If a provision profile is used in a Build Profile, it will continue to be used with the renewed version after the profile is renewed.

:::

### Adding Device to Provision Profile

With Appcircle’s Apple Profiles feature, you can easily add the UDIDs of your test devices to the corresponding provisioning profile.

To manage devices and view the current device list, click the **Profile Action** button and navigate to the **Apple Devices** section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5008-deviceAction.png' />

When you click the **Apple Devices** action, you will see a list of devices currently included in the **selected** provisioning profile. In the modal that opens, you can update this list by clicking the **Manage Devices** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5008-manageDeviceModal.png' />

After clicking the Manage Devices button, you will see two different lists.

The **Existing Devices** list displays the device **UDIDs** currently included in the **selected** provisioning profile. You can remove a device from the provisioning profile by unchecking its checkbox in this list.

Below this, there is the **Non-Existing Devices** list. This list shows the devices that are **registered** in your **Apple Developer Portal** account but are not **included** in the provisioning profile. To add a new device **UDID** to the provisioning profile, select the desired device from this list and proceed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5008-deviceAddRemove.png' />

:::caution Minimum Device Count

According to **Apple’s Developer Portal** rules, a provisioning profile must include at least **one** device. Therefore, you cannot **remove** all devices from a provisioning profile.

:::

After selecting the devices, you will see a final **Preview** screen. This screen displays the updated device list that will be included in the provisioning profile. You can update the devices in the provisioning profile by clicking the **Update Profile** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5008-addDevicePreview.png' />

When the profile update is successfully completed, the updated version of the selected provisioning profile will be displayed in the Apple Profiles list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5008-updatedList.png' />

:::info Updated Provision Profile

When a provisioning profile is updated, Appcircle replaces the old profile with a new one under a different name. The new name includes the update date and time.

:::

### Assign signing identities in the Build module for distribution

For both iOS or Android build projects, you need to assign your signing identities to your build profile for distribution. The distribution-ready binaries will be signed with the selected signing identities both in manual and automatic distribution cases.

You can sign your application either with automatic signing or with manual signing.

## Automatic Signing

Automatic signing allows you to sign your application without uploading any provisioning profiles. Profile creation is done automatically by Xcode. Following prequisites must be met for automatic signing to work:

- Project must be built with Xcode 13 or higher.
- Both Developer and Distribution certificates must be added to Appcircle.
- App Store Connect Key must be added to Appcircle.

<Screenshot url="https://cdn.appcircle.io/docs/assets/signing-ios-configuration-auto-code-sign.png" />

You must also select distribution type from the dropdown menu. If you're uploading your app to App Store or TestFlight, you should select **App Store**. If you're uploading your app to Adhoc or Appcircle's distribution module, you should select **Adhoc**. Please check [Apple's documentation](https://developer.apple.com/documentation/technotes/tn3125-inside-code-signing-provisioning-profiles) for more details.

:::danger

If you don't upload developer and distribution certificates, Xcode will create new certificates each time you start a build. Since you don't have the private keys, you will not be able to use those certificates later on. If you don't want to clutter your account with unused certificates, you must upload both developer and distribution certificates.

:::

## Manual Signing

You can also select bundle identifier and provisioning profile to sign your application.

<Screenshot url='https://cdn.appcircle.io/docs/assets/03-02-iOS-Build-Signing.jpg' />

:::danger

If your app has multiple targets such as watchOS, Widgets etc, you need to add all the provisioning profiles for every bundle id. Click **+** button and add related bundle id and provisioning profile.

:::

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::
