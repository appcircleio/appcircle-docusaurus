---
title: Signing History
description: Understand the Signing History Report in Appcircle, providing visibility on the usage of signing identities over a given time period.
tags: [reports, signing history, signing identities, testing]
---

# Signing History

This report is accessible from the Signing Identities module.

The Signing History Report contains the list of builds selected for signing in a given time period.

<ContentRef url="/signing-identities/">Signing Identities</ContentRef>

Each signed build is listed with the utilized provisioning profile name for iOS and the utilized keystore name for Android.;

Since the primary objective of this report is to provide visibility on who used which signing identity and when this report includes all builds that consumed a signing identity from the centralized Signing Identities module regardless of the status of the build or the signing operation. (e.g. if the build failed for some reason or if the signing identity is incompatible with the selected project)

The date and time are displayed in the current timezone.

You can filter the report pages according to the organization.

:::info
In the filtering options, you can only view and select the organization and sub-organization you belong to.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/signing-history-new.png' />
