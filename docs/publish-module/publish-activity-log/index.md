---
title: Publish Activity Log
sidebar_position: 1
tags: [publish, activity log, search]
description: Understand the Activity Log for Publish in Appcircle, providing visibility on the usage of Publish to Stores module over a given time period.

---

import Screenshot from '@site/src/components/Screenshot';
import CSVExport from '@site/docs/\_csv-export.mdx';

# Activity Log

You can view Publish to Stores module actions such as Publish Flow and Publish Step statutes, along with resign binary operations within the Organizations or Sub Organizations in the Activity Log section.

<Screenshot url='https://cdn.appcircle.io/docs/assets/7112-11.png' alt="Activity Log for Publish" />

Here is the full list of actions that can be monitored:

- Profile Created
- Profile Deleted
- Publish Step Starting
- Publish Step Started
- Publish Step Success
- Publish Step Failed
- Publishing Failed
- Publishing Stopped
- Publishing Success
- Publishing Success Without Artifacts
- Publishing Restarted
- Publishing Restart Cancelled
- Play Store Release Updated
- Play Store Release Update Failed
- Metadata File Deleted
- Metadata Imported
- Metadata Updated
- Metadata Importing
- Publish Item Archived
- Publish Flow Updated
- Marked as Release Candidate
- Unmarked as Release Candidate
- App Version Uploaded
- App Version Created
- App Version Deleted
- Resign Success
- Resign Failed
- Resign Cancelled
- Release Notes Updated
- App Info Store Update Failed
- App Info Store Update Succeeded
- App Info Store Update Partially Failed
- App Version Rejected
- Review Submission Cancelled

:::caution

Only Organization / Sub-Organization Owners and users with Organization Management Role will have access to this area.

Information about other Organizations and their Sub-Organizations will not be accessible without the required level of clearance.

:::

:::info

Organization Owners can also observe the actions of their Sub-Organizations.

:::

You can edit the required date range by clicking the time filter in the top filter header as the default search time option is the last 30 days. Alternatively, you can choose custom dates from the calendar by selecting 'In Between' option.

Another method to search is by **Actions**. Simply click the filter option and select **Actions**. Then you can choose a specific action to refine your search.

<Screenshot url='https://cdn.appcircle.io/docs/assets/7112-12.png' alt="Filtering Activity Log for Publish" />

<CSVExport />