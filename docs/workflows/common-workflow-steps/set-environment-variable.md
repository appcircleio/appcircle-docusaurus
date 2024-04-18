---
title: Set Environment Variable
description: Set Environment Variable step sets environment value for given keys
tags: [set, environment, variable]
sidebar_position: 12
---

import Screenshot from '@site/src/components/Screenshot';

# Set Environment Variable

The **Set Environment Variable** step enables the setting of environment values for specified keys. Although creating environment variables via the [Environment Variables](/environment-variables/) page is typically recommended, this step provides flexibility to modify environment variables directly within the build workflow when necessary.
### Prerequisites

There is no prerequisites step before the **Set Environment Variable** step. It can be implemented at any point within the workflow as necessary.

:::warning

Please note that you must use the **Set Environment Variable** step before the step in which you intend to use the environment variable.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_1.png'/>

### Input Variables

Each component requires specific input variables for operation. For the **Set Environment Variable** step, the necessary input variables are:
<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_2.png'/>

:::warning

Confidential information should be entered as a [secret environment variable](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs). Also, ensure that the [environment variable group](/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the [Configuration](/build/build-process-management/build-profile-configuration/).

:::

| Variable Name      | Description                                                                                                     | Status   |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_SETENV_KEYS`  | Specifies the key of the environment variable to be set. This should be a space-separated list of environment variable keys.  | Required |
| `$AC_SETENV_VALUE` | Specifies the value of the environment variable to set. If this field is left blank, the environment variable will be set to `null`. | Optional |

### Output Variables

The **Set Environment Variable** step generates no output variables. Success or failure of this step depends on whether the environment variable is set correctly, allowing subsequent use within the workflow.

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-setenvironment-component.git