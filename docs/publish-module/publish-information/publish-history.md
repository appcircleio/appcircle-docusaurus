---
title: Publish History
description: Learn how to access and review the Publish History in Appcircle
tags: [publish history, publish module, publish information]
sidebar_position: 4
---

# Publish History

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

The Publish History section is a record of all the publishing actions that have been performed for different versions of an application. It serves as a log for tracking the deployment lifecycle of each release.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-button.png' />

## Overview

You can access the Publish History to gain insight into the sequence of events for each published version. It is an invaluable tool for auditing, troubleshooting, and understanding the timeline of version deployments.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-history-list.png' />

### Accessing Publish History

To view the Publish History, navigate to the corresponding section in the Publish module. This section lists all versions of the app along with the dates and times their publishing actions started.

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
