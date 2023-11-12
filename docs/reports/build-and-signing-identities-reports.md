---
title: Build and Signing Identities Reports
metaTitle: Build and Signing Identities Reports
metaDescription: Build and Signing Identities Reports
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Build and Signing Identities Reports

## Build History

This report is accessible from the Build module.

Build History Report contains the list of build sessions initiated in a given time period.

Each build session is defined as an initiated manual or automatic build for a commit under a branch of a build profile.

The duration indicates the minutes spent by the build agent for the specified build operation. This value only includes the actual duration that the agent was active, including the agent boot duration but excluding the queue wait duration.;

The date and time are displayed in the current timezone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (11).png' />

## Signing History

This report is accessible from the Signing Identities module.

The Signing History Report contains the list of builds selected for signing in a given time period.

<ContentRef url="/signing-identities/">Signing Identities</ContentRef>

Each signed build is listed with the utilized provisioning profile name for iOS and the utilized keystore name for Android.;

Since the primary objective of this report is to provide visibility on who used which signing identity and when this report includes all builds that consumed a signing identity from the centralized Signing Identities module regardless of the status of the build or the signing operation. (e.g. if the build failed for some reason or if the signing identity is incompatible with the selected project)

The date and time are displayed in the current timezone.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (12).png' />
