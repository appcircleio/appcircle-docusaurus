---
title: Send Apps to App Store and TestFlight
metaTitle: Send Apps to App Store and TestFlight
metaDescription: Send Apps to App Store and TestFlight
sidebar_position: 1
---
import Screenshot from '@site/src/components/Screenshot';

# Send Apps to App Store and TestFlight

## Send Apps to App Store

To submit iOS applications to the App Store, click on the **iOS Publish** button on the left in the Publish module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-leftbar-ios.png' />

Appcircle creates a default flow after [sending your application to the Publish module via the Build module](/publish-module) or adding a manual version. This flow can be customized. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-flow-button.png' />

After clicking the **Publish Flow** button, the active steps for the related flow will appear.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore.png' />

The **Send to App Store** workflow is used for sending to the store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-appstore-flow.png' />

After adding the Send to App Store workflow to Publish Flow, we enter it by clicking on the relevant workflow. Appcircle allows this step to be customized.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-appstore-workflow-in.png' />

In the Send to App Store workflow, XCode Version, App Store Connect API Key, Submit Type. You can make selections for features such as.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-appstore-selection-1.png' />

:::tip
You can send both to the store and to TestFlight within the Send to App Store workflow. However, Appcircle will only send to TestFlight in the Send to TestFlight workflow.
:::

After completing the Publish Flow adjustments, we click on the "Details" button by clicking on the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can click on the **Restart Flow** button to start the workflow that includes publish to the store.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-restart-flow.png' />

If no errors occur, the sending process to the store will be completed successfully.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-succes-1.png' />

:::caution
After creating the publish profile, Appcircle will ask us to restart the workflow because we changed the default "Send to App Store" publishing flow step from "Send to TestFlight." Here, you can use the "Restart Flow" button on the top right to start the process of sending to the store.
:::

## Send Apps to TestFlight

With its publishing module, Appcircle allows you to submit your app to TestFlight without submitting it to the store. To do this, the application must be sent to the Publish module from the Build module or manually.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-main.png' />

After the application is sent to the publish module, it will now be necessary to select the **Send to TestFlight** workflow from the work steps in the publish flow.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-2.png' />

After clicking on the Send to TestFlight workflow, you can choose between the properties of this workflow in the window that opens. These will be the XCode Version and, App Store Connect API Key.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-send-testflight-in.png' />

After completing the Publish Flow adjustments, we click on the **Details** button by clicking on the three dots on the right side of the version list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-details-modal.png' />

In the window that opens afterwards, you can start the workflow including the submission to TestFlight by clicking the **Restart Flow** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-run.png' />

If no error is received in this step, Appcircle will have sent the relevant application to the TestFlight tool.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-testflight-success.png' />