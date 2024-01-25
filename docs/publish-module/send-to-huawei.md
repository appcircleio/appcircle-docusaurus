---
title: Send Apps to Huawei AppGallery
metaTitle: Send Apps to Huawei AppGallery
metaDescription: Send Apps to Huawei AppGallery
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

Appcircle supports sending APK and AAB binaries to Huawei AppGallery through the Publish module.

To publish Android applications to Huawei AppGallery, click on the **Android Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-android.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow.png' />

In **Publish Flow**, the default flow steps will appear. For Android publish flow, `Send to Google Play Store` is the default step.

So, for Huawei AppGallery, you need to replace it with the `Send to Huawei AppGallery` flow step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-1.png' />

Click on **Manage Flow** button to edit flow steps. From there, delete `Send to Google Play Store` from the flow and add `Send to Huawei AppGallery` to the flow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-huawei.png' />

Click on the **Save** button to return and then click on `Send to Huawei AppGallery` to configure the step settings.

In the step settings, select a **Huawei API Key** from the drop-down list and enter **Huawei App ID** into the text field.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-huawei-workflow-detail.png' />

:::caution
Appcircle will require **Huawei App ID** for Huawei AppGallery submissions. This form field should be correct for successful store submission.
:::

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-after-build) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-android-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to Huawei AppGallery.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-huawei-app-gallery-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-huawei-app-gallery-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-huawei-success.png' />