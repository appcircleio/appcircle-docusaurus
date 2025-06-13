---
title: Publish Walkthrough for Google Play Console
description: Learn how to use the Publish module in Appcircle.
tags: [publish, google play console, android, metadata, walkthrough, android app release]
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

## Why Use the Publish Module: Features and Benefits

The Publish module in Appcircle is a powerful tool designed for managing the release process of mobile applications to various app stores, including the Apple App Store, Google Play Console, and Huawei AppGallery. This module streamlines the complex process of app release, enabling users to:

- **Centralized Release Management**: Monitor, manage, and audit releases from a single platform, making the release process more efficient and organized.
- **Automate Releases**: Automate the submission of applications to multiple stores, reducing the manual workload and minimizing the risk of errors.
- **Flexibility in Publishing**: Appcircle provides the flexibility to publish your applications to various platforms, including app stores and internal app distribution systems. This ensures that your app reaches the right audience through the most suitable channels.
- **Isolation from Complex Interactions**: Eliminate the need for direct interaction with individual app stores like the Apple App Store, Google Play Console, and Huawei AppGallery. Appcircle acts as a central hub, isolating you from the complexities and variances of each store’s submission processes. 

By using the Publish module, you can ensure a smooth, reliable, and scalable release process for your mobile applications, enhancing the overall efficiency and effectiveness of your app release strategy. 

https://appcircle.io/publish-to-stores

## Getting Started

The Publish module in Appcircle is a versatile tool that simplifies the app release process. To make the most of this module, it's important to ensure that you meet all prerequisites and properly configure the necessary settings. The following sections outline the initial steps to start a release process using the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishstart2.png' />

## Prerequisites for Using the Publish Module

Before you can start using the Publish module, there are several key prerequisites to address:

### Creating and Adding a Google Play Developer API Key

The most important requirement before getting started is a Google Play Console account and an API key generated for that account.
For detailed instructions on generating a Google Play Console API key, please refer to the Appcircle documentation below:

- [**Creating and Adding a Google Play Developer API Key to Appcircle**](/account/my-organization/security/credentials/adding-google-play-service-account)

Once the Google API Key file is successfully integrated, you can proceed to the next step.

:::caution The JSON file is not recoverable

The Google API key JSON file can only be downloaded once and cannot be retrieved later from Google Play Console or Appcircle. **Make sure to store it securely right after downloading.**

:::

### Binary and Metadata Preparation

Before starting the release process, it's essential to prepare all necessary app metadata and binary files. This preparation ensures a smooth and efficient publishing experience.

:::info Binary Upload Methods

The binary file can be uploaded to the Publish module either manually or through the Build or Testing Distribution modules. For more detailed instructions, please refer to the [**Upload Binary**](/publish-module/publish-walkthrough-for-google-play#uploading-a-binary) section.

:::

- Gather all required metadata for your app for the Google Play Console, such as:

    - Application name
    - Description
    - App icons and screenshots
    - Privacy policy URL
    - Contact information

- Having this information prepared in advance will streamline the publishing process.

## Publish Setup Process

### Creating a Publish Profile 

- Your Publish profile should be correctly set up within the Appcircle platform. This includes having a configured profile with the necessary app builds (binary files) available for release. To set up a profile, click the **Add New** button on the top right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishStartCreate2.png' />

:::tip Creating a Publish Profile

If you haven't set up a Publish profile in Appcircle before, follow the detailed [**Creating a Publish profile guide**](/publish-module/creating-publish-profiles) provided in the Appcircle documentation to ensure everything is ready for publishing.

:::

- There are two different ways to create a Publish profile. One option is to create the profile manually, and the other is to retrieve an existing profile from Google Play Console. For detailed information, please visit the [**Creating Publish Profile**](/publish-module/creating-publish-profiles) documentation.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-profileCreateModal.png' />

:::info Create from Google Play Console

To use this profile creation method, you must have a Google Play API key integration. And the package name defined in the Publish profile must exactly match the package name registered in your Google Play Console. Please refer to the detailed documentation for [**Create from Google Play Console**](/publish-module/creating-publish-profiles#create-from-google-play-console) and [**API integration**](/account/my-organization/security/credentials/adding-google-play-service-account).  

:::

### Selecting a Google Play Developer API Key

If you choose to create the profile manually, you must select the required Google Play Developer API key integration from your profile in the Publish module. To initiate the release process, select the credentials for the relevant store from the Settings screen under the selected Publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishSetting.png' />

- All available integrations will be shown in the Settings screen. Here, you should select the Google Play Developer API key that you want to link to release your app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishSettingDetail.png' />

### Updating Google Play Console App Information

- Within the Publish module, you can update and review your app's information directly. This includes updating email address, phone number, website URL, primary languages, Please visit the [**Google Play Console Information**](/publish-module/publish-information/google-play-information) documentation for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-appInfoButton.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-appInfoDetails.png' />

### Customizing the Publish Flow

Publish flow are used to automate multiple tasks and introduce automation checkpoints for application deployments to stores. You can manage flow within the Publish module as outlined below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-flows.png' />

- **Update the existing publish flow**: Update the flow from the `Publish Flow` section. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-manageFlowDetails.png' />

- You can choose from predefined steps or create custom steps based on your specific needs.

You can drag and drop steps into your Publish flow. Any unwanted Publish flow steps can be removed or deactivated.
You can also reorder steps so that they will be executed in the order you specify.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-dragDropFlow.png' />


- **Configure Flow Steps**: Fill in all required inputs for each step in the flow with the necessary information according to your requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-configureStep.png' />

- **Save**: Once the flow is configured, you can save and then activate it for use in the deployment process.

### Publish Flow Sample

Here is a sample publishing flow for an Android app, including track selection and deployment steps.

- [**Custom Script**](/publish-integrations/common-publish-integrations/custom-script): You can use the Custom Script steps to add extra functionalities in your Publish flow. Appcircle will execute the commands specified in your custom scripts, allowing you to perform custom actions. These scripts will run on the runner, giving you access to all the capabilities of the Publish environment.
- [**Get Approval via Email**](/publish-integrations/common-publish-integrations/get-approval-via-email): The Get Approval via Email step allows you to get approval from the email addresses entered as input in the step before moving on to the next steps in Publish.
- [**Send to Google Play**](/publish-integrations/android-publish-integrations/publish-to-google-play): With this step, the binary is uploaded to the desired Google Play Console Track.
You can select one of the following options:

   - Internal track
   - Alpha track
   - Beta track
   - Production track
   - Custom track (a user-defined track for specific testing or release scenarios outside the standard tracks)
- [**The Distribute to Track**](/publish-integrations/android-publish-integrations/distribute-to-track): This step enables automated deployment of Android applications to specific tracks within the Google Play Console. This functionality allows developers to manage releases efficiently, targeting different user groups such as internal testers, beta users, or the general public.
- [**App Information from Google Play**](/publish-integrations/android-publish-integrations/app-information-from-google-play): The App Information from Google Play step checks the status of the app releases in the Google Play Console. This allows you to monitor the progress of your app.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-betaReleaseFlow.png' />

### Setting Up Notifications

- Keeping your team informed about the release progress is essential for a coordinated effort. The Publish module can be integrated with collaboration tools like [**Slack**](/account/my-organization/notifications/slack-notifications) or [**Microsoft Teams**](/account/my-organization/notifications/teams-notifications) for notifications. By setting up these integrations, you can automatically send notifications about key events in the release process—such as successful deployments or issues that need attention—ensuring that everyone stays in the loop and can act swiftly when needed. Please visit the related [**Notifications Integration**](/account/my-organization/notifications) documentation for more detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-notificationInteg.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-notiIntegDetail.png' />

## Managing Releases

Effective release management is crucial for ensuring the success of your app updates. The Publish module provides you with the tools to monitor, control, and optimize the release process. You can track the status of your releases in real time, manage approvals, and address any issues that arise during the process. Also, the Publish module offers customizable flow to provide more detailed management of the release process.

Additionally, you have full control over your app's distribution. By leveraging these features, you can maintain a smooth and efficient release cycle, minimizing disruptions and maximizing the impact of your updates.

### Uploading a Binary 

Easily upload your binary file to the Publish module **manually**, via the **Build** or **Testing Distribution** modules, or through **Appcircle CLI and API** to begin the release process.

#### Manual Binary Upload

You can upload your binary file directly to the Publish module using the manual upload option.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-manuelUpload.png' />

#### Upload via Build Module 

You can automatically deploy your binary file to the Publish module directly from the Build module. This method streamlines the binary deployment process by transferring your binary immediately after the build pipeline completes, making it ready for release. It simplifies the flow and reduces the risk of manual errors.

:::info Upload via Build Module

To upload a binary from the Build module, please refer to the [**Distribution Configuration**](/build/build-process-management/configurations#distribution-configuration) document for auto upload or the [**Post-Build Operations**](/build/build-process-management#binary-actions) document for manual upload.

:::

#### Upload via Testing Distribution

You can send your application from a testing distribution profile to a designated Publish profile. For detailed steps, see the [**Upload via Testing Distribution**](/testing-distribution/create-or-select-a-distribution-profile#send-your-application-to-publish) documentation.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4163-main12.png" />

#### Upload via Appcircle CLI & API 

If you have your own CI environment or need to integrate Appcircle into a specific process or job, you can use the Appcircle API & CLI to upload binaries to the related Publish profile.

- **Other CI/CD Tools**: You can integrate the Publish module with CI/CD tools like Jenkins and GitHub Actions to automate your build and release pipeline. With the Appcircle [**API & CLI**](/appcircle-api-and-cli), you can seamlessly connect these tools, allowing for automated triggers that initiate a release as soon as a new build is ready. This integration ensures a consistent and efficient deployment process, reducing manual intervention and the risk of errors. You can check out [**Appcircle Marketplace**](/marketplace) for more integrations.

To get more information, please refer to our [**API & CLI**](/appcircle-api-and-cli) documentation.

#### Marking Binary as Release Candidate

- Designate the current build as the Release Candidate, signaling that it is ready for potential release. You can refer to the [**Marking as Release Candidate**](/publish-module/publish-information/marking-release-candidates) document for detailed information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-markRc.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rcTag.png' />

### Updating Metadata

- Within the Publish module, you can manage your app's metadata directly. This includes updating the app's metadata, including video, descriptions, and app name. Please visit the [**Metadata Details**](/publish-module/publish-information/meta-data-information#android-metadata-information) documentation for more information.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadata.png' />

- Regularly review and update your app's metadata to ensure it is current and relevant, as outdated information can negatively impact your app's visibility and user experience.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadataDetails.png' />

### Starting the Flow

- You can start the Publish flow manually by clicking on the `Publish Details` or you can run it to automate the entire publishing process. The flow will handle everything from submitting the binary to obtaining approvals and completing the release actions for the Google Play Console.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-startPublish.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-publishLog2.png' />

### Managing Release Status 

After initiating a release, the Publish module provides tools to monitor and manage the process.

#### Release Dashboard 

View the real time status of your release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-monitorRelease.png' />

#### Rejecting a Binary 

- The binary can be rejected to be excluded from the publish process, and the rejection reason is displayed as a tag on the binary.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejection.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejectionMessage.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-rejectionTag.png' />

### Auditing Releases

The Publish module provides comprehensive auditing and reporting features that give you full visibility into your release process.

- **Activity Log**: The activity log keeps a detailed record of every action taken during the release process, including who performed each action and when it occurred. This log is invaluable for tracking changes, identifying issues, and ensuring accountability within your team.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-logActivity3.png' />

## Publish Module Troubleshooting

When using the Publish module, it's essential to know how to troubleshoot potential issues that may arise during the release process. Whether you're dealing with failed submissions, integration errors, or flow execution problems, having a clear understanding of common issues and their solutions can save you time and ensure a smooth release. 

### Frequently Asked Questions About the Publish Module

#### What happens if I upload an APK/AAB signed with a different keystore?

Google Play rejects the upload with an error like
"Upload failed. You uploaded an APK or Android App Bundle that is signed with a different certificate."

If you’ve lost your original keystore and Play App Signing is enabled, you can request a new upload key. Otherwise, you must use the original keystore or publish the app under a new package name.

For more information, please refer to the [**What to do if I lost my key store**](/signing-identities/android-keystores#what-to-do-if-i-lost-my-keystore-signing-file) document.

#### Can I re-sign an Android binary with a different keystore?

Yes. The Resign Binary step allows you to re-sign your APK or AAB using a different keystore. This is useful when distributing the same build under a different signing identity. The Publish module fully supports Android binary re-signing.

:::caution

Re-signing an Android binary with a different keystore may cause installation or update issues. Android does not allow an app signed with one key to be updated with another. If a different keystore is used, the app must be uninstalled first, which results in loss of user data. Also, changing the signing key is not allowed on Google Play after the first release, unless you're using Play App Signing with an approved key change process.

:::

For more information, please refer to the [**Resign binary**](/publish-module/publish-information/resign-binary) document.

#### How to Distribute an Android App to Different Release Tracks (Alpha, Beta, Production) on Google Play?

Yes. By setting the `Distribute to track` step, you can upload your application to a specific track, such as Internal, Beta, or Production. This allows you to manage multiple release flow and target different user groups within the same pipeline.

For more information, please refer to the [**Distribute to Track**](/publish-integrations/android-publish-integrations/distribute-to-track) document.

#### How can I control the rollout percentage when distributing to a Google Play track?

In the `Distribute to track` step, if you set `AC_RELEASE_STATUS` to partial, a rollout percentage slider becomes available. Use it to define what percentage of users should receive the update initially (e.g., 10%). This lets you perform phased rollouts and monitor stability before doing a full release.

#### How do I update my app's metadata?

To update your app's metadata, navigate to the Publish module, select the relevant profile, click the `Actions` button for the binary, and go to Metadata details. You can now update the metadata fields, such as the app name, description, and screenshots. After saving your changes, submit the updated metadata for review if required.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadata.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-actionMetadataDetails.png' />

#### Is it possible to automate notifications for team members during the release process?

Yes, it is possible. The Publish module allows you to set up automated notifications for your team members at various stages of the release process. You can configure notifications to be sent via email or integrate with collaboration tools like `Slack` or `Microsoft Teams`, ensuring that everyone involved is kept up to date on the release status.

For more information, please refer to the [**Notification Integrations**](/account/my-organization/notifications) document.

#### Can I use the Publish Module with other CI tools?

Yes, you can use other CI tools to upload a binary to the Publish module. By utilizing Appcircle [**API & CLI**](/appcircle-api-and-cli) within your chosen CI tool, you can directly send the binary to the relevant profile and manage the publish process. 

Additionally, you can check our existing integrations in the [**Appcircle Marketplace**](/marketplace) documentation for integration alternatives for the **Appcircle API and CLI**.

#### Can I manage team member roles for the Publish Module?

Appcircle provides users with a comprehensive role management system. This system allows you to assign specific permissions to all organization members on an organization-wide basis. 

For more information, please refer to the [**Role Management**](/account/my-organization/profile-and-team/role-management) document.

#### Can I manage multiple Play Store accounts within the Publish Module?

Yes, the Publish module allows you to manage multiple Play Store accounts within a single interface. You can set up and integrate different accounts, such as Apple App Store, Google Play, and Huawei AppGallery, and then select the appropriate account during the release process. This flexibility ensures that you can handle releases across multiple platforms efficiently.

#### How do I create a custom flow in the Publish Module?

To create a custom flow, navigate to the Publish module and select the "Publish Flow" option. From there, you can choose and arrange the steps needed for your release process, configure each step according to your requirements, and save the flow for future use. Custom flow allow you to tailor the release process to fit your specific needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6003-flows.png' />

#### Why can't I edit the Publish Flow?

The Publish Module is an **enterprise-level** solution, so only users with an **Appcircle Enterprise License** have access to all of its features. Users with other licenses have limited access to the module. To get more information about the Enterprise License, please [**contact us**](https://appcircle.io/contact) directly.

#### How can I roll back to a previous version if needed?

If you need to roll back to a previous version, you can do so by selecting the desired version from your release history within the Publish module. This process involves re-uploading the previous binary and metadata, then executing a flow to re-release that version. Rolling back ensures that you can quickly address any issues with the current release without significant downtime.

### Further Support and Resources

If you need additional help with the Publish module, the following resources are available:

- **Appcircle Support**: Contact [**Appcircle Slack support**](https://slack.appcircle.io/) for personalized assistance with your specific issues. 

- **Technical Documentation**: Refer to the Appcircle user documentation for detailed guides and troubleshooting tips for the Publish module.

- **Commercial Details**: The Publish module is an **enterprise-level** solution; therefore, for commercial details, please [**contact us**](https://appcircle.io/contact) directly.