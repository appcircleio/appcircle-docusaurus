---
title: Converting XCResult to HTM/XML
metaTitle: Converting XCResult to HTM/XML
metaDescription: Converting XCResult to HTM/XML
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Converting XCResult to HTML/XML

[**Xcodebuild for Unit and UI Test**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/#xcodebuild-for-unit-and-ui-tests) results are generated with `.xcresult` extension. You can convert the test results from this step to HTML or XML format.

### Prerequisites

The steps that must run before this step are given below with explanations.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Unit and UI Test**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/#xcodebuild-for-unit-and-ui-tests) | This step runs the **Unit/UI** tests in the project and produces a test report in `.xcresult` format. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2571-convertOrder.png' />

:::caution
If the [**Xcodebuild for Unit and UI Test**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/#xcodebuild-for-unit-and-ui-tests) step is not run before this step, a file not found error will be received because a test result file to be converted will not be generated.
:::

### Input Variables

The steps required for the operation of this step are listed below with their descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2571-convertInput.png' />

| Variable Name                            | Description                         | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_OUTPUT_DIR`              | This variable specifies the path of the artifacts that will be generated after the build is complete. | Required |
| `$AC_TEST_RESULT_PATH`        | Path of the result file that will be produced after the Xcodebuild for Unit and UI test step runs. It will be generated automatically after running this step. | Required |
| `$AC_CONVERT_FILE_NAME`       | The name to be given to the file after the test results are converted. The default name is `test_results`. | Required |
| `$AC_CONVERT_TYPE`            | `.xcresult` file type to convert extension type `html` or `xml`. The default value is `xml`. |  |


### Output Variables

The outputs that can result from the operation of this component are listed as follows:

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `$AC_CONVERTED_TEST_RESULT_PATH`       | Test resultları istenilen formata dönüştürüldükten sonraki path. It can be accessed from the [Download Artifact](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) section. |


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-xcresult-convert-html-xml-component