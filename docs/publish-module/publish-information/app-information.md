---
title: App Store Connect Information
description: Learn how to update App Information in the Publish module of Appcircle
tags: [publish, publish module, app information, app store connect, review]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# App Store Connect Information

For a binary to be successfully sent for review, certain information must be completed. By using Appcircle's App Information feature, you can update the required information for binary submission.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-appInfoNew.png' />

### Localizable Informations

The localization dropdown allows you to select the language in which you want to present your app’s information on the App Store. This feature supports multiple languages, ensuring that you can target specific demographics and cater to a global audience.

When you select a language, you will provide localized versions of your app's information, including name, subtitle, and privacy policies. Localization helps in reaching a wider audience by providing information in the users' native language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3926-localizeInfo.png' />

### General Informations

General information area allows you to see and update some of your information that will appear on the market for your application. 

In these fields, you can specify the category of your application and provide information about the content it contains.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3926-generalInfo.png' />

### Update and Save

You can instantly view your current App Information details and, if desired, simultaneously update these values on your App Store Connect account. Each time this screen is opened, the current information will be retrieved.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3926-appInfoDetails.png' />

:::danger App Information Save

When you make a change to these informations and click the **save button**, the updates will be **immediately** applied to your App Store Connect account. Make sure your selections are **correct** and the information entered is **accurate**.

:::

### Fields Explained

#### Localizable Information

- **Name**: The name of your app as it will appear on the App Store.
- **Subtitle**: A brief summary of your app, limited to 30 characters.
- **Privacy URL**: A URL that links to your privacy policy. A privacy policy is required for all apps.
- **User Privacy Choices URL**(Optional): A URL where users can modify and delete the data collected from the app, or decide how their data is used and shared.

#### General Information

- **BundleID**(Read-Only): The bundle ID must match the one you used in Xcode. It can't be changed after you upload your first build.
- **SKU**(Read-Only): A unique ID for your app that is not visible to users.
- **Apple ID**(Read-Only): An automatically generated ID assigned to your app.
- **Primary Language**: If localized app information isn’t available in a country or region, the information from your primary language will be used instead.
- **Primary Category**: The primary category that best describes this app.
- **Secondary Category**(Optional): The secondary category that best describes this app.
- **Content Rights**: If your app contains, shows, or accesses any third-party content, you must have the rights to it or be permitted to use the content.
