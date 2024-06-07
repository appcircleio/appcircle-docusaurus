---
title: History
description: Learn how to access and review the History for Publish History and Resign History in Appcircle
tags: [publish history, publish module, publish information, resign history, history]
sidebar_position: 4
---

# History

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The History section has two parts: The Publish History and The Resign History.

The Publish History section is a record of all the publishing actions that have been performed for different versions of an application. It serves as a log for tracking the deployment lifecycle of each release.

The Resign History section is a record of all the resign actions that have been performed within the Publish module for a specific app version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub4.png' />

## Overview

Once you select the History section you can access both the Publish History and the Resign History.

You can access the Publish History to gain insight into the sequence of events for each published version. It is an invaluable tool for auditing, troubleshooting, and understanding the timeline of version deployments.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub5.png' />

You can also access the Resign History for an app version by navigating to it's tab to monitor the resign actions for that specific version.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub9.png' />

### Accessing Publish History

To view the Publish History, navigate to the History section in the Publish module. Once History is selected, The Publish History tab will be displayed by default. This section lists all versions of the app along with the dates and times their publishing actions started.

### Viewing Logs

- **Description:** Each entry in the Publish History is clickable and will provide a detailed log of the publish action.
- **Purpose:** These logs contain information about the start time, the steps executed during publishing, any issues encountered, and the eventual success or failure of the publish action.

### Example Entry

Here is an example of what an entry in the Publish History might look like:

- **Current Tag:** Indicates the version is the most recent one that has been published.
- **Start Date:** Shows the date and time when the publish action for this version commenced.

### Log Details

Upon selecting a specific version, you will be presented with a detailed log. This log may include:

- The initiation of the publish action.
- Progress updates through various stages of the process.
- Any warnings or errors that were logged.
- The completion status of the publish action.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-log.png' />

### Best Practices

- **Regular Reviews:** It is recommended to review the Publish History regularly to monitor the health and status of your publishing pipeline.
- **Error Handling:** In the case of a failed publish action, use the detailed logs to identify and troubleshoot the issue.
- **Record Keeping:** Keep records of your Publish History for compliance purposes and to maintain a historical reference.

---

The Publish History is a key feature that provides transparency and traceability in the application deployment process. By regularly reviewing this section, you can ensure that your publish actions are performing as expected and maintain a high level of quality control over your release management process.

### Accessing Resign History

To view the Resign History, navigate to the History section in the Publish module, then simply select the Resign History tab.

### Viewing Logs

Each signing process will be listed for that binary. If you click on the displayed resign action , you can get more details about the process by seeing the logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub9.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub10.png' />

:::info

You need the check the history of the original application that has been signed.

:::

<ContentRef
url="/publish-module/publish-information/resign-binary">
Read more about Resign Binary
</ContentRef>