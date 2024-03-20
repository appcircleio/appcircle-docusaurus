---
title: Convert Xcresult to HTML/XML 
metaTitle: Convert Xcresult to HTML/XML
metaDescription: Convert Xcresult to HTML/XML
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Convert Xcresult to HTML/XML

After the [**Xcodebuild for Unit and UI Tests**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests) step runs, it creates a test_result.xcresult file. In some specific cases, this test file needs to be converted to another format accordingly. The **Convert Xcresult to HTML/XML** step is used to convert this test file to `HTML` and `XML` formats.


### Prerequisites
| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Unit and UI Tests**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests) | This step allows you to run unit and UI tests in your project. |

:::caution
Please note that if you do not run Xcodebuild for Unit and UI Tests before this step, the step will give an error because there will be no test result file to convert.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2989-convertOrder.png' />

### Input Variables

The parameters required for the operation of this stepper are given below with explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2989-convertInput.png' />

| Variable Name                 | Description                         | Status           |
|-------------------------------|-------------------------------------|------------------|
| `$AC_OUTPUT_DIR`              |  | Required |
| `$AC_TEST_RESULT_PATH`        | This directory will be used for converting to `HTML/XML`. | Required |
| `$AC_CONVERT_FILE_NAME`       | The name of the converted test result file. This name will be the new result file name. | Required |
| `$AC_CONVERT_TYPE`            | This is the convert-type option. Which type will be converted to? The default variable is `xml`. | Required |
| `$AC_INCLUDE_COVERAGE`        | It will include the coverage result in the converted file. The default variable is `NO`. | Required |


### Output Variables

| Variable Name                 | Description                         | 
|-------------------------------|-------------------------------------|
| `$AC_CONVERTED_TEST_RESULT_PATH`           | Converted result path. The user can find the converted result file at this path. Also, it will be able to download from [**Download Artifact**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts).  |
