---
title: Distribution Activity Reports
metaTitle: Distribution Activity Reports
metaDescription: Distribution Activity Reports
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Distribution Activity Reports

## App Versions Report

This report is accessible from the Testing Distribution.

App Versions Report contains the list of binaries deployed to a distribution profile in a given time period.

<ContentRef url="/distribute/create-or-select-a-distribution-profile">
  Create a Distribution Profile and Sharing with Testers
</ContentRef>

Each version is defined as an app binary for iOS and Android deployed manually or automatically or uploaded directly to a distribution profile. Even if a binary is deleted, it will still be visible in this report.

The date and time are displayed in the current timezone.

You can filter the report pages according to the organization.

:::info
In the filtering options, you can only view and select the organization and sub-organization you belong to.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/app-version-new.png' />

## App Sharing Report

This report is accessible from the Testing Distribution.

App Sharing Report list of app versions sent to the testers in a given time period.

Each line indicates an individual share operation conducted using the "Share with Testers" feature manually or automatically along with the number of testers with whom the app is shared. The number of testers is not unique and specifies the number of recipients for that specific share operation.

The date and time are displayed in the current timezone.

You can filter the report pages according to the organization.

:::info
In the filtering options, you can only view and select the organization and sub-organization you belong to.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/app-sharing-new.png' />
