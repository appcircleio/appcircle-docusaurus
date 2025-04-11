---
title: Metadata Approval
description: Learn how to use Metadata Approval in Publish
tags: [publish, metadata, approve]
---

import Screenshot from '@site/src/components/Screenshot';

# Metadata Approval

The Metadata Approval step is used to get email-based approval before publishing your app's metadata. This ensures that designated users can review and either approve or reject the App Store, Google Play, Microsoft Intune and Huawei AppGallary metadata before proceeding with the publishing step.

This step is useful in team environments where metadata needs to be validated manually before release.

When this step runs in your workflow, Appcircle sends a unique approval email to the recipients defined in the step inputs. The email contains a secure link to a dedicated Metadata Approval Panel, which allows recipients to:

- View the metadata details
- Approve or reject the metadata
- Provide feedback in case of rejection

:::caution Metadata Approval Panel

Access to the Metadata Approval Panel is **exclusively** available via the link sent in the approval email; it is **not** accessible through the standard Publish module UI.

:::


### Prerequisites

This step is one of the dependent steps. The table below lists the dependent steps with their descriptions.

| Prerequisite Workflow Step                                                                                                                  | Description                                                                                                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Update Metadata on Microsoft Intune**](/publish-integrations/common-publish-integrations/update-metadata-on-microsoft-intune) | This step uploads all edited metadata information from the [**Metadata Information**](/publish-module/publish-information/meta-data-information#microsoft-intune-metadata-information) page to the corresponding sections on Microsoft Intune. Ensure the [**Microsoft Intune API Key**](/account/my-organization/security/credentials/adding-microsoft-intune-api-key) is added to Appcircle and selected. |
| [**Update Metadata on App Store Connect**](/publish-integrations/ios-publish-integrations/update-metadata-on-app-store-connect) | This step uploads all edited metadata information from the [**Metadata Information**](/publish-module/publish-information/meta-data-information#ios-metadata-information) page to the corresponding sections on App Store Connect. Ensure the [**App Store Connect API Key**](/account/my-organization/security/credentials/adding-an-app-store-connect-api-key) is added to Appcircle and selected. |

:::caution Prerequisites

Please note that the **Metadata Approval** step **must** be used before the steps listed in the table above. 

Running **Metadata Approval** step after your updated metadata has been applied in your developer accounts may **cause unexpected errors** in your publish flows.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-metadataApprovalNew1.png'/>

### Input Variables

The parameters required for this step to work as expected are listed below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish3.png'/>

| Field                        | Description                                                                                                                                      |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **All Required Approval Emails** | List of email addresses that **must** approve the metadata. If any of these reject or don't approve, the step fails. <br />Example: `info@appcircle.io` |
| **Optional Emails to Approve**   | Additional email addresses that can optionally approve. Their approvals contribute to the total approval count. <br />Example: `support@appcircle.io, team@appcircle.io` |
| **Minimum Required Approval Count** | The minimum number of total approvals (required + optional) needed for the step to be considered successful. <br />Example: `2`                      |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish7.png'/>

:::caution Minimum Approval Count
If the Minimum Required Approval Count cannot be achieved, the step will fail.

For example, if the Minimum Required Approval Count is set to 3 and there are a total of 3 users, all recipients will need to approve the metadata. 

Please note that required approval email users take priority in this case, as all of them must approve—even if the minimum requirement is already met by optional users.
:::

## Approval or Rejection Process

### Approval

To approve a metadata, follow the steps below:

1. Emails are sent to the recipients with a private link to the approval panel.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish1.png'/>

2. Recipients click the link and are directed to the Metadata Approval Panel.
3. If the user is not logged in, they are redirected to the login screen first and then returned to the panel.
4. The user can approve the metadata by clicking the **Approve** button in the panel that opens.

:::caution Metadata Approval Panel

Please note that all of the data displayed in the metadata approval panel is **read‑only**. No values can be changed within this panel.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish5.png'/>

:::info Successful Approval

**The step is marked as successful if:**

- All required email addresses approve the metadata.
- The minimum required approval count is satisfied.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish6.png'/>

:::warning Lock/Unlock Rules for Metadata Update 

Please note that in order to make any updates within [**Metadata Details**](/publish-module/publish-information/meta-data-information), certain rules must be met. While the Publish Flow is running, Metadata Details are locked and no changes are permitted. Please pay close attention to the business rules outlined below.

**Metadata will be locked when:**
- the **Metadata Approval** step starts, is in progress, or is completed
- the **[Update Metadata on App Store Connect](/publish-integrations/ios-publish-integrations/update-metadata-on-app-store-connect)/Google Play Console** step starts

**Metadata will be unlocked when:**
- the **Metadata Approval** step completes with a status of `Failed` or `Stopped`
- the **[Update Metadata on App Store Connect](/publish-integrations/ios-publish-integrations/update-metadata-on-app-store-connect)/Google Play Console** step completes with a status of `Success`, `Failed`, or `Stopped`
- the Publish Flow completes

:::

### Rejection

When a user wants to reject a metadata, they can reject by clicking the **Reject** button on the metadata approval panel that opens. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish5.png'/>

**When a rejection occurs;**

- The rejecting user is asked to provide a **Rejection Message**.
- This message is included in the **step logs** for an easy review.
- The app version will also be tagged with `Metadata Rejected` in the Publish profile dashboard.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5906-publish4.png'/>

## Output Variables

**Metadata Approval** step does not produce any output, but the success or failure of the step depends on the approvals or rejections received from the sent emails. This outcome affects the subsequent steps in the [Publish flow](/publish-module/publish-flow).