---
title: Android Unit Tests
description: Learn how to use the Android Unit Tests workflow step in Appcircle
tags: [android, mobile, unit, testing]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Unit Tests

The **Android Unit Tests** workflow step executes the unit tests within your project, ensuring comprehensive test coverage. The results of these tests will be included in the artifact archive for further analysis and review.

Please check out this document for more information: [Running Android Unit Tests](/continuous-testing/android-testing/running-android-unit-tests)

### Prerequisites

Before running the **Android Unit Tests** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                            | Description                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | To initiate the **Android Unit Tests** process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the **Git Clone** step, it generates the `$AC_REPOSITORY_DIR` variable, which is then used as the input for the **Android Unit Tests** step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-unit-tests_1.png'/>

:::danger

If you wish to view the test results on Appcircle's Test Reports page, it is essential to use the [Test Reports for Android](/workflows/android-specific-workflow-steps/test-reports-for-android) step after the **Android Unit Tests**. Please check out this document for more information: [Generating Test Report](/continuous-testing/android-testing/running-android-unit-tests#generating-test-report).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-unit-tests_2.png'/>

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-unit-tests_3.png' alt="image2" />

| Variable Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR` | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](/workflows/common-workflow-steps/git-clone) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`         | This variable specifies the project module to be built. This variable can also be set via the build [Configuration](/build/build-process-management/build-profile-configuration). In Android Studio, you can locate the available modules for your project. For more information, please refer to this [Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_VARIANTS`       | This variable specifies the project variant to be built. This variable can also be set via the build [Configuration](/build/build-process-management/build-profile-configuration). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants).               | Required |
| `$AC_PROJECT_PATH`   | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path. The default value is: `./`.                                                                                                                                                                                               | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name          | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| `AC_TEST_RESULT_PATH` | Specifies the directory where your JUnit XML report is stored. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-unit-test-component.git
