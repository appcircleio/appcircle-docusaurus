---
title: Test Reports for iOS
description: Test Report step displays your test results and code coverage in an aesthetically pleasing user interface for iOS applications.
tags: [test, test report, test result, automation]
---

import Screenshot from '@site/src/components/Screenshot';

# Test Reports for iOS

The Appcircle **Test Report** step displays your test results and code coverage in an aesthetically pleasing user interface.

This component supports the following test and coverage formats:

- [Xcode 13+ XCTest](https://developer.apple.com/documentation/xctest) - For Apple's native test framework.
- [JUnit](https://junit.org) - For Java-based test reporting.
- [Cobertura](https://cobertura.github.io/cobertura) - For coverage reporting.
- [lcov.info](https://lcov-viewer.netlify.app) - For GCC coverage data.

For additional details, please refer to the document: [**Generating Test Report**](/continuous-testing/ios-testing/running-ios-unit-and-ui-tests#generating-test-report)


### Prerequisites

Before executing the **Test Report** workflow step, certain prerequisite workflow steps must be completed:

| Prerequisite Workflow Step                                   | Description                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [**Xcodebuild for Unit and UI Test**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test) | Run unit and UI tests in your project to generate an `.xcresult` file containing the test outcomes. |


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
