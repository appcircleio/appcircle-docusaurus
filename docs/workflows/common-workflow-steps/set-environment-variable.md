---
title: Set Environment Variable
description: Set Environment Variable step sets environment value for given keys
tags: [set, environment, variable]
---

import Screenshot from '@site/src/components/Screenshot';

# Set Environment Variable

The **Set Environment Variable** step enables the setting of environment values for specified keys. Although creating environment variables via the [Environment Variables](/environment-variables/) page is typically recommended, this step provides flexibility to modify environment variables directly within the build workflow when necessary.
### Prerequisites

There are no prerequisites required before using the **Set Environment Variable** step. It can be implemented at any point within the workflow as necessary.

:::danger

Please note that you must use the **Set Environment Variable** step before the step in which you intend to use the environment variable.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/set-environment-variable_2.png'/>

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/environment-variables/managing-variables) groups for such sensitive variables.

:::

| Variable Name      | Description                                                                                                     | Status   |
| ------------------ | --------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_SETENV_KEYS`  | Specifies the key of the environment variable to be set. This should be a space-separated list of environment variable keys.  | Required |
| `$AC_SETENV_VALUE` | Specifies the value of the environment variable to set. If this field is left blank, the environment variable will be set to `null`. | Optional |

:::info Output Variables

The **Set Environment Variable** step generates no output variables. Success or failure of this step depends on whether the environment variable is set correctly, allowing subsequent use within the workflow.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-setenvironment-component.git