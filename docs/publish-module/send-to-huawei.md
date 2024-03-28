---
title: Publish to Huawei AppGallery
metaTitle: Publish to Huawei AppGallery
metaDescription: Publish to Huawei AppGallery
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Publish to Huawei AppGallery

Appcircle supports sending APK and AAB binaries to Huawei AppGallery through the Publish module.

### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Huawei AppGallery Connect and the initial binary is manually uploaded with the same keystore and the application ID (package name). Otherwise, the store upload process will fail.

You also need to have an AppGallery Connect API and its key as a JSON file. Please refer to the following document for more information on creating your API key.

<ContentRef url="/account/my-organization/api-integrations/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>

### Adding a Huawei AppGallery API Key

To send apps from Appcircle, you need to provide a Huawei AppGallery Developer API key. To add a key, go to the [My Organization](https://docs.appcircle.io/account/my-organization) and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Huawei AppGallery Developer API Keys" item under the Connections section. The `Add Key` screen will be displayed.

[Create a key in JSON format in the AppGallery Connect](https://developer.huawei.com/consumer/en/doc/development/AppGallery-connect-Guides/agcapi-getstarted-0000001111845114) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

<ContentRef url="/account/my-organization/api-integrations/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-HuaweiAppGallery-ApiKey.png' />

### Uploading your Keystore file

Your uploaded keystore file should also be uploaded to Huawei AppGallery. Follow the [AppGallery documentation](https://developer.huawei.com/consumer/en/doc/development/AppGallery-connect-Guides/agc-appsigning-newapp-0000001052418290#EN-US_TOPIC_0000001052418290__section1959661616436) to convert your keystore file and upload it to `App Signing` section on AppGallery.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-8signing.png' />

### Deploying the Binary from the Testing Distribution

You can deploy the binaries to the Publish module from the [Testing Distribution](https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile.md). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for Huawei AppGallery. (e.g. in [release mode](https://docs.appcircle.io/build/building-android-applications/) and [signed](https://docs.appcircle.io/signing-identities/android-keystores) properly if APK - you can manage this in the [build configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration.) for all types of development frameworks.)

Select a binary in the list and press "Send to Publish" from the three dots. The package name of the binary will be matched automatically if there is an existing Publish profile. If not, you have to create a new Publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-distribution-publish-1.png' />

### Publish Profile Details

Once deployed, the binary will be available in the related publish profile. Note that the profile name and icon are automatically fetched from the latest binary.

There are six actions available for each version in the version list.

The `Details` button lets you start the workflow, while `App Information` gives you key details about the app.
`History` shows logs of past actions. You can use `Mark as RC` to indicate the application as a release candidate.
`Download` allows you to get the app version easily.
Lastly, `Delete` helps you remove the app version easily.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-android-publish-actions.png' />

### Sending Apps to Huawei AppGallery

To publish Android applications to Huawei AppGallery, click on the **Android Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-android.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow.png' />

In **Publish Flow**, the default flow steps will appear. For Android publish flow, `Send to Google Play Store` is the default step.

So, for Huawei AppGallery, you need to replace it with the `Send to Huawei AppGallery` flow step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-1.png' />

Click on **Manage Flow** button to edit flow steps. From there, delete `Send to Google Play Store` from the flow and add `Send to Huawei AppGallery` to the flow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-huawei.png' />

Click on the **Save** button to return and then click on `Send to Huawei AppGallery` to configure the step settings.

In the step settings, select a **Huawei API Key** from the drop-down list and enter **Huawei App ID** into the text field.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-huawei-workflow-detail.png' />

:::caution
Appcircle will require **Huawei App ID** for Huawei AppGallery submissions. This form field should be correct for successful store submission.
:::

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-profile) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-android-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to Huawei AppGallery.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-huawei-app-gallery-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-huawei-app-gallery-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-huawei-success.png' />

### Deleting Huawei Publish Profiles

Either for freeing up space purposes or if you wish to not use the Publish module, you can delete your Publish Profile. Click on the three-dot menu on the profile card:

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-delete-profile.png' />

#### Delete a Single Publish Version

If you want to free up space but don't want to lose your Publish profile, you can delete a submitted version from the Android Publish module. Note that if the version is sent to the Huawei AppGallery, your version **will not be deleted** from the Huawei AppGallery.

Click on the three dot menu on the version, and click on the **Delete** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-version-delete.png' />

After typing the name, your version will be deleted.

:::info

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. For example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::
