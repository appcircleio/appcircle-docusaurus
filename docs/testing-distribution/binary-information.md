---
title: Testing Distribution Binary Information
description: Learn how to use Binary Information on a Testing Distribution profile in Appcircle
sidebar_label: Binary Information
tags: [testing distribution, binary information]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Binary Information

This window provides information about your binary, including the provisioning profile type, certificate name, and build details, such as the branch and logs. Also you can compare the current binary with another one of your choice.

1. Select the binary.

You can select the files from the list.

2. Click the **...** button and select **Binary Information**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE8124-14.png' />

3. This window provides information about your binary, including the provisioning profile type, certificate name, and build details, such as the branch and logs.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA-48-td.png' />

#### Build Metadata Details

The following metadata is displayed in the Binary Information section of a Testing Distribution Profile only when the binary is generated via the Build Module, either through automatic or manual triggers, and subsequently distributed using Auto Distribution to the Testing Distribution module.

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA-48-td3.png' />

- **Trigger Type**: Indicates what initiated the build. Possible values include:

1. Pull Request: The build was triggered by the creation or update of a pull request.
2. User: A build was manually triggered by a user.
3. Commit: A new commit triggered the build automatically.
4. Tag: The build was initiated when a new Git tag was pushed to the repository.

- **Branch Name**: The source branch used during the build process.
- **Target Branch**: Typically used in pull request or merge-based triggers, this is the destination branch for the pull request or merge target.
- **Git Tag**: If the trigger type is Tag, this field shows the tag that initiated the build.
- **Triggered Internal User**: Displays the email address of the internal user who triggered the build or the user responsible for the action.
- **Workflow Name**: The name of the workflow profile name executed during the build process (e.g., Default Push Workflow).
- **Config Name**: Indicates the configuration profile name used within the selected workflow (e.g., Default Configuration).

### Binary Comparison

In the top-right corner of the Binary Information screen, you can click the **Compare** button to compare the current binary with another of your choice. The comparison highlights differences between the two binaries using color-coded indicators for easy identification.

:::caution Build Details Comparison

Binaries generated through the Appcircle Build Module include associated build details. **However**, if the compared binary was **manually** uploaded to Appcircle, those details **will not be available** for comparison.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/QA-48-td4.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/QA-48-td2.png' />
