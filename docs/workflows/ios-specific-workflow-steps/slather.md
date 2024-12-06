---
title: Slather
description: Use Slather to convert Xcode's test results into various formats. Prerequisites include Xcodebuild for Tests and Git Clone.
tags: [slather, ios, build, test, unit, testing, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Slather

This step converts Xcode's test results to different formats by using [**Slather**](https://github.com/SlatherOrg/slather/). You can convert your test coverage results, such as `cobertura`, `JSON`, etc.

### Prerequisites

Before running the **Slather** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                                                                               | Description                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Git Clone**](/workflows/common-workflow-steps/git-clone)                                                    | This step will clone your repository. After this step works, the variable `$AC_REPOSITORY_DIR` will be created. This variable is the required input variable for **Slather**. |
| [**Xcodebuild for Unit and UI Tests**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test) | This step executes your unit and UI tests, generating a `.xcresult` file. This file serves as the mandatory test result input for **Slather**.                               |


<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2830-slatherOrder.png' />

:::danger

**Slather** component needs test results in `.xcresult` format to work. Therefore, make sure that the tests of the project are run. Otherwise, **Slather** will throw an error for not finding the file and the pipeline will break. 

:::

## Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2830-slatherInput.png' />

| Variable Name           | Description                          | Status                           |
|-------------------------|--------------------------------------|----------------------------------|
| `$AC_REPOSITORY_DIR`    | Specifies the cloned repository directory. It's generated after the **Git Clone** step. | Required |
| `$AC_TEST_RESULT_PATH`  | This is the path of **`.xcresult`** file. It will be generated after the [**Xcodebuild for Unit and UI Test**](/workflows/ios-specific-workflow-steps/xcodebuild-for-unit-and-ui-test) step. | Required |
| `$AC_SCHEME`            | Specifies the project scheme for build. If you filled in `Config => Build Schema` in the Configuration, this variable comes from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration). | Required |
| `$AC_PROJECT_PATH`      | Specifies the project path. For example: **`./appcircle.xcodeproj`**. If you filled in `Config => Xcode Project or Workspace Path` in the Configuration, this variable comes from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration). But if you have a different location, specify this parameter. | Required |
| `$AC_WORKSPACE_PATH`    | Specifies the workspace path. For example : **`./appcircle.xcworkspace`**. If you filled in `Config => Xcode Project or Workspace Path` in the Configuration, this variable comes from [Configuration](/build/platform-build-guides/building-ios-applications#build-configuration). But if you have a different location, specify this parameter. | Optional |
| `$AC_COVERAGE_FORMAT`   | Exported coverage format. You can change the output format of the coverage test results for Slather with the **Coverage Type** variable. The default value is **cobertura**. | Optional |
| `$AC_CONFIGURATION_NAME`| If you have a configuration that you want to specify while **Slather** is running, you can add it to the command line with the **Configuration** parameter. | Optional |
| `$AC_SLATHER_OPTIONS`   | If you want to add an extra command to the command line, you can do it with the **Extra Option** variable. | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-slather-component