---
title: Send Apps to Huawei AppGallery
metaTitle: Send Apps to Huawei AppGallery
metaDescription: Send Apps to Huawei AppGallery
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Send Apps to Huawei AppGallery

Appcircle uses the Android Publish section on the left in the Publish module for Huawei AppGallery Store application publish, just like for the Google Play Store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-android.png' />

Appcircle creates a default flow after [sending your application to the Publish module via the Build module](/publish-module) or adding a manual version. This flow can be customized.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow.png' />

After clicking the **Publish Flow** button, the active steps for the related flow will appear.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-1.png' />

We need to replace this default workflow with the **Send to Huawei AppGallery** workflow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-huawei.png' />

After this change, when we enter the **Send to Huawei AppGallery** workflow by clicking on it, we can select Huawei API Key and enter Huawei App ID.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-huawei-workflow-detail.png' />

:::caution
Appcircle will require **Huawei App ID** for Huawei AppGallery submissions. If this field is not filled in, Appcircle may not send it to the store successfully.
:::

After completing the Publish Flow adjustments, we click on the **Details** button by clicking on the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-android-modal.png' />

In the window that opens afterwards, you can click on the **Restart Flow** button to start the workflow that includes publish to the store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-huawei-run.png' />

If no errors occur, the sending process to the store will be completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-huawei-success.png' />