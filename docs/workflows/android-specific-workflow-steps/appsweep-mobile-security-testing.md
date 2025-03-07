---
title: AppSweep Mobile Security Testing
description: Learn how to use the AppSweep Mobile Security Testing workflow step in Appcircle
tags: [android, mobile, security, testing, appsweep]
---

import Screenshot from '@site/src/components/Screenshot';

# AppSweep Mobile Security Testing

[AppSweep Mobile Security Testing](https://www.guardsquare.com/appsweep-mobile-application-security-testing) is a comprehensive security solution designed to protect mobile applications from various threats and vulnerabilities. It offers advanced scanning capabilities to identify security flaws, privacy concerns, and compliance issues within mobile apps. By thoroughly analysing app code, configurations, and dependencies, AppSweep helps developers and organisations mitigate risks and ensure the integrity and safety of their mobile applications.

The Appcircle **AppSweep Mobile Security Testing** step allows you to comprehensively analyse your mobile applications for potential security vulnerabilities, privacy risks, and compliance issues, thereby ensuring the robustness and integrity of your software before deployment.

### Prerequisites

Before running the **AppSweep Mobile Security Testing** step, you must complete certain prerequisites, as detailed in the table below:

| Prerequisite Workflow Step                                                        | Description                                                                                                                               |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [**Git Clone**](/workflows/common-workflow-steps/git-clone) | The **AppSweep Mobile Security Testing** step requires the repository to be cloned from the Git provider before it can function properly. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-appsweep-mobile-security-testing_1.png'/>

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/android-workflow-components-appsweep-mobile-security-testing_2.png'/>

:::danger Sensitive Variables

Please do not use sensitive variables such as **Username**, **Password**, **API Key**, or **Personal Access Key** directly within the step.

We recommend using [**Environment Variables**](/build/build-environment-variables) groups for such sensitive variables.

:::

| Variable Name          | Description                                                                                                                                                                                                                                                                                                                                                             | Status   |
| ---------------------- |-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| -------- |
| `$AC_APPSWEEP_API_KEY` | Specifies the API key of the AppSweep account. You can create an API key in the API Keys section of your project settings on the AppSweep website.                                                                                                                                                                                                                      | Required |
| `$AC_APPSWEEP_VARIANT` | Specifies the project variant to be built. This variable can also be set via the build [Configuration](/build/build-process-management/configurations). In Android Studio, you can find the available variants for your project. For more information, please refer to this [Android document](https://developer.android.com/build/build-variants). | Required |
| `$AC_PROJECT_PATH`     | Specifies the project path. If your project that needs to be built is **not located** in the root directory where it was cloned from Git, you should provide the subpath as a relative path.                                                                                                                                                                            | Optional |

### Output Variables

The output(s) resulting from the operation of this component are as follows:

| Variable Name      | Description                                                   |
| ------------------ | ------------------------------------------------------------- |
| `AC_APPSWEEP_URL` | A direct link to the scan results is on the AppSweep website. |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-appsweep-component.git
