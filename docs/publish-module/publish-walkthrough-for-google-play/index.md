---
title: Publish Walkthrough for Google Play
description: Learn how to use Publish module in Appcircle
tags: [publish module, benefits, google play, android, metadata, publish, appcircle, walkthrough]
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

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishstart2.png' />

## Prerequisites for Using the Publish Module

Before you can start using the Publish module, there are several key prerequisites to address:

### Creating and Adding Google Play Developer API key.

The most important requirement before getting started is a Google Play Console account and an API key generated for that account.
For detailed instructions on generating a Google Play Console API key, please refer to the Appcircle documentation below:

- [**Creating and Adding Google Play Developer API key to Appcircle**](/account/my-organization/security/credentials/adding-google-play-service-account)

:::caution Google Play Console Integration Permissions

Ensure that your developer account has the necessary permissions to publish apps, manage app information, and access reports and statistics.
If you're part of a team, make sure you have the appropriate role within your Google Play Console account (Admin or a custom role with required permissions).

For more information, please visit the Google Play Console User Roles and Permissions documentation.

Please visit the [**Google Play Console User Roles and Permissions**](https://support.google.com/googleplay/android-developer/answer/9844686?hl=en) documentation for more information.

:::

For Google Play Console integration, 

- Go to **Integrations** under **My Organization**.
- Select **Google Play Developer API Key** from the **Credentials** section.
- On the next screen, fill in the required information and click Save.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-orgIntegration.png' />

- **Save API Key For Reuse**: Give this key a reusable name.
- **.json File**: Generated API key json file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-integrationModal.png' />

:::caution For .json File

**You can upload the file only once**. If the file is lost, you need to generate a new key.

:::

### App Metadata and Binary Preparation (Binary and Metadata Preparation)

Before starting the release process, it's essential to prepare all necessary app metadata and binary files. This preparation ensures a smooth and efficient publishing experience.

:::info Binary

The binary file can be uploaded to the Publish module either manually or through the Build module. For more detailed instructions, please refer to the [**Upload Binary**](/publish-module/publish-walkthrough-for-google-play#uploading-a-binary) section.

:::

- Gather all required metadata for your app for the targeted store(s), such as:

    - Package name
    - Description
    - Keywords
    - App icons and screenshots
    - Privacy policy URL
    - Contact information

- Having this information prepared in advance will streamline the publishing process.

## Publish Setup Process

- Your mobile app should be correctly set up within the Appcircle platform. This includes having a configured project with the necessary app builds (binary files) available for release. To set up a profile, click the **Add New** button on the top right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishStartCreate2.png' />

:::tip Set Up Project

If you haven't set up a project in Appcircle before, follow the detailed [**setup guide**](/publish-module/creating-publish-profiles) provided in the Appcircle documentation to ensure everything is ready for publishing.

:::

### Creating a Publish Profile 

- There are two different ways to create a Publish Profile. One option is to create the profile manually, and the other is to retrieve an existing profile from Google Play Console. For detailed information please visit the [**Creating Publish Profile**](/publish-module/creating-publish-profiles) documentation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-profileCreateModal.png' />

:::info Create from Google Play Console

To use this profile creation method, you must have an API key integration in place. Please refer to the detailed documentation for [**Create from Google Play Console**](/publish-module/creating-publish-profiles#create-from-google-play-console) and [**API integration**](/account/my-organization/security/credentials/adding-google-play-service-account).

:::

### Selecting a Google Play Developer API Key 

Once the required integrations are set up, you can access these platforms from your profile within the Publish module. To initiate a release process, you need to select the credentials for the related store from the Settings screen under the Publish Profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishSetting.png' />

- All available integrations will be shown in the Settings screen.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishSettingDetail.png' />

### Updating Google Play Console App Information

- Within the Publish module, you can update and review your app's information directly. This includes updating app name, subtitle, categories, and other store-related information such as privacy URLs, primary languages, etc. Please visit the [**Google Play Console Information**](/publish-module/publish-information/google-play-information) documentation for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-appInfoButton.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-appInfoDetails.png' />

### Customizing the Publish Flow


Publish flows are used to automate multiple tasks and introduce automation checkpoints for application deployments to stores. You can create and manage flows within the Publish module as outlined below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-flows.png' />

- **Create a New Flow**: Start by creating a new flow from the "Publish Flows" section. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-manageFlowDetails.png' />

- You can choose from predefined flows or create a custom flow based on your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-dragDropFlow.png' />


- **Configure Flow Steps**: Define each step of the flow, such as submitting to internal track, or updating metadata. Configure the settings for each step according to your requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-configureStep.png' />

- **Save and Activate**: Once the flow is configured, you can save and activate it for use in the deployment process.

### Publish Flow Samples 

- [**App Information from Google Play**](/publish-integrations/android-publish-integrations/app-information-from-google-play): The App Information from Google Play step checks the status of the app releases in the Google Play Console. This allows you to monitor the progress of your app.
- [**Send to Google Play**](/publish-integrations/android-publish-integrations/publish-to-google-play): With this step, the binary is uploaded to desired Google Play Console Track.
You can select as:
1. Internal track
2. Alpha track 
3. Beta track
4. Production track 
5. Custom made track
- [**The Distribute to Track**](/publish-integrations/android-publish-integrations/distribute-to-track): The Distribute to Track step in Appcircle enables automated deployment of Android applications to specific tracks within the Google Play Console. This functionality allows developers to manage releases efficiently, targeting different user groups such as internal testers, beta users, or the general public.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): After receiving approval from TestFlight and uploading the metadata, you can send an approval email to the Release Manager to review the Beta Test and the updated metadata. If everything is in order, the Release Manager can approve the process, allowing the flow to continue and submit the version for release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-betaReleaseFlow.png' />

### Setting Up Notifications

- Keeping your team informed about the release progress is essential for a coordinated effort. The Publish module can be integrated with collaboration tools like [**Slack**](/account/my-organization/notifications/slack-notifications) or [**Microsoft Teams**](/account/my-organization/notifications/teams-notifications) for notifications. By setting up these integrations, you can automatically send notifications about key events in the release process—such as successful deployments or issues that need attention—ensuring that everyone stays in the loop and can act swiftly when needed. Please visit the related [**Notifications Integration**](/account/my-organization/notifications) documentation for more detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-notificationInteg.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-notiIntegDetail.png' />

## Managing Releases

Effective release management is crucial for ensuring the success of your app updates. The Publish module provides you with the tools to monitor, control, and optimize the release process. You can track the status of your releases in real-time, manage approvals, and address any issues that arise during the process. Also, the Publish Module offers customizable flows to provide more detailed management of the release process.

Additionally, the module allows you to roll back to previous versions if needed, ensuring that you have full control over your app's distribution. By leveraging these features, you can maintain a smooth and efficient release cycle, minimizing disruptions and maximizing the impact of your updates.

### Uploading a Binary 

Easily upload your binary file to the Publish module, either manually or via the Build module, to begin the release process.

#### Manual Binary Upload

You can upload your binary file directly to the Publish module using the manual upload option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-manuelUpload.png' />

#### Upload via Build Module 

You can deploy your binary file to the Publish module from the Build module automatically. This method automates the binary deployment process, ensuring that your binary is transferred directly from the Build pipeline to the Publish module, ready for release. It simplifies the flows and reduces the risk of manual errors.

:::info Upload via Build Module

To upload a binary from the Build module, please refer to the [**Distribution Configuration**](/build/build-process-management/configurations#distribution-configuration) and [**Post-Build Operations**](/build/build-process-management#binary-actions) documents for step-by-step instructions.

:::

#### Upload via Appcircle CLI & API 

If you have your own CI environment, you can use the Appcircle API & CLI to upload binaries to the related publish Profile.

- **Other CI/CD Tools**: You can integrate the Publish module with continuous integration/continuous deployment (CI/CD) tools like Jenkins and GitHub Actions to automate your build and release pipeline. With the Appcircle [**API & CLI**](/appcircle-api-and-cli), you can seamlessly connect these tools, allowing for automated triggers that initiate a release as soon as a new build is ready. This integration ensures a consistent and efficient deployment process, reducing manual intervention and the risk of errors. You can check out [**Appcircle Marketplace**](/marketplace) for more integrations.

To get more information, please refer to our [**API & CLI**](/appcircle-api-and-cli) documentation.

#### Upload via Testing Distribution

You can send your application from your Testing Distribution profile to a designated Publish profile by following this documentation, [**Upload via Testing Distribution**](/testing-distribution/create-or-select-a-distribution-profile#send-your-application-to-publish) 

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main12.png" />

#### Marking Binary as Release Candidate

- Designate the current build as the Release Candidate, signaling that it is ready for final testing and potential release. You can refer to the [**Marking as Release Candidate**](/publish-module/publish-information/marking-release-candidates) document for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-markRc.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rcTag.png' />

### Updating Metadata

- Within the Publish module, you can manage your app's metadata directly. This includes updating app descriptions, keywords, and other store-related information. Please visit the [**Metadata Details**](/publish-module/publish-information/meta-data-information#android-metadata-information) documentation for more information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadata.png' />

- Regularly review and update your app's metadata to ensure it is current and relevant, as outdated information can negatively impact your app's visibility and user experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadataDetails.png' />

### Starting the Flow

- Once the flow is selected, you can run it to automate the entire publishing process. The flow will handle everything from submitting the binary to obtaining approvals and completing the release actions for the selectd app stores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-startPublish.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishLog.png' />

### Managing Release Status 

After initiating a release, the Publish module provides tools to monitor and manage the process:

#### Release Dashboard 

View the status of your release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-monitorRelease.png' />

#### Rejecting a Binary 

- The binary can be rejected to be excluded from the publish process, and the rejection reason is displayed as a tag on binary

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejection.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejectionMessage.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejectionTag.png' />

### Auditing Releases

The Publish module provides comprehensive auditing and reporting features that give you full visibility into your release process.

- **Activity Log**: The Activity Log keeps a detailed record of every action taken during the release process, including who performed each action and when it occurred. This log is invaluable for tracking changes, identifying issues, and ensuring accountability within your team.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-logActivity2.png' />

## Publish Module Troubleshooting

When using the Publish module, it's essential to know how to troubleshoot potential issues that may arise during the release process. Whether you're dealing with failed submissions, integration errors, or flow execution problems, having a clear understanding of common issues and their solutions can save you time and ensure a smooth release. 

### Frequently Asked Questions About the Publish Module

#### How do I update my app's metadata?

To update your app's metadata, navigate to the Publish module, select the relevant profile, click the Actions button for the binary, and go to Metadata details. You can now update the metadata fields such as the app name, description, and screenshots. After saving your changes, submit the updated metadata for review if required.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadata.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadataDetails.png' />

#### Is it possible to automate notifications for team members during the release process?

Yes, it is possible. The Publish module allows you to set up automated notifications for your team members at various stages of the release process. You can configure notifications to be sent via email or integrate with collaboration tools like Slack or Microsoft Teams, ensuring that everyone involved is kept up to date on the release status.

For more information, please refer to the [**Notification Integrations**](/account/my-organization/notifications) document.

#### Can I use the Publish Module with other CI tools?

Yes, you can use other CI tools to upload a binary to the Publish module. By utilizing Appcircle [**API & CLI**](/appcircle-api-and-cli) within your chosen CI tool, you can directly send the binary to the relevant profile and manage the Publish process. 

Additionally, you can check our existing integrations in the [**Appcircle Marketplace**](/marketplace) documentation for integration alternatives for the **Appcircle API and CLI**.

#### Can I manage team member roles for the Publish Module?

Appcircle provides users with a comprehensive role management system. This system allows you to assign specific permissions to all organization members on an organization-wide basis. 

For more information, please refer to the [**Role Management**](/account/my-organization/profile-and-team/role-management) document.

#### Can I manage multiple Play Store accounts within the Publish Module?

Yes, the Publish module allows you to manage multiple Play Store accounts within a single interface. You can set up and integrate different accounts, such as Apple App Store, Google Play, and Huawei AppGallery, and then select the appropriate account during the release process. This flexibility ensures that you can handle releases across multiple platforms efficiently.

#### How do I create a custom flow in the Publish Module?

To create a custom flow, navigate to the Publish module and select the "Publish Flow" option. From there, you can choose and arrange the steps needed for your release process, configure each step according to your requirements, and save the flow for future use. Custom flows allow you to tailor the release process to fit your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-flows.png' />

#### Why can't I edit the Publish Flow?

The Publish Module is an **enterprise-level** solution, so only users with an **Appcircle Enterprise Licence** have access to all of its features. Users with other licences have limited access to the module. To get more information for Enterprise Licence please [**contact us**](https://appcircle.io/contact) directly.

#### How can I roll back to a previous version if needed?

If you need to roll back to a previous version, you can do so by selecting the desired version from your release history within the Publish module. This process involves re-uploading the previous binary and metadata, then executing a flow to re-release that version. Rolling back ensures that you can quickly address any issues with the current release without significant downtime.

### Further Support and Resources

If you need additional help with the Publish module, the following resources are available:

- **Appcircle Support**: Contact [**Appcircle Slack support**](https://slack.appcircle.io/) for personalized assistance with your specific issues. 

- **Technical Documentation**: Refer to the Appcircle user documentation for detailed guides and troubleshooting tips for Publish Module.

- **Commercial Details**: The Publish module is an **enterprise-level** solution; therefore, for commercial details, please [**contact us**](https://appcircle.io/contact) directly.