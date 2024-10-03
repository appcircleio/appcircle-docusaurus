---
title: Apple Devices
description: Distribute your iOS apps to Apple devices with Appcircle
tags: [distribution, apple devices, ios]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Apple Devices

When it comes to developing and testing iOS apps, one of the most important tasks is registering your devices with the Apple Developer portal. This is necessary so that you can install your app on those devices for testing purposes. However, this process can be a bit tedious, especially if you need to register a large number of devices. That's where Appcircle comes in.

Ad-hoc distribution is a method of distributing iOS apps outside of the App Store. To use Ad-hoc distribution, you need to register your devices with the Apple Developer portal and include them in your app's provisioning profile. Appcircle makes this process much easier.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-AppleDevices.png' />

:::caution Apple Devices

Please note that Ad Hoc provisioning can only be used for internal distribution and testing, and not for App Store submission or external distribution. The number of devices that can be registered in an Apple Developer account is **limited to 100 iOS devices**, which can only be reset once a year.

For more information, please visit [Apple Developer documentations](https://developer.apple.com/documentation/appstoreconnectapi/devices).

:::

## Adding Device

With Appcircle's advanced Apple Devices feature, device management is made very easy. With this feature, you can fetch existing registered devices, add and register a device manually or via email.

For this, you can manage your devices by visiting the sections in Apple Devices.

- **Registered Devices**: This section lists the devices registered to your Apple Developer Account using an API key.
- **Non-Registered Devices**: This section lists only the devices registered on Appcircle that you have not yet registered in your Apple Developer account. You can add a new device manually in this section.
- **Invited Users**: This section lists the users you have sent an email invitation to receive device information. You can get a new device informations with email.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-sections.png' />

Follow this document for detailed usage and purpose of all sections.

## Registered Device

When you come to the Registered Devices section in Apple Devices, you can list the devices that are already registered in your Apple Developer account, and synchronise them.

:::caution Registered Devices

In order to list your registered devices, the App Store Connect API key must be added to Appcircle. Please follow the related [document](/account/my-organization/integrations/credentials/adding-an-app-store-connect-api-key) to add App Store Connect API key.

:::


### Fetching Registered Devices

In order to be able to list the registered devices, you must first fetch these devices using the API key. For this, you can use the ‘Get Devices from Apple Developer Portal’ button to fetch the devices with the relevant API key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-fetch.png' />

After fetch process completed successfully, you will see the whole registered device in list below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-fetchedList.png' />

### Filtering Devices by Apple Developer Accounts

Since Appcircle's credential structure allows multiple API key connections at the same time, you can list your devices in different accounts with the account filtering feature on the registerd devices page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-filterStore.png' />

### Filtering Devices by Device Status

Apple provides Disable and Enable device options for registered devices. This feature makes the registered device disable or enable. Disable devices are not added to provision profiles and are not included in any development process. You can use the filtering provided by Appcircle to filter according to device status. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-filterStatus.png' />

### Disable Device

Apple provides a disable option to exclude registered devices from development processes. To disable a registered device on Apple, select the relevant device, and use the **Disable** button at the bottom. This process will simultaneously change the status for the relevant device registered in your Apple Developer account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-disableDevice.png' />

:::caution Disable Device

Disabling this device will invalidate all associated provisioning profiles. You can remove this device from your account at the start of your new membership year.

:::

### Enable Device

Apple provides an enable option to include registered devices from development processes. To enable a registered device on Apple, select the relevant device, and use the **Enable** button at the bottom. This process will simultaneously change the status for the relevant device registered in your Apple Developer account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-enableDevice.png' />

### Registering Device to different Apple Developer Portal

A device that is already registered to any Apple Developer Account can be added to different Apple accounts if desired. For this, after selecting the device, you can register it by selecting a different API key with the Register device to Apple Developer button in the menu that opens at the bottom. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-registerDevice.png' />

When you select different API key in the list, Appcircle will automatically register your device to selected Apple Developer Account

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-registerAPI.png' />

### Device Information

When you click on any device UDID in the Registered Device list, you can find detailed information about that device. This information includes the related device;

- Which API keys the device is registered to
- Which Provision Profiles are available in
- Device type
- And the date it was recorded

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-udidClick.png' />

You can see it in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-deviceInfo.png' />


## Not Registered Devices

With Appcircle's advanced Apple Devices feature, you can also add user devices manually.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-nonRegistered.png' />

### Adding Device Manually

With this feature, you can manually enter the UDID of the device you want to register and register it to your Appcircle Account. For this, you can add a device by going to the Non-Registered tab and clicking the **Add Manually** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-addManuel12.png' />

:::caution Manuel Added Devices

Remember, manually added devices are not automatically registered to your Apple Developer Portal Account. 

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-addManuelModal.png' />

### Registering Device to Apple Developer Portal

After selecting a Non-Register device, you can register the device to your Apple account with the Register to Apple Developer Portal button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-registerNonDevice.png' />

## Invited Users

In addition to manually saving devices to your Appcircle account, you can also do this by sending an e-mail invitation to the users whose device information you want to receive. If a device is saved with the invitation sent, the device UDID will be listed in the Non-Registered Device tab when the registration process takes place.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-invitedUser.png' />

:::info

More than one device can be registered with the link in the invitation sent via e-mail, and does not require any authentication method.

:::

To invite a user by e-mail, click **Invite User by Email** button, and specify the email address and invitation message.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-inviteButton.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-inviteForm.png' />


The mail containing the e-mail invitation will look like this.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-emailContent.png' />

When you send an invite to a user, the invitation you sent is listed in the Invited User list. If the user has not taken any action, their status appears as `Pending`. If the user has registered the device UDID, this status will change to `Registered`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-pending.png' />

### Adding Device by Email

- When the link in the e-mail invitation is clicked, you will see a screen like below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone1.png' />

- Specify the device name and press the Register this Device button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone1.png' />

- Appcircle will ask to download a temporary profile to get the device UDID. You must allow this.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone2.png' />


- Once this profile has been downloaded, go to the iPhone settings and install the downloaded profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone4.png' />


- After the installation process is completed, you will be automatically redirected to the web portal containing your device information. When this screen comes up, you can see all the information about the device. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone5.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-iphone6.png' />

- After this step, the device UDID has been successfully registered in Appcircle. You can go to the Appcircle interface and see the relevant device in the Non-Registered Devices tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-afterEmailInvite.png' />

### Cancel Invitation

When an invitation is selected, you can delete this invitation by clicking the Delete button from the menu below. When the invitation is deleted, the link in the e-mail will become inactive and cannot be used again.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404New-inviteCancel.png' />




