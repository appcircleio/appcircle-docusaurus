---
title: Update Metadata on Google Play Console
description: This step enables you to upload the Metadata information of application on Google Play Console.
tags: [publish, android, metadata, google play console]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';
import RunnerUsage from '@site/docs/\_publish-steps-runner-usage-caution.mdx';

# Update Metadata on Google Play Console

This step uploads all edited metadata information from the [**Metadata Information**](/publish-module/publish-information/meta-data-information) page to the corresponding sections on Google Play Console.

<RunnerUsage />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5968-google1.png' />


### Prerequisites

This step operates independently; it does not require any specific prior steps. You can incorporate it anywhere in the Publish Flow according to your workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5968-google3.png' />

### Input Variables

Below are the parameters necessary for this step's operation, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5968-google2.png' />

| Input Variables                                            | Description                                                                                                                                                                                                                                                       |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Uploads screenshots while sending METADATA**             | This value is `true` by default and includes screen shots uploaded in [**Metadata Information**](/publish-module/publish-information/meta-data-information#ios-metadata-information) during the upload process. If `false`, screen shots will not be uploaded.    |
| **Update Metadata fields**                                 | This value is `true` by default and ensures that the [**Metadata Information**](/publish-module/publish-information/meta-data-information#ios-metadata-information) to be updated is uploaded. If `false`, the entered metadata information will not be uploaded. |
| **Synchronize Image Uploads with the Google Play Console** | If enabled, only new images will be uploaded. Previously uploaded and unchanged images will be skipped.                                                                                                                                                           |
| **Auto Send for Review**                                   | Automatically submits the updated metadata and app version for review on the Google Play Console.                                                                                                                                                                 |

:::warning Mandatory Google Play Metadata Fields

On **Google Play Console**, certain metadata fields are **mandatory** and must be completed before you can **save** the metadata details in Appcircle.

The following fields are required by Google Play:

- **App Name**
- **Short Description**
- **Full Description**
- **App Icon**
- **Feature Graphic**
- **Phone Screenshots**

If any of these required fields are missing, Google Play Console will not allow the metadata to be saved or updated. Make sure all mandatory fields are properly filled and uploaded before running the **Update Metadata on Google Play Console** publish step.

:::