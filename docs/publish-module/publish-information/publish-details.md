---
title: Publish Details
description: Learn how to view the details of the publish flow in Appcircle
tags: [publish, publish details, publish flow]
sidebar_position: 2
---

# Publish Details

This option provides an in-depth view of the selected version's publish process. Users can review the steps taken, configurations used, and outcomes of the publish sequence. It's an essential resource for understanding the specific details of a version's journey through the publish workflow.

<!--
The "Publish Details" feature in the Publish module provides a comprehensive view of the publish flow for both Android and iOS builds. It is where you can see the progress and logs of your publishing process to different platforms like Google Play Store and TestFlight. -->

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3973-publishDetails.png' />

## Accessing Publish Details

To view the details of your publish flow:

1. **Select the Version:**

   - Locate and select the build version you want to review in the Publish module.

2. **Open Publish Details:**

   - Click on the "Publish Details" option to open the detailed view of the publish flow.

3. **Review the Logs:**
   - Examine the logs to monitor the progress of your publishing actions.
   - The logs will provide step-by-step updates on the status of each task within the flow.

## Features of Publish Details

- **Workflow Status:** Displays the current status of the publishing flow, indicating whether actions are in progress, completed, or if there are any errors.
- **Step-by-Step Logs:** Provides a detailed log for each step within the publish process, including timestamps, which can be useful for troubleshooting and verification.
- **Restart Flow:** If needed, you can restart the publish flow from scratch. Please note that restarting the flow will cause current logs to be lost.

## Publish Flow for Android & iOS

- **Android:**

  - The publish flow for Android includes steps like sending builds to the Google Play Store and managing additional settings specific to the Android ecosystem.

- **iOS:**
  - For iOS, the publish flow includes steps for sending builds to TestFlight, getting approval from TestFlight, and submitting to the App Store.

Ensure to regularly check the Publish Details to confirm that your app versions have been successfully published to the respective app stores. The logs within this section are crucial for identifying and resolving any issues during the publish process.
