---
title: Enterprise App Store Profile
description: Learn how to create an Enterprise App Store profile in Appcircle
tags: [enterprise app store, enterprise profile, enterprise app store setup]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The Enterprise App Store provides a centralized platform for managing your organization's mobile applications. This guide will walk you through the essential steps involved in setting up your profile, uploading application binaries, configuring profile settings, and executing actions on your uploaded binaries.

## Creating a Profile

There are several ways to create an Enterprise build profile. You can either manually upload your IPA or APK files or you can send them from Appcircle's Distribution, Build or Publish modules.

## Uploading Binary

Uploading binaries to the Enterprise App Store is an important step in managing your organization's mobile applications. The platform offers several methods to perform this action, each catering to different stages of the application lifecycle. Below are the available options for uploading a binary:

### Manual Binary Upload

- If you haven't created any profile before, you will see the following screen. Click the **Add New App** button to open the upload panel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-upload1.png' />

- Choose your APK or IPA file and click the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-upload2.png" />

- If you have uploaded a valid APK or IPA file, you should see your brand new profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile2.png' />

:::caution

Make sure that the bundle ID matches your current profile and version or build number is different from the other files in the list.

:::

### Upload via Build Module

Binaries can also be uploaded via the Build module. For more information, please visit the [Build Configuration](/build/build-process-management/build-profile-configuration#distribution-configuration) and [Build Actions](/build/post-build-operations/after-a-build) documentations.

### Upload via Testing Distribution Module

Binaries can also be uploaded via the Testing Distribution module. For more information, please visit the [Testing Distribution](/testing-distribution/create-or-select-a-distribution-profile#send-your-application-to-enterprise-app-store) documentation.

### Upload via Publish Module

You can customize your Publish Flow steps to send your binary to the Enterprise App Store. For more information, please visit the [Publish Integrations](/publish-integrations/common-publish-integrations/send-to-enterprise-app-store) documentation.

### Upload via API & CLI

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>

## Profile Actions

Within the Enterprise App Store, you have several key actions that allow you to manage and interact with your profiles efficiently. Below are the descriptions of the available profile actions:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile3.png' />

#### 1. **Open**
The "Open" action allows you to enter a specific profile, giving you access to all the details and settings associated with that profile. By selecting "Open," you can view and manage the apps, binaries, and configurations linked to the profile.

#### 2. **Pin**
The "Pin" action enables you to prioritize a profile by pinning it to the top of your profile list. When a profile is pinned, it remains easily accessible, especially if you manage multiple profiles. This action is particularly useful for frequently accessed profiles, ensuring they stay at the forefront of your workflow.

#### 3. **Delete**
The "Delete" action permanently removes a profile from the Enterprise App Store. Once a profile is deleted, all associated data, including uploaded binaries and settings, are also erased.

:::info

Unlike the profiles from other modules within the Appcircle, Enterprise App Store profiles cannot be named or renamed manually. The profiles will display the binary names instead.

:::

## Profile Settings

After you have created your profile, it is time to configure it and send it to different users and channels.

You can reach your profile information and add users for them to gain access to the Live and Beta channels by clicking the **Settings** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile4.png' />

### Information

You can copy your Profile ID from the Info tab by clicking the copy icon on the right side of your displayed ID.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profilesettings.png" />

### Manage Access

You can add multiple users to the Beta and Live channels by hitting the Tab key.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify1.png" />

:::important

To configure the Manage Access tab, the authentication method for your Enterprise Store must be either SSO or LDAP. For more information about authentication types, please refer to the [Store Settings](/enterprise-appstore/store-settings#store-authentication) documentation.

:::


:::caution
If you work for a sub-organization, you will only have visibility of the apps within that organization. However, if an app is published, it will also be displayed in the parent organization's showcase on the Enterprise App Store.

To manage user permissions within the Enterprise App Store, **Okta SAML** can be utilized. By configuring authorization groups through **Okta** and subsequently using these group names on **Alpha** or **Beta** channels via Appcircle, only relevant users will have access to them.

For further details, please refer to the document: [Okta Managing User Groups](https://docs.appcircle.io/account/my-organization/sso-providers-configuration/sso-login/okta-saml#okta-managing-user-groups).
:::

:::info
If Beta Channel Access is not set, the versions marked as the Beta channel will not be visible to anyone by default.

If the Live Channel Access is not set, the versions marked as the Live channel will be visible to everyone by default.

:::

You can add defined user groups from your provider after configuration.

<Screenshot url="https://cdn.appcircle.io/docs/assets/2812-entstore-okta-group-new.png" />

:::tip 

You can also update the logo of your Enterprise App Store profile by clicking on the logo icon. Please note that this will not affect your Enterprise Store login customization.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-logo5.png" />

## Binary Actions

### Publish

The Enterprise App Store module includes two channels: Beta and Live.

- **Beta Channel**: This channel could be used for testing new updates, features, or changes before they are rolled out to all users. The beta channel is ideal for trialing updates without affecting the broader user base, ensuring that everything works as expected before moving to production.
- **Live Channel**: The live channel is the production environment where all end users interact with the Enterprise App Store. This channel could contain the stable, fully tested binary versions.

Apps can be sent to the Beta or Live channels by hitting the `...` button and then selecting the **Publish** menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta1.png" />

You can select the channel and write a summary and release notes for your release. When you hit the **Publish** button, that particular binary will be available to all beta users.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta2.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta3.png" />

You can send a version to the Live Channel in two ways:

- Click the **Publish** button and select **Live** for the channel.
- Click the ... button for any beta build and select **Go Live** from the menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-golive.png" />

:::info

You can only send **one binary version** to the Live and Beta channels. When you send another Beta or Live binary version, the previous app version will be replaced from that channel.

:::

:::tip

If you are part of a sub-organization, the app versions that you publish to the **Live** or **Beta** channel will be available on the Enterprise Store for users to view and download, just as they are for a root organization.

:::

When you publish a binary to the Live or Beta channel, the binary will be displayed with the corresponding channel tag. This information will also be shown in the profile header within the profile and on the profile card in the Enterprise App Store profile list.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-tags.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profiles.png" />

:::info

If you have two binaries that are published to Beta and Live channels, the profile header will display the one from the Live channel.

:::

#### Unpublish

You can remove any binary from the Live or Beta channels by selecting the **Unpublish** action from the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-unpublish.png" />

### Notify

You can send an email to your users by selecting the **Notify** action from the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify2.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify3.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify4.png" />


Your users will receive an email with the subject and message you entered in this form. Users will be able to download the binary by clicking the link in the incoming email.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notifymail.png" />

:::important

To use the Notify feature, the authentication method for your Enterprise Store must be either SSO or LDAP. For more information about authentication types, please refer to the [Store Settings](/enterprise-appstore/store-settings#store-authentication) documentation.

Additionally, you need to have registered emails within the [Manage Access](/enterprise-appstore/enterprise-app-store-profile#manage-access) settings for your Enterprise App Store profile.

:::

### Share

If you want to share the link to a specific version without sending an email, you can select the **Share** menu from the actions.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-share1.png" />

:::caution

The Enterprise App Store share feature doesn't allow public sharing. It only helps access the specific app version and follows all authentication rules.

:::

:::info

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>

### Download

You can download the binary artifact in the Enterprise App Store profile by selecting the Download button in the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profile5.png" />


### Delete

Binaries in the Enterprise App Store profiles can be deleted by clicking the Delete button in the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-delete.png" />

:::info

Please note that you **cannot** delete a binary that is published to the Beta or Live channels. You must unpublish it before you can delete it.

:::

## Apple Enterprise Program

The Apple Developer Enterprise Program allows large organizations to develop and deploy proprietary, internal-use apps to their employees. This program is for specific use cases that require private distribution directly to employees using secure internal systems or through a Mobile Device Management solution.

The Apple Developer Enterprise Program is only for the internal use and distribution of proprietary apps in specific use cases that are not adequately addressed with public apps on the App Store, custom apps through Apple Business Manager or Ad Hoc distribution, or beta testing through TestFlight.

https://developer.apple.com/programs/enterprise/


:::danger Apple Enterprise Program

**Please note that** if you have an **Apple Developer** account with an **Enterprise Organization** and you are using an app signed with an [**Enterprise Certificate**](/signing-identities/apple-certificates) for **internal distribution**, you must use [**authentication**](https://docs.appcircle.io/enterprise-appstore/customize-ent-store#authentication) for user access.

Apple does not allow public distribution of internally distributed apps, and if Apple detects that you are distributing an app signed with an Enterprise certificate without using authentication, it will impose severe sanctions.

You can access the relevant terms and conditions from the links below and get detailed information.

- [**Apple Developer Enterprise Program License Agreement**](https://developer.apple.com/support/terms/)
    - Please navigate the `Apple Developer Enterprise Program License Agreement` section and see Section 2.1 on page 8 for **usage and restrictions**, and Section 11.2 on page 34 for **terms and terminations**.

:::