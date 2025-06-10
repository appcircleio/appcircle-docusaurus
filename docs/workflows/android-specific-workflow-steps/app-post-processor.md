---
title: App Post-Processor
description: App Post-Processor step performs the necessary system operations to identify and process the Android output binary files.
tags: [android, mobile, post processor]
---

import Screenshot from '@site/src/components/Screenshot';

# Android App Post-Processor

This step performs the necessary system operations to identify and process the Android output binary files.

:::warning

This step also verifies whether the app is signed or not. If this step is not included in your workflow or if it is determined that there is no signed app as a result of this step, **the app cannot be distributed**.

:::

:::info Debug Variant Signing  

As noted in the [**Android Developer documentation**](https://developer.android.com/build/build-for-release):

> If the build variant you've selected is a debug build type, then the APK is signed with a debug key and it's ready to install. If you've selected a release variant, then, by default, the APK is unsigned and you must manually [sign the APK](https://developer.android.com/studio/publish/app-signing).

This means that when you build your app with the **debug** variant, the **Android Post Processor** step in Appcircle will recognize the app as already signed, even if it was not signed in Appcircle or your repository.

:::

### Prerequisites

The workflow steps that need to be executed before running the **Android App Post-Processor** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | This step relies on the **Android Build** step and the **Git Clone** step is necessary for the **Android Build** step to run successfully. |
| [**Android Build**](/workflows/android-specific-workflow-steps/android-build) | To process Android output, these outputs must be obtained from the build step. |
| [**Android Sign**](/workflows/android-specific-workflow-steps/android-sign) | If a signed app is created, this step needs to be run beforehand to process this output. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-post-processor_1.png' alt="image2" />

:::caution

If a step other than the **Android Build** or **Android Sign** step is used to build or sign the app, then the **Android App Post-Processor** step depends on this step.

:::

### Input Variables

There is no need to enter an input for this component. It will process Android files under the output directory (`$AC_OUTPUT_DIR`).

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-post-processor_2.png' alt="image2" />

| Variable Name                          | Description                                       |
|----------------------------------------|---------------------------------------------------|
| `AC_ANDROID_POST_PROCESS_OUTPUT_PATH` | Specifies the application post process file path. This file specifies the base name for each app and whether it is signed or not. |

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

To share the signed apps created as a result of this step or to view them on the **Download Artifacts** page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

---
To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-post-process-component.git