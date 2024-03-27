---
title: Android Increment Build and Version Number
metaTitle: Android Increment Build and Version Number
metaDescription: Android Increment Build and Version Number
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Android Increment Build and Version Number
This component increments the `versionCode` and `versionName` according to the provided strategies.

For more information about Android versioning, you can refer to this document: [Android Versioning](https://docs.appcircle.io/versioning/android-version/).

:::caution
If you are not incrementing the version via **Appcircle** and have not enabled this feature through [**Configuration**](https://docs.appcircle.io/build/build-profile-configuration#versioning-configuration), this step completes the step without making any version changes.
:::

### Prerequisites
The workflow steps that need to be executed before running the **Android Increment Build and Version Number** workflow step, along with their respective reasons, are listed in the table below:

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | Upon completion of the **Git Clone** step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for this step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-increment-build-and-version-number_1.png' alt="image2" />

### Input Variables
For each component, specific input variables are required for its operation on your system. The input variables necessary for the **Android Increment Build and Version Number** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-increment-build-and-version-number_2.png' alt="image2" />

| Variable Name                 | Description                                    | Status |
|-------------------------------|------------------------------------------------|--------|
| `$AC_REPOSITORY_DIR`         | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) step, the variable will be automatically populated. | Required |
| `$AC_BUILD_NUMBER_SOURCE`    | Version code source type (environment variable or gradle file). | Required |
| `$AC_ANDROID_BUILD_NUMBER`   | Version code to set. If `$AC_BUILD_NUMBER_SOURCE` is set to gradle, this variable will be read from the project. | Required |
| `$AC_BUILD_OFFSET`           | The number to be added or subtracted from the `$AC_ANDROID_BUILD_NUMBER`. | Required |
| `$AC_VERSION_NUMBER_SOURCE`  | Version name source type (environment variable or gradle file). | Required |
| `$AC_ANDROID_VERSION_NUMBER` | Version name to set. If `$AC_VERSION_NUMBER_SOURCE` is set to gradle, this variable will be read from the project. | Required |
| `$AC_VERSION_STRATEGY`       | Version increment strategy (`major`, `minor`, `patch`, or `keep`). | Required |
| `$AC_VERSION_OFFSET`         | The number to be added or subtracted from the `$AC_ANDROID_VERSION_NUMBER`. | Required |
| `$AC_PROJECT_PATH`           | Specifies the project path. If the project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path. | Optional |
| `$AC_VERSION_FLAVOR`         | Build flavor. If you select a flavor from the [**Advanced Settings**](https://docs.appcircle.io/versioning/android-version/#advanced-settings) section, the versioning of the chosen flavor will be applied (for example, the Gradle file of the selected flavor will be used). | Optional |
| `$AC_OMIT_ZERO_PATCH_VERSION`| If `true`, it omits zero in the patch version. | Optional |

:::info
You can also configure many of those variables via build [**Configuration**](https://docs.appcircle.io/build/build-profile-configuration). For further details, visit [Android Versioning](https://docs.appcircle.io/versioning/android-version/).
:::

### Output Variables
The outputs that can result from the operation of this component are listed as follows:

| Variable Name                  | Description                                              |
|--------------------------------|----------------------------------------------------------|
| `$AC_ANDROID_NEW_VERSION_CODE` | Represents the incremented version code applied to the project. |
| `$AC_ANDROID_NEW_VERSION_NAME` | Represents the incremented version name applied to the project. |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-build-version-increment-component.git
