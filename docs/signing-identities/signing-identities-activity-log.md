---
title: Activity Log
description: Understand the Activity Log for Signing Identities in Appcircle, providing visibility on the usage of signing identities module over a given time period.
tags: [activity log, signing identities]
sidebar_position: 7
---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/\_csv-export.mdx';

# Activity Log

You can view Signing Identity module actions such as creating, deleting, and adding Apple Certificates or Android Keystores to Organizations or Sub Organizations in the Activity Log section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/7112-1.png' />

Here is the full list of actions that can be monitored:

- P12 Added
- Csr Generated
- Certificate Uploaded 
- Certificate Will Expire
- Certificate Downloaded
- Certificate Deleted
- Provisioning Profile Deleted
- Provisioning Profile Added
- Provisioning Profile Renewed
- Provisioning Profile Downloaded
- Provisioning Profile Will Expire
- Keystore Created
- Keystore Uploaded
- Keystore Deleted
- Keystore Downloaded
- Keystore Will Expire
- App Store BundleIdentifier Created
- App Store BundleIdentifier Deleted
- App Store BundleIdentifier Created In App Store
- App Store BundleIdentifier Updated In App Store
- Tester Devices Added
- Tester Device Deleted
- Tester Device Invitation Deleted
- Device Provisioned
- Device Provision Failed
- Device Registration Link Sent
- Device Registered
- Multiple Devices Registered
- Multiple Device Registration Failed
- App Store Authentication Failed
- App Store Device Synced
- App Store Device Sync Cancelled
- Add Multiple Devices To App Store Request
- Apple Device Updated
- Apple Device Update Failed
- Apple Multiple Device Updated
- Apple Multiple Device Update Failed

:::caution

Only Organization / Sub-Organization Owners and users with Organization Management Role will have access to this area.

Information about other Organizations and their Sub-Organizations will not be accessible without the required level of clearance.

:::

:::info

Organization Owners can also observe the actions of their Sub-Organizations.

:::

You can edit the required date range by clicking the time filter in the top filter header as the default search time option is the last 30 days. Alternatively, you can choose custom dates from the calendar by selecting 'In Between' option.

Team activity logs also include filters to help users perform more precise searches. By clicking the 'All' option next to Organizations, you can select a specific organization or sub-organization from the list, provided you have access to monitor their signing identities activity.

<Screenshot url='https://cdn.appcircle.io/docs/assets/7112-1.png'/>

Another method to search is by **Actions**. Simply click the filter option and select **Actions**. Then you can choose a specific action to refine your search.

<CSVExport />