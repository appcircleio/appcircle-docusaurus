---
title: Signing Reports
description: Understand the Signing Reports in Appcircle, providing visibility on the usage of signing identities over a given time period.
tags: [reports, signing reports, signing identities, testing]
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/\_csv-export.mdx';

# Signing Reports

This report is accessible from the Signing Identities module.

The Signing Reports section contains the list of builds selected for signing in a given time period.

Each signed build is listed with the utilized provisioning profile name for iOS and the utilized keystore name for Android, along with their build status.

Since the primary objective of this report is to provide visibility on who used which signing identity and when this report includes all builds that consumed a signing identity from the centralized Signing Identities module regardless of the status of the build or the signing operation. (e.g. if the build failed for some reason or if the signing identity is incompatible with the selected project)

The date and time are displayed in the current timezone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/7112-10.png' alt="Signing Reports" />

You can filter the report pages according to the organization.

:::info
In the filtering options, you can only view and select the organization and sub-organization you belong to.
:::

<CSVExport />