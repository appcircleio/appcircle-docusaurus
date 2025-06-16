---
title: Appcircle CodePush Workflow
sidebar_label: Appcircle CodePush
description: Learn how to integrate Appcircle CodePush SDK.
tags: [appcircle codepush, build, ci, build module]
sidebar_position: 1
---

# Appcircle CodePush

The **Appcircle CodePush** step allows you to automate the process of releasing over-the-air (OTA) updates for your React Native apps as part of your CI/CD workflow.

For more information about Appcircle CodePush feature, please visit the [**CodePush**](/code-push) documentations.

### Prerequisites

Before running the **Appcircle CodePush** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step | Description                                                                                                                                                                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Git Clone**              | Clone the selected repository to the build machine. Please use the **Appcircle CodePush** step after this step.                                                                                                                                                          |
| **Node Install**           | This step will install Node modules for your application. Please note that the **Appcircle CodePush** step should be used after this step.                                                                                                                               |
| **NPM/Yarn Commands**      | This step installs the [NPM](https://www.npmjs.com/) or [Yarn](https://www.npmjs.com/package/yarn) package manager to install specific dependencies for your React Native applications. Please note that the **Appcircle CodePush** step should be used after this step. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-stepOrder.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6122-stepInputs.png' />

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/build/build-environment-variables) groups for such sensitive variables.

:::

| Variable Name                         | Description                                                                                                                                                                                                                                                                                       | Status   |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| `$AC_REPOSITORY_DIR`                  | Relative path of the React Native project.                                                                                                                                                                                                                                                        | Required |
| `$AC_CODE_PUSH_TOKEN`                 | Appcircle personal access token. You can create a new token in the Appcircle dashboard under `Settings > Security > Personal Access Token`. For details, see [Generating and Managing Personal API Tokens](/appcircle-api-and-cli/api-authentication#generatingmanaging-the-personal-api-tokens). | Required |
| `$AC_CODE_PUSH_SERVER_URL`            | This parameter specifies the server URL used by self-hosted Appcircle instances to authenticate CLI access. Ignore this if you are not a self-hosted Appcircle user.                                                                                                                              | Optional |
| `$AC_CODE_PUSH_AUTH_URL`              | This parameter specifies the authentication URL used by self-hosted Appcircle instances to authenticate CLI access. Ignore this if you are not a self-hosted Appcircle user.                                                                                                                      | Optional |
| `AC_CODE_PUSH_APP_NAME`               | This parameter specifies the name of the app in Appcircle. The App Name parameter is the Appcircle CodePush profile name.  For example `MyApp-Android` or `MyApp-iOS`.                                                                                                                            | Required |
| `$AC_CODE_PUSH_DEPLOYMENT_NAME`       | This parameter specifies the deployment channel name in Appcircle. The Deployment Channel parameter is the Appcircle CodePush deployment name. For example `Staging` or `Production`.                                                                                                             | Required |
| `$AC_CODE_PUSH_TARGET_BINARY_VERSION` | This parameter specifies the target binary version of the app that this update is intended for. It should be in the format `1.0.0`.                                                                                                                                                               | Required |
| `$AC_CODE_PUSH_DESCRIPTION`           | This parameter provides an optional changelog for the deployment.                                                                                                                                                                                                                                 | Optional |
| `$AC_CODE_PUSH_ROLLOUT_PERCENTAGE`    | This parameter specifies the percentage of users (as an integer between 1 and 100) that should be eligible to receive this update.                                                                                                                                                                | Optional |
| `$AC_CODE_PUSH_EXTRA_ARGUMENTS`       | Extra command line arguments for Appcircle CodePush CLI command. For example, add `--debug` for verbose logs.                                                                                                                                                                                     | Optional |


### CodePush Code Signing

With the **Appcircle CodePush** step, you can also publish a **signed CodePush release**. The required actions are outlined below, step by step.

- First, create a group in the **Environment Variables** sub‑section under the **Build** module, and upload your `.pem` file into that group. For more information, please visit the Environment Variable [documentation](/environment-variables).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6352-envPem.png' />

:::caution Environment Variables

In order to use the **Environment Variable** group you created in the relevant profile, you need to select this group from the build configuration. For more detailed information, please refer to the Build Configuration [documentation](/build/build-process-management/configurations#environment-variables-configuration).

:::

- Next, in the **Appcircle CodePush** step, use the **Extra Arguments** input to pass the `--privateKeyPath <YOUR_ENV_KEY>` parameter and reference the environment variable you created.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6352-inputPem.png' />

Once these steps are completed, running the **Appcircle CodePush** step will automatically sign the generated CodePush release with your provided `.pem` file and publish it.
