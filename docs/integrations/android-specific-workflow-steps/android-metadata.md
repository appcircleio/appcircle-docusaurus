---
title: Android Metadata
metaTitle: Android Metadata
metaDescription: Android Metadata
sidebar_position: 15
---

import Screenshot from '@site/src/components/Screenshot';

# Android Metadata
The **Android Metadata** step enables the detection of application [modules](https://developer.android.com/studio/projects#ApplicationModules) and [build variants](https://developer.android.com/build/build-variants) within your Android project.

Example of metadata output:

```json
{
  "modules": [
    {
      "modulePath": ".",
      "module": "app",
      "variants": [
        "release",
        "debug"
      ]
    }
  ]
}
```

### Prerequisites
The workflow steps that need to be executed before running the **Android Metadata** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                       | Description                                      |
 |-------------------------------------------------|--------------------------------------------------|
 | [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) | This step requires the project to be cloned from a Git provider before metadata will be generated. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-metadata_1.png'/>

### Input Variables
For each step, specific input variables are required for its operation on your system. The input variables necessary for the **Android Metadata** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-metadata_2.png'/>

| Variable Name              | Description                                    | Status |
|----------------------------|------------------------------------------------|--------|
| `$AC_REPOSITORY_DIR`       | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) step, the variable will be automatically populated. | Required |

# Output Variables
The outputs that can result from the operation of this component are listed as follows:

| Variable Name              | Description                                    |
|----------------------------|------------------------------------------------|
| `$AC_METADATA_OUTPUT_PATH` | This variable represents the path of the `metadata.json` file. The default value is `AC_TEMP_DIR`.

:::caution
 If there is an output generated, ensure to use the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts) step afterward to ensure it is included in the [**Download Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts/#download-exported-artifacts) page.
:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-metadata-component.git