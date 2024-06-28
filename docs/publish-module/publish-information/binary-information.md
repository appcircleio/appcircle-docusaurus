---
title: Binary Information
description: Learn how to view and manage binary information in Appcircle
tags: [publish module, binary information]
sidebar_position: 4
---

# Binary Information

The "Binary Information" feature in the Publish module provides essential details about the app's binary file. This information is critical for understanding the specifics of each build.

## Viewing Binary Information

To access the binary details for a specific version of your app:

1. **Navigate to the Appropriate Version:**

   - Within the Publish module, locate and select the version you want to examine.

2. **Open Binary Information:**
   - Click on the "Binary Information" option to display the binary details.

## Contents of Binary Information

The Binary Information section typically includes:

- **App Name:** The name of the application.
- **Binary:** The file name of the binary.
- **Binary Size:** The size of the binary file.
- **Version:** The release version of the application.
- **Version Code:** An internal version number used for identifying builds.
- **Bundle ID:** The unique bundle identifier for iOS apps.
- **Signed Certificate Name:** The name of the certificate used to sign the app.
- **Provision Profile Type:** The type of provisioning profile used for the build.

Additionally, you'll find:

- **Release Notes:** Any notes or remarks associated with the release.
- **Entitlements:** A list of app entitlements that grant specific capabilities to the app.

## Example

Here's an example of how binary information might appear:

```plaintext
App Name: My App
Binary: my-app.ipa
Binary Size: 25 MB
Version: 1.0.0
Version Code: 100
Bundle ID: com.mycompany.myapp
Signed Certificate Name: iOS Distribution
Provision Profile Type: App Store
Release Notes: Initial release
Entitlements: Push Notifications, In-App Purchases
```

## Release Notes

Release Notes are an important part of the binary information, providing context and details about what is included in each version of the application. These notes are shared with the users or testers and often contain information about new features, bug fixes, and other updates.

### Adding Release Notes

Before publishing your binary to the app stores, you can add Release Notes in the Publish module:

1. **Access Binary Information:**

   - Navigate to the 'Binary Information' section for the selected app version in the Publish module.

2. **Input Release Notes:**

   - Click on the text field under 'Release Notes' to type in your message.
   - Detail the key points that users should know about the new app version, such as new features, improvements, or issues resolved.

3. **Save Release Notes:**
   - Once you have entered the release notes, save your changes.
   - These notes will accompany the binary when it is published, so ensure they are clear and concise.

### Best Practices for Release Notes:

- **Be Clear:** Write in a simple, direct language so that all users can understand the changes.
- **Be Concise:** Keep the notes brief but informative — avoid overwhelming the user with too much information.
- **Highlight Important Changes:** Clearly state any major new features, bug fixes, or any changes that affect user interactions.
- **Localization:** If your app supports multiple languages, consider localizing the release notes for each supported language.

Release Notes are an essential tool for communication with your users. They can significantly impact the user's perception and adoption of new updates. Always include them as part of your publishing process.

:::caution Release Notes Character Limit on TestFlight
When submitting updates through TestFlight, the "What to Test" section has a 4,000-character limit. If your release notes exceed this limit, Apple will automatically trim the message to fit. Please ensure your notes are within this limit to avoid any important information being cut off.
:::

## Entitlements Detail

Entitlements are key-value pairs that define various permissions and features your app can use. You might see entries like:

- `aps-environment`: Determines the push notification environment.
- `application-identifier`: Uniquely identifies your app.
- `keychain-access-groups`: Defines groups for sharing keychain data.
- `get-task-allow`: Controls the app's ability to be debugged.

Remember, the binary information reflects the build details at the time of its creation and is crucial for troubleshooting and validating app versions.

Ensure to review the binary information for each build to confirm that the correct details are included before proceeding with the publish flow. This information is essential for ensuring that the app is correctly configured and ready for submission to the app stores.
