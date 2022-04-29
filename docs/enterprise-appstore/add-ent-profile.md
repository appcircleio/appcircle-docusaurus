---
title: Add a Profile
metaTitle: Add a Profile
metaDescription: Add a Profile
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# Enterprise Store

If you want to distribute your in-house applications to your users, you may use Appcircle's Enterprise Store. Appcircle's Enterprise store helps you to set up your own store and have full control over deployment and access management. 

### Prerequisites

In order for your users to download IPA or APK files, those files must be signed with proper certificates or Keystore files. 

Android apps can be signed with any Keystore if the user's device allows installing apps from other sources.

Although iOS apps can be signed with Ad-Hoc provisioning profiles for in-house distribution, this type of distribution is limited to 100 devices per year. You also need to add the UUID of your users' device to Apple's Developer website.

If you have more than 100 users and don't want to deal with device enrollment, you need to use sign your apps with Enterprise Certificate. 

### Adding a Profile

There are several ways to create an Enterprise build profile. You can either manually upload your IPA or APK files or you can send them from Appcircle's Distribution Module.

### Manual Upload

- Click the Enterprise App Store button on the left menu bar. 

![](<https://cdn.appcircle.io/docs/assets/entstore-select.png>)

- If you haven't created any profile before, you will see the following screen.

![](<https://cdn.appcircle.io/docs/assets/entstore-manual-add.png>)

- Click the **Add New App** button to open the upload panel.

![](<https://cdn.appcircle.io/docs/assets/entstore-selectfile.png>)

- Choose your APK or IPA file and click the **Upload** button.
- If you have uploaded a valid APK or IPA file, you should see your brand new profile

![](<https://cdn.appcircle.io/docs/assets/entstore-profilelist.png>)

### Sending from Distribution

- Go to your build profile, hit the config button, and enable **Publish Enterprise App Store**.

![](<https://cdn.appcircle.io/docs/assets/entstore-buildconfig.png>)

- Whenever you create a new *signed* build, that build will be sent to Enterprise App Store.
- You can also manually send your APK or IPA files by hitting the **...** button and selecting **Distribute Binary**

![](<https://cdn.appcircle.io/docs/assets/07-01-Output.jpg>)


After you created a build profile, you can manage the deployment and access settings by visiting that profile.

:::info

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api/about-the-appcircle-cli">Appcircle CLI</ContentRef>
