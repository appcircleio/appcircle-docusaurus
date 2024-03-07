---
title: Send Apps to Google Play 
metaTitle: Send Apps to Google Play
metaDescription: Send Apps to Google Play
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Send Apps to Google Play

Appcircle supports sending APK and AAB binaries to Google Play through the Publish module.

### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Google Play and the initial binary is manually uploaded with the same keystore and the application ID (package name). Otherwise, the store upload process will fail. This is a known limitation of Google Play that is in place for security purposes.

You also need to have a Google Service Account and its key as a JSON file. Please refer to the following document for more information about service accounts.

<ContentRef url="/account/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>


### Adding a Google Play Developer API Key

To send apps from Appcircle, you need to provide a Google Developer API key. To add a key, go to my [My Organization](https://docs.appcircle.io/account/my-organization) Integration tab and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Google Play Developer API Keys" item under the Connections section. The `Add Key` screen will be displayed.

[Create a key in JSON format in the Google Developer Console](https://developers.google.com/android-publisher/getting_started#using_a_service_account) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

<ContentRef url="/account/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-UploadGooglePlay-ApiKey.png' />

### Deploying the Binary from the Testing Distribution

You can deploy the binaries to the Publish module from the [Testing Distribution](https://docs.appcircle.io/distribute/create-or-select-a-distribution-profile). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for Google Play. (e.g. in [release mode](https://docs.appcircle.io/build/building-android-applications/) and [signed](https://docs.appcircle.io/signing-identities/android-keystores) properly if APK - you can manage this in the [build configuration](https://docs.appcircle.io/build/build-profile-configuration) for all types of development frameworks.)

Select a binary in the list and press "Send to Publish" from the three dots. The package name of the binary will be matched automatically if there is an existing publish profile. If not, you have to create a new Publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-distribution-publish-1.png' />

### Publish Profile Details

Once deployed, the binary will be available in the related publish profile. Note that the profile name and icon are automatically fetched from the latest binary.

There are six actions available for each version in the version list.

The `Details` button lets you start the workflow, while `App Information` gives you key details about the app.
`History` shows logs of past actions. You can use `Mark as RC` to indicate the application as a release candidate.
`Download` allows you to get the app version easily.
Lastly, `Delete` helps you remove the app version easily.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-android-publish-actions.png' />


### Sending Apps to Google Play

To publish Android applications to Google Play, click on the **Android Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-android.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow.png' />

In **Publish Flow**, the default flow steps will appear. There should be `Send to Google Play Store` step in the default flow as a single step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-1.png' />

You can also add other flow steps to your flow using the **Manage Flow** button. For basic usage, only the `Send to Google Play Store` step would be sufficient.

Click on the **Save** button if you make any changes to your flow steps, or use the **Back** button without any change.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-in.png' />

Click on `Send to Google Play Store` to configure the step settings.

In the step settings, select an **Google Play Store API Key** from the drop-down list, and change the default **Track Type** and **Play Store App Status** according to your needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow-details.png' />

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-profile) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-android-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to Google Play.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-run-android.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-google-play-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-android-success.png' />
