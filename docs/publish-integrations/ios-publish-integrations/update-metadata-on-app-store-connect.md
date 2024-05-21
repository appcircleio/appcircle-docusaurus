---
title: Update Metadata on App Store Connect
description: This step enables you to upload the Metadata information of application on App Store Connect.
tags: [publish, ios, metadata, app store connect]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Update Metadata on App Store Connect

When this step runs, it uploads all metadata information edited on [**Metadata Information**](/publish-module/publish-information/meta-data-information) to the relevant places on App Store Connect. 

### Prerequisites

This step is an independent one, and there is no specific step required for the step to work. It can be used anywhere in Publish Flow,step according to the workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3741-metadataOrder.png' />

### Input Variables

Below are the parameters necessary for this step's operation, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3741-metadataInput.png' />

:::info

- **Uploads screenshots while sending METADATA** : This value is `true` by default and includes screen shots uploaded in [**Metadata Information**](/publish-module/publish-information/meta-data-information#ios-metadata-information) during the upload process. If `false`, screen shots will not be uploaded.
- **Update Metadata fields** : This value is `true` by default and ensures that the [**Metadata Information**](/publish-module/publish-information/meta-data-information#ios-metadata-information) to be updated is uploaded. If `false`, the entered metadata information will not be uploaded.
- **Clear all previously uploaded screenshots** : This value is `false` by default. If `true`, screen shots on the App Store Connect will be deleted and new ones will be uploaded. 

:::danger Clear all previously uploaded screenshots

Note that when this value is selected as `true`, your **screen shots** will be **deleted** from your **App Store Connect** account.

:::



| Variable Name                     | Description                                                                                                                                                | Status   |
| --------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------------------------------| -------- |
| `$AC_XCODE_LIST_DIR`              | Specifies the Xcode folder list directory. Current Xcode folder structure examples: `/Applications/Xcode/14.3/Xcode` or `/Applications/Xcode/15.0/Xcode`.  | Optional |
| `$AC_XCODE_VERSION`               | Specifies the Xcode version.                                                                                                                               | Required |
| `$AC_UPLOAD_SCREENSHOT_FILES`     | Uploads screenshot files to App Store Connect for the related app version.                                                                                 | Optional |
| `$AC_UPDATE_METADATA_INFO`        | If disabled updating METADATA info will be ignored.                                                                                                        | Optional |
| `$AC_CLEAR_SCREENSHOTS`           | If enabled all screenshots on App Store Connect will be removed before upload.                                                                             | Optional |
