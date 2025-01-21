---
title: Lint
description: Learn how to use the Android Lint workflow step in Appcircle
tags: [android, mobile, lint]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Lint

[Android Lint](https://developer.android.com/studio/write/lint) is a static analysis tool provided by the Android SDK that helps identify potential issues in Android projects. It scans the source code for common programming errors, performance optimizations, usability issues, and other problems. **Android Lint** can detect a wide range of issues, such as unused resources, layout performance problems, memory leaks, and security vulnerabilities.

This step is used to run Lint Gradle tasks in your project via Appcircle.

### Prerequisites

Before running the **Android Lint** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                        | Description                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | To start the **Android Lint** process, the repository that needs to be built must be fetched from the branch. This generates the `$AC_REPOSITORY_DIR` variable, which is then used as the input for the **Android Lint** step. |

:::caution

Please ensure that you insert the **Android Lint** step before using the **Android Build** step.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lint_1.png' alt="image2" />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lint_2.png' alt="image2" />

| Variable Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR` | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](/workflows/common-workflow-steps/git-clone) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`         | This variable specifies the project module to be built. This variable can also be set via the build [Configuration](/build/build-process-management#profile-configuration). In Android Studio, you can locate the available modules for your project. For more information, please refer to this [Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_VARIANTS`       | This variable specifies the project variant to be built. This variable can also be set via the build [Configuration](/build/build-process-management#profile-configuration). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants).               | Required |
| `$AC_PROJECT_PATH`   | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path.                                                                                                                                                                                                                           | Optional |

:::info

If you have filled in the required variables in the **Configuration** section, you will not need to redefine these variables again on the [**Workflows**](/workflows/). For more information about configurations, refer to the [Build Profile Configuration Overview](/build/build-process-management#profile-configuration) document.

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lint_3.png' alt="Configuration Image" />

1. The input corresponds to the 1st field: `$AC_MODULE`
2. The input corresponds to the 2nd field: `$AC_VARIANTS`

:::

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-lint_4.png' alt="image2" />

| Variable Name | Description                                                                                                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-`           | Lint does not assign the XML/HTML file output to a variable. However, the resulting file from **Lint** appears in the output (`$AC_OUTPUT_DIR`) and report directory (`<gradlew folder path>/$AC_MODULE/build/reports`). |

:::caution

To view the Lint report on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts/#download-exported-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps#export-build-artifacts) step is included in your **Workflow** after this step.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-lint-component
