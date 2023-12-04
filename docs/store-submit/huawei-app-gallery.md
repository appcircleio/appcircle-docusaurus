---
title: Send Apps to Huawei AppGallery
metaTitle: Send Apps to Huawei AppGallery
metaDescription: Send Apps to Huawei AppGallery
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Send Apps to Huawei AppGallery

Appcircle supports sending APK or AAB to Huawei AppGallery through the Store Submission module.

You can send the same binary for testing to a pre-release track or to the production track.

:::info

Store upload will use an account's build time and concurrency
:::


### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Huawei AppGallery Connect and the initial binary is manually uploaded with the same keystore and the application ID (package name). Otherwise, the store upload process will fail.

You also need to have an AppGallery Connect API and its key as a JSON file. Please refer to the following document for more information on creating your API key.

<ContentRef url="/account/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>


### Adding a Huawei AppGallery API Key

To send apps from Appcircle, you need to provide a Huawei AppGallery Developer API key. To add a key, go to [My Organization](../account/my-organization.md) and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Huawei AppGallery Developer API Keys" item under the Connections section. The add key screen will be displayed.

[Create a key in JSON format in the AppGallery Connect](https://developer.huawei.com/consumer/en/doc/development/AppGallery-connect-Guides/agcapi-getstarted-0000001111845114) and upload it here for API authentication. Please keep this file as it is the only copy and it will be required during every store submission for security purposes.

<ContentRef url="/account/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>

Then enter a user-friendly name to identify the key in the lists and press save. You can use this key in multiple apps without the need for key uploads at every upload process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-1addkey.png' />

### Uploading your Keystore file

Your upload keystore file should also be uploaded to Huawei AppGallery. Follow the [AppGallery documentation](https://developer.huawei.com/consumer/en/doc/development/AppGallery-connect-Guides/agc-appsigning-newapp-0000001052418290#EN-US_TOPIC_0000001052418290__section1959661616436) to convert your keystore file and upload it to `App Signing` section on AppGallery.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-8signing.png' />


### Deploying the Binary from the Testing Distribution

You can deploy the binaries to the Store Submit module from the [Testing Distribution](../distribute/create-or-select-a-distribution-profile.md). Both directly uploaded apps and built apps deployed from the build module are supported as long as they are valid for Huawei AppGallery. (e.g. in [release mode](../build/building-android-applications/) and [signed](../signing-identities/android-keystores.md) properly if APK - You can manage this in the [build configuration](../build/build-profile-configuration.md) for all types of development frameworks.).;

Select a binary in the list and press "Send to Store Submit for AppGallery" from the top right menu. The package name of the binary will be matched automatically if there is an existing store submission profile. If not, a new store submission profile will be created automatically.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-2sendstore.png' />

### Store Submit Profile Details

Once deployed, the binary will be available in the related store submission profile. Note that the profile name and icon are automatically fetched from the latest binary.

There are three actions available for each version in the version list. The first action displays a screen where you can initiate the store upload. The second action allows you to view the logs of the latest upload of that binary and the third action button allows you to delete that version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-3upload.png' />

### Sending Apps to Huawei AppGallery Console

When you press the "Upload to Huawei AppGallery" button, the Send App screen is displayed. If you don't have a previously saved key, you will be prompted to [upload a Huawei AppGallery Developer API Key](#adding-a-huawei-appgallery-api-key).

If you have saved keys, you can select them from the list.

With the next option, write the [Huawei App ID](https://developer.huawei.com/consumer/en/doc/development/connectivity-Guides/addingappid-packagename-0000001050818013) for your app.

When you press the "Send App" button, the binary will be uploaded to the Huawei AppGallery Console.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-4select.png' />


### Viewing the Binary Upload Status

The upload status of the binary can be tracked on the same screen.

Once the process is complete, you can click on the status or click on the "View Logs" button to see the logs. If the upload is successful, you can submit this binary to the store from the "Version Information" section in the Huawei AppGallery Dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/storesubmit-appgallery-version-logs.png' />

### Troubleshooting Common Huawei AppGallery Upload Errors

The binary sent to Huawei AppGallery must be production-ready, so you can encounter certain errors if the binary does not meet the release criteria. You can see the explanations of some of the common errors:

- `Cannot obtain upload url, please check API Token / Permissions (status code: 403).`

Check your API key and App ID

- `[!] {"ret"=>{" code"=>204144662, "msg"=>" [cds]add apk failed, additional msg is {\"packageName\": \"com.appcircle.appcircle_sample_android\", \"userType\":2}]"}}`

Error during uploading your package. This may happen if your bundle identifier is not unique.

### Deleting Huawei AppGallery Submit Profiles

Either for freeing up space purposes or if you wish to not use the Store Submit module, you can delete your store submit profile. Click on the three dot menu on the profile card:

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-6deteleprofile.png' />

#### Delete a Single Store Submit Version

If you want to free up space but you don't want to lose your Store Submit profile, you can delete a submitted version from Huawei AppGallery Submit module. Note that if the version is sent to the Huawei AppGallery, your version **will not be deleted **from Huawei AppGallery.

Click on the three dot menu on the version, and click on the Delete Version

<Screenshot url='https://cdn.appcircle.io/docs/assets/huawei-7deletebuild.png' />

After typing the name, your version will be deleted.

:::info

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. For example, if you have the same artifact on the builds, you should also delete those artifacts as well.

:::
