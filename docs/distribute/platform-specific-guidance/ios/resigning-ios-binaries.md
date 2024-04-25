---
title: Resigning iOS Binaries
description: Understand the process of resigning iOS binaries with a new certificate or keystore. Crucial for publishing under a different developer account.
tags: [resigning, ios, binaries, resigning ios binaries]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Resigning

Resigning is the process of modifying an existing binary with a new signing certificate or keystore, which is required when an application needs to be published under a different developer account or when updating an existing application. It involves removing the original signature and replacing it with a new one.

## Resigning iOS Binaries

To sign an iOS binary, you need a valid certificate and provisioning profile. Appcircle supports both IPA and xcarchive files. The process of signing an iOS binary involves selecting the correct certificate and provisioning profile and specifying the bundle identifier and version number. Once these details are entered, Appcircle will generate a new signed binary with the updated information.

### iOS Resign Process

1. Select the binary.

You can either select the files from the list or upload IPA, xcarchive files by clicking the **Upload New Version** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign1.png' />

2. Click the... button and select **Resign Binary**

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign2.png' />

This form will show the following details of the original binary.

**Display Name**

CFBundleDisplayName: The user-visible name for the bundle, used by Siri and visible on the iOS Home screen.

**Version**

CFBundleShortVersionString: The release or version number of the bundle.

**Build Number**

CFBundleVersion: The version of the build that identifies an iteration of the bundle.

**Entitlements**

- Entitlements from provisioning profiles

Use entitlements from the new provisioning profile

- Combine app entitlements

Extract app bundle codesigning entitlements and combine them with entitlements from new provisioning

- New Entitlements.

You can edit this XML file to edit capabilities. Resigning process uses a **single** entitlement XML file.

If your provisioning profiles have the correct entitlements set, using the first option is the safest option.

**Targets**

You need to select new provisioning profiles for each target. Bundle ids will be automatically populated when you select a new provisioning profile. However, if you use a wildcard provisioning profile, you may need to write the correct bundle id for the selected target.

:::caution

You must select a provisioning profile for each target. Otherwise resigning will fail.

:::

3. Fill in the details for resign process and hit the **Sign** button

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign3.png' />

## Binary Details

1. Select the binary.

You can either select the files from the list or upload binaries by clicking the **Upload New Version** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign1.png' />

2. Click the... button and select **Binary Details**

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign2.png' />

3. This window will show basic information about your binary.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign6.png' />

## Resign History

1. Select the binary.

You can either select the files from the list or upload binaries by clicking the **Upload New Version** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign1.png' />

2. Click the... button and select **Resign History**

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign2.png' />

3. Each signing process will be listed for that binary. If you click the **View Log** button, you can get more details about the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign5.png' />

:::info

You need the check the history of the original application that has been signed.

:::
