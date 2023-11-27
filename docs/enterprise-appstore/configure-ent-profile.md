---
title: Configure a Profile
metaTitle: Configure a Profile
metaDescription: Configure a Profile
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';

# Configure a Profile

After you have created your profile, it is time to configure it and send it to different users and channels.


### Manage Access

You can add users to your live and beta channels by clicking the **Settings** button. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-versionlist.png' />


You can add multiple users to beta and live channels by hitting the Tab key.


<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-useraccess.png" />

:::caution
If you work for a sub-organization, you can only see the apps belonging to that organization. However, if the app is published, it will also appear in the parent organization's showcase.
:::


### Add Version

If you enabled  **Publish Enterprise Store** settings in your config, all the new signed builds will automatically appear in the list. You can also manually upload a new version to your profile. 

Click the **Add Version** button and select IPA or APK file and hit the **Upload** button.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-upload.png" />


:::caution

Make sure that the bundle id matches your current profile and version or build number is different than the other files in the list. 

:::

### Publish to Channel

Apps can be sent to Beta or Live channels by hitting the ... button and then selecting the **Publish** menu. 

<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-publish.png" />


You can select the channel and write a summary and release notes for your release. When you hit the **Publish** button that particular build will be available to all beta users.

You can send a version to Live Channel in two ways

- Click the **Publish** button and select **Live** for the channel
- Click the ... button for any beta build and select **Go Live** from the menu.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/entstore-golive.png" />


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


:::info

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api/about-the-appcircle-cli">Appcircle CLI</ContentRef>
