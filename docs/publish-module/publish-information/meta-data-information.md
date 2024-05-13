---
title: Metadata Information
description: Detailed guide on filling out metadata for app distribution platforms within the Appcircle dashboard.
tags: [metadata, app distribution, appcircle dashboard]
---

import Screenshot from '@site/src/components/Screenshot';

# Metadata Information

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3667-meta-data-information-menu.png' />

## Overview

The Metadata Information section in the Appcircle dashboard is essential for defining the presence of your application on digital distribution platforms. This document will guide you through each field and its significance to ensure your app's metadata is complete and effective.

:::note
The Metadata Information section is available for iOS apps only currently. We will be adding support for Android apps in the future.
:::

## iOS Metadata Information

### Localization Settings

The localization dropdown allows you to select the language in which you want to present your app’s metadata on the App Store. This feature supports multiple languages, ensuring that you can target specific demographics and cater to a global audience.

When you select a language, you will provide localized versions of your app's metadata, including promotional texts, descriptions, and what’s new in this version. Localization helps in reaching a wider audience by providing information in the users' native language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3667-meta-data-information-localization.png' />

### Metadata Auto-Population

If there is existing metadata associated with your app on the App Store, the **Metadata Information** page will automatically populate these fields with the existing data. This feature simplifies the update process by allowing you to review and modify the pre-filled information rather than starting from scratch. It ensures consistency and accuracy in your app’s metadata across different versions and localizations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3667-meta-data-information-localization-get.png' />

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

## Conclusion

Filling out the Metadata Information section accurately is crucial for the successful listing and update of your app on the App Store. It ensures that potential users receive the most current information and that your app meets all necessary guidelines for
