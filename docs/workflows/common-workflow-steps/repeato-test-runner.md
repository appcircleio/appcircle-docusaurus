---
title: Repeato Test Runner
description: Repeato Test Runner facilitates the execution of automated tests for mobile applications directly within Appcircle.
tags: [repeato, test runner, mobile, automation]
---

import Screenshot from '@site/src/components/Screenshot';

# Repeato Test Runner

[Repeato](https://www.repeato.app) is a test automation platform designed for mobile applications. It enables developers to create, manage, and execute automated tests for mobile apps across different platforms and devices. Repeato supports various testing frameworks and provides features for test script creation, test execution, result analysis, and reporting. It helps streamline the testing process, improve test coverage, and enhance the overall quality of mobile applications.

The **Repeato Test Runner** integrates as a service within the Appcircle CI/CD workflow, streamlining the execution of automated tests directly within Appcircle. This service enables developers to validate the functionality and performance of their mobile applications before deployment, ensuring releases of high quality.

For more information, please check out this blog post:

https://appcircle.io/blog/streamline-project-integration-and-test-automation-with-repeato-and-appcircle

### Prerequisites

Before executing the **Repeato Test Runner** workflow step, certain prerequisite workflow steps must be completed:

| Prerequisite Workflow Step                                   | Description                                                                                                                                                                                                                  |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/#git-clone) | The repository that needs to be built must be fetched from the branch. Upon completion of the **Git Clone** step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for the Android Build step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-repeato_1.png'/>

:::danger
If you wish to view the test results on Appcircle's Test Reports page, it is essential to use the [Test Reports](https://github.com/appcircleio/appcircle-test-report-component) step after the **Repeato Test Runner**. Please check out this document for more information: [Generating Test Report](/continuous-testing/android-testing/running-android-unit-tests#generating-test-report)

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-unit-tests_2.png'/>
:::

### Input Variables

Specific input variables are required for the **Repeato Test Runner** to function correctly:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-repeato_2.png'/>

:::danger

Confidential information must be entered as a [secret environment variable](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Additionally, ensure that the appropriate [environment variable group](/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](/build/build-process-management/build-profile-configuration/).

:::

| Variable Name               | Description                                                                                                                                                           | Status   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPEATO_CLI_VER`       | Specifies the Repeato CLI version compatible with your workspace tests.                                                                                               | Optional |
| `$AC_REPEATO_WORKSPACE_DIR` | The workspace path is required by the Repeato test runner to set up the workspace before executing the batch. Example: `./mypath`.                                    | Required |
| `$AC_REPEATO_BATCH_ID`      | Provides the batch ID for test execution. For more details, please refer to [this document](https://www.repeato.app/documentation/continuous-integration/#appcircle). | Required |
| `$AC_REPEATO_LIC_KEY`       | Provides a license key for test execution.                                                                                                                            | Required |
| `$AC_REPEATO_LOG_LEVEL`     | Switch to `DEBUG` if you encounter issues while running your batches. This prints additional information to the log. Options: `INFO`, `DEBUG`, `WARN`.                | Required |

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name              | Description                                              |
| -------------------------- | -------------------------------------------------------- |
| `AC_REPEATO_REPORT`       | Report of Repeato batches that have been executed.       |
| `AC_REPEATO_JUNIT_REPORT` | Report of Repeato executed tests in JUnit XML format.    |
| `AC_TEST_RESULT_PATH`     | The directory where your JUnit XML report will be saved. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-repeato-component
