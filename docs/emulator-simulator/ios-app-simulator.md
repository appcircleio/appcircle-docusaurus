---
title: Online iOS Simulator for Apps
metaTitle: Online iOS Simulator for Apps
metaDescription: Online iOS Simulator for Apps
sidebar_position: 3
---

# Online iOS Simulator for Apps

Appcircle online iOS Simulator allows you to upload simulator app bundles and run them on an iOS device in the browser without the need for a Mac, Xcode, or any downloads.

To use the iOS Simulator, you need to have a simulator app bundle that is compatible with the x86 architecture. This app bundle needs to be provided as a compressed ZIP or TAR.GZ file.

:::caution

IPA files are not compatible with the iOS simulator due to Apple's restrictions.

:::

To start, click the Emulator/Simulator button from the left menu and then click the "Upload a compressed simulator app bundle" button.

![](<https://cdn.appcircle.io/docs/assets/image (117).png>)

You will be presented with the option to upload a local file or enter a remote file URL.

![](<https://cdn.appcircle.io/docs/assets/image (118).png>)

To upload a local file, click on the "Browse" button to select a file or drag and drop a compressed app bundle file to the upload field and click on the "Launch Simulator" button.

![](<https://cdn.appcircle.io/docs/assets/image (119).png>)

To deploy a remote file, enter the file URL and click on the "Launch Simulator" button. The URL must end with the ZIP or TAR.GZ extension.

![](<https://cdn.appcircle.io/docs/assets/image (120).png>)

:::caution

If you're uploading a compressed file, make sure to compress only the .app folder. Nested folders are not supported.

:::

Once the simulator gets launched, select a device type and an OS version from the dropdowns and then press "Play" on the simulator screen.

![](<https://cdn.appcircle.io/docs/assets/image (122).png>)

Your app will then be deployed to the simulator. You can now use it just like an actual device. To end your session, just navigate away from the simulator screen. Your session will not be preserved.

:::caution

If your app is not compatible with the x86 architecture or if it is one of the blacklisted apps for security purposes, you will receive an error and the app will not run.

:::

![](<https://cdn.appcircle.io/docs/assets/image (121).png>)

;
