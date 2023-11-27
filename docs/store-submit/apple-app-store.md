---
title: Send Apps to App Store Connect and TestFlight
metaTitle: Send Apps to App Store Connect and TestFlight
metaDescription: Send Apps to App Store Connect and TestFlight
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef'

# Send Apps to App Store Connect and TestFlight

Appcircle supports sending IPA binaries to App Store Connect and TestFlight through the Store Submission module.

:::info

Both App Store Connect and TestFlight use the same binary pool, so once you send a binary to any of the destinations, it can be used across App Store Connect for testing and app releases.

:::

:::info

Store upload will use an account's build time and concurrency
:::


### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in App Store Connect. Otherwise, the store upload process will fail.

You also need to provide either:

- An App Store Connect API Key as a P8 file along with the key ID and the issuer ID. This is the recommended authentication method. Please refer to the following document for more information about the App Store Connect API key:\
  [https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api)

or

- An Apple Developer ID with an app-specific password. Please refer to the following document for more information about the app-specific passwords: [https://support.apple.com/en-us/HT204397](https://support.apple.com/en-us/HT204397)

### Adding an App Store Connect API Key (Recommended Method)

To send apps from Appcircle, you need to provide an App Store Connect API key. To add a key, go to [My Organization](../account/my-organization.md) Integrations tab and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "App Store Connect API Keys" item under the Connections section. The add key screen will be displayed.

[Create an API key in App Store Connect](https://developer.apple.com/documentation/appstoreconnectapi/creating_api_keys_for_app_store_connect_api) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

With the next option, enter the key ID and the issuer ID that can be obtained from the [keys section in App Store Connect](https://appstoreconnect.apple.com/access/api).

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (93).png' />

### Deploying the Binary from the Distribute Module

You can deploy the binaries to the Store Submit module from the [Distribute Module](../distribute/create-or-select-a-distribution-profile.md). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for App Store (signed with an App Store Distribution certificate).

Select a binary in the list and press "Send to Store Submit for App Store" from the top left menu. The bundle ID of the binary will be matched automatically if there is an existing store submission profile. If not, a new store submission profile will be created automatically.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (84).png' />

### Store Submit Profile Details

Once deployed, the binary will be available in the related store submission profile. Note that the profile name and icon is automatically fetched from the latest binary.

There are three actions available for each version in the version list. The first action displays a screen where you can initiate the store upload to the specified destination. The second action allows you to view the logs of the latest upload of that binary and the third action allows you to delete that version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (95).png' />

###

### Sending Apps to App Store Connect (and TestFlight)

:::info

Both App Store Connect and TestFlight use the same binary pool, so once you send a binary to any of the destinations, it can be used across App Store Connect for testing and app releases.

:::

When you press the "Upload to App Store Connect" button, you will be prompted to select an authentication method: with an App Store Connect API Key or with an Apple Developer ID using an app-specific password.

When you select an option, if you don't have a previously saved API key or Apple ID, you will be prompted to add one. If you have saved keys or IDs, you can select them from the list.

When you press the "Send App" button, the binary will be uploaded to App Store Connect.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (96).png' />

### Viewing the Binary Upload Status

The upload status of the binary can be tracked on the same screen.

Once the process is complete, you can click on the status or click on the "View Logs" button to see the logs. If the upload is successful, the app will be visible under the builds section in the TestFlight tab as well as in the builds list in the Add Build dialog in the App Store tab.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (88).png' />

### Deleting App Store Connect Profiles

Either for freeing up space purposes or if you wish to not use the Store Submit module, you can delete your App Store Connect. Click on the three dot menu on the profile card:

<Screenshot url='https://cdn.appcircle.io/docs/assets/storesubmit-appstore-delete.png' />

#### Delete a Single Store Submit Version

If you want to free up space but you don't want to lose your Store Submit profile, you can delete a submitted version from App Store Connect module. Note that if the version is sent to the App Store, your version **will not be deleted **from App Store.

Click on the three dot menu on the version, and click on the Delete Version

<Screenshot url='https://cdn.appcircle.io/docs/assets/storesubmit-appstore-version-delete.png' />

After typing the name, your version will be deleted.

:::info

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. For example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::
