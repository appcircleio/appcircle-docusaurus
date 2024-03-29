---
title: Configure a Profile
metaTitle: Configure a Profile
metaDescription: Configure a Profile
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Configure a Profile

After you have created your profile, it is time to configure it and send it to different users and channels.


### Manage Access

You can add users to your live and beta channels by clicking the **Settings** button. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-detail-setting-button.png' />


You can add multiple users to beta and live channels by hitting the Tab key.


<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-detail-setting-access-users.png" />

:::caution
If you work for a sub-organization, you can only see the apps belonging to that organization. However, if the app is published, it will also appear in the parent organization's showcase.
:::

:::info
If Beta Channel Access is not set, the versions marked as beta will not be visible to anyone by default.
:::

:::info
If Live Channel Access is not set, the versions marked as live channel will be visible to everyone by default.
:::

You can add defined user groups from your provider after configuration.

<Screenshot url="https://cdn.appcircle.io/docs/assets/2812-entstore-okta-group-new.png" />

:::info
For more information how to manage user groups, please follow the steps that is available in [Okta Managing User Groups](../account/sso-login/okta-saml.md#okta-managing-user-groups)
:::

### Add Version

If you enabled  **Publish Enterprise Store** settings in your config, all the new signed builds will automatically appear in the list. You can also manually upload a new version to your profile. 

Click the **Add Version** button and select IPA or APK file and hit the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-android-apk-upload.png" />


:::caution

Make sure that the bundle id matches your current profile and version or build number is different than the other files in the list. 

:::

### Publish to Channel

Apps can be sent to Beta or Live channels by hitting the ... button and then selecting the **Publish** menu. 

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-publish-button.png" />


You can select the channel and write a summary and release notes for your release. When you hit the **Publish** button that particular build will be available to all beta users.

You can send a version to Live Channel in two ways

- Click the **Publish** button and select **Live** for the channel
- Click the ... button for any beta build and select **Go Live** from the menu.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-golive-button.png" />


:::info

You can only send **one** version to live and beta channels. When you send another beta or live version, the previous app version will be removed from that channel.

:::

### Unpublish
You can remove any build from Live or Beta channels by selecting the **Unpublish** menu from the actions. 

### Notify Users
You can send an email to your users by selecting the **Notify** menu from the actions. 

Your users will receive an email with the subject and message you entered in this form. Users will be able to download the program by clicking the link in the incoming email.

### Other Actions
If you want to share the link to a specific version without sending an email, you can select the **Share** menu from the actions. You can also download and delete versions from the list by selecting corresponding menus.

:::caution

The Enterprise App Store share feature doesn't allow public sharing. It only helps access the specific app version and follows all authentication rules.

:::

:::warning
**Please note that** if you have an **Apple Developer** account with an **enterprise organization** and you are using an app signed with an [**enterprise certificate**](https://docs.appcircle.io/signing-identities/ios-certificates-and-provisioning-profiles#ios-certificates) for **internal distribution**, you must use [**authentication**](https://docs.appcircle.io/enterprise-appstore/customize-ent-store#authentication) for user access.

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
