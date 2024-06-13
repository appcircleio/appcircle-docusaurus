---
title: Registering BundleID
description: Learn how to register BundleIDs in Appcircle
tags: [BundleID, application, identifier]
---

import Screenshot from '@site/src/components/Screenshot';

# Registering Bundle Identifier

The first requirement for publishing an application on the Apple App Store is to determine the unique identifier that identifies your application. For this reason, you must first register a BundleID. For more information, please refer to the [**Apple Documentation**](https://developer.apple.com/documentation/appstoreconnectapi/bundle_ids).


The BundleID option in Appcircle's Signing Identities module, you can easily register a BundleID on the Apple Developer Portal or list your existing BundleIDs on Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-bundleID.png' />

### Manuel Register Bundle Identifier

The Register Bundle Identifier option, you can register a new BundleID on the Apple Developer portal using Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-registerBundle.png' />

You can specify the BundleID you want to save, a description to identify this identifier and the capabilities you want it to have. When you click the Save button, Appcircle will save this BundleID for you in your Apple Developer account.

:::info Manuel Register Bundle Identifier

When you register a BundleID, it will be simultaneously created in your Apple Developer account.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-registerBundleDetails.png' />

- **Description**: A brief explanation to distinguish BundleID.
- **BundleID**: BundleID value to be saved.
- **Capabilities**: The capability values you want BundleID to have.


### Get Bundle Identifiers from Apple Developer Portal

In this option, all currently registered BundleIDs are listed. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-getBundle.png' />

You can list your registered BundleIDs on Appcircle by making selections from this list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-getBundleDetails.png' />

After the registration process is completed, the selected or registered BundleIDs will be listed as follows.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-bundleList.png' />

### Edit BundleID

The Action button in the BundleID list, you can edit your existing BundleID content.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-editBundle.png' />

:::info Edit Bundle

The changes you make here will be **simultaneously** modified and saved in your Apple Developer account.

:::

In the Edit screen, you can see all the capabilitiy it has in BundleID and you can add or remove them if you wish.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-editBundleDetails.png' />