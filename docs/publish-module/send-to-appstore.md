---
title: Send Apps to App Store and TestFlight
metaTitle: Send Apps to App Store and TestFlight
metaDescription: Send Apps to App Store and TestFlight
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# Send Apps to App Store and TestFlight

Appcircle supports sending IPA binaries to the App Store and TestFlight through the Publish module.

### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in App Store Connect. Otherwise, the store upload process will fail.

You also need to provide either:

- An App Store Connect API Key as a P8 file along with the key ID and the issuer ID. This is the recommended authentication method. Please refer to the following document for more information about the [App Store Connect API key](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api).

or

- An Apple Developer ID with an app-specific password. Please refer to the following document for more information about the [App-Specific Passwords](https://support.apple.com/en-us/HT204397).

### Adding an App Store Connect API Key (Recommended Method)

To send apps from Appcircle, you need to provide an App Store Connect API key. To add a key, go to the [My Organization](https://docs.appcircle.io/account/my-organization) Integrations tab and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "App Store Connect API Keys" item under the Connections section. The `Add Key` screen will be displayed.

[Create an API key in App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

With the next option, enter the key ID and the issuer ID that can be obtained from the keys section in the [App Store Connect](https://appstoreconnect.apple.com/access/api).

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-UploadAppstoreConnect-ApiKey.png' />

### Deploying the Binary from the Testing Distribution

You can deploy the binaries to the Publish module from the [Testing Distribution](https://docs.appcircle.io/distribute/). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for the App Store (signed with an App Store Distribution certificate).

Select a binary in the list and press "Send to Publish" from the three dots. The bundle ID of the binary will be matched automatically if there is an existing store submission profile. If not, you have to create a new Publish profile.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-distribution-publish-ios.png' />

### Publish Profile Details

Once deployed, the binary will be available in the related publish profile. Note that the profile name and icon are automatically fetched from the latest binary.

There are six actions available for each version in the version list.

The `Details` button lets you start the workflow, while `App Information` gives you key details about the app.
`History` shows logs of past actions. You can use `Mark as RC` to indicate the application as a release candidate.
`Download` allows you to get the app version easily.
Lastly, `Delete` helps you remove the app version easily.

<Screenshot url='https://cdn.appcircle.io/docs/assets/2821-ios-publish-actions.png' />

### Send Apps to App Store

To submit iOS applications to the App Store, click on the **iOS Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-ios.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-button.png' />

In **Publish Flow**, the default flow steps will appear. If there is no `Send to App Store` step in the default flow click on **Manage Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore.png' />

Find the `Send to App Store` step in the steps list, and then drag and drop it into the flow.

:::info
For basic usage, only the `Send to App Store` step will be enough for sending applications to the App Store.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore-flow.png' />

After adding the step to the flow, click on **Save** to return, and then click on `Send to App Store` to configure the step settings.

In the step settings, you can customize the **Xcode Version**, select an **App Store Connect API Key** from the drop-down list, and change the default **Stage Type** according to your needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-appstore-selection-1.png' />

:::tip

You can use `Send to App Store` to send an application to TestFlight. For this purpose, you can select  `TestFlight` in **Stage Type**.

However, Appcircle will only send to TestFlight in the `Send to TestFlight` step. See details [here](#send-apps-to-testflight).
:::

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-profile) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to the App Store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-app-store-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-succes-1.png' />

### Send Apps to TestFlight

Within Appcircle, you can also submit your applications to TestFlight.

You can use the [Send to App Store](#send-apps-to-app-store) step with the customizations given there (Stage Type), or you can use the dedicated `Send to TestFlight` step explained in the following section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-main.png' />

After adding the step to the flow, click on **Save** to return, and then click on `Send to TestFlight` to configure the step settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-2.png' />

In the step settings, you can customize the **Xcode Version**, select an **App Store Connect API Key** from the drop-down list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-in.png' />

When you complete configuring the publish flow, add an application version by [configuring the build module ](index.md#publish-profile) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to TestFlight.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-test-flight-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-run.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to TestFlight was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-success.png' />

### Deleting iOS Publish Profiles

Either for freeing up space purposes or if you wish to not use the Publish module, you can delete your iOS Publish Profile. Click on the three-dot menu on the profile card:

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-ios-delete-profile.png' />

#### Delete a Single Publish Version

If you want to free up space but don't want to lose your Publish profile, you can delete a submitted version from the iOS Publish Profile module. Note that if the version is sent to the App Store, your version **will not be deleted** from the App Store.

Click on the three dot menu on the version, and click on the Delete

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-ios-version-delete.png' />

After typing the name, your version will be deleted.

:::info

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. For example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::
