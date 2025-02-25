---
title: Publish to Huawei AppGallery
description: Publish your Android applications to Huawei AppGallery with Appcircle
tags: [android, android integrations, android publish integrations, huawei appgallery, publish appgallery]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Publish to Huawei AppGallery

Appcircle supports sending [APK](https://developer.huawei.com/consumer/en/doc/app/agc-help-releaseapkrpk-0000001106463276) and [AAB](https://developer.huawei.com/consumer/en/doc/app/agc-help-releasebundle-0000001100316672) binaries to [Huawei AppGallery](https://appgallery.huawei.com/) through the Publish module.

### Prerequisites

Before uploading a binary to the store, please make sure that an application listing is created in Huawei AppGallery Connect and the initial binary is manually uploaded with the same keystore and the application ID. Otherwise, the store upload process will fail.

You also need to have an AppGallery Connect API and its key as a JSON file. Please refer to the following document for more information on creating your API key.

<ContentRef url="/account/my-organization/security/credentials/adding-huawei-api-key">
  Adding Huawei AppGallery API Key
</ContentRef>

After completing the integration with Huawei AppGallery API Key, go to [Publishing Settings](/publish-module/publish-settings). In the [`Store Credential`](/publish-module/publish-settings#store-credentials) section, select the Huawei AppGallery API Key you uploaded, from the drop-down list.

If you are using [Publish Variables](/publish-module/publish-settings#publish-variables), you should select them in the [Publishing Settings](/publish-module/publish-settings) window.

## Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-publishflow-publish-huawei-appgallery-1.png'/>

| Variable Name       | Description                                                                                                                                                                                                                                  | Status    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `$AC_HUAWEI_APP_ID` | It is required to publish the app to Huawei AppGallery. You can find the App ID on the [Huawei Developer Console](https://developer.huawei.com/consumer/en/console) by navigating to `App Services` > `AppGallery Connect` > `My Apps` > `your app` > `App Information`. | Required  |
| `$AC_RELEASE_NOTES` | Provides release notes for the submission to Huawei AppGallery. | Optional  |

## Output Variables

**Publish to Huawei AppGallery** step does not produce any output. However, you can check the logs to see whether your app has successfully accessed Huawei AppGallery.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-send-to-appgallery.git