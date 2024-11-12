---
title: Test Reports for Android
description: Explore the Test Report feature for Android in Appcircle. Understand how it presents test results and code coverage in a user-friendly interface.
tags: [test, test report, test result, automation]
---

import Screenshot from '@site/src/components/Screenshot';

# Test Reports for Android

The Appcircle **Test Report** step displays your test results and code coverage in an aesthetically pleasing user interface.

This component supports the following test and coverage formats:

- [**JUnit**](https://junit.org)
- [**JaCoCo**](https://www.jacoco.org)
- [**Cobertura**](https://cobertura.github.io/cobertura)
- [**lcov.info**](https://lcov-viewer.netlify.app)

For additional details, please refer to the document: [**Generating Test Report**](https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report)

### Prerequisites

Before executing the **Test Report** workflow step, certain prerequisite workflow steps must be completed:

| Prerequisite Workflow Step                                   | Description                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [**Android Unit Tests**](/workflows/android-specific-workflow-steps/android-unit-tests) | This step must be executed to obtain the test report output. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-test-report_1.png'/>


### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for **Test Reports** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-test-report_2.png'/>

| Variable Name            | Description                                                      | Status    |
| ------------------------ | ---------------------------------------------------------------- | --------- |
| `$AC_TEST_RESULT_PATH`    | Specifies the directory and its subdirectories where compatible test files will be searched. | Required  |
| `$AC_COVERAGE_RESULT_PATH`| Specifies the coverage path. | Optional  |
| `$AC_JACOCO_COVERAGE_TYPE`| Determines the parameter in your JaCoCo report based on which the coverage will be calculated. This setting is necessary when using JaCoCo parseable coverage results and specifying the coverage result path. Types description can be found in this [documentation](/continuous-testing/android-testing/running-android-unit-tests#jacoco-test-coverage) | Required  |


### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name              | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| `AC_TEST_REPORT_JSON_PATH` | Specifies the path of the JSON report.               |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-test-report-component