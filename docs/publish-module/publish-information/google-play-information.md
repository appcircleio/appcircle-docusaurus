---
title: Google Play Console Information
description: Learn how to update App Information in the Publish module of Appcircle for Google Play Console
tags: [publish, publish module, app information, google play console, review]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Google Play Console Information

For Android binaries, by using Appcircle's Google Play Console Information feature, you can update the required information for binary submission.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-236.png' />

### Contact Information

You can fill in your contact information to be displayed on Google Play, including your email address, phone number, and website.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-236-2.png' />

### General Information

The general information area allows you to see and update the default language and configure your auto review setting for your app on Google Play Console.

#### Default Language

The default language for an app on Google Play Console is the primary language in which the app’s store listing (title, description, and other metadata) is displayed when a user visits the app’s page. If a user’s device language is not supported by the app’s store listing, they will see the information in the default language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5649-info.png' />

#### Auto Send for Review

Auto Send for Review is where you select whether your changes should automatically go for review on the Google Play Console. Please note that this setting is optional.

:::info Understanding the `changesNotSentForReview` Parameter in Google Play Android Publisher API
When making release requests via the Google Play Android Publisher API, the `changesNotSentForReview` parameter determines whether your changes are immediately sent for review or not. However, Google enforces certain constraints, requiring this parameter to be either `true` or `false` depending on the current status of the app and other factors. To handle this behavior efficiently.
:::

We provide four different options for managing releases:

1. **Send for Review Automatically but Rescue Errors**: 
- The system will attempt to send changes for review. 
- If an error occurs due to `changesNotSentForReview` being set incorrectly, the API call will be retried with the opposite value.

2. **Don't Send for Review Automatically but Rescue Errors**: 
- The system will attempt to keep changes in a draft state without sending them for review.
- If an error occurs due to `changesNotSentForReview` being set incorrectly, the API call will be retried with the opposite value.

3. **Always Send for Review Automatically**: 
- The system will always attempt to send changes for review.
- If an error occurs, the process will fail without retrying.

4. **Never Send for Review Automatically**: 
- The system will always attempt to keep changes in a draft state.
- If an error occurs, the process will fail without retrying.

By selecting the appropriate option, you can ensure that your release process aligns with Google's requirements while maintaining flexibility in handling potential API constraints.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5649-info2.png' />

### Update and Save

You can instantly view your current App Information details and, if desired, simultaneously update these values on your Google Play Console account. Each time this screen is opened, the current information will be retrieved.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-236-3.png' />

:::danger App Information Save

When you make a change to this information and click the **save button**, the updates will be **immediately** applied to your Google Play Console account. Make sure your selections are **correct** and the information entered is **accurate**.

:::

### Fields Explained

#### Contact Information

- **Email Address**: The email address that will be displayed on Google Play.
- **Phone Number**: The phone number that will be displayed on Google Play.
- **Website**: The website that will be displayed on Google Play.

#### General Information

- **Default Language**: The default language for your app.
- **Auto Send for Review**: Select whether your changes should automatically go for review on the Google Play Console.