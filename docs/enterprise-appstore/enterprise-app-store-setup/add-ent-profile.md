---
title: Creating a Profile
metaTitle: Creating a New App Store Profile
metaDescription: Creating a New App Store Profile
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

There are several ways to create an Enterprise build profile. You can either manually upload your IPA or APK files or you can send them from Appcircle's Distribution Module.

### Manual Upload

- Click the Enterprise App Store button on the left menu bar.

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-main-menu.png' />

- If you haven't created any profile before, you will see the following screen. Click the **Add New App** button to open the upload panel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-create-no-apps.png' />

- Choose your APK or IPA file and click the **Upload** button.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-binary-file-upload.png" />

- If you have uploaded a valid APK or IPA file, you should see your brand new profile

<Screenshot url='https://cdn.appcircle.io/docs/assets/entstore-profilelist.png' />

### Sending from Distribution

- Go to your build profile, hit the config button, and enable **Automatically Distribute to Enterprise App Store**.

<Screenshot url="https://cdn.appcircle.io/docs/assets/entstore-enable-build-configuration.png" />

- Whenever you create a new _signed_ build, that build will be sent to Enterprise App Store.
- You can also manually send your APK or IPA files by hitting the **...** button and selecting **Distribute Binary**

<Screenshot url='https://cdn.appcircle.io/docs/assets/build-ios-distribute-artifacts.png' />

After you created a build profile, you can manage the deployment and access settings by visiting that profile.

:::info

The above tasks can also be initiated by our Appcircle CLI. Please check the Appcircle CLI documentation for the command line parameters.

:::

<ContentRef url="/appcircle-api">Appcircle CLI</ContentRef>
