---
title: Check App Store Release Status
description: Learn how to get approval from TestFlight in Appcircle
tags: [application, app store, app store connect, app store version, app store status]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Check App Store Release Status

With Appcircle's **Check App Store Release Status** component, you can get the status information of your published application, bind this step to a condition according to the status, and check and run your flow.

### Prerequisites

Below are the prerequisite steps necessary for this operation, accompanied by their descriptions.

:::caution

This is a standalone step. The steps listed below should precede this step if they are part of your Publish Flow.

:::

| Prerequisite Workflow Step                                                                                           | Description                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**App Information from App Store**](/publish-integrations/ios-publish-integrations/app-information-app-store)       | This step compares the Release Candidate version with the TestFlight and the App Store versions.                                          |
| [**Sent to Testflight**](/publish-integrations/ios-publish-integrations/send-to-app-store)                           | This step allows you to submit your application to TestFlight.                                                                            |
| [**Get Approval from TestFlight**](/publish-integrations/ios-publish-integrations/approval-test-flight)              | This step checks the TestFlight status of your application and advances the Publish Flow according to the specified acceptance condition. |
| [**Add for Review on App Store Connect**](publish-integrations/ios-publish-integrations/add-for-review-on-app-store) | This step checks the Release status of your application and advances the Publish Flow according to the specified acceptance condition.    |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2915-checkReleaseStatus.png' />

### Input Variables

Below are the parameters necessary for this step's operation, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2915-checkReleaseDetails.png' />

:::caution Success Statuses

For this step to work depending on a condition, a valid status must be given. You can give more than one status by putting commas between them. Some statuses that can be given are listed below. For more information, please see the Apple documentation [**here**](https://developer.apple.com/help/app-store-connect/reference/app-and-submission-statuses/).

Note: A few status are shown below as examples. For this step to be successful, if the status of the version on App Store Connect matches one or more of the given statuses, the step will be considered successful. 

- **PREPARE_FOR_SUBMISSION**: Version ready for submission to review.
- **READY_FOR_REVIEW**: Version ready to be submitted, waiting for submission.
- **WAITING_FOR_REVIEW**: Version submitted, waiting for review.
- **IN_REVIEW**: Version is being reviewed.
- **READY_FOR_SALE**: Version review was successful, released on App Store.

:::

| Variable Name         | Description                                                                                                                  | Status   |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_SUCCES_STATUSES` | Specifies the release status that has requirements for successful completion. For example: `WAITING_FOR_REVIEW`, `IN_REVIEW` | Required |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-publish-appstore-status-check