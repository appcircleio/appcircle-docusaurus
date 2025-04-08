---
title: Metadata Approval
description: Learn how to use Metadata Approval in Publish
tags: [publish, metadata, approve]
---

import Screenshot from '@site/src/components/Screenshot';

# Metadata Approval

The Metadata Approval step is used to get email-based approval before publishing your app's metadata. This ensures that designated users can review and either approve or reject the App Store metadata before proceeding with the publishing step.

This step is useful in team environments where metadata needs to be validated manually before release.

--screenshot--

When this step runs in your workflow, Appcircle sends a unique approval email to the recipients defined in the step inputs. The email contains a secure link to a dedicated Metadata Approval Panel, which allows recipients to:

- View the metadata details
- Approve or reject the metadata
- Provide feedback in case of rejection

--screenshot--

💡 The Metadata Approval Panel is only accessible via the link in the email and is not listed in the Appcircle dashboard.

### Input Variables

--screenshot--

| Field                        | Description                                                                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **All Required Approval Emails** | List of email addresses that **must** approve the metadata. If any of these reject or don't approve, the step fails. <br />Example: `info@appcircle.io` |
| **Optional Emails to Approve**   | Additional email addresses that can optionally approve. Their approvals contribute to the total approval count. <br />Example: `support@appcircle.io, team@appcircle.io` |
| **Minimum Required Approval Count** | The minimum number of total approvals (required + optional) needed for the step to be considered successful. <br />Example: `2`                      |

### Approval Process
1. Emails are sent to the recipients with a private link to the approval panel.
2. Recipients click the link and are directed to the Metadata Approval Panel.
3. If the user is not logged in, they are redirected to the login screen first and then returned to the panel.
4. Users can either:
- ✅ Approve the metadata
- ❌ Reject the metadata and provide a Rejection Message

--screenshot--

:::info Successful Approval
The step is marked as successful if:
- All required email addresses approve the metadata.
- The minimum required approval count is satisfied.
  :::

--screenshot--

:::warning
Please note that after a Metadata gets the approval, you will not be able to edit it anymore.
:::

#### Rejection Feedback
- When a rejection occurs, the rejecting user is asked to provide a Rejection Message.
- This message is included in the step logs for an easy review.
- The app version will also be tagged with `metadata rejected` in the Appcircle dashboard.

--screenshot--

### Output Variables

**Metadata Approval** step does not produce any output, but the success or failure of the step depends on the approvals or rejections received from the sent emails. This outcome affects the subsequent steps in the [Publish flow](/publish-module/publish-flow).