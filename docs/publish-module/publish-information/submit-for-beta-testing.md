---
title: Submit for Beta Testing
description: Learn how to submit apps for beta testing on App Store Connect in Appcircle
slug: /publish-to-stores-module/publish-information/submit-for-beta-testing
tags: [publish, publish details, publish flow, beta, submit]
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

# Submit for Beta Testing

The **Submit for Beta Testing** feature allows users to manage TestFlight beta distributions directly from the Publish Dashboard without running a new build pipeline.

With this feature, Release Managers can:

- View the current testing status of binaries in TestFlight
- Submit builds to Internal and External TestFlight groups
- Manage beta distributions directly from the Publish Dashboard
- Track detailed submission results through Activity Logs and Reports

## Testing Status

The **Testing Status** tab provides visibility into binaries that are currently assigned to TestFlight testing groups.

This tab displays testing-related statuses such as:

- Ready to Submit
- Approved
- In Testing

The information shown in this section is based on the TestFlight Beta Information available on App Store Connect.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8766-3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8766-4.png' />

## Submit for Beta Testing

The **Submit for Beta Testing** action is available from the binary action menu.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8766-1.png' />

This option is only visible for binaries that are in a status eligible for beta submission. Binaries that are not ready for beta testing will not display this action.

Using this screen, users can:

- Assign a build to one or multiple Internal TestFlight groups
- Assign a build to External TestFlight groups
- Manage beta testing distributions without rebuilding the application

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8766-2.png' />

## Release Notes for External Testers

When submitting a build to External TestFlight groups, users can provide release notes with language support.

These release notes are shared with external testers through TestFlight.


:::info Partial Success Handling

Beta submissions may complete partially successfully.

For example, if a build is submitted to multiple beta groups and Apple rejects one of the groups due to validation or compliance requirements, the build can still be assigned successfully to the remaining groups.

Failed group assignments are displayed in the Activity Logs with detailed error information.
:::