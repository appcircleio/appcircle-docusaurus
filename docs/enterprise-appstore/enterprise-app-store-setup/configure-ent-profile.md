---
title: Configuring the Profile
description: Learn how to configure your enterprise app store profile in Appcircle
tags: [enterprise app store, enterprise app store profile, configure profile]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Setting Up Your App Store Profile

After you have created your profile, it is time to configure it and send it to different users and channels.

### Manage Access

You can add users to the Live and Beta channels by clicking the **Settings** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-detail-setting-button.png' />

You can add multiple users to the Beta and Live channels by hitting the Tab key.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-detail-setting-access-users.png" />

:::danger
If you work for a sub-organization, you will only have visibility of the apps within that organization. However, if an app is published, it will also be displayed in the parent organization's showcase on the Enterprise App Store.

To manage user permissions within the Enterprise App Store, **Okta SAML** can be utilized. By configuring authorization groups through **Okta** and subsequently using these group names on **Alpha** or **Beta** channels via Appcircle, only relevant users will have access to them.

For further details, please refer to the document: [Okta Managing User Groups](https://docs.appcircle.io/account/my-organization/sso-providers-configuration/sso-login/okta-saml#okta-managing-user-groups).
:::

:::info
If Beta Channel Access is not set, the versions marked as the Beta channel will not be visible to anyone by default.
:::

:::info
If the Live Channel Access is not set, the versions marked as the Live channel will be visible to everyone by default.
:::

You can add defined user groups from your provider after configuration.

<Screenshot url="https://cdn.appcircle.io/docs/assets/2812-entstore-okta-group-new.png" />

### Add Version

If you enable **Publish Enterprise App Store** settings in your config, all the new signed builds will automatically appear in the list. You can also manually upload a new version to your profile.

Click the **Add Version** button, select an IPA or APK file, and hit the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-android-apk-upload.png" />

:::caution

Make sure that the bundle ID matches your current profile and version or build number is different from the other files in the list.

:::

### Publish to Channel

Apps can be sent to the Beta or Live channels by hitting the `...` button and then selecting the **Publish** menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-publish-button.png" />

You can select the channel and write a summary and release notes for your release. When you hit the **Publish** button, that particular build will be available to all beta users.

You can send a version to the Live Channel in two ways:

- Click the **Publish** button and select **Live** for the channel.
- Click the ... button for any beta build and select **Go Live** from the menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-golive-button.png" />

:::info

You can only send **one** version to the Live and Beta channels. When you send another beta or live version, the previous app version will be removed from that channel.

:::

### Unpublish

You can remove any build from the Live or Beta channels by selecting the **Unpublish** menu from the actions.

### Notify Users

You can send an email to your users by selecting the **Notify** menu from the actions.

Your users will receive an email with the subject and message you entered in this form. Users will be able to download the program by clicking the link in the incoming email.

### Other Actions

If you want to share the link to a specific version without sending an email, you can select the **Share** menu from the actions. You can also download and delete versions from the list by selecting the corresponding menus.

:::caution

The Enterprise App Store share feature doesn't allow public sharing. It only helps access the specific app version and follows all authentication rules.

:::

:::danger

**Please note that** if you have an **Apple Developer** account with an **enterprise organization** and you are using an app signed with an [**enterprise certificate**](/signing-identities/apple-certificates) for **internal distribution**, you must use [**authentication**](https://docs.appcircle.io/enterprise-appstore/customize-ent-store#authentication) for user access.

Apple does not allow public distribution of internally distributed apps, and if Apple detects that you are distributing an app signed with an Enterprise certificate without using authentication, it will impose severe sanctions.

You can access the relevant terms and conditions from the links below and get detailed information.

- [Apple Developer Enterprise Program Agreement](https://developer.apple.com/support/downloads/terms/apple-developer-enterprise-program/Apple-Developer-Enterprise-Program-License-Agreement-20230605-English.pdf)
  - See Section 2.1 on page 8 for usage and restrictions, and Section 11.2 on page 33 for terms and terminations.
- [Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise/)

:::

:::info

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>
