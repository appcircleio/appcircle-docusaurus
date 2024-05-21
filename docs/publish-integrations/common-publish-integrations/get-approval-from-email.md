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

If some optional users reject, but there is still a chance to achieve the minimum approval count, the step will remain in `Waiting` status, awaiting responses from other users. For instance, if the minimum approval count is set to 3, and there are a total of 10 users with only one required user, even if 7 non-required users reject, there is still a possibility of obtaining approval from the remaining 3 users. However, if 8 non-required users reject, the step will fail, as the minimum requirement of 3 approvals cannot be fulfilled anymore.

:::info

Once a user makes a decision, it cannot be changed unless the step is restarted, even if the user sees the "Thank you" page. The step must be restarted to allow the user to make a new decision.

When the step restarts or begins, all answers will be reset to `Waiting`, and users must provide their answers again. Consequently, they will receive approval emails again.

:::

### Prerequisites

There are no required steps that must precede the **Get Approval via Email** step. However, please note that any steps executed before the **Get Approval via Email** step in the Publish flow will not be impacted by the approval process. The approval logic will only affect the steps that follow the **Get Approval via Email** step.

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

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-email-send.git