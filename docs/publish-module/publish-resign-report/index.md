---
title: Publish Re-sign Report
sidebar_position: 1
tags: [publish, report, re-sign]
description: Understand the Report for Publish Re-sign in Appcircle, providing visibility on the usage of re-sign operations within the publish module over a given time period.

---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/\_csv-export.mdx';

# Publish Re-sign Report

The Publish Re-sign Report provides detailed visibility into the manual and automatic re-sign operations performed within the publish module. This report helps you monitor and analyze re-sign activities across your organization over a selected time period.

<Screenshot url="https://cdn.appcircle.io/docs/assets/7112-9.png" />

These are the displayed fields within the Publish Report:

- Org Name
- Profile Name
- Platform
- Source Binary
- Target Binary
- Status
- Initiated By
- Trigger Type
- Start Date
- Duration

## Filtering Options

Users can refine the report data using multiple filters:

- **Date Range:** Select specific time periods to analyze publish re-sign activity.
- **Platform:** Filter by iOS or Android
- **Trigger Type:** View actions triggered manually or automatically.
- **Email:** Filter by the email address of the user who initiated the publish process.
- **Profile Name:** Filter by the name of the Publish profile.
- **App Name:** Filter by the application name that was used in the Publish action.
- **Status:** Filter by Status of the Publish such as Success, Failed or Canceled.

<Screenshot url="https://cdn.appcircle.io/docs/assets/7112-8.png" />

:::info
In the filter options, you can only view and select the organization and sub-organization you belong to.
:::

:::warning
Please note that the Publish Re-sign Report displays only the re-sign operations that were triggered in the Publish module.
:::

<CSVExport />