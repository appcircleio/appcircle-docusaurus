---
title: iOS Signing
description: Learn how to manage signing identities in Appcircle
tags:
  [signing identities, android keystores, certificates, provisioning profiles]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';

# iOS Signing Overview


<iframe width="600" height="315" src="https://www.youtube.com/embed/BTmOJTn3kuY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You need to have your iOS Certificates and Provisioning Profiles ready to be able to build and deploy your applications to Apple Appstore.

:::info

For app builds, the signing identities are not mandatory. (e.g. you can use unsigned apps to run on the simulator or for use on third party platforms that resign your app such as AWS Device Farm)

However, unsigned binaries cannot be installed on actual devices; therefore they cannot be used in the Appcircle Testing Distribution.

:::

You can obtain your developer certificates and provisioning profiles from the Apple Developer Portal:

[https://developer.apple.com/support/code-signing/](https://developer.apple.com/support/code-signing/)

