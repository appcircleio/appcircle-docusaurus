---
title: Reporting
description: Access download activity reports to monitor application downloads from Testing Distribution.
tags:
  - reports
  - download reports
  - testing distribution
  - analytics
  - tracking
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/_csv-export.mdx';

# Download Reports

The Download Reports page provides visibility into application download activity within Testing Distribution. It helps organizations track which app versions have been downloaded, when the downloads occurred, and which devices and operating system versions were used.

You can access Download Reports from the **Testing Distribution > Download Reports** section.

## Overview

The Download Reports page lists download events for applications distributed through the Testing Portal.

<Screenshot url='https://cdn.appcircle.io/docs/assets/qa55-new.png' />

Each record includes:

- User
- App name
- Distribution profile name
- App version
- Device platform
- Operating system version
- Download date and time

The summary section at the top of the page displays:

- **Total Apps**: The number of unique applications downloaded during the selected period.
- **Total Downloads**: The total number of download events recorded during the selected period.

The date and time are displayed in the current timezone.

## Filtering Reports

Download records can be filtered by date range to help you analyze download activity for a specific period.

The report is automatically updated when filters are applied.

<Screenshot url='https://cdn.appcircle.io/docs/assets/qa55-new2.png' />

:::info Public Link Downloads
When an application is downloaded through an email invitation, the user information is associated with the recipient and displayed in the **User** column.

If the application is downloaded using a **Public Link**, the downloader cannot be identified individually. In such cases, the **User** column displays: N/A
:::

<CSVExport />