---
title: Enterprise App Store Profile
description: Learn how to create an Enterprise App Store profile in Appcircle
tags: [enterprise app store, enterprise profile, enterprise app store setup]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The Enterprise App Store provides a centralized platform for managing an organization’s mobile applications. This guide will outline the essential steps involved in setting up the profile, uploading application binaries, configuring profile settings, and executing actions on the uploaded binaries.

## Creating a Profile

An Enterprise build profile can be created in several ways. IPA or APK files can either be manually uploaded or sent from Appcircle’s Distribution, Build, or Publish modules.

## Uploading Binary

Uploading binaries to the Enterprise App Store is an important step in managing an organization’s mobile applications. Several methods are offered by the platform to perform this action, each catering to different stages of the application lifecycle. The available options for uploading a binary are listed below:

### Manual Binary Upload

- If no profile has been created before, the following screen will be displayed. The **Add New App** button should be clicked to open the upload panel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-upload1.png' />

- Choose your APK or IPA file and click the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-upload2.png" />

- If a valid APK or IPA file has been uploaded, a brand new profile should be displayed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile2.png' />

:::caution

Ensure that the bundle ID matches the current profile and that the version or build number differs from the other files in the list.

:::

### Upload via Build Module

Binaries can also be uploaded via the Build module. For more information, please visit the [Build Configuration](/build/build-process-management/build-profile-configuration#distribution-configuration) and [Build Actions](/build/post-build-operations/after-a-build) documentations.

### Upload via Testing Distribution Module

Binaries can also be uploaded via the Testing Distribution module. For more information, please visit the [Testing Distribution](/testing-distribution/create-or-select-a-distribution-profile#send-your-application-to-enterprise-app-store) documentation.

### Upload via Publish Module

The Publish Flow steps can be customized to send the binary to the Enterprise App Store. For more information, please visit the [Publish Integrations](/publish-integrations/common-publish-integrations/send-to-enterprise-app-store) documentation.

### Upload via API & CLI

The above tasks can also be initiated using the Appcircle CLI. The Appcircle CLI documentation should be checked for the command line parameters.

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>

## Profile Actions

Several key actions are available within the Enterprise App Store to manage and interact with profiles efficiently. The descriptions of the available profile actions are provided below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile3.png' />

#### 1. **Open**
The "Open" action allows entry into a specific profile, providing access to all details and settings associated with that profile. By selecting "Open" the apps, binaries, and configurations linked to the profile can be viewed and managed.

#### 2. **Pin**
The "Pin" action allows a profile to be prioritized by pinning it to the top of the profile list. When a profile is pinned, it remains easily accessible, especially when multiple profiles are managed. This action is particularly useful for frequently accessed profiles, ensuring they stay at the forefront of the workflow.

#### 3. **Delete**
The "Delete" action results in the permanent removal of a profile from the Enterprise App Store. Once a profile is deleted, all associated data, including uploaded binaries and settings, is also erased.

:::info

Unlike profiles from other modules within Appcircle, Enterprise App Store profiles cannot be manually named or renamed. Instead, the binary names will be displayed for these profiles.

:::

## Profile Settings

After the profile has been created, it should be configured and sent to different users and channels.

Profile information can be accessed, and users can be added to grant them access to the Live and Beta channels by clicking the **Settings** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-4225-profile4.png' />

### Information

The Profile ID can be copied from the Info tab by clicking the copy icon located on the right side of the displayed ID.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profilesettings.png" />

### Manage Access

Multiple users can be added to the Beta and Live channels by pressing the Tab key.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify1.png" />

:::important

To configure the Manage Access tab, the authentication method for the Enterprise Store must be set to either SSO or LDAP. For more information about authentication types, please refer to the [Store Settings](/enterprise-app-store/store-settings#store-authentication) documentation.

:::


:::caution
If a sub-organization is being worked for, visibility will be limited to the apps within that organization. However, if an app is published, it will also be displayed in the showcase of the parent organization on the Enterprise App Store.

User permissions within the Enterprise App Store can be managed using **Okta SAML**. By configuring authorization groups through **Okta** and subsequently applying these group names to **Alpha** or **Beta** channels via Appcircle, access will be restricted to only the relevant users.

For further details, please refer to the document: [Okta Managing User Groups](https://docs.appcircle.io/account/my-organization/sso-providers-configuration/sso-login/okta-saml#okta-managing-user-groups).
:::

:::info
If Beta Channel Access is not configured, versions marked for the Beta channel will not be visible to anyone by default.

If Live Channel Access is not configured, versions marked for the Live channel will be visible to everyone by default.

:::

Defined user groups from your provider can be added after configuration.

<Screenshot url="https://cdn.appcircle.io/docs/assets/2812-entstore-okta-group-new.png" />

:::tip 

The logo of the Enterprise App Store profile can also be updated by clicking on the logo icon. Please note that this will not affect the customization of your Enterprise Store login.

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-logo5.png" />

## Binary Actions

### Publish

The Enterprise App Store module includes two channels: Beta and Live.

- **Beta Channel**: This channel can be used for testing new updates, features, or changes before they are rolled out to all users. The beta channel is ideal for trialing updates without affecting the broader user base, ensuring that everything works as expected before being moved to production.
- **Live Channel**: The live channel serves as the production environment where all end users interact with the Enterprise App Store. This channel may contain stable, fully tested binary versions.

Apps can be sent to the Beta or Live channels by hitting the `...` button and then selecting the **Publish** menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta1.png" />

The channel can be selected, and a summary and release notes for the release can be written. Once the **Publish** button is clicked, the particular binary will be made available to all beta users.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta2.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-beta3.png" />

A version can be sent to the Live Channel in two ways:

- Click the **Publish** button and select **Live** for the channel.
- Click the ... button for any beta build and select **Go Live** from the menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-golive.png" />

:::info

Only **one binary version** can be sent to the Live and Beta channels. When another Beta or Live binary version is sent, the previous app version in that channel will be replaced.

:::

:::tip

Any app versions published by sub-organizations to the **Live** or **Beta** channel will be available in the Enterprise Store created by the root organization for users to view and download.

:::

When a binary is published to the Live or Beta channel, it will be displayed with the corresponding channel tag. This information will also be shown in the profile header within the profile and on the profile card in the Enterprise App Store profile list.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-tags.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profiles.png" />

:::info

If two binaries are published to the Beta and Live channels, the profile header will display the binary from the Live channel.

:::

#### Unpublish

Any binary can be removed from the Live or Beta channels by selecting the **Unpublish** action from the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-unpublish.png" />

### Notify

An email can be sent to your users by selecting the **Notify** action from the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify2.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify3.png" />

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notify4.png" />


An email with the subject and message entered in this form will be sent to your users. The users will be able to download the binary by clicking the link provided in the email.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-notifymail.png" />

:::important

To use the Notify feature, the authentication method for the Enterprise Store must be set to either SSO or LDAP. For more information about authentication types, please refer to the [Store Settings](/enterprise-app-store/store-settings#store-authentication) documentation.

Additionally, registered emails must be included in the [Manage Access](/enterprise-app-store/enterprise-app-store-profile#manage-access) settings for your Enterprise App Store profile.

:::

### Share

If you want to share the link to a specific version without sending an email, you can select the **Share** menu from the actions.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-share1.png" />

:::caution

The Enterprise App Store share feature does not permit public sharing. It only facilitates access to the specific app version and adheres to all authentication rules.

:::

:::info

The above tasks can also be initiated using the Appcircle CLI. Please refer to the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>

### Download

The binary artifact in the Enterprise App Store profile can be downloaded by selecting the Download button from the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-profile5.png" />


### Delete

Binaries in the Enterprise App Store profiles can be deleted by clicking the Delete button in the actions menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/BE-4225-delete.png" />

:::info

Please note that you **cannot** delete a binary that is published to the Beta or Live channels. You must unpublish it before you can delete it.

:::

## Apple Enterprise Program

The Apple Developer Enterprise Program allows large organizations to develop and deploy proprietary, internal-use apps directly to their employees. This program is designed for specific use cases that require private distribution through secure internal systems or a Mobile Device Management solution.

The Apple Developer Enterprise Program is intended solely for the internal use and distribution of proprietary apps in scenarios that are not adequately addressed by public apps on the App Store, custom apps through Apple Business Manager, Ad Hoc distribution, or beta testing via TestFlight.

https://developer.apple.com/programs/enterprise/


:::danger Apple Enterprise Program

**Please note that** if you have an **Apple Developer** account with an **Enterprise Organization** and you are using an app signed with an [**Enterprise Certificate**](/signing-identities/apple-certificates) for **internal distribution**, you must use [**authentication**](https://docs.appcircle.io/enterprise-app-store/store-customization#authentication) for user access.

Apple does not allow public distribution of internally distributed apps, and if Apple detects that you are distributing an app signed with an Enterprise certificate without using authentication, it will impose severe sanctions.

You can access the relevant terms and conditions from the links below and get detailed information.

- [**Apple Developer Enterprise Program License Agreement**](https://developer.apple.com/support/terms/)
    - Please navigate the `Apple Developer Enterprise Program License Agreement` section and see Section 2.1 on page 8 for **usage and restrictions**, and Section 11.2 on page 34 for **terms and terminations**.

:::