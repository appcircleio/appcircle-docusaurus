---
title: Set Environment Variable
description: Set Environment Variable step sets environment value for given keys
tags: [set, environment, variable]
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

# Set Environment Variable

The **Set Environment Variable** step allows you to set environment values for given keys. While it's generally recommended to create environment variables from the [Environment Variables](https://docs.appcircle.io/environment-variables/) page, there may be instances where you need to set or change environment variables within the build workflow. In such cases, the **Set Environment Variable** step can be used.

### Prerequisites

There is no mandatory step before the **Set Environment Variable** step. You can use this step anywhere in the workflow as needed.

:::warning

Please note that you must use the **Set Environment Variable** step before the step in which you intend to use the environment variable.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_1.png'/>

### Input Variables

For each component, specific input variables are required for its operation on your system. The input variables necessary for **Set Environment Variable** are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_2.png'/>

:::warning

Confidential information should be entered as a [secret environment variable](https://docs.appcircle.io/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [environment variable group](https://docs.appcircle.io/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](https://docs.appcircle.io/build/build-process-management/build-profile-configuration/).

:::

| Variable Name      | Description                                                                                                     | Status   |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_SETENV_KEYS`  | Specifies the key of the environment variable to be set. This should be a space-separated list of environment variable keys.  | Required |
| `$AC_SETENV_VALUE` | Specifies the value of the environment variable to set. If this field is left blank, the environment variable will be set to `null`. | Optional |

### Output Variables

The **Set Environment Variable** step does not produce any output variables. If the environment variable is successfully set, the step will succeed, and you can use the environment variable after this step. Otherwise, it will fail.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-setenvironment-component.git