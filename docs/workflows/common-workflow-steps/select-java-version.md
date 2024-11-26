---
title: Select Java Version
description: Switch the current Java version to the selected one.
tags: [change, select, java, version, java version, android java, jdk]
---

import Screenshot from '@site/src/components/Screenshot';

# Select Java Version

The **Select Java Version** step updates the JDK and Java version to the selected one during the build process.

If your project requires a different JDK or Java version than the default in your runner, you can use this step to switch to the selected version. To check the default Java version used in Appcircle, refer to this document:

- [Android Build Stacks - Java Version](/infrastructure/android-build-infrastructure#java-version)

Note that available Java versions may vary based on the runner you are using.

For self-hosted users, the versions listed for the cloud Appcircle runner may not apply. Refer to the FAQ below for guidance:

- [How do I check available Java versions in the Appcircle runner?](#how-do-i-check-available-java-versions-in-the-appcircle-runner)

:::tip Check Java Version for Android

If you are unsure which Java version is required for your Android project, you can find it by following the steps in this FAQ:

- [How can I check the Java version of my Android project?](#how-can-i-check-the-java-version-of-my-android-project)

:::


## Prerequisites

There are no prerequisites required before using the **Select Java Version** step.

:::caution

If you have a step that necessitates changing the Java version (e.g., the [**Android Build**](/workflows/android-specific-workflow-steps/android-build) step), the **Select Java Version** step should run before that step in the [workflow](/workflows).

:::

For reference, you can see the workflow sequence in the image below:

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-select-java-version-1.0.png' />

:::caution

If your runner is self-hosted, ensure that the selected Java version is available in your environment. If not, you must install the required version before the **Select Java Version** step.

:::


## Input Variables

A required parameter for this step is outlined in the table below, along with its description.

<Screenshot url='https://cdn.appcircle.io/docs/assets/common-workflow-components-select-java-version-2.0.png' />


| Variable Name               | Description                                                                                                 | Status   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_SELECTED_JAVA_VERSION` | Specify the Java version to switch to. The default value is `17`. Options: `8`, `11`, `17`, and `21`. | Required |

:::info

If the selected Java version is not available on the runner, an error message will indicate that `this version is not found` and will display the available Java versions for your runner. Beforehand, check available Java versions for cloud runner [here](/infrastructure/android-build-infrastructure#java-version).

:::

## Output Variables

This step does not produce any visible output. However, if run successfully, it will update both the default Java version (`$JAVA_HOME`) and the system JDK version to the selected version.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-select-java-version-component

---

## FAQ

### How do I check available Java versions in the Appcircle runner?

To view the Java versions available in the Appcircle runner, you can run the following [Custom Script](/workflows/common-workflow-steps/custom-script) in your workflow:

```bash
echo "Default Java version:" $JAVA_HOME

echo "OpenJDK 8:" $JAVA_HOME_8_X64
echo "OpenJDK 11:" $JAVA_HOME_11_X64
echo "OpenJDK 17:" $JAVA_HOME_17_X64
echo "OpenJDK 21:" $JAVA_HOME_21_X64
```

Any variables that output non-empty values indicate the available Java versions in your runner.

### How can I check the Java version of my Android project?

You can determine the required SDK version by looking at the `compileSdk` field in your `build.gradle` file under the **module** used in your Android project. The table below lists the Java versions corresponding to these SDK versions:

| Android       | Java     |
| ------------- | -------- |
| 14 (API 34)   | 17       |
| 13 (API 33)   | 11       |
| 12 (API 32)   | 11       |
| 11 and lower  | ..       |


The Java version for API level 11 and lower is not specified in the Android document. For more details, please refer to the Android documentation linked below:

- [Which Java APIs can I use in my Java or Kotlin source code?](https://developer.android.com/build/jdks#compileSdk)