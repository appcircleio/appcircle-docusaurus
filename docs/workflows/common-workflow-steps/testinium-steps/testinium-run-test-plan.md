---
title: Testinium Run Test Plan
description: The Testinium Run Test Plan step allows users to run automated tests on their mobile applications using Testinium directly from the Appcircle.
tags: [testinium, plan, run, test, mobile, automation, app automate]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import SensitiveVariablesDanger from '@site/docs/\_sensitive-variables-danger.mdx';
import TestiniumEnterpriseWhitelistDanger from '@site/docs/workflows/common-workflow-steps/testinium-steps/\_testinium-enterprise-whitelist-danger.mdx';

# Testinium Run Test Plan

The **Testinium Run Test Plan** step integrates the [Testinium](https://testinium.com/) testing platform into Appcircle's CI/CD workflow, allowing for automated testing of mobile applications directly within the Appcircle environment. This step enables developers to execute the test plan, analyze test outcomes, and verify the quality of their mobile apps before deployment.

### Prerequisites

Before running the **Testinium Run Test Plan** step, you must complete certain prerequisites, as detailed in the table below:

<TestiniumEnterpriseWhitelistDanger />

| Prerequisite Workflow Step        | Description                                                                                              |
| --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [**Testinium Upload App**](/workflows/common-workflow-steps/testinium-steps/testinium-upload-app) | Required to upload your application to Testinium before executing test plans with the **Testinium Run Test Plan** step. |

:::tip

After using the [**Testinium Upload App**](/workflows/common-workflow-steps/testinium-steps/testinium-upload-app) step once, you can add multiple **Testinium Run Test Plan** steps to the workflow for each test plan.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_run_test_plan-1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_run_test_plan_2-1.png'/>

<SensitiveVariablesDanger />

| Variable Name               | Description                                                                                                 | Status   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_TESTINIUM_USERNAME`    | Specifies the Testinium username used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PASSWORD`    | Specifies the Testinium password used for logging in.                                                       | Required |
| `$AC_TESTINIUM_PLAN_ID`     | Specifies the Testinium plan ID. This ID must be obtained from the Testinium platform.                      | Required |
| `$AC_TESTINIUM_ENTERPRISE_BASE_URL` | The base URL for Testinium enterprise. This is required if you are using Testinium enterprise.  Only for Testinium cloud users is this input not mandatory. | Optional |
| `$AC_TESTINIUM_COMPANY_ID`  | Specifies the Testinium company ID. This ID must be obtained from the Testinium platform.                   | Required |
| `$AC_TESTINIUM_MAX_FAIL_PERCENTAGE` | Specifies the maximum failure percentage limit to interrupt the workflow. It must be in the range `0`-`100`. Selecting `0` means failures will not interrupt the workflow. | Optional |
| `$AC_TESTINIUM_TIMEOUT`     | Specifies the Testinium plan timeout in minutes.                                                            | Required |
| `$AC_TESTINIUM_MAX_API_RETRY_COUNT` | Specifies the maximum retry in case of Testinium platform congestion or API errors.            | Required |
| `$AC_TESTINIUM_UPLOADED_APP_ID` | The unique identifier for the application was uploaded to Testinium. This ID is generated after the **Testinium App Upload** step.  | Required |
| `$AC_TESTINIUM_APP_OS` | The operating system of the uploaded application, either `iOS` or `Android`. This value is determined after the **Testinium App Upload** step.  | Required |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-testinium_run_test_plan_3-1.png'/>

| Variable Name                          | Description                                                                     |
| -------------------------------------- | ------------------------------------------------------------------------------- | 
| `AC_TESTINIUM_TEST_REPORT`             | The file path of the test report generated by Testinium after running the plan. |
| `AC_TESTINIUM_RESULT_FAILURE_SUMMARY`  | Total number of failures in the test results.                                   |
| `AC_TESTINIUM_RESULT_ERROR_SUMMARY`    | Total number of errors in the test results.                                     |
| `AC_TESTINIUM_RESULT_SUCCESS_SUMMARY`  | Total number of successes in the test results.                                  |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-testinium-run-test-plan-component