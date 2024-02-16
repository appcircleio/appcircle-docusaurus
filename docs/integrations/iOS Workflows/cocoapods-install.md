---
title: Cocoapods Install
metaTitle: Cocoapods Install
metaDescription: Cocoapods Install
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

## Cocoapods Install

Runs the Cocoapods install command for dependency management. This step install your all pod dependencies. And it should be used after **Git Clone** step

- For this, open workflow and check **Cocoapods Install** step

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_order.png' />

- You can specify the Cocoapods version. Default is empty. If you leave empty this parameter, Appcircle will read **Podfile.lock** and install related version of Cocoapods.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2588-pod_version.png' />

:::warning
Remember, if the project extension is not **.xcworkpace**, the pod install step will not work as expected. In the Configuration tab, make sure that the extension in the project path is **.xcworkspace**.
:::

https://github.com/appcircleio/appcircle-cocoapods-component