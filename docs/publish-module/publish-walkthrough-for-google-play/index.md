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

### App Metadata and Binary Preparation (Binary and Metadata Preparation)


----
# TODO


## Publish Setup Process

Creating a Publish Profile 
Selecting a Google Play Developer API Key 
Updating Google Play Console App Information (?)
Customizing the Publish Flow 
Publish Flow Samples (?)(nested bullet) Internal, Beta, Alpha Testing and Production (? Production)
Setting Up Notifications (?)
## Managing Releases

Uploading a Binary Manual Binary Upload 
Upload via Build Module 
Upload via Appcircle CLI & API 
Upload via Testing Distribution   (?, via,)
Marking Binary as Release Candidate (?, up) (iOS)
Updating Metadatahttps://docs.appcircle.io/publish-module/publish-information/meta-data-information#android-metadata-information 
Starting the Flow (? , start)
Managing Release Status Release Dashboard 
Rollback Options 
Auditing Releases (?)
## Publish Module Troubleshooting

Common Issues and Solutions 
## Frequently Asked Questions About the Publish Module

How do I update my app's metadata? 
How do I request or approve metadata changes?  
Is it possible to automate notifications for team members during the release process? 
Can I track the progress of the app release in real-time? 
Can I use the Publish Module with other CI tools? 
Can I manage team member roles for the Publish Module? 
Can I manage multiple Play Store accounts within the Publish Module? 
How do I create a custom flow in the Publish Module? 
Why can't I edit the Publish Flow? 
How can I roll back to a previous version if needed?
