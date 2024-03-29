---
title: Resigning Android Binaries
metaTitle: Resigning Android Binaries
metaDescription: Resigning Android Binaries
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Resigning

Resigning is the process of modifying an existing binary with a new signing certificate or keystore, which is required when an application needs to be published under a different developer account or when updating an existing application. It involves removing the original signature and replacing it with a new one.

## Resigning Android Binaries

To sign an Android binary, you need a valid keystore file. Appcircle supports both APK and AAB files. The process of signing an Android binary involves selecting the correct keystore file. Once these details are entered, Appcircle will generate a new signed binary with the updated information.

1. Select the binary.

You can either select the files from the list or upload APK, and AAB files by clicking the **Upload New Version** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign1.png' />

2. Click the... button and select **Resign Binary**

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign2.png' />

This form will show the following details of the original binary.

3. Select the correct keystore and click the **Sign** button to sign your binary. You may also change the Package ID, Version Name and Version Code.

<Screenshot url='https://cdn.appcircle.io/docs/assets/resign4.png' />

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
