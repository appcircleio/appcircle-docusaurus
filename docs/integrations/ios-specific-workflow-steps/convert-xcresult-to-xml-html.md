---
title: Convert Xcresult to HTML/XML 
description: Convert Xcresult to HTML/XML
tags: [xcresult, convert, html, xml, unit tests, UI tests, test reports]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Convert Xcresult to HTML/XML

After the [**Xcodebuild for Unit and UI Tests**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests) step runs, it generates a `test_result.xcresult` file. In specific cases, this test file must be converted to another format. The **Convert Xcresult to HTML/XML** step is used for converting this test file to `HTML` and `XML` formats.


### Prerequisites
| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Xcodebuild for Unit and UI Tests**](https://docs.appcircle.io/continuous-testing/running-ios-unit-and-ui-tests) | This step allows you to run unit and UI tests on your project. After this step runs, the related path, `AC_TEST_RESULT_PATH` will be generated automatically. |

:::caution
Please note that if you do not run **Xcodebuild for Unit and UI Tests** before this step, the step will produce an error because there will be no test result file to convert.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2989-convertOrder.png' />

### Input Variables

The parameters required for the operation of this stepper are given below with explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2989-convertInput.png' />

| Variable Name                 | Description                         | Status           |
|-------------------------------|-------------------------------------|------------------|
| `$AC_OUTPUT_DIR`              | Specifies the path for outputs for generated artifacts. This path will be automatically defined. Do not change if it is not necessary. | Required |
| `$AC_TEST_RESULT_PATH`        | This directory will be used for converting from `Xcresult` to `HTML` or `XML`. | Required |
| `$AC_CONVERT_FILE_NAME`       | The name of the converted test result file. This will be the new filename for the result file. | Required |
| `$AC_CONVERT_TYPE`            | Specify the convert-type option. Which type should it be converted to? The options are `XML` and `HTML`. The default value is `XML`. | Required |
| `$AC_INCLUDE_COVERAGE`        | If set to `Yes`, it will include the coverage result in the converted file. The default value is `No`. | Required |


### Output Variables

| Variable Name                 | Description                         | 
|-------------------------------|-------------------------------------|
| `$AC_CONVERTED_TEST_RESULT_PATH`           | Specifies the path where the converted result is stored. Users can access this path via this variable. Additionally, it will be available for download in the [**Download Artifact**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) section.  |

:::caution
To view the converted test reports on the [**Download Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts/#download-exported-artifacts) page, please ensure that the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts) step is included in your Workflow after this step.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-xcresult-convert-html-xml-component