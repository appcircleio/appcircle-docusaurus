---
title: Send Apps to App Store and TestFlight
metaTitle: Send Apps to App Store and TestFlight
metaDescription: Send Apps to App Store and TestFlight
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

Appcircle supports sending IPA binaries to the App Store and TestFlight through the Publish module.

### Send Apps to App Store

To submit iOS applications to the App Store, click on the **iOS Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-ios.png' />

Click on **Add New** to create a new publish profile, **Open** details, and click on **Publish Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-button.png' />

In **Publish Flow**, the default flow steps will appear. If there is no `Send to App Store` step in the default flow click on **Manage Flow**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore.png' />

Find the `Send to App Store` step in the steps list, and then drag and drop it into the flow.

:::info
For basic usage, only the `Send to App Store` step will be enough for sending applications to the App Store.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore-flow.png' />

After adding the step to the flow, click on **Save** to return, and then click on `Send to App Store` to configure the step settings.

In the step settings, you can customize the **Xcode Version**, select an **App Store Connect API Key** from the drop-down list, and change the default **Stage Type** according to your needs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-appstore-selection-1.png' />

:::tip

You can use `Send to App Store` to send an application to TestFlight. For this purpose, you can select  `TestFlight` in **Stage Type**.

However, Appcircle will only send to TestFlight in the `Send to TestFlight` step. See details [here](#send-apps-to-testflight).
:::

When you complete configuring the publish flow, add an application version by [configuring the build module](index.md#publish-after-build) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to the App Store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-app-store-restart-flow.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to the store was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-succes-1.png' />

### Send Apps to TestFlight

Within Appcircle, you can also submit your applications to TestFlight.

You can use the [Send to App Store](#send-apps-to-app-store) step with the customizations given there (Stage Type), or you can use the dedicated `Send to TestFlight` step explained in the following section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-main.png' />

After adding the step to the flow, click on **Save** to return, and then click on `Send to TestFlight` to configure the step settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-2.png' />

In the step settings, you can customize the **Xcode Version**, select an **App Store Connect API Key** from the drop-down list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-in.png' />

When you complete configuring the publish flow, add an application version by [configuring the build module ](index.md#publish-after-build) or [manually adding a version](index.md#add-version) by binary upload.

Click on the three dots to open the **Actions** menu for the version and select **Details** there.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can click on the **Start Flow** button to start the flow that includes publish to TestFlight.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-to-test-flight-start-flow.png' />

:::info
You can add or remove steps, change the order of steps in the flow, and edit step settings anytime you need.

When you **change the publish flow** for some reason **after adding an application version**, you will see the **Restart Flow** button in the version **Details**. You can use the same button for either starting flow for the first time or restarting flow for a previously executed one.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-run.png' />
:::

After publish flow execution, if no errors occurred, that means the sending to TestFlight was completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-success.png' />