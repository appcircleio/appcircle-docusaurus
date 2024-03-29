---
title: Distributing to Apple Devices
metaTitle: Distributing to Apple Devices
metaDescription: Distributing to Apple Devices
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Distributing to Apple Devices

When it comes to developing and testing iOS apps, one of the most important tasks is registering your devices with the Apple Developer portal. This is necessary so that you can install your app on those devices for testing purposes. However, this process can be a bit tedious, especially if you need to register a large number of devices. That's where Appcircle comes in.

Ad-hoc distribution is a method of distributing iOS apps outside of the App Store. To use Ad-hoc distribution, you need to register your devices with the Apple Developer portal and include them in your app's provisioning profile. Appcircle makes this process much easier.

### Manually Registering Devices

Navigate to the Distribute / Apple Devices section. Click the... button and then choose "Add Device".

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-adddevice1.png' />

Here, you can manually add a device by entering the UDID and device name, clicking the... button, and then choosing "Add Device".

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-adddevice2.png' />

### Automatically Registering Devices

Alternatively, you can add devices automatically by installing a mobile configuration profile. If you enable [Device Registration](/distribute/create-or-select-a-distribution-profile#device-registration-ios-only) for your distribution profile, each Ad Hoc distribution email will have a Register Device link at the bottom. You may click that link to register your devices.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-email1.png" width="300" />

After clicking the link, you should see the below screen to enter your device name.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-email2.png" width="300"/>

When you click the **Register this Device** button, iOS will ask you to download a configuration profile.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-email3.png" width="300" />

Close the dialog and open settings.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-email4.png" width="300" />

Download that profile and install it by opening your device's settings

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-ios-settings1.png" width="300"/>

Review the profile and check that it's signed with Appcircle's key and verified by Apple.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-ios-settings2.png" width="300"/>

Click the **Install** button to install this mobile configuration to your device. The only purpose of this mobile configuration is to get the UDID of your devices.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-ios-settings3.png" width="300" />

If the installation process succeeds, you'll be forwarded to the following screen.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/adhoc-profile-success.png" width="300" />

### Deleting Devices from List

You can remove devices from Appcircle's list by selecting the devices and clicking **Delete from List** button. Please be aware that this action only removes the device from Appcircle. This action will not have any effect on the registration status of the device in the
Apple Developer portal.

## Add to Provisioning Profile

After you registered your devices, you need to add those devices to provisioning profiles. Registered devices can be added to provisioning profiles manually or automatically.

### Manually adding registered devices to the provisioning profile

After you added your devices, you can add your devices to Adhoc provisioning profiles by selecting the device(s) and clicking the **Add to Provisioning Profile** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-addprovision1.png' />

Choose your AppStore Connect API Key

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-selectkey.png' />

Choose your Ad Hoc provisioning profile

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-selectprofile.png' />

Your new device will be added to the newly created provisioning profile. New provisioning profiles will have AC and date suffixes. Ex: _Dashboard Adhoc AC-d3b6-January-16-2023-1048_

Appcircle will also update all build profiles with updated provisioning profiles.

### Automatically adding registered devices to the provisioning profile

You can add registered devices to selected provisioning profiles by editing your distribution profile's settings.

Go to your distribution profile and then click the **Settings/Apple Devices Registration** tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/adhoc-profile-auto.png' />

By enabling this setting, every registered device will be automatically added to the selected build profile's configured branch.

:::tip

If you use Automatic code signing, you don't need to select any provisioning profiles. Xcode will automatically select the correct provisioning profiles and add all registered devices to provisioning profiles.

:::
