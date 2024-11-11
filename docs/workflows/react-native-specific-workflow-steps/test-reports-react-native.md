---
title: Test Reports for React Native
description: Test Report step displays your test results and code coverage in an aesthetically pleasing user interface for React Native applications.
tags: [test, test report, test result, automation]
---

import Screenshot from '@site/src/components/Screenshot';

# Test Reports for React Native

The Appcircle **Test Report** step displays your test results and code coverage in an aesthetically pleasing user interface.

This component supports the following test and coverage formats:

- [JUnit](https://junit.org) - For Java-based test reporting.

For additional details, please refer to the document: [**Generating Test Report**](/continuous-testing/react-native-testing/react-native-ui-test-with-detox#generating-test-report)

### Prerequisites

Before executing the **Test Report** workflow step, **one of the** following steps must be run to generate the report:

| Prerequisite Workflow Step                                                                           | Description                                                                                    |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [**React Native Unit Test**](/workflows/react-native-specific-workflow-steps/react-native-unit-test) | Run unit tests in your project to generate an `junit-report.xml` file containing the test outcomes.   |
| [**React Native UI Test**](/workflows/react-native-specific-workflow-steps/react-native-ui-test)     | Run UI tests in your project to generate an `e2e-report.xml` file containing the test outcomes. |

:::caution Prerequisites

To able to use the **Test Report** component, not necessary to use both test step **React Native UI Test** and **React Native Unit Test** at the same time. But if these test steps are included in the flow, they must be used before the **Test Report** component.

:::

### Input Variables

For each component, specific input variables are required for its operation on your system.

| Variable Name             | Description                                                                                                                      | Status   |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_TEST_RESULT_PATH`     | Define the directory and its subdirectories for searching compatible test files.                                                 | Required |
| `$AC_COVERAGE_RESULT_PATH` | For native iOS projects, tests automatically set this variable. For other projects, you must specify the coverage path manually. | Optional |

:::caution

To view the output artifacts on the [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) page, please ensure that the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.

:::

### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name              | Description                            |
| -------------------------- | -------------------------------------- |
| `AC_TEST_REPORT_JSON_PATH` | Specifies the path of the JSON report. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-test-report-component
