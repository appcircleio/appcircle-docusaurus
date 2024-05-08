---
title: SwiftLint
description: Improve your code with SwiftLint, a tool for identifying programmatic and stylistic errors. Prerequisites include Git Clone and Cocoapods Install.
tags: [ios, build, test, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# SwiftLint
SwiftLint checks the source code for programmatic as well as stylistic errors. This is helpful in identifying some common and uncommon mistakes that are made during coding. This step installs [SwiftLint](https://github.com/realm/SwiftLint/) and runs SwiftLint with the given options. 

### Prerequisites

Remember, SwiftLint must be used after the following steps in order to work as expected.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | The repo needs to be cloned in order to start the CocoaPods installation process. After the clone, CocoaPods will be installed, and then SwiftLint will be run. After this step works, the variable `AC_REPOSITORY_DIR` will be created. This variable is the input variable for CocoaPods and SwiftLint. |
| [Cocoapods Install](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#cocoapods-install)| This step will install the dependencies in the project before SwiftLint can run. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lint_order.png' />

:::danger
If you are using **CocoaPods**, note that this step is dependent on the [**CocoaPods Install**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#cocoapods-install) step. Otherwise, the SwiftLint component will **fail**, and the **pipeline will break.**
:::
:::caution
If you are using **Swift Package Manager (SPM)**, do not use this step. SPM packages will be compiled in other steps that work with **Xcode**, such as [**Xcodebuild for Devices**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps#xcodebuild-for-devices-archive--export).

If you have SPM in your project and you are using the SwiftLint component in your workflow, the Linter component will give an error because it cannot find the required dependencies.
:::

### Input Variables

You can also customize your SwiftLint step with the options in the component. You can find all the detailed descriptions for all variables in the table below.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2613-lintInput.png' />

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_REPOSITORY_DIR`         | Specifies the cloned repository directory. | Required |
| `$AC_LINT_PATH`               | This is the path of SwiftLint dependency. It comes from the Xcode Build Phase section. | Optional |
| `$AC_LINT_RANGE`              | With the Range option, you can run SwiftLint on your entire project or only on changes in PR. Default is **all**. | Optional |
| `$AC_LINT_CONFIG`             | Specifies the linting configuration file. For example: `/.swiftlint.yml` | Optional |
| `$AC_LINT_REPORTER`           | You can change the report type with the `Reporter Format` option. This option supports extensions such as **`html`**, **`json`**, **`junit`**, etc. The default is **Xcode**. | Optional |
| `$AC_LINT_STRICT`             | If there is a failure in the running lint, you can break the pipeline with the **Strict** option. The default value is `NO`. | Optional |
| `AC_LINT_QUIET`               | If you want the logs to be simpler, you can make the report file simpler with the **Quiet Mode** feature. | Optional |

### Output Variables

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `$AC_LINT_OUTPUT_PATH`        | The path of the SwfitLint results output file. After SwiftLint runs, all results will be written in a .txt file. It can be found in the download artifacts. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-swiftlint-component