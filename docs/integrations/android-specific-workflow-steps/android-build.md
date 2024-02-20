---
title: Android Build
metaTitle: Android Build
metaDescription: Android Build
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

# Android Build
The Appcircle Android Build step is designed to build your Android application for the architectures specified in your project. 

### Prerequisites
The workflow steps that need to be executed before running the **Android Build** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | To initiate the Android build process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the Git Clone step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for the Android Build step. |

### Configuration
Ensure that you have completed all the necessary **Configuration** fields before starting the build. For more information about configurations, refer to the [Build Profile Configuration Overview](https://docs.appcircle.io/build/build-profile-configuration) document. The information you fill in the configuration will be used as input in the Android Build step. Please replace the example information with your own details:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_1.png' alt="image2" />

### Workflow
The Android Build step is part of the Default Workflow. If you wish to incorporate this step into your workflow, you can navigate to **Manage Workflow** and select the **Android Build** step from the list to include it in your workflow. For detailed information about workflows, please refer to the document titled [What are Workflows and How to Use Them?](https://docs.appcircle.io/workflows/why-to-use-workflows) available on the page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_3.png' alt="image2" />

:::warning
To ensure the successful execution of this step, the Git repository must be cloned beforehand. Please ensure that [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) is executed before attempting this step again.
:::

### Input Variables

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_2.png' alt="image2" />

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`          | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) step, the variable will be automatically populated. | ✅ |
| `$AC_MODULE`                  | This variable specifies the project module to be build, which is selected in the [Configuration](https://docs.appcircle.io/build/build-profile-configuration/). In Android Studio, you can locate the available modules for your project. For more information, please refer to [this Android document](https://developer.android.com/studio/projects#ApplicationModules) (Configuration Image, 1st field). | ✅ |
| `$AC_VARIANTS`                | This variable specifies the project variant to be build, which is selected in the [Configuration](https://docs.appcircle.io/build/build-profile-configuration/). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants). (Configuration Image, 2nd field). | ✅ |
| `$AC_OUTPUT_TYPE`             | This variable specifies the output type for your build file (APK or AAB), which is selected in the [Configuration](https://docs.appcircle.io/build/build-profile-configuration/). (Configuration Image,  3rd field). | ✅ |
| `$AC_PROJECT_PATH`            | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path. | ➖ |
| `$AC_GRADLE_BUILD_EXTRA_ARGS` | Extra arguments passed to build task. For more information, please refer to [this Gradle document](https://docs.gradle.org/current/userguide/writing_build_scripts.html#sec:extra_properties). | ➖ |

:::tip
If you are using Gradle 4.3 and above in your project, you can just use the --scan flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to https://scans.gradle.com/
:::

### Output Variables

| Variable Name     | Description                                |
|-------------------|--------------------------------------------|
| `$AC_APK_PATH`    | Path for the generated **APK** file.           |
| `$AC_AAB_PATH`    | Path for the generated **AAB** file.           |

The resulting files will be either APK or AAB, depending on whether you choose the Android App in the project [Configuration](https://docs.appcircle.io/build/build-profile-configuration).

If your project has [the signing configuration in Gradle](https://developer.android.com/studio/build/gradle-tips#sign-your-app), this step will generate a signed artifact. 
:::caution
If you do not disable the **Sign Application** step, your artifact will remain unsigned and will be re-signed using the keystore selected in the build configuration.
:::
