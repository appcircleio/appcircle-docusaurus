---
title: Android Build
description: Learn how to use the Android Build workflow step in Appcircle
tags: [android, mobile, android, build]
---

import Screenshot from '@site/src/components/Screenshot';

# Android Build

The Appcircle Android Build step is designed to build your Android application for the architectures specified in your project.

### Prerequisites

The workflow steps that need to be executed before running the **Android Build** workflow step, along with their respective reasons, are listed in the table below.

| Prerequisite Workflow Step                                                        | Description                                                                                                                                                                                                                                                                                  |
| --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | To initiate the Android build process, the repository that needs to be built must be fetched from the branch. This is achieved as follows: Upon completion of the Git Clone step, it generates the `AC_REPOSITORY_DIR` variable, which is then used as the input for the Android Build step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_3.png' alt="image2" />

### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for the **Android Build** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_2.png' alt="image2" />

| Variable Name                 | Description                                                                                                                                                                                                                                                                                                                                                                                                            | Status   |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_REPOSITORY_DIR`          | This variable represents the path of the cloned Git repository. If this step runs after the [Git Clone](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) step, the variable will be automatically populated.                                                                                                                                                                                      | Required |
| `$AC_MODULE`                  | This variable specifies the project module to be build. This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/). In Android Studio, you can locate the available modules for your project. For more information, please refer to [this Android document](https://developer.android.com/studio/projects#ApplicationModules). | Required |
| `$AC_VARIANTS`                | This variable specifies the project variant to be build. This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants).               | Required |
| `$AC_OUTPUT_TYPE`             | This variable specifies the output type for your build file (APK or AAB). This variable can also be set via the build [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/).                                                                                                                                                                                          | Required |
| `$AC_PROJECT_PATH`            | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path.                                                                                                                                                                                                                           | Optional |
| `$AC_GRADLE_BUILD_EXTRA_ARGS` | Extra arguments were passed to build task. For more information, please refer to [this Gradle document](https://docs.gradle.org/current/userguide/writing_build_scripts.html#sec:extra_properties).                                                                                                                                                                                                                    | Optional |

:::info
If you have filled in the necessary variables in the **Configuration** section, you will not need to redefine these variables again in the Workflow. For more information about configurations, refer to the [Build Profile Configuration Overview](https://docs.appcircle.io/build/build-process-management/build-profile-configuration) document. The information you fill in the configuration will be used as input in the Android Build step. Please replace the example information with your own details:

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-android-build_1.png' alt="Configuration Image" />

1. The input corresponding to the 1st field: `$AC_MODULE`
2. The input corresponding to the 2nd field: `$AC_VARIANTS`
3. The input corresponding to the 3rd field: `$AC_OUTPUT_TYPE`
:::

:::tip
If you are using Gradle 4.3 and above in your project, you can just use the `--scan` flag in the build step to enable build scans. For existing projects, you may need to add the Gradle Scan (Gradle Enterprise) plugin. For more information, please refer to https://scans.gradle.com/
:::

### Output Variables

The outputs that can result from the operation of this component are listed as follows:

| Variable Name  | Description                                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `$AC_APK_PATH` | Path for the generated **APK** file. This path will be created after the **Android Build** step runs.                        |
| `$AC_AAB_PATH` | Path for the generated **AAB** file. This path will be created after the Android Build step runs and when `AAB` is selected. |

The resulting files will be either APK or AAB, depending on whether you choose the Android App in the project [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration).

If your project has the [signing configuration](https://developer.android.com/studio/build/gradle-tips#sign-your-app) in Gradle, this step will generate a signed artifact.

:::caution
If you do not disable the **Android Sign** step and your project has no signing configuration defined in Gradle, your artifact will remain unsigned.

So, in order to sign your app using the keystore selected in the build configuration, you should enable the **Android Sign** step after **Android Build**.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-android-build-component.git

## FAQ

### How can I solve the `Out of memory error: Java heap memory` or set the heap memory during the build?

To resolve this issue, you need to adjust the Java heap size using the following parameters in the [system properties](https://docs.gradle.org/current/userguide/build_environment.html#sec:gradle_system_properties):
> - [`-Xms:<size>`](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/jrdocs/refman/optionX.html#wp999527), which sets the initial and minimum heap size
> - [`-Xmx:<size>`](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/jrdocs/refman/optionX.html#wp999528), which sets the maximum heap size
>
> For example:
>
> ```bash
> java -Xms:1g -Xmx:1g MyApplication
> ```
>
> This starts up the JVM with a heap size fixed to 1 GB.

Please refer following documentation for more information:

https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/memman.html#wp1086978

You can implement this solution using one of the following methods:

#### Method 1: Using a Custom Script During the Build

If your project has varying heap size requirements, you can adjust the heap size during the build phase with a [**Custom Script**](/workflows/common-workflow-steps/custom-script) before the **Android Build** step. Your script should include the following command:

```bash
echo "org.gradle.jvmargs=-Xms1g -Xmx7168M"  >> $AC_REPOSITORY_DIR/gradle.properties
```

- Adjust the `-Xms1g -Xmx7168M` values according to your project needs.
- Ensure the path `$AC_REPOSITORY_DIR/gradle.properties` matches your file's location. `$AC_REPOSITORY_DIR` represents the root project directory.
- You can extend the command with additional parameters as needed. For example, for Kotlin, you might add: `"org.gradle.jvmargs=-Xms1g -Xmx7168M kotlin.daemon.jvm.options=-Xms700m -Xmx7168M"`

#### Method 2: Modifying the `gradle.properties` File

If the heap size requirement is constant, you can directly add the following code to the end of your project's `gradle.properties` file. Feel free to modify this code to fit your specific project requirements:

```bash
org.gradle.jvmargs=-Xms1g -Xmx7168M
```

:::tip

Also, if you want to solve this issue via Android Studio you can follow this documentation:

[Android Developer documentation on adjusting heap size](https://developer.android.com/studio/intro/studio-config#adjusting_heap_size).

:::


