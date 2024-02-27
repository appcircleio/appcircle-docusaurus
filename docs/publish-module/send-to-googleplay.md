---
title: Send Apps to Google Play 
metaTitle: Send Apps to Google Play
metaDescription: Send Apps to Google Play
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

Appcircle supports sending APK and AAB binaries to Google Play through the Publish module.

To publish Android applications to Google Play, click on the **Android Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-android.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow.png' />

In **Publish Flow**, the default flow steps will appear. There should be `Send to Google Play Store` step in the default flow as a single step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-1.png' />

You can also add other flow steps to your flow using the **Manage Flow** button. For basic usage, only the `Send to Google Play Store` step would be sufficient.

Click on the **Save** button if you make any changes to your flow steps, or use the **Back** button without any change.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-android-in.png' />

Click on `Send to Google Play Store` to configure the step settings.

In the step settings, select an **Google Play Store API Key** from the drop-down list, and change the default **Track Type** and **Play Store App Status** according to your needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-android-flow-details.png' />

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-after-build) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-android-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to Google Play.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-run-android.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-google-play-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-android-success.png' />