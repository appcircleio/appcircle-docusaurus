---
title: Binary Management
description: Learn how to manage binaries in Appcircle
tags: [publish module, binary management]
---

# Binary Management

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

Appcircle supports publishing the application to the stores without using the Build module. To add an application version manually, you need to add a publish profile beforehand and then **Open** its details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-manuel.png' />

You can then upload the application by clicking on the **Add Version** button on the right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-upload.png' />

When the upload is completed successfully, the relevant application versions will appear in the list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishBinaryList.png' />

:::caution BUNDLE ID AND PACKAGE NAME MUST BE UNIQUE
You can install iOS app versions with different BundleIDs under the same Publishing Profile. However, you can only initiate the Publish process with the binary that matches the BundleID specified when creating the profile or within the profile itself.

Similarly, for Android Publish Profiles, all app versions must have identical Package Names within the Android Publish Profile.

You can view the Bundle ID (iOS) and Package Name (Android) beneath the Publish Profile name. Users can also verify this information by selecting the [Binary Information](/publish-module/publish-information/binary-information) for an app version under the actions menu.
:::

### BundleID Matching

When a binary BundleID uploaded to the Publish profile does not match the master BundleID specified for the profile, a warning icon will appear next to the binary. This icon indicates that the BundleID of the related binary does not match. For this reason, you **cannot start the Publish process** with the mismatched binary and send your application to the stores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-binaryMatch.png' />

:::caution BundleID Matching

Note that you cannot mark your application version with a mismatched BundleID as a [**Release Candidate**](/publish-module/publish-information/marking-release-candidates). 

For BundleID change, you can use the [**Resign Binary**](/publish-module/publish-information/resign-binary) feature in the Action button or upload a matching binary.

:::

Afterwards, you can start submitting your application to the stores with the publish flow that you have configured.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-version-list.png' />

For this, click on the **Actions** button for the relevant version and go to **Details**. From there, you can manually **Start Flow** for the uploaded application version.

## Store Status

Appcircle now allows you to track the App Store status of your applications directly within the Publish module. This powerful feature is tailored for **Enterprise License** holders, ensuring continuous monitoring of your application's deployment status.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3681-publish-store-status.png' />

### How It Works

- **Enterprise License**: This feature is accessible to users with an enterprise license.
- **Continuous Monitoring**: Once a version is set as a **Release Candidate**, it is automatically monitored **every 30 minutes** to check its status on **TestFlight** and the **App Store Distribution**.
- **Priority on Distribution**: If the version is available in both **TestFlight** and **App Store Distribution**, the system prioritizes the status from **App Store Distribution**.
- **Version Status**: If a version has **never** been submitted to the **App Store**, it will show as **`Not Available`**.
- **Completion of Distribution**: When a version reaches **`Ready for Distribution`**, Appcircle stops monitoring it, allowing you to focus resources on versions that still require attention.

:::caution Store Credentials Required
Ensure you select store credentials in the [Publish settings](/publish-module/publish-settings#store-credentials) to start monitoring. If the credentials are **not** selected, the status will display as **`Not Available`**.
:::

This streamlined approach ensures that you are always informed of your application's status, simplifying management and enhancing your deployment strategy directly from the Appcircle dashboard.

### Filter By Status

In the Publish module, where your Publish profiles are listed, you can use the filter option to display specific Publish profiles based on their latest store status.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter1.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter2.png' />

:::tip

The iOS Publish filter options will only display the available statuses from the existing Publish profiles in your profile list.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter4.png' />