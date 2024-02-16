---
title: Xcodebuild for iOS Simulator
metaTitle: Xcodebuild for iOS Simulator
metaDescription: Xcodebuild for iOS Simulator
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

## Xcodebuild for iOS Simulator

This step builds your application for the iOS Simulator in x86_64 or arm64 architecture. This step creates an unsigned `xarchive` file. You may also optionally install the application for given simulator.

Use this step after **Cocoapods Install** step (If you use Cocoapods in your project).  

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_order.png' />

:::caution
If you use SPM (Swift Package Manager) Xcode will manage itself when project build.
:::

#### Changing Architecture

You can change architecture directly from inside of Step with **Architecture** parameter.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_arc.png' />

#### Specify Simulator 

You can easily specify simulator that you want to build one. Write simulator name as hard coded. For example; **`iPhone 14`**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_name.png' />

:::caution
Be avoid, which Xcode version you used, simulator type should match that Xcode version. For example, if you use **Xcode 15.x** you can not use **iPhone 14** simulator.
:::

#### Adding Archive Flags

You can easily add a new parameter to **xcodebuild** command. **Archive Flags** parameter of step will allow you to do that. For example; add directly **`-quiet`**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_flag.png' />

#### Adding Configuration

With this parameter, you can build your project with any configuration you want. Specify configuration as hard coded. Appcircle will add automatically this configuration to xcodebuild command. For example; **`Debug`**

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2586-sim_config.png' />

https://github.com/appcircleio/appcircle-ios-build-simulator