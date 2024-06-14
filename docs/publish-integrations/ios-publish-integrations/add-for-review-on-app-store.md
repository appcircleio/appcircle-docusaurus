---
title: Add for Review on App Store
description: Boost your app's visibility by submitting for review on the App Store. Ensure quality, reach more users, and enhance credibility with our expert guidance.
tags: [application, app store, app store connect, app store version]
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# Add for Review on App Store

Appcircle Publish Module isolates the user to a great extent in the App Store Connect interface with its steps. In this way, you can manage your publish process from a single place. With the Add for Review on App Store step, you can send your application version in TestFlight directly to the review.

:::caution Add for Review on App Store

When this step works, Appcircle will directly submit the relevant version for review. 

For this reason, if there is an error in your [**Metadata Information**](/publish-module/publish-information/meta-data-information) or [**App Information**](/publish-module/publish-information/app-information) details, the step will fail.

:::

### Prerequisites

In order for this step to work, the following steps must be present before this step.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Send to TestFlight**](/publish-integrations/ios-publish-integrations/sent-to-testflight) | This step allows you to submit your application to TestFlight. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3926-submissionOrder.png' />

:::danger Prerequisites

When this step runs, Appcircle will first search for the relevant version match on **TestFlight**. When the relevant version match is provided, the binary will be sent directly to review.

For this reason, the binary file must be present on **TestFlight**.

:::


### Input Variables

Below are the parameters necessary for this step's operation, along with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3926-submissionInput.png' />


| Variable Name                 | Description                         | Status           |
|-------------------------------|-------------------------------------|------------------|
| `$AC_XCODE_LIST_DIR`          | Specifies the Xcode folder list directory. Current Xcode folder structure examples: `/Applications/Xcode/14.3/Xcode` or `/Applications/Xcode/15.0/Xcode`. | Optional |
| `$AC_XCODE_VERSION`           | Specifies the Xcode version. | Required |
