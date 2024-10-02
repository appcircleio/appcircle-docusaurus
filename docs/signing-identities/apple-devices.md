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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-AppleDevices.png’ />

:::caution Apple Devices

Please note that Ad Hoc provisioning can only be used for internal distribution and testing, and not for App Store submission or external distribution. The number of devices that can be registered in an Apple Developer account is **limited to 100 iOS devices**, which can only be reset once a year.

For more information, please visit [Apple Developer documentations](https://developer.apple.com/documentation/appstoreconnectapi/devices).

:::

## Adding Device

With Appcircle's advanced Apple Devices feature, device management is made very easy. With this feature, you can fetch existing registered devices, add and register a device manually or via email.

## Registered Device

When you come to the Registered Devices section in Apple Devices, you can list the devices that are already registered in your Apple Developer account, and synchronise them.

:::caution Registered Devices

In order to list your registered devices, the App Store Connect API key must be added to Appcircle. Please follow the related [document](/account/my-organization/integrations/credentials/adding-an-app-store-connect-api-key) to add App Store Connect API key.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-registeredDevice.png’ />

### Fetching Registerd Devices

In order to be able to list the registered devices, you must first fetch these devices using the API key. For this, you can use the ‘Get Devices from Apple Developer Portal’ button to fetch the devices with the relevant API key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-fetchDevices1.png’ />

After fetch process completed successfully, you will see the whole registered device in list below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-registeredList.png’ />

### Filtering Devices by Apple Developer Accounts

Since Appcircle's credential structure allows multiple API key connections at the same time, you can list your devices in different accounts with the account filtering feature on the registerd devices page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-storeFilter.png’ />

### Filtering Devices by Device Status

Apple provides Disable and Enable device options for registered devices. This feature makes the registered device disable or enable. Disable devices are not added to provision profiles and are not included in any development process. You can use the filtering provided by Appcircle to filter according to device status. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-statusFilter.png’ />

### Disable Device

Apple provides a disable option to exclude registered devices from development processes. To disable a registered device on Apple, select the relevant device, and use the **Disable** button at the bottom. This process will simultaneously change the status for the relevant device registered in your Apple Developer account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-disableDevice.png’ />

### Enable Device

Apple provides an enable option to include registered devices from development processes. To enable a registered device on Apple, select the relevant device, and use the **Enable** button at the bottom. This process will simultaneously change the status for the relevant device registered in your Apple Developer account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4404-enableDevice.png’ />

## Not Registered Devices

With Appcircle's advanced Device management, you can also add user devices manually. For this, you can add a device by going to the Not Registered tab and clicking the Add manually button.

