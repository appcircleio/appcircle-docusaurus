---
title: Test Reports for React Native
description: Test Report step displays your test results and code coverage in an aesthetically pleasing user interface.
tags: [test, test report, test result, automation]
---

import Screenshot from '@site/src/components/Screenshot';

# Test Reports for React Native

The Appcircle **Test Report** step displays your test results and code coverage in an aesthetically pleasing user interface.

This component supports the following test and coverage formats:

- [JUnit](https://junit.org) - For Java-based test reporting.
- [Cobertura](https://cobertura.github.io/cobertura) - For coverage reporting.
- [lcov.info](https://lcov-viewer.netlify.app) - For GCC coverage data.

For additional details, please refer to the document: [**Generating Test Report**](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests#generating-test-report)


### Prerequisites

Before executing the **Test Report** workflow step, certain prerequisite workflow steps must be completed:

| Prerequisite Workflow Step                                   | Description                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [**React Native Unit Test**](/workflows/react-native-specific-workflow-steps/react-native-unit-test) | Run unit tests in your project to generate an `JUnit.xml` file containing the test outcomes. |
| [**React Native UI Test**](/workflows/react-native-specific-workflow-steps/react-native-ui-test) | Run UI tests in your project to generate an `e2e-repot.xml` file containing the test outcomes. |

:::caution Prerequisites

To able to use Test Report component, not necessary to use both test step **React Native UI Test** and **React Native Unit Test** at the same time. But, if these test steps are included in the flow, they must be used before the Test Report component. 

:::


### Input Variables

For each component, specific input variables are required for its operation on your system. 

| Variable Name            | Description                                                      | Status    |
| ------------------------ | ---------------------------------------------------------------- | --------- |
| `AC_TEST_RESULT_PATH`    | Define the directory and its subdirectories for searching compatible test files. | Required  |
| `AC_COVERAGE_RESULT_PATH`| For native iOS projects, tests automatically set this variable. For other projects, you must specify the coverage path manually. | Optional  |


### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name              | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| `AC_TEST_REPORT_JSON_PATH` | Specifies the path of the JSON report.               |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-test-report-component
