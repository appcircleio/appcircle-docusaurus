---
title: Test Reports
description: Test Report step displays your test results and code coverage in an aesthetically pleasing user interface.
tags: [test, test report, test result, automation]
sidebar_position: 18
---

import Screenshot from '@site/src/components/Screenshot';

The Appcircle **Test Report** step displays your test results and code coverage in an aesthetically pleasing user interface.

This component supports the following test and coverage formats:

- [**Xcode 13+ XCTest**](https://developer.apple.com/documentation/xctest)
- [**JUnit**](https://junit.org)
- [**Cobertura**](https://cobertura.github.io/cobertura)
- [**lcov.info**](https://lcov-viewer.netlify.app)

For additional details, please refer to the document: [**Generating Test Report**](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests#generating-test-report)


### Prerequisites

Before executing the **Test Report** workflow step, certain prerequisite workflow steps must be completed:

| Prerequisite Workflow Step                                   | Description                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [**Xcodebuild for Unit and UI Test**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test) | This step allows you to run unit and UI tests in your project. When this step runs, all your tests are run, and an .xcresult file is created as a result. |


### Input Variables

For each component, specific input variables are required for its operation on your system. 

| Variable Name            | Description                                                      | Status    |
| ------------------------ | ---------------------------------------------------------------- | --------- |
| `AC_TEST_RESULT_PATH`    | Specifies the directory and its subdirectories where compatible test files will be searched. | Required  |
| `AC_COVERAGE_RESULT_PATH`| This environment variable is automatically set for native iOS projects when you run tests. For other projects, you need to set the coverage path. | Optional  |


### Output Variables

The outputs resulting from the operation of this component are as follows:

| Variable Name              | Description                                          |
| -------------------------- | ---------------------------------------------------- |
| `AC_TEST_REPORT_JSON_PATH` | Specifies the path of the JSON report.               |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-test-report-component
