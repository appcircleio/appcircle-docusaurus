---
title: Android App Post-Processor
description: This step performs the necessary system operations to identify and process the Android output binary files.
tags: [android, mobile, post-processor]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Android App Post-Processor
This step performs the necessary system operations to identify and process the Android output binary files.

:::warning
This step also verifies whether the app is signed or not. If this step is not included in your Workflow or if it is determined that there is no signed app as a result of this step, __the app cannot be distributed__.
:::

### Prerequisites
The workflow steps that need to be executed before running the **Android App Post-Processor** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | This step relies on the **Android Build** step and the **Git Clone** step is necessary for the **Android Build** step to run successfully. |
| [Android Build](https://docs.appcircle.io/workflows/android-specific-workflow-steps#android-build) | To process Android output, these outputs must be obtained from the build step. |
| [Android Sign](https://docs.appcircle.io/workflows/android-specific-workflow-steps#android-sign) | If a signed app is created, this step needs to be run beforehand to process this output. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-post-processor_1.png' alt="image2" />

:::caution
If a step other than the **Android Build** or **Android Sign** step is used to build or sign the app, then the **Android App Post-Processor** step depends on this step.
:::

### Input Variables
There is no need to enter an input for this component. It will process Android files under the output directory (`$AC_OUTPUT_DIR`).

### Output Variables
The outputs that can result from the operation of this component are listed as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-post-processor_2.png' alt="image2" />

| Variable Name                          | Description                                       |
|----------------------------------------|---------------------------------------------------|
| `$AC_ANDROID_POST_PROCESS_OUTPUT_PATH` | Specifies the application post process file path. This file specifies the base name for each app and whether it is signed or not. |

:::info
The output post-processing JSON file should adhere to the following structure:
```jsx title="ac_post_process_output.json"
[
  {
    "signed": true|false, 
    "app_name": "app base name"
  },
  {...}
]
```
:::

:::caution
To share the signed apps created as a result of this step or to view them on the **Download Artifacts** page, please ensure that the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps#export-build-artifacts) step is included in your Workflow after this step.
:::

---
To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-build-component.git