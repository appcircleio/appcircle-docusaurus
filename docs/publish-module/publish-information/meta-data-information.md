---
title: Metadata Details
description: Detailed guide on filling out metadata for app distribution platforms within the Appcircle dashboard.
tags: [metadata, app distribution, appcircle dashboard]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Metadata Details

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-metadataDetails.png' />

## Overview

The Metadata Information section in the Appcircle dashboard is essential for defining the presence of your application on digital distribution platforms. This document will guide you through each field and its significance to ensure your app's metadata is complete and effective.

## iOS Metadata Information

### Localization Settings

The localization dropdown allows you to select the language in which you want to present your app’s metadata on the App Store. This feature supports multiple languages, ensuring that you can target specific demographics and cater to a global audience.

When you select a language, you will provide localized versions of your app's metadata, including promotional texts, descriptions, and what’s new in this version. Localization helps in reaching a wider audience by providing information in the users' native language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3667-meta-data-information-localization.png' />

### Metadata Auto-Population

If there is existing metadata associated with your app on the App Store, the **Metadata Information** page will automatically populate these fields with the existing data. This feature simplifies the update process by allowing you to review and modify the pre-filled information rather than starting from scratch. It ensures consistency and accuracy in your app’s metadata across different versions and localizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3667-meta-data-information-localization-get.png' />

### Metadata from Last Updated

With Appcircle's **Retrive from Last Updated** feature, you can automatically update your metadata. When a new version is added, you can directly retrieve the metadata information updated in the previous version with the **Retrive From Last Updated** function on the metadata screen. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4007-metadataUpdate1.png' />

:::caution Metadata from Last Update

With this feature, the last metadata information you saved in Appcircle is copied to the relevant version. 

Please note that if this function is used, **no data will be pulled from App Store Connect**. The data retrieved will be the metadata information saved in the **previous version**.

:::

### Fields Explained

#### iOS Previews and Screenshots

- **Drag and Drop**: Upload up to 3 app previews and 10 screenshots.
  - **iPhone**: Supported resolutions are 1290 x 2796px or 2796 x 1290px.
  - **iPad**: Supported resolutions are 2048 x 2732px or 2732 x 2048px.

#### App Information

- **Promotional Text**: Optional text to inform App Store visitors about any current app features without requiring an updated submission.
- **Description**: Provide a detailed description of your app, highlighting its features and functionalities.
- **What’s New**: Describe what’s new in this version of your app, such as new features, improvements, and bug fixes.

:::info What’s New Field
Please note, this field is constantly visible on Appcircle. However, on App Store Connect, it will **only** appear when a new version is **released**. For this reason, if you are not going to release a **new version**, you may not see the information you enter here on **App Store Connect**.
:::

- **Name**: The name of your app as it will appear on the App Store.
- **Subtitle**: A brief summary of your app, limited to 30 characters.
- **Keywords**: Include keywords that describe your app. Separate keywords with English commas, Chinese commas, or a mix of both.
- **Support URL**: A URL with support information for your app. This will be visible on the App Store.
- **Marketing URL**: A URL with marketing information about your app. This will be visible on the App Store.

#### App Version Information

- **Version**: The version number of the app following standard software versioning conventions.
- **Copyright**: The name of the person or entity that owns the copyright to your app.

#### App Review Information

- **Sign-In Information**: If your app requires a sign-in, provide credentials that will be used by the review team.
- **Contact Information**: Provide the name, phone number, and email of the contact person for the App Review team.
- **Notes**: Include any additional information that you want to share with the App Review team.

#### App Release Information

- **App Store Version Release**: Choose how you want to release your app on the App Store:
  - Manually release this version
  - Automatically release this version
  - Automatically release this version after App Review, no earlier than a specified date and time
- **Phased Release for App Store Automatic Updates**: Opt in to gradually release updates over a 7-day period to users.
- **Reset iOS App Store Summary Rating**: Decide if you want to reset the app's rating when the new version is released.

:::danger Reset iOS App Store Summary Rating
Please note, this comes with **Keep Existing Rating** selected by default. If you choose to **Reset rating when this version released** option, it will reset all past **reviews and ratings** of your app in **App Store**.
:::

## Android Metadata Information

### Localization Settings

The localization dropdown allows you to select the language in which you want to present your app’s metadata on the Google Play Console. This feature supports multiple languages, ensuring that you can target specific demographics and cater to a global audience.

When you select a language, you will provide localized versions of your app's metadata, including video, descriptions, and app name. Localization helps in reaching a wider audience by providing information in the users' native language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-235.png' />

### Metadata Auto-Population

If there is existing metadata associated with your app on the Google Play Console, the **Metadata Information** page will automatically populate these fields with the existing data. This feature simplifies the update process by allowing you to review and modify the pre-filled information rather than starting from scratch. It ensures consistency and accuracy in your app’s metadata across different versions and localizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-235-2.png' />

:::info

**Updating Android Metadata:** You can easily update your Google Play Console metadata for your app via Appcircle by following these steps:

- Update your app's metadata on Appcircle within the Publish module.
- Add the **Update Metadata on Google Play Console** Publish flow step to your workflow.
- Run your Publish Flow of your app by selecting the Publish Details under actions menu.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-235-3.png' />

This step can be configured further by selecting the step options.

<Screenshot url='https://cdn.appcircle.io/docs/assets/SP-235-4.png' />

:::caution

Your app version within the Publish profile needs to be marked as Release Candidate before you can retrieve or update Google Play Console metadata.

:::

### Fields Explained

#### Android Previews and Screenshots

- **Drag and Drop**: Upload up to 8 screenshots.
  - **Phone**: Supported resolutions are 320 to 3840 px.
  - **Tablet**: Supported resolutions are 320 to 3840px or 1080 to 7680px.
  - **Android TV**: Supported resolutions are 320 to 3840px.
  - **Wear OS**: Supported resolutions are 384 to 3840px.

#### App Information

- **Video**: Add a video by entering a YouTube URL. This video must be public or unlisted, ads must be turned off, and it must not be age restricted, and it should be landscape.
- **App Name**: This is how your app will appear on Google Play.
- **Short Description**: A short description for your app. Users can expand to view your full description.
- **Full Description**: A full description for your app.

## Microsoft Intune Metadata Information

The metadata information field can be changed according to the store credentials selection in Publish Settings. If Intune credential is selected as store credentials, the metadata screen will automatically include Microsoft Intune metadata information.

:::danger Microsoft Intune Metadata and Credential

If the Microsoft Intune credential is not selected, the metadata fields will not change. For this reason, make sure that you have integrated [**Microsoft Intune credential**](/account/my-organization/integrations/credentials/adding-microsoft-intune-api-key) and selected the correct credentials in [**Publish Settings**](/publish-module/publish-settings#store-credentials).

:::

### Metadata Auto-Population

If there is existing metadata associated with your app on the Microsoft Intune, the **Metadata Information** page will automatically populate these fields with the existing data. This feature simplifies the update process by allowing you to review and modify the pre-filled information rather than starting from scratch. It ensures consistency and accuracy in your app’s metadata across different versions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3954-inTuneMetadataRetrieve.png' />

### Fields Explained

- **Name**: Name for the app. This name will be visible in the Intune apps list and to users in the Company Portal.​
- **Description**: Help your device users understand what the app is and/or what they can do in the app. This description will be visible to them in Company Portal.
- **Publisher**: The name of the developer or company that distributes the app. This information will be visible to users in Company Portal.
- **Applicable Device Type**: Select the device types that can install this app
- **Minimum Operating System**: Select the earliest operating system version on which the app can be installed. If you assign the app to a device with an earlier operating system, it will not be installed.​
- **Category**: Categorize the app to make it easier for users to sort and find in Company Portal. You can choose multiple categories
- **Featured App**: Featured apps are prominently placed in Company Portal so that users can quickly get to them.
- **Information URL**: Link people to a website or documentation that has more information about the app. The information URL will be visible to users in Company Portal.
- **Privacy URL**: Provide a link for people who want to learn more about the app's privacy settings and terms. The privacy URL will be visible to users in Company Portal.
- **Developer**: The name of the company or Individual that developed the app. This information will be visible to people signed into the admin center.
- **Owner**: The name of the person in your organization who manages licensing or is the point-of-contact for this app. This name will be visible to people signed in to the admin center.​
- **Notes**: Add additional notes about the app. Notes will be visible to people signed in to the admin center.


## Conclusion

Filling out the Metadata Information section accurately is crucial for the successful listing and update of your app on the App Store and Microsoft Intune. It ensures that potential users receive the most current information and that your app meets all necessary guidelines for
