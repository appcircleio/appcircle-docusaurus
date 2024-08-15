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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishMainPage.png' />

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
- If you haven't set up your project in Appcircle, follow the [setup guide](/publish-module/creating-publish-profiles) provided in the Appcircle documentation to ensure everything is ready for publishing.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-createProfile.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-createModal.png' />

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


## Managing the Store Integrations and Settings for Publish
Configuring store integrations and managing settings is crucial for the smooth operation of the Publish module. Here's how to set up and manage these integrations:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-integrations.png' />

### Adding and Configuring Store Integrations

#### App Store Connect Integration

For App Store Connect integration, go to integrations in your organisation. Select the App Store Connect API key from the Connections section. Fill in the information in the modal that opens and save.

- **Issuer ID**: Identifies the issuer who created the authentication token. Your issuer ID from the API Keys page in App Store Connect, for example, `57246542-96fe-1a63-e053-0824d011072a`
- **Key ID**: The .p8 file ID value.
- **.p8 File**: Generated API key file.

:::caution

**You can only download the file once**. If you lose the file, you need to generate a new key.

:::

For more information about the Generate App Store Connect API key and its integration with Appcircle, please visit the [documentation](/account/my-organization/api-integrations/adding-an-app-store-connect-api-key#login-to-app-store-connect).

#### Google Play Service Account Integration

For Google Play Service Account integration, go to integrations in your organisation. Select the Google Play Developer API Keys from the Connections section. Upload the `JSON` file in the modal that opens and save.

For more information about the Google Play Service Account API key and its integration with Appcircle, please visit the [documentation](/account/my-organization/api-integrations/adding-google-play-service-account).

#### Huawei AppGallary Integration


For Huawei AppGallery API Key integration, go to integrations in your organisation. Select the Huawei AppGallery API Key from the Connections section. Upload the `JSON` file in the modal that opens and save.

For more information about the Huawei AppGallery API Key and its integration with Appcircle, please visit the [documentation](/account/my-organization/api-integrations/adding-huawei-api-key).

#### Microsoft Intune Integration

For Microsoft Intune integration, go to integrations in your organisation. Select the Microsoft Intune from the Connections section. Fill in the information in the modal that opens and save.

- **Client ID**: Specifies the [**Application (client) ID**](https://learn.microsoft.com/en-us/entra/identity-platform/howto-call-a-web-api-with-curl?tabs=dotnet6&pivots=no-api#register-the-web-api) which uniquely identifies your application in the Microsoft cloud ecosystem, across all tenants.
- **Client Secret**: A client secret, sometimes referred to as an application password, is a string value your app can use to identify itself. Learn how to create one [here](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#option-2-add-a-client-secret).
- **Auth URL**: Specifies the authorization URL generated by the application you created on the Microsoft Identity Platform. This URL should be in the following format: `https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token`. More details [here](https://learn.microsoft.com/en-us/entra/identity-platform/howto-call-a-web-api-with-curl?tabs=dotnet6&pivots=no-api#register-the-web-api).

For more information about the Microsoft Intune and its integration with Appcircle, please visit the [documentation](/account/my-organization/api-integrations/adding-microsoft-intune-api-key).

### Accessing the Store Integrations

Once the relevant integrations are completed, you can access these connections from your profile within the Publish module. To initiate a release process, you need to select the appropriate store's credentials from the Settings screen within the Publish Profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishSetting.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishSettingDetail.png' />

### Managing Metadata and App Informations

- Within the Publish module, you can manage your app's metadata directly. This includes updating app descriptions, keywords, categories, and other store-related information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-binaryActions.png' />

- Regularly review and update your app's metadata to ensure it is current and relevant, as outdated information can negatively impact your app's visibility and user experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-metadataDetails.png' />

- At the same time, you can fill, update and review your App information, which is required for store submission, through Appcircle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-appInfo.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-appInfoDetails.png' />


## What are Publish Flows?

Publish flows are predefined or custom sequences of actions that automate the release process of mobile applications. These flows allow you to define the steps required to prepare, submit, and monitor your app releases across different app stores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flows.png' />

### Creating and Managing Flows

To create and manage flows within the Publish module:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flowDetails.png' />

- **Create a New Flow**: Start by creating a new flow from the "Publish Flows" section. You can choose from predefined flows or create a custom flow based on your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-manageFlow.png' />

- **Configure Flow Steps**: Define each step of the flow, such as fetching app information, submitting to TestFlight, or updating metadata. Configure the settings for each step according to your requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flowConfig.png' />

- **Save and Activate**: Once the flow is configured, save it and activate it for use in the release process.

### Flow Configuration Options

Flow configuration options allow you to customize each step of the release process. Options include:

- **Conditional Logic**: Set conditions for when specific steps should be executed based on certain criteria.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flowConditions.png' />

- **Notifications**: Configure notifications to alert team members when a step is completed or when an issue arises. To configure a type of Notification please follow the [Notification Integration](/account/my-organization/notifications-and-communication) documentation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-notifications.png' />


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


## Managing Releases

Effective release management is crucial for ensuring the success of your app updates. The Publish module provides you with the tools to monitor, control, and optimize the release process. You can track the status of your releases in real-time, manage approvals, and address any issues that arise during the process. 

Additionally, the module allows you to roll back to previous versions if needed, ensuring that you have full control over your app's distribution. By leveraging these features, you can maintain a smooth and efficient release cycle, minimizing disruptions and maximizing the impact of your updates.

### Releasing a New Version

Releasing a new version of your app through the Publish module involves a few key steps:

- **Prepare the App**: Start by ensuring your app is fully prepared for release. This includes compiling the binary, verifying that all necessary metadata (such as app descriptions, keywords, and screenshots) is up-to-date, and ensuring that your app meets all store requirements.

- **Select a Flow**: Next, choose the appropriate flow that aligns with your release strategy. This could be a standard release flow for a regular update or a custom flow tailored to specific needs, such as beta testing.

- **Execute the Flow**: Once the flow is selected, execute it to automate the entire submission process. The flow will handle everything from submitting the binary to obtaining approvals and completing the release across the chosen app stores. Each step in the flow ensures that your app is released smoothly and efficiently.

### Monitoring and Managing Releases

After initiating a release, the Publish module provides tools to monitor and manage the process:

- **Release Dashboard**: View the status of your releases in real-time, including pending approvals, successful submissions, and any errors that occur.

- **Notifications**: Receive notifications for key events, such as when a release is approved or when an issue is detected.

- **Rollback Options**: If needed, rollback to a previous version of your app or pause a release to address any issues.

### Third Party Integrations

The Publish module offers robust support for integrations with third-party tools, enhancing and streamlining your app release process. By connecting with these tools, you can automate, monitor, and improve every aspect of your app's lifecycle.

- **CI/CD Tools**: Integrate the Publish module with continuous integration/continuous deployment (CI/CD) tools like Jenkins, GitHub Actions to automate your build and release pipeline. Through the Appcircle API, you can seamlessly connect these tools, allowing for automated triggers that initiate a release as soon as a new build is ready. This integration ensures a consistent and efficient deployment process, reducing manual intervention and the risk of errors.

- **Analytics Platforms**: Post-release, it’s crucial to monitor your app’s performance and gather user feedback. The Publish module can be integrated with analytics platforms such as Google Analytics, Firebase, or Mixpanel via the Appcircle API. These integrations enable you to track key metrics, user behavior, and overall app health in real-time, helping you make informed decisions for future updates.

- **Notification Tools**: Keeping your team informed about the release progress is essential for a coordinated effort. The Publish module can be integrated with collaboration tools like Slack or Microsoft Teams. By setting up these integrations, you can automatically send notifications about key events in the release process—such as successful deployments or issues that need attention—ensuring that everyone stays in the loop and can act swiftly when needed.

### Auditing and Reporting Releases

The Publish module provides comprehensive auditing and reporting features that give you full visibility into your release process.

- **Activity Log**: The Activity Log keeps a detailed record of every action taken during the release process, including who performed each action and when it occurred. This log is invaluable for tracking changes, identifying issues, and ensuring accountability within your team.


## Publish Module Troubleshooting

When using the Publish module, it's essential to know how to troubleshoot potential issues that may arise during the release process. Whether you're dealing with failed submissions, integration errors, or flow execution problems, having a clear understanding of common issues and their solutions can save you time and ensure a smooth release. The troubleshooting section will guide you through diagnosing and resolving problems efficiently, providing tips on how to maintain successful integrations, correct configuration errors, and ensure that your app releases proceed without interruptions.

### Common Issues and Solutions

While the Publish module is designed for reliability, you may occasionally encounter issues. Here are some common problems and their solutions:

- **Failed Submissions**: Submissions can fail for various reasons. One common issue is a conflicting version number—if the version you're trying to submit already exists on the store, you'll need to increment the version number. Another issue could be an invalid binary, which might occur if the app doesn’t meet store requirements or if there are missing assets. Always check the error logs for specific details, correct any issues, and attempt the submission again.

- **Integration Errors**: Integration errors often stem from misconfigured store connections. If the API connection fails, it could be due to incorrect credentials or an expired API token. Additionally, ensure that the account you're using has the necessary permissions to perform actions like submitting apps or updating metadata. Double-check all API keys, tokens, and permissions to resolve these issues.

- **Flow Execution Problems**: If a flow doesn't execute as expected, it might be due to incorrect configuration settings. Review each step of the flow to ensure everything is set up correctly, such as conditions, triggers, and action sequences. If the problem persists, try testing the flow in a staging environment to isolate the issue before rerunning it in production.

### Frequently Asked Questions

This section provides answers to frequently asked questions about the Publish module, including:

#### How do I update my app's metadata?

#### What happens if a release is rejected by the app store?

### Further Support and Resources

If you need additional help with the Publish module, the following resources are available:

- **Appcircle Support**: Contact [**Appcircle Slack support**](https://slack.appcircle.io/) for personalized assistance with your specific issues. 

- **User Documentation**: Refer to the Appcircle user documentation for detailed guides and troubleshooting tips for Publish Module.




