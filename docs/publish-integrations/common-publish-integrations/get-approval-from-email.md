---
title: Get Approval via Email
description: Learn how to Get Approval via Email in Publish
tags: [publish, email publish, approve]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Get Approval via Email

The **Get Approval via Email** step allows you to get approval from the email addresses entered as input in the step before moving on to the next steps in Publish.

Based on your business requirements, you can designate certain email addresses to require approval, specify others as optional approvers, or set a minimum number of approvals needed from the provided email addresses.

If some optional users reject the request but there is still a chance to achieve the minimum approval count, the step will remain in `Waiting` status, awaiting responses from other users. For instance, if you set the minimum approval count to 3, and out of 10 users, only one is required, the step can still succeed. Even if 7 optional users reject, approval can still be obtained from the remaining 3 users. However, if 8 optional users reject, the step will fail, as it will no longer be possible to meet the minimum requirement of 3 approvals.

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-publishflow-components-approval-email-1.png'/>

:::info

Once a user makes a decision, it cannot be changed unless the step is restarted, even if the user sees the "Thank you" page. The step must be restarted to allow the user to make a new decision.

Upon restarting or initiating the step, it resets all answers to `Waiting`. Users must then provide their answers again and will receive new approval emails.

:::

### Prerequisites

There are no required steps that must precede the **Get Approval via Email** step. However, please note that any steps executed before the **Get Approval via Email** step in the [Publish flow](/publish-module/publish-flow) will not be impacted by the approval process. The approval logic will only affect the steps that follow the **Get Approval via Email** step.

### Input Variables

The parameters required for this step to work as expected are listed below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-publishflow-components-approval-email.png'/>

| Variable Name                  | Description                                                                                                                                                                                                                                        | Status   |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| `$AC_APPROVAL_EMAILS`          | The **All Required Approval Emails** specify the required email addresses, separated by commas, to which special approve and reject links will be sent. All email addresses in this field must be approved for this step to be successful. If one of the required users rejects it, the step will fail. The count of emails cannot be less than the **Minimum Required Approval Count**.                    | Optional |
| `$AC_OPTIONAL_APPROVAL_EMAILS` | The **Optional Required Approval Emails** specify optional email addresses, separated by commas, to which special approve and reject links will be sent. Optional approval emails may need to be approved if the **Minimum Required Approval Count** is lower than the count of **All Required Approval Emails**.                            | Optional |
| `$AC_MINIMUM_APPROVAL_COUNT`   | The **Minimum Required Approval Count** specify the minimum number of required email approvals. The total of required and optional email approvals must be equal to or greater than this number. The step will not succeed unless the minimum number of approvals is fulfilled.                                                     | Required |


:::warning

If the **Minimum Required Approval Count** cannot be achieved, the step will fail. For example, if the **Minimum Required Approval Count** is set to 3 and there are a total of 3 users, if one of them rejects, the minimum count cannot be met because only 2 users with approval rights remain.

:::

### Output Variables

**Get Approval via Email** step does not produce any output, but the success or failure of the step depends on the approvals or rejections received from the sent emails. This outcome affects the subsequent steps in the [Publish flow](/publish-module/publish-flow).

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-email-send.git