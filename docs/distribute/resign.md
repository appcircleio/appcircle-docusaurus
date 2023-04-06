---
title: Resign Binaries
metaTitle: Resign Binaries
metaDescription: Resign Binaries
sidebar_position: 6
---

import NarrowImage from '@site/src/components/NarrowImage';

# Resigning

Resigning is the process of modifying an existing binary with a new signing certificate or keystore, which is required when an application needs to be published under a different developer account or when updating an existing application. It involves removing the original signature and replacing it with a new one. This process ensures that the app is verified by the new signing authority and can be installed on users' devices.

## Resigning iOS Binaries

To sign an iOS binary, you need a valid certificate and provisioning profile. Appcircle, our product, supports both IPA and xcarchive files. The process of signing an iOS binary involves selecting the correct certificate and provisioning profile, and specifying the bundle identifier and version number. Once these details are entered, Appcircle will generate a new signed binary with the updated information.

## Resigning Android Binaries

To sign an Android binary, you need a valid keystore file. Appcircle supports both apk and aab files. The process of signing an Android binary involves selecting the correct keystore file. Once these details are entered, Appcircle will generate a new signed binary with the updated information.
