---
title: Benefits of Publish Module
description: Learn how to use Publish module in Appcircle
tags: [publish module, benefits, key features]
---



import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

## Why to Use the Publish Module: Features and Benefits

The Publish module in Appcircle is a powerful tool designed for managing the release process of mobile applications to various app stores, including the Apple App Store, Google Play, and Huawei AppGallery. This module streamlines the complex process of app release, enabling users to:

- **Automate Releases**: Automate the submission of apps to multiple stores, reducing the manual workload and minimizing the risk of errors.
- **Customizable Flows**: Create custom flows tailored to your release management needs, ensuring that each step of the release process aligns with your unique requirements.
- **Metadata Management**: Update and manage metadata details directly within the Publish module, keeping your app information consistent across all platforms.
- **Centralized Release Management**: Monitor, manage, and audit releases from a single platform, making the release process more efficient and organized.

By using the Publish module, you can ensure a smooth, reliable, and scalable release process for your mobile applications, enhancing the overall efficiency and effectiveness of your app release strategy.

## Getting Started

The Publish module in Appcircle is a versatile tool that simplifies the app release process. To make the most of this module, it's important to ensure that you meet all prerequisites and properly configure the necessary settings.

## Prerequisites for Using the Publish Module

Before you can start using the Publish module, there are several key prerequisites to address:

### App Stores Integrations
- You need to have developer accounts for each app store where you intend to publish your app. This includes:

    - Apple Developer Account for the **App Store** and **TestFlight**.
    - Google Play Console Account for **Google Play**.
    - Huawei Developer Account for **Huawei AppGallery**.

- Ensure that these accounts are active, and you have the necessary credentials (API keys, client secrets, etc.) to connect them to Appcircle.

### Appcircle Project Setup

- Your mobile application should be correctly set up within the Appcircle platform. This includes having a configured project with the necessary app builds (binary files) available for release.
- If you haven't set up your project in Appcircle, follow the setup guide provided in the Appcircle documentation to ensure everything is ready for publishing.

### App Metadata Preparation

- Gather all required metadata for your app, such as:

    - App name
    - Description
    - Keywords
    - App icons and screenshots
    - Privacy policy URL
    - Contact information

- Having this information prepared in advance will streamline the publishing process.

### Store Integration Permissions

- Ensure that your developer accounts have the necessary permissions to publish apps, manage metadata, and access analytics. If you're part of a team, verify that you have the appropriate role within your developer account (e.g., Admin, Release Manager).







## What are Publish Flows?

Publish flows are predefined or custom sequences of actions that automate the release process of mobile applications. These flows allow you to define the steps required to prepare, submit, and monitor your app releases across different app stores.

### Creating and Managing Flows

To create and manage flows within the Publish module:

- **Create a New Flow**: Start by creating a new flow from the "Publish Flows" section. You can choose from predefined flows or create a custom flow based on your specific needs.
- **Configure Flow Steps**: Define each step of the flow, such as fetching app information, submitting to TestFlight, or updating metadata. Configure the settings for each step according to your requirements.
- **Save and Activate**: Once the flow is configured, save it and activate it for use in the release process.

### Flow Configuration Options

Flow configuration options allow you to customize each step of the release process. Options include:


- **Conditional Logic**: Set conditions for when specific steps should be executed based on certain criteria.
- **Notifications**: Configure notifications to alert team members when a step is completed or when an issue arises.

## Publish Flow Customization

### Creating Customizable Flows

Static flows enable you to tailor the release process to your exact needs. To create a static flow:

- **Select Publish Flows**: Choose the option to create a custom flow.
- **Add Steps**: Add the steps required for your release process, such as "Send to TestFlight," "Get Approval via Email," or "Update Metadata on Microsoft Intune."
- **Configure Each Step**: Customize each step by defining the specific actions, conditions, and notifications needed for your workflow.

### Publish Flow Examples

The Publish module is designed to cater to a wide range of needs, making it suitable for both enterprise-level companies and individual developers. It possesses the capabilities to address diverse requirements effectively. Here are a few examples of custom flows you might create:

#### Beta Testing

Automatically send your app to TestFlight via Send to TestFlight step. This step will upload your binary file to TestFlight and allow you to send it to your test groups. For example, a flow has been created below using certain steps, allowing you to send your app to TestFlight solely for Beta testing purposes. The steps have been utilized in the following sequential order:

- [**App Information from App Store**](/publish-integrations/ios-publish-integrations/app-information-app-store): This step compares the Release Candidate version with the latest versions in both the TestFlight and Production environments, giving you an idea of how the release process will begin.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): After the version comparison is completed, an approval email is sent to the Release Manager to decide whether or not to proceed with the release process. This email informs the Release Manager about the release that is set to go to Beta Test. If the Release Manager sees no issues, they can click the Approve link within the email to move the process forward.
- [**Send to TestFlight**](/publish-integrations/ios-publish-integrations/sent-to-testflight): With this step, the binary is sent to TestFlight.
- [**Get Approval from TestFlight**](/publish-integrations/ios-publish-integrations/approval-test-flight): This step is presented with a UI that includes test information for the app you sent to TestFlight for beta testing. Here, you can either send the binary to a selected test group immediately or obtain approval from testers to confirm that the binary is issue-free. If the step succeeds under the selected conditions, it will proceed with a success status.

:::caution Beta Testing

The example flow provided here is limited solely to TestFlight submission and Beta Testing purposes. With this flow, the binary is only sent to TestFlight and distributed to the relevant test groups.

:::

#### Release Flow

Thanks to the capabilities of the Appcircle Publish module, you can manage your entire release process from scratch without needing to access the developer interfaces of the app stores. Below is an example flow that demonstrates how to manage a release process from start to finish. The steps have been utilized in the following sequential order:

- [**App Information from App Store**](/publish-integrations/ios-publish-integrations/app-information-app-store): This step compares the Release Candidate version with the latest versions in both the TestFlight and Production environments, giving you an idea of how the release process will begin.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): After the version comparison is completed, an approval email is sent to the Release Manager to decide whether or not to proceed with the release process. This email informs the Release Manager about the release that is set to go to Beta Test. If the Release Manager sees no issues, they can click the Approve link within the email to move the process forward.
- [**Send to TestFlight**](/publish-integrations/ios-publish-integrations/sent-to-testflight): With this step, the binary is sent to TestFlight.
- [**Get Approval from TestFlight**](/publish-integrations/ios-publish-integrations/approval-test-flight): This step is presented with a UI that includes test information for the app you sent to TestFlight for beta testing. Here, you can either send the binary to a selected test group immediately or obtain approval from testers to confirm that the binary is issue-free. If the step succeeds under the selected conditions, it will proceed with a success status.
- [**Update Metadata on App Store Connect**](/publish-integrations/ios-publish-integrations/update-metadata-on-app-store-connect): This step will assist you in updating metadata. It comes with a custom UI that displays previews of the metadata to be uploaded, allowing you to upload your most recently updated metadata to the app stores. With support for localization and screenshots, you can manage this process without needing to access the developer interfaces.





