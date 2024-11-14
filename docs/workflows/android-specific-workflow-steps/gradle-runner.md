---
title: Gradle Runner
description: The Gradle Runner workflow step executes the specified Gradle task provided by the user.
tags: [android, mobile, gradle]
---

import Screenshot from '@site/src/components/Screenshot';

# Gradle Runner

The **Gradle Runner** workflow step executes the specified [Gradle task](https://docs.gradle.org/current/userguide/tutorial_using_tasks.html) provided by the user.

### Prerequisites

Before running the **Gradle Runner** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                            | Description                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | To initiate the **Gradle Runner** process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the **Git Clone** step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for the **Gradle Runner** step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-gradle-runner_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-gradle-runner_2.png' />

| Variable Name                      | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR`               | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`                       | This variable specifies the project module to be built. This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/). In Android Studio, you can locate the available modules for your project. For more information, please refer to this [Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_VARIANTS`                     | This variable specifies the project variant to be built. This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants).               | Required |
| `$AC_OUTPUT_DIR`                   | Specifies the directory path for the generated app files.                                                                                                                                                                                                                                                                                                                                                              | Required |
| `$AC_GRADLE_TASK`                  | Specifies the name of the Gradle task. Refer to the documentation for detailed information: [List available tasks](https://docs.gradle.org/current/userguide/tutorial_using_tasks.html#list_available_tasks).                                                                                                                                                                                                          | Required |
| `$AC_PROJECT_PATH`                 | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path. The default value is: `./`                                                                                                                                                                                                | Optional |
| `$AC_GRADLE_TASK_EXTRA_PARAMETERS` | Extra arguments were passed to the Gradle task. For more information, please refer to [this Gradle document](https://docs.gradle.org/current/userguide/writing_build_scripts.html#sec:extra_properties).                                                                                                                                                                                                               | Optional |

### Output Variables

As the output may vary depending on the task you execute, there is no specific output defined by default.

:::caution

If there is an output generated, ensure to use the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps#export-build-artifacts) step afterward to ensure it is included in the [**Download Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts/#download-exported-artifacts) page.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-gradle-task-component.git
