---
title: Huawei AppGallery API Key
description: Learn how to add a Huawei AppGallery API Key to your account in Appcircle
tags: [account, my organization, api integrations, huawei appgallery, api key]
sidebar_position: 7
---

import Screenshot from '@site/src/components/Screenshot';

# Huawei AppGallery API Key

Huawei AppGallery API Key is required to upload your binary to Huawei AppGallery. This JSON key must be added to your account to publish apps Huawei AppGallery.

1. Please go to Go to [Huawei AppGallery Console](https://developer.huawei.com) and login with your account and then head over to **Users and Permissions** and then click **Connect API**

<Screenshot url='https://cdn.appcircle.io/docs/assets/huaweiaccount-1addkey.png' />

2. Create a [Team-Level Api Key](https://developer.huawei.com/consumer/en/doc/distribution/app/appgallerykit-createapiclient). Don't select a project in order to create Team-Level API Key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huaweiaccount-2permissions.png' />

3. Hit the `Download` button to download the API key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huaweiaccount-3downloadkey.png' />

Your account key is ready. To add a key, go to [My Organization](/account/my-organization) and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Huawei AppGallery API Keys" item under the Connections section.

### FAQ

#### Why am I getting the error `"[AppGalleryConnectFileService]distContryList is empty and usage route site is not China"`?

This error may occur if the [Huawei Supported Countries ](https://developer.huawei.com/consumer/en/doc/app/agc-help-supported-countries-overview-0000001146718725) list has been updated.To resolve this issue, please follow these steps:

1. Open the page with your app information in your [Huawei Developer](https://developer.huawei.com/consumer/en/console/service/AppService) account (App Release > HarmonyOS|Android > Your app on list > Version Information > Your app version).
2. Update the `Country/Region for release` list and save the changes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/huaweiaccount-faq-1.png' />

3. Try again to send the release to Huawei AppGallery via Appcircle.
