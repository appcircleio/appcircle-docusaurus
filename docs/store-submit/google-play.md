---
title: Send Apps to Google Play Console
metaTitle: Send Apps to Google Play Console
metaDescription: Send Apps to Google Play Console
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Send Apps to Google Play Console

Appcircle supports sending APK and AAB binaries to Google Play Console through the Store Submission module.

You can send the same binary for testing to a pre-release track or to the production track.

:::info

Store upload will use an account's build time and concurrency
:::


### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Google Play and the initial binary is manually uploaded with the same keystore and the application ID (package name). Otherwise, the store upload process will fail. This is a known limitation of Google Play, which is in place for security purposes.

You also need to have a Google Service Account and its key as a JSON file. Please refer to the following document for more information about service accounts

<ContentRef url="/account/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>


### Adding a Google Play Developer API Key

To send apps from Appcircle, you need to provide a Google Developer API key. To add a key, go to [My Organization](../account/my-organization.md) Integratiion tab and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Google Play Developer API Keys" item under the Connections section. The add key screen will be displayed.

[Create a key in JSON format in the Google Developer Console](https://developers.google.com/android-publisher/getting_started#using_a_service_account) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

<ContentRef url="/account/adding-google-play-service-account">
  Adding Google Play Service Accounts
</ContentRef>

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (92).png' />

### Deploying the Binary from the Testing Distribution

You can deploy the binaries to the Store Submit module from the [Testing Distribution](../distribute/create-or-select-a-distribution-profile.md). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for Google Play. (e.g. in [release mode](../build/building-android-applications/) and [signed](../signing-identities/android-keystores.md) properly if APK - You can manage this in the [build configuration](../build/build-profile-configuration.md) for all types of development frameworks.).;

Select a binary in the list and press "Send to Store Submit for Play Store" from the top left menu. The package name of the binary will be matched automatically if there is an existing store submission profile. If not, a new store submission profile will be created automatically.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (69).png' />

### Store Submit Profile Details

Once deployed, the binary will be available in the related store submission profile. Note that the profile name and icon are automatically fetched from the latest binary.

There are three actions available for each version in the version list. The first action displays a screen where you can initiate the store upload. The second action allows you to view the logs of the latest upload of that binary and the third action button allows you to delete that version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (89).png' />

### Sending Apps to Google Play Console

When you press the "Upload to Google Play" button, the Send App screen is displayed. If you don't have a previously saved key, you will be prompted to [upload a Google Play Developer API Key](google-play.md#adding-a-google-play-developer-api-key).

If you have saved keys, you can select them from the list.

With the next option, [select a release track](https://support.google.com/googleplay/android-developer/answer/3131213) for your app.

When you press the "Send App" button, the binary will be uploaded to the Google Play Console.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (91).png' />

###

### Viewing the Binary Upload Status

The upload status of the binary can be tracked on the same screen.

Once the process is complete, you can click on the status or click on the "View Logs" button to see the logs. If the upload is successful, you can submit this binary to the store from the "App releases" section in the Google Play Dashboard under the selected track.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (74).png' />

### Troubleshooting Common Google Play Upload Errors

The binary sent to Google Play must be production-ready, so you can encounter certain errors if the binary does not meet the release criteria. You can see the explanations of some of the common errors:

`APK specifies a version code that has already been used.` : You cannot upload an app with the same version code. The app can still have the same release version, but its version code must be increased. - You can update the version code from the app source code.

`Cannot update a published APK.` : If a binary has already been sent to a specific track, you cannot reupload it. - You can change its track from the Google Play Dashboard.

`APK is marked as debuggable.` : The binary must in the release mode for release distribution. - You can change the release mode in the build configuration and rebuild the app.

`APK was signed with the wrong key.` : The binary is signed with a different keystore than the previous version. - You need to change the keystore in the build configuration and rebuild the app.

### Deleting Google Play Store Submit Profiles

Either for freeing up space purposes or if you wish to not use the Store Submit module, you can delete your store submit profile. Click on the three dot menu on the profile card:

<Screenshot url='https://cdn.appcircle.io/docs/assets/storesubmit-playstore-delete.png' />

#### Delete a Single Store Submit Version

If you want to free up space but you don't want to lose your Store Submit profile, you can delete a submitted version from Google Play Store Submit module. Note that if the version is sent to the Google Play Store, your version **will not be deleted **from Google Play.

Click on the three dot menu on the version, and click on the Delete Version

<Screenshot url='https://cdn.appcircle.io/docs/assets/storesubmit-playstore-version-delete.png' />

After typing the name, your version will be deleted.

:::info

In order to free up storage on your organization, you should also remove the other references pointing to the artifact. In example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::
