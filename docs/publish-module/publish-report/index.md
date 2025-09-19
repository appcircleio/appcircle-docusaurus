---
title: Publish Report
sidebar_position: 1
tags: [publish, report]
description: Understand the Report for Publish in Appcircle, providing visibility on the usage of publish module over a given time period.

---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/\_csv-export.mdx';

# Publish Report

The Publish Report provides a detailed overview of all actions performed within the Publish Module. It allows users to monitor, filter, and export publish-related activities across different platforms, trigger types, and stores.

These are the displayed fields within the Publish Report:

- Org Name
- Profile Name
- App Name
- Version
- Version Code
- Initiated By
- Trigger Type
- Platform
- Store
- Start Date
- Duration

<Screenshot url="https://cdn.appcircle.io/docs/assets/7112-7.png" />

## Filtering Options

Users can refine the report data using multiple filters:

- **Date Range:** Select specific time periods to analyze publish activity.
- **Platform:** Filter by iOS or Android
- **Trigger Type:** View actions triggered manually or automatically.
- **Store:** Filter by target app stores such as App Store Connect, Google Play Store, Microsoft Intune or Huawei AppGallery.
- **Email:** Filter by the email address of the user who initiated the publish process.
- **Profile Name:** Filter by the name of the Publish profile.
- **App Name:** Filter by the application name that was used in the Publish action.
- **Status:** Filter by Status of the Publish such as Success, Failed or Canceled.

<Screenshot url="https://cdn.appcircle.io/docs/assets/7112-5.png" />

:::info
In the filter options, you can only view and select the organization and sub-organization you belong to.
:::

<CSVExport />