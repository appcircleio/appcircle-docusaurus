---
title: Android Dependency Report
description: Learn how to use the Android Dependency Report workflow step in Appcircle
tags: [android, mobile, dependency, report]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Dependency Report

The **Android Dependency Report** workflow step visualizes the whole dependency tree for every [configuration](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) available in the project.

Rendering the dependency tree is particularly useful if you’d like to identify which dependencies have been resolved at runtime. It also provides you with information about any dependency conflict resolution that occurred in the process and clearly indicates the selected version. The dependency report always contains declared and transitive dependencies.

### Prerequisites

Before running the **Android Dependency Report** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                            | Description                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/build/build-process-management/build-profile-configuration) | To initiate the **Android Dependency Report** process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the **Git Clone** step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for the **Android Dependency Report** step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-dependency-report_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-dependency-report_2.png' alt="image2" />

| Variable Name                  | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR`           | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](/build/build-process-management/build-profile-configuration) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`                   | This variable specifies the project module to be built. This variable can also be set via the build [Configuration](/build/build-process-management/build-profile-configuration). In Android Studio, you can locate the available modules for your project. For more information, please refer to this [Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_DEPENDENCY_CONFIGURATION` | Specifies the [configuration](https://docs.gradle.org/current/userguide/declaring_dependencies.html#sec:what-are-dependency-configurations) to resolve for displaying dependency information. The default value is: `implementation`.                                                                                                                                                                                  | Required |
| `$AC_PROJECT_PATH`             | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path. The default value is: `./`                                                                                                                                                                                                | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name                        | Description                                                            |
| ------------------------------------ | ---------------------------------------------------------------------- |
| `AC_ANDROID_DEPENDENCY_REPORT_PATH` | Specifies the path where the Android dependency report file is stored. |

:::danger

If you wish to review or download the **Android Dependencies Report**, you can find them directly from [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts). To do this, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step follows the **Android Dependency Report** workflow step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-dependency-report_3.png'/>

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-dependency-report.git
