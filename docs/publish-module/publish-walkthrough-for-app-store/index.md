---
title: Publish Walkthrough for App Store
description: Learn how to use Publish module in Appcircle
tags: [publish module, benefits, key features]
---



import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

## Why to Use the Publish Module: Features and Benefits

The Publish module in Appcircle is a powerful tool designed for managing the release process of mobile applications to various app stores, including the Apple App Store, Google Play, and Huawei AppGallery. This module streamlines the complex process of app release, enabling users to:

- **Centralized Release Management**: Monitor, manage, and audit releases from a single platform, making the release process more efficient and organized.
- **Automate Releases**: Automate the submission of apps to multiple stores, reducing the manual workload and minimizing the risk of errors.
- **Flexibility in Publishing**: Appcircle provides the flexibility to publish your applications to various platforms, including app stores and internal app distribution systems. This ensures that your app reaches the right audience through the most suitable channels.
- **Isolation from Complex Interactions**: Eliminate the need for direct interaction with individual app stores like the App Store, Google Play, and Huawei AppGallery. Appcircle acts as a central hub, isolating you from the complexities and variances of each store’s submission processes. 

By using the Publish module, you can ensure a smooth, reliable, and scalable release process for your mobile applications, enhancing the overall efficiency and effectiveness of your app release strategy. 

https://appcircle.io/publish-to-stores

## Getting Started

The Publish module in Appcircle is a versatile tool that simplifies the app release process. To make the most of this module, it's important to ensure that you meet all prerequisites and properly configure the necessary settings. The following sections outline the initial steps to start a release process using the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishStart.png' />

## Prerequisites for Using the Publish Module

Before you can start using the Publish module, there are several key prerequisites to address:

### App Store Integration

The most important requirement before getting started is an Apple Developer account and an API key generated for that account. For detailed instructions on generating an App Store Connect API key, please refer to Apple's documentation as follows:

https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api

:::caution App Store Connect Integration Permissions

Ensure that your developer accounts have the necessary permissions to publish apps, manage metadata, and access analytics. If you're part of a team, verify that you have the appropriate role within your developer account (Release Manager and above role).

Please visit the [**Apple App Store Connect Permission**](https://developer.apple.com/help/account/manage-your-team/roles/) documentation for more information.

:::

### Adding an App Store Connect API Key

For App Store Connect integration, go to Integrations under My Organization. Select the App Store Connect API Key from the Connections section. Fill in and save the information in the next screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-orgIntegration.png' />


- **Issuer ID**: Identifies the issuer who created the authentication token. Your issuer ID from the API Keys page in App Store Connect, for example, `57246542-96fe-1a63-e053-0824d011072a`
- **Key ID**: The .p8 file ID value.
- **.p8 File**: Generated API key file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-integrationModal.png' />

:::caution For .p8 File

**You can download the file only once**. If the file is lost, you need to generate a new key.

:::

For more information about the generating App Store Connect API key and App Store Connect integration in Appcircle, please refer to the [documentation](/account/my-organization/api-integrations/adding-an-app-store-connect-api-key#login-to-app-store-connect).


### App Metadata and Binary Preperation

Before starting the release process, it's essential to prepare all necessary app metadata and binary files. This preparation ensures a smooth and efficient publishing experience.

:::info Binary

The binary file can be uploaded to the Publish module either manually or through the Build module. For more detailed instructions, please refer to the [**Upload Binary**](/publish-module/publish-walkthrough-for-app-store#uploading-binary) section.

:::

- Gather all required metadata for your app for the targeted store(s), such as:

    - App name
    - Description
    - Keywords
    - App icons and screenshots
    - Privacy policy URL
    - Contact information

- Having this information prepared in advance will streamline the publishing process.


## Publish Setup Process

- Your mobile app should be correctly set up within the Appcircle platform. This includes having a configured project with the necessary app builds (binary files) available for release. To set up a profile, click the **Add New** button on the top right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishStartCreate.png' />

:::tip Set Up Project

If you haven't set up a project in Appcircle before, follow the detailed [**setup guide**](/publish-module/creating-publish-profiles) provided in the Appcircle documentation to ensure everything is ready for publishing.

:::

### Creating a Publish Profile

- There are two different ways to create a Publish Profile. One option is to create the profile manually, and the other is to retrieve an existing profile from App Store Connect. For detailed information please visit the [**Creating Publish Profile**](/publish-module/creating-publish-profiles) documentation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-profileCreateModal.png' />

:::info Create from App Store Connect

To use this profile creation method, you must have an API key integration in place. Please refer to the detailed documentation for [**Create from App Store Connect**](/publish-module/creating-publish-profiles#create-from-app-store-connect) and [**API integration**](/account/my-organization/api-integrations/adding-an-app-store-connect-api-key).

:::

### Select an App Store API Key

Once the required integrations are set up, you can access these platforms from your profile within the Publish module. To initiate a release process, you need to select the credentials for the related store from the Settings screen under the Publish Profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishSetting.png' />

- All available integrations will be shown in the Settings screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishSettingDetail.png' />

### Update App Store Connect Information

- Within the Publish module, you can update and review your app's information directly. This includes updating app name, subtitle, categories, and other store-related information such as privacy URLs, primary languages, etc. Please visit the [**App Store Connect Information**](/publish-module/publish-information/app-information) documentation for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-appInfoButton.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-appInfoDetails.png' />



### Publish Flow Customization

Publish flows are used to automate multiple tasks and introduce automation checkpointsfor application deployments to stores. You can create and manage flows within the Publish module as outlined below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flows.png' />

- **Create a New Flow**: Start by creating a new flow from the "Publish Flows" section. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-manageFlowDetails.png' />

- You can choose from predefined flows or create a custom flow based on your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-dragDropFlow.png' />


- **Configure Flow Steps**: Define each step of the flow, such as fetching app information, submitting to TestFlight, or updating metadata. Configure the settings for each step according to your requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-configureStep.png' />

- **Save and Activate**: Once the flow is configured, you can save and activate it for use in the deployment process.



### Publish Flow Samples

The Publish module is designed to cater to a wide range of needs, making it suitable for both enterprise-level companies and individual developers. Here are a few examples of custom flows you might create:

#### Beta Testing and Release Flow

With the Appcircle Publish module, you can manage your entire release process from scratch without needing to access the developer interfaces of the app stores. Below is an example flow that demonstrates how to manage a release process including testing from start to finish. The steps are utilized in the following order:

- [**App Information from App Store**](/publish-integrations/ios-publish-integrations/app-information-app-store): This step compares the Release Candidate version with the latest versions in both the TestFlight and Production environments, giving you an idea of how the release process will begin.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): After the version comparison is completed, an approval email is sent to the Release Manager to decide whether or not to proceed with the release process. This email informs the Release Manager about the release that is set to go to Beta Test. If the Release Manager sees no issues, they can click the Approve link within the email to move the process forward.
- [**Send to TestFlight**](/publish-integrations/ios-publish-integrations/sent-to-testflight): With this step, the binary is uploaded to TestFlight.
- [**Get Approval from TestFlight**](/publish-integrations/ios-publish-integrations/approval-test-flight): This step is presented with a UI that includes test information for the app you sent to TestFlight for beta testing. Here, you can either send the binary to a selected test group immediately or obtain approval from testers to confirm that the binary is issue-free. If the step succeeds under the selected conditions, it will proceed accordingly.
- [**Update Metadata on App Store Connect**](/publish-integrations/ios-publish-integrations/update-metadata-on-app-store-connect): This step will assist you in updating metadata. It comes with a custom UI that displays previews of the metadata to be uploaded, allowing you to update metadata in the app stores for this new release. With support for localization and screenshots, you can manage metadata updates without the need for direct access the app store listing management interfaces.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): After receiving approval from TestFlight and uploading the metadata, you can send an approval email to the Release Manager to review the Beta Test and the updated metadata. If everything is in order, the Release Manager can approve the process, allowing the flow to continue and submit the version for release.
- [**Submit for Review on App Store**](/publish-integrations/ios-publish-integrations/add-for-review-on-app-store): After receiving the final approval from the Release Manager, the binary file and the updated metadata are sent to the final step of the release process: app review. This step directly submits the version for review in the store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-betaReleaseFlow.png' />


### Setting Up Notifications

- Keeping your team informed about the release progress is essential for a coordinated effort. The Publish module can be integrated with collaboration tools like [**Slack**](/account/my-organization/notifications-and-communication/slack/slack-notifications) or [**Microsoft Teams**](/account/my-organization/notifications-and-communication/teams-notifications) for notifications. By setting up these integrations, you can automatically send notifications about key events in the release process—such as successful deployments or issues that need attention—ensuring that everyone stays in the loop and can act swiftly when needed. Please visit the related [**Notifications Integration**](/account/my-organization/notifications-and-communication) documentation for more detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-notificationInteg.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-notiIntegDetail.png' />

## Managing Releases

Effective release management is crucial for ensuring the success of your app updates. The Publish module provides you with the tools to monitor, control, and optimize the release process. You can track the status of your releases in real-time, manage approvals, and address any issues that arise during the process. Also, the Publish Module offers customizable flows to provide more detailed management of the release process.

Additionally, the module allows you to roll back to previous versions if needed, ensuring that you have full control over your app's distribution. By leveraging these features, you can maintain a smooth and efficient release cycle, minimizing disruptions and maximizing the impact of your updates.

### Uploading a Binary

Easily upload your binary file to the Publish module, either manually or via the Build module, to begin the release process.

#### Manual Binary Upload

You can upload your binary file directly to the Publish module using the manual upload option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-manuelUpload1.png' />

#### Upload via Build Module

You can deploy your binary file to the Publish module from the Build module automatically. This method automates the binary deployment process, ensuring that your binary is transferred directly from the Build pipeline to the Publish module, ready for release. It simplifies the flows and reduces the risk of manual errors.

:::info Upload via Build Module

To upload a binary from the Build module, please refer to the [**Distribution Configuration**](/build/build-process-management/build-profile-configuration#distribution-configuration) and [**Post-Build Operations**](/build/post-build-operations/after-a-build) documents for step-by-step instructions.

:::

#### Upload using CLI & API

If you have your own CI environment, you can use the Appcircle API & CLI to upload binaries to the related publish Profile.

- **Other CI/CD Tools**: You can integrate the Publish module with continuous integration/continuous deployment (CI/CD) tools like Jenkins and GitHub Actions to automate your build and release pipeline. With the Appcircle [**API & CLI**](/appcircle-api), you can seamlessly connect these tools, allowing for automated triggers that initiate a release as soon as a new build is ready. This integration ensures a consistent and efficient deployment process, reducing manual intervention and the risk of errors. You can check out [**Appcircle Marketplace**](/marketplace) for more integrations.

To get more information, please refer to our [**API & CLI**](/appcircle-api) documentation.


### Update Metadata

- Within the Publish module, you can manage your app's metadata directly. This includes updating app descriptions, keywords, and other store-related information. Please visit the [**Metadata Details**](/publish-module/publish-information/meta-data-information) documentation for more information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-actionMetadata.png' />

- Regularly review and update your app's metadata to ensure it is current and relevant, as outdated information can negatively impact your app's visibility and user experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-actionMetadataDetails.png' />


### Set Binary as Release Candidate

- Designate the current build as the Release Candidate, signaling that it is ready for final testing and potential release. You can refer to the [**Marking as Release Candidate**](/publish-module/publish-information/marking-release-candidates) document for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-markRc.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-rcTag.png' />

### Execute the Flow

- Once the flow is selected, you can run it to automate the entire publishing process. The flow will handle everything from submitting the binary to obtaining approvals and completing the release actions for the selectd app stores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-startPublish.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-publishLog.png' />

### Manage Release Status

After initiating a release, the Publish module provides tools to monitor and manage the process:

#### Release Dashboard

View the status of your releases in real-time, including pending approvals, successful submissions, and any errors that occur.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-monitorRelease.png' />

#### Rollback Options

If needed, you can rollback to a previous version of your app or pause a release to address any issues. Appcircle provides [**Cancel Submission**](/publish-module/publish-information/cancel-submission) and [**Reject Binary**](/publish-module/publish-information/reject-binary) features. If a version faces an issue or the wrong binary was sent for release, you can reject the binary or cancel the current submission in Appcircle.

- You can cancel the submission on App Store Connect if the binary was sent for review.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-subCancel.png' />

- Additionally, the binary can be rejected to be excluded from the publish process, and the rejection reason is displayed as a tag on binary

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-rejection.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-rejectionMessage.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-rejectionTag.png' />


### Auditing Releases

The Publish module provides comprehensive auditing and reporting features that give you full visibility into your release process.

- **Activity Log**: The Activity Log keeps a detailed record of every action taken during the release process, including who performed each action and when it occurred. This log is invaluable for tracking changes, identifying issues, and ensuring accountability within your team.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-logActivity.png' />


## Publish Module Troubleshooting

When using the Publish module, it's essential to know how to troubleshoot potential issues that may arise during the release process. Whether you're dealing with failed submissions, integration errors, or flow execution problems, having a clear understanding of common issues and their solutions can save you time and ensure a smooth release. 

### Common Issues and Solutions

While the Publish module is designed for reliability, you may occasionally encounter issues due to various reasons. Here are some common problems and their solutions:

- **Failed Submissions**: Submissions can fail for various reasons. One common issue is a conflicting version number—if the version you're trying to submit already exists on the store, you'll need to increment the version number. Another issue could be an invalid binary, which might occur if the app doesn’t meet store requirements, have a technical issıes or if there are missing assets. Always check the error logs for specific details, correct any issues, and attempt the submission again.

- **Integration Errors**: Integration errors often stem from misconfigured store connections. If the API connection fails, it could be due to incorrect credentials or an expired API token. Additionally, ensure that the account you are using has the necessary permissions to perform actions like submitting apps or updating metadata. Double-check all API keys, tokens, and permissions to resolve these issues.

- **Flow Execution Problems**: If a flow doesn't execute as expected, it might be due to incorrect configuration settings. Review each step of the flow to ensure everything is set up correctly, such as conditions, triggers, and action sequences. If the problem persists, try testing the flow in a staging environment to isolate the issue before rerunning it in production.

### Frequently Asked Questions About the Publish Module

#### How do I update my app's metadata?

To update your app's metadata, navigate to the Publish module, select the relevant profile, click the Actions button for the binary, and go to Metadata details. You can now update the metadata fields such as the app name, description, and screenshots. After saving your changes, submit the updated metadata for review if required.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-actionMetadata.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-actionMetadataDetails.png' />

#### Is it possible to automate notifications for team members during the release process?

Yes, it is possible. The Publish module allows you to set up automated notifications for your team members at various stages of the release process. You can configure notifications to be sent via email or integrate with collaboration tools like Slack or Microsoft Teams, ensuring that everyone involved is kept up to date on the release status.

For more information, please refer to the [**Notification Integrations**](/account/my-organization/notifications-and-communication) document.

#### Can I track the progress of the app release in real-time?

Yes, the Publish module provides real-time tracking of the app release process. You can monitor each step of the flow, view the status of your submission, and receive notifications about any changes or issues. This feature allows you to stay informed and take action immediately if necessary.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-monitorRelease.png' />

#### What happens if a release is rejected by Apple?

If your binary is rejected by Apple in App Store Connect, the status on Appcircle will change to **Rejected**. You can view the binary's status directly from Appcircle without the need to visit App Store Connect. However, the rejection reasons are not shared with external parties through the App Store Connect APIs. To find out the specific reason for the rejection, you can view them on App Store Connect.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-monitorRelease.png' />

#### Can I use the Publish Module with other CI tools?

Yes, you can use other CI tools to upload a binary to the Publish module. By utilizing Appcircle [**API & CLI**](/appcircle-api) within your chosen CI tool, you can directly send the binary to the relevant profile and manage the Publish process. 

Additionally, you can check our existing integrations in the [**Appcircle Marketplace**](/marketplace) documentation for integration alternatives for the **Appcircle API and CLI**.

#### Can I manage the team members roles for Publish Module?

Appcircle provides users with a comprehensive role management system. This system allows you to assign specific permissions to all organization members on an organization-wide basis. 

For more information, please refer to the [**Role Management**](/account/my-organization/role-management) document.

#### Can I manage multiple app store accounts within the Publish module?

Yes, the Publish module allows you to manage multiple app store accounts within a single interface. You can set up and integrate different accounts, such as Apple App Store, Google Play, and Huawei AppGallery, and then select the appropriate account during the release process. This flexibility ensures that you can handle releases across multiple platforms efficiently.

#### How do I create a custom flow in the Publish module?

To create a custom flow, navigate to the Publish module and select the "Publish Flow" option. From there, you can choose and arrange the steps needed for your release process, configure each step according to your requirements, and save the flow for future use. Custom flows allow you to tailor the release process to fit your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE4255-flows.png' />

#### How can I roll back to a previous version if needed?

If you need to roll back to a previous version, you can do so by selecting the desired version from your release history within the Publish module. This process involves re-uploading the previous binary and metadata, then executing a flow to re-release that version. Rolling back ensures that you can quickly address any issues with the current release without significant downtime.

### Further Support and Resources

If you need additional help with the Publish module, the following resources are available:

- **Appcircle Support**: Contact [**Appcircle Slack support**](https://slack.appcircle.io/) for personalized assistance with your specific issues. 

- **User Documentation**: Refer to the Appcircle user documentation for detailed guides and troubleshooting tips for Publish Module.



