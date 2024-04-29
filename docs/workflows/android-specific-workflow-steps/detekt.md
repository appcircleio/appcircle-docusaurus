---
title: Detekt
description: Detekt step, checks for code smells, performance problems, bugs, and adherence to best practices, offering configurable rules and plugins for customization.
tags: [detekt, android, code-quality]
---

import Screenshot from '@site/src/components/Screenshot';

# Detekt

[Detekt](https://detekt.dev/) is a static code analysis tool for [Kotlin](https://kotlinlang.org/) used in Android development. It identifies issues, enforces standards, and improves code quality by checking for code smells, performance issues, bugs, and adherence to best practices, with configurable rules and plugins for customization. Its integration into workflows promotes clean and efficient Kotlin codebases.

The Appcircle Detekt step executes the Detekt Gradle task. For further details, please refer to the [Run detekt using the Detekt Gradle Plugin](https://detekt.dev/docs/gettingstarted/gradle/) documentation.

### Prerequisites

Below are the prerequisite workflow steps required before running the **Detekt** step, along with their reasons:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/git-clone) | The **Git Clone** step is necessary to fetch the repository before conducting code checks and must precede the **Detekt** step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-detekt_1.png'/>

### Input Variables

Each component requires specific input variables for its operation. The input variables necessary for the **Detekt** step are:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-detekt_2.png'/>

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_DETEKT_TASK`             | Specifies the name of the Detekt task. The default value is `detekt`. | Required |
| `$AC_DETEKT_EXTRA_PARAMETERS` | Additional command-line parameters for Detekt. | Optional |
| `$AC_DETEKT_SAVE_REPORT`      | Specifies whether the Detekt report will be saved. If set to `true`, report files will be saved into the artifacts folder. The default value is `false`. | Optional |
| `$AC_DETEKT_OUTPUT_PATH`      | Specifies the Detekt output path. If the `AC_DETEKT_SAVE_REPORT` input is set to `true` and this value is not defined, then `<ac_module>/build/reports` will be used as the default path. | Optional |

:::warning

If `$AC_DETEKT_SAVE_REPORT` is set to `true`, place the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts) step after the **Detekt** step to ensure proper transfer of outputs to the [Download Artifacts](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) section.

:::

### Output Variables

The output is not stored in any variable. If `AC_DETEKT_SAVE_REPORT` is set to `true`, the file output will be saved in the `$AC_PROJECT_PATH/$AC_MODULE/build/reports` directory (check these variables on the [Appcircle-Specific Environment Variables](https://docs.appcircle.io/environment-variables/appcircle-specific-environment-variables#ios--android-common-environment-variables) page). If you've added the [**Export Build Artifacts**](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts) step after the **Detekt** step, this output will also be accessible in the [Download Artifacts](https://docs.appcircle.io/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts) section.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-detekt-component.git