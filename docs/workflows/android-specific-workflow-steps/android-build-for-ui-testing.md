---
title: Android Build for UI Testing
description: Learn how to use the Android Build for UI Testing workflow step in Appcircle
tags: [android, mobile, android, ui testing, testing]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Build for UI Testing

The **Android Build for UI Testing** workflow step is tailored to [build your Android test application](https://developer.android.com/training/testing/instrumented-tests) using [Gradle Wrapper (gradlew)](https://docs.gradle.org/current/userguide/gradle_wrapper.html) for the designated architectures outlined in your project. This process employs the following gradle command: `./gradlew clean <your-module>:assembleAndroidTest`

### Prerequisites

The workflow steps that need to be executed before running the **Android Build for UI Testing** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                                                            | Description                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | To initiate the **Android Build for UI Testing** process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the **Git Clone** step, it generates the `$AC_REPOSITORY_DIR` variable, which is then used as the input for the **Android Build for UI Testing** step. |

:::caution
If you're updating the version via Appcircle, ensure that the following step comes before the **Android Build for UI Testing** step:

- [**Android Increment Build and Version Number**](https://docs.appcircle.io/workflows/android-specific-workflow-steps/increment-build-and-version-number)

:::

:::caution
If you're working with a **React Native Android** project, ensure that the following steps come before the **Android Build for UI Testing** step:

- [**Install Node**](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps/#install-node)
- [**NPM/Yarn Commands**](https://docs.appcircle.io/workflows/react-native-specific-workflow-steps/npm-yarn-commands)

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build-for-ui-testing_1.png'/>

:::note
The **[Firebase Test Lab for Android](https://docs.appcircle.io/continuous-testing/firebase-test-lab-for-android/)** step has been added as an example. You can use the APK you produce for UI testing in any component you choose.
:::

### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for the **Android Build for UI Testing** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build-for-ui-testing_2.png' alt="image2" />

| Variable Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR` | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`         | This variable specifies the project module to be built. This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/). In Android Studio, you can locate the available modules for your project. For more information, please refer to this [Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_PROJECT_PATH`   | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path.                                                                                                                                                                                                                           | Optional |

### Output Variables

The outputs that can result from the operation of this component are listed as follows:

| Variable Name       | Description                                                                                                          |
| ------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `AC_APK_PATH`      | Path for the generated **APK** file. This path will be created after the **Android Build for UI Testing** step runs. |
| `AC_TEST_APK_PATH` | Path for the generated `*androidTest.apk` file. This output can be utilized wherever necessary for UI testing.       |

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-build-ui-test-component.git
