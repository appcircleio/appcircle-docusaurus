---
title: Preview on Device (Emulator/Simulator) in the Distribute Module
metaTitle: Preview on Device (Emulator/Simulator) in the Distribute Module
metaDescription: Preview on Device (Emulator/Simulator) in the Distribute Module
sidebar_position: 3
---

import ContentRef from '@site/src/components/ContentRef';

# Preview on Device (Emulator/Simulator) in the Distribute Module

Appcircle offers in-browser iOS simulators and Android emulators. If you deploy your app through the Appcircle Build module and if the app is compatible with the x86 architecture, you can preview your iOS and Android app on a virtual device in your browser.

This document outlines the use of the "Preview on Device" feature within the Distribute module. For standalone emulators/simulators, please refer to the following guide:

<ContentRef url="/emulator-simulator/android-app-emulator">Emulator / Simulators</ContentRef>

Please follow the steps below to run your app online: (For the demonstration of these steps, you can check our introduction video at [https://www.youtube.com/watch?v=OUoZFGqJFdM](https://www.youtube.com/watch?v=OUoZFGqJFdM))

<iframe width="560" height="315" src="https://www.youtube.com/embed/OUoZFGqJFdM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

1. [Create a distribution profile and add an app version](create-or-select-a-distribution-profile.md). You can then just press the "Preview on Device" button to run it.\

2. For iOS apps, you need to [build your app from source](../build/adding-a-build-profile/) with the [Xcode Build for iOS Simulator workflow step](../workflows/ios-specific-workflow-steps.md#xcodebuild-for-ios-simulator) **enabled** (it is enabled by default) and then [send it to the Distribute module](../build/after-a-build.md). (IPA files are not supported as per Apple's restrictions.)\

3. For Android apps, if your app has x86 architecture in it, [you can manually upload APK files](create-or-select-a-distribution-profile.md#manually-upload-your-version) to run them in the emulator or you can [build your app from source](../build/adding-a-build-profile/) and then[ send it to the Distribute module](../build/after-a-build.md).

:::info

With manual uploads, only Android applications can be previewed on a virtual device. (The uploaded APK must be compatible with the x86 architecture.)

IPA files cannot be previewed due to Apple's restrictions.

:::

When viewing an app version in the Distribute module, simply click preview and you can run your app on different iOS and Android devices and on different OS versions.

:::info

You can preview your applications in your browser instantly without the need for an actual device and downloads.

:::

![](https://cdn.appcircle.io/docs/assets/06-06a-PreviewOnDevice.jpg)
